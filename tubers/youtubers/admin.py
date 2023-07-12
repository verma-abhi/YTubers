from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html
# Register your models here.

class YTAdmin(admin.ModelAdmin):

    def myphoto(self, object):        #allows us to format specific features 
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))
    
    list_display = ('id', 'myphoto', 'name' ,'category', 'subs_count', 'is_featured')
    search_fields = ('name','camera_type', 'category')
    list_filter =  ('category', 'city')
    list_display_links = ('id', 'name')
    list_editable = ('is_featured',)   

admin.site.register(Youtuber, YTAdmin)

 