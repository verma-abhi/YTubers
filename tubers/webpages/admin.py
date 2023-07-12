from django.contrib import admin
from .models import Slider, Team 
from django.utils.html import format_html
# Register your models here.


class TeamAdmin(admin.ModelAdmin):      # for customization of display 

    def myphoto(self, object):        #allows us to format specific features 
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))
    
    list_display = ('id', 'myphoto' ,'first_name' , 'role' , 'created_date')
    list_display_links = ('first_name', 'id')          #clickable links 
    search_fields = ('first_name', 'role')  
    list_filter = ('role',)
      # we can try many such 

admin.site.register(Slider)  # regiters the model class at admin
admin.site.register(Team , TeamAdmin)    