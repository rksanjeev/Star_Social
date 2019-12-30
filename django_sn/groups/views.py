from django.shortcuts import render
from . import models as gr_models
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
# Create your views here.

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = gr_models.Group

class SingleGroup(generic.DetailView):
    model = gr_models.Group

class ListGroups(generic.ListView):
    model = gr_models.Group