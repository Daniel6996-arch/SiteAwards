from django.shortcuts import render, redirect
from django.views import View
from .models import Website
from .forms import SiteForm


# Create your views here.
def index(request):
    return render(request, 'index.html') 


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