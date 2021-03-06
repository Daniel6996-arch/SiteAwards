from django.shortcuts import render, redirect
from django.views import View
from .models import Website, UserProfile, Comment
from .forms import SiteForm, CommentForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer, WebsiteSerializer
from .permissions import IsAdminOrReadOnly
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    return render(request, 'index.html') 
 


class WebsiteListView(View):
    def get(self, request):
        websites = Website.objects.all().order_by('-uploaded_on')
        site_of_day = Website.objects.all().order_by('-uploaded_on').first()
        form = SiteForm()

        context = {
            'site_list':websites,
            'site_of_day':site_of_day,
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

class ProfileEditView(UpdateView):
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

class UserList(APIView):
    def get(self, request, format=None):
        permission_classes = (IsAdminOrReadOnly,)
        all_users = UserProfile.objects.all()
        serializers = UserSerializer(all_users, many=True)
        return Response(serializers.data) 

class SiteList(APIView):
    def get(self, request, format=None):
        permission_classes = (IsAdminOrReadOnly,)
        all_sites = Website.objects.all()
        serializers = WebsiteSerializer(all_sites, many=True)
        return Response(serializers.data)

class Usability(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        site = Website.objects.get(pk=pk)        

        is_usability = False

        for usability in site.usability.all():
            if usability == request.user:
                is_usability = True
                break

        if not is_usability:
            site.usability.add(request.user)
        if is_usability:
            site.usability.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

class Design(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        site = Website.objects.get(pk=pk)        

        is_design = False

        for design in site.design.all():
            if design == request.user:
                is_design = True
                break

        if not is_design:
            site.design.add(request.user)
        if is_design:
            site.design.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)    

class Content(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        site = Website.objects.get(pk=pk)        

        is_content = False

        for content in site.content.all():
            if content == request.user:
                is_content = True
                break

        if not is_content:
            site.content.add(request.user)
        if is_content:
            site.content.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)            