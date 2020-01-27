from django.db import models
from django.utils.text import slugify
# import misaka
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse
# Create your models here.

User = get_user_model()
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    descripction = models.TextField(blank=True, default='')
    descripction_html = models.TextField(editable = True, blank=True, default='')
    members = models.ManyToManyField(User, through='GroupMember')
    

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # self.descripction_html = misaka.html(self.description)
        suprt().save(*args, **kwargs)
    
    def get_abs_url(self):
        return reverse('groups:single', kwargs= {'slug':self.slug})
    
    class Meta:
        ordering = ['name']



class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete = models.DO_NOTHING, related_name='memberships')
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING, related_name='user_groups')

    def __str__(self):
        return self.user.username
    
    class Meta:
        unique_together = ('group', 'user')
        



