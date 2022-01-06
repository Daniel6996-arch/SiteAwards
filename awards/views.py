from django.shortcuts import render, redirect
from django.views import View
from .models import Website, UserProfile, Comment
from .forms import SiteForm, CommentForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.
def index(request):
    return render(request, 'index.html') 

def newsletter(request):
    author = request.POST.get('author')
    title = request.POST.get('title')
    description = request.POST.get('description')
    country = request.POST.get('country')
    landing_page = request.POST.get('landing_page')
    uploaded_on = request.POST.get('uploaded_on')

    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)
 


class WebsiteListView(View):
    def get(self, request):
        websites = Website.objects.all().order_by('-uploaded_on')
        form = SiteForm()

        context = {
            'site_list':websites,
            'form':form,
        }

        return render(request, 'website_of_day.html', context) 

    def post(self, request):
        websites = Website.objects.all().order_by('-uploaded_on')
        site_of_day = Website.objects.all().order_by('-uploaded_on').first()
        form = SiteForm(request.POST, request.FILES)

        if form.is_valid():
            new_site = form.save(commit = False)
            new_site.author = request.user

            if 'img' in request.FILES:
                new_site.image = request.FILES['img']

            new_site.save()   

        context = {
            'site_list':websites,
            'site_of_day':site_of_day,
            'form':form,
        }

        return render(request, 'website_of_day.html', context)  

class ProfileView(View):
    def get(self, request, pk):
        profile = UserProfile.objects.get(pk=pk)
        user = profile.user
        websites = Website.objects.filter(author = user).order_by('-uploaded_on')   

        context = {
            'user':user,
            'profile':profile,
            'websites':websites,
        }        

        return render(request, 'profile.html', context)     

class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    fields = ['full_name', 'bio', 'profile_pic']
    template_name = 'profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk':pk})

    def test_func(self):
        profile = self.get_object()               

class WebsiteDetailView(View):
    def get(self, request, pk,  *args, **kwargs):
        #pk = self.kwargs.get('pk')
        website = Website.objects.get(pk=pk)
        form = CommentForm() 

        comments = Comment.objects.filter(website = website).order_by('-created_on')

        template_name = 'website_detail.html'

        context = {
            'website':website,
            'form':form,
            'comments':comments,
        }

        return render(request, 'website_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        website = Website.objects.get(pk=pk)
        form = CommentForm(request.POST) 
 
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.website = website
            new_comment.save()

        comments = Comment.objects.filter(website = website).order_by('-created_on')    

        context = {
            'website':website,
            'form':form,
            'comments':comments,
        }

        return render(request, 'website_detail.html', context)

def search(request):

    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = UserProfile.search_user(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"users":searched_users})

    else:
        return render(request, 'search.html', {"message":message})     