from django.shortcuts import render
from . import models as gr_models
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib import messages
# Create your views here.

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = gr_models.Group

class SingleGroup(generic.DetailView):
    model = gr_models.Group

class ListGroups(generic.ListView):
    model = gr_models.Group

class JoinGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs = {'slug': self.kwargs.get('slug')})

    def get(self,request,  *args, **kwargs ):
        group = get_object_or_404(gr_models.Group, slug = self.kwargs.get('slug'))

        try:
            gr_models.GroupMember.objects.create(user = self.request.user, group = group)
        except:
            messages.warning(self.request,'Warning! Already a member')
        else:
            messages.success(self.request, 'Successfully joined the group !')
        return super().get(request, *args, **kwargs)

class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:all')
    
    def get(self,request,  *args, **kwargs):
        try:
            membership = gr_models.GroupMember.objects.filter( user = self.request.user, group__slug = self.kwargs.get('slug') ).get()
        except:
            messages.warning(self.request, 'Not a Group Member !')
        else:
            membership.delete()
            messages.success(self.request, 'You have left the group!') 
        return super().get(request, *args, **kwargs)


