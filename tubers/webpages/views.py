from django.shortcuts import render
from .models import Slider , Team
from youtubers.models import Youtuber #req. bz we take data from diffnt app youtubers
# Create your views here.

def home(request): 
   sliders = Slider.objects.all() #fetches all the information from the slider that we are having
   teams = Team.objects.all() 

   featured_youtubers = Youtuber.objects.order_by(
        '-created_date').filter(is_featured=True) # here not all but filtered data recieved
   
   all_tubers = Youtuber.objects.order_by('-created_date')

   data = {           # data is an object where we pass and fetch all information     
       'sliders':sliders,  #sliders will get all inform. from sliders above
        'teams': teams,
       'featured_youtubers' : featured_youtubers,
       'all_tubers' : all_tubers,

   }
   return render(request, 'webpages/home.html',data)   #passing data 


def about(request):
   teams = Team.objects.all() 
   data = {           # data is an object where we pass and fetch all information     
        'teams': teams,
   }
   return render(request ,'webpages/about.html',data)


def services(request):
    return render(request ,'webpages/services.html')


def contact(request):
    return render(request ,'webpages/contact.html')

