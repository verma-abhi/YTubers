from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Youtuber
# Create your views here.

def youtubers(request):
    tubers = Youtuber.objects.order_by('-created_date')
    data ={
        'tubers': tubers
    }
    return render(request, 'youtubers/youtubers.html' , data)

def youtubers_detail(request, id):
    tuber = get_object_or_404(Youtuber, pk=id) #used to pass single object
    data = {
        'tuber' : tuber 
    }
    return render(request, 'youtubers/youtuber_detail.html', data)

def search(request):
    tubers = Youtuber.objects.order_by('-created_date')
    
    city_search = Youtuber.objects.values_list('city', flat=True).distinct()
    camera_type_search = Youtuber.objects.values_list('camera_type', flat=True).distinct()
    category_search = Youtuber.objects.values_list('category', flat=True).distinct()
    #these 3 fields are used to pass all the particular data in database for the dropdown in options

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains=keyword)  # here we are doing query in description ,but we can do that in name,etc also

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city) 

    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=camera_type) 
    
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=category) 


     
    data = {
        'tubers' : tubers,
        'city_search' : city_search,  #this data is for dropdown in search
        'camera_type_search' : camera_type_search,
        'category_search' : category_search,
    }
    return render(request, 'youtubers/search.html', data)


    