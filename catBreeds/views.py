from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from .models import CatBreed
from django.http import Http404
from django.db.models import Q



# First page when server run
def firstPage(request):
    return HttpResponse("<h1>The Server is Running</h1>")


# '/catBreeds/' endpoint
def get_all_breeds(request):

    modelData = CatBreed.objects.all()
    allData = []

    if modelData:
        for data in modelData:
            allData.append(model_to_dict(
                data, fields=['id', 'image', 'breed', 'description']))

        # return JsonResponse("There is no data", safe=False, status=404)

    return JsonResponse(allData, safe=False, status=200)


#  popularCatBreed/
def get_popular_breeds(request):

    modelData = CatBreed.objects.filter(popularity__gt=0).order_by('-popularity')
    allData = []

    if modelData:
        for data in modelData:
            allData.append(model_to_dict(data))
           #     data, fields=['id', 'image', 'breed', 'description']))
    else:
        return JsonResponse("There is no data", safe=False, status=404)

    return JsonResponse(allData, safe=False, status=200)



# '/catBreeds/id' endpoint
def get_breed(request, id):
    try:
        modelData = CatBreed.objects.get(id=id)
        modelData.popularity += 1
        modelData.save() 
    except:
        raise Http404("Sorry There is no data with this id")
        # return JsonResponse("Sorry There is no data with this id", safe=False, status=404)

    #data = {}
    if modelData:
        data = {
            "id": modelData.id,
            "image": modelData.image,
            "breed": modelData.breed,
            "description": modelData.description,
            "temperament": modelData.temperament,
            "origin": modelData.origin,
            "lifeSpan": modelData.lifeSpan,
            "popularity": modelData.popularity,
            "prope":[{"title": "adaptability", "rate": modelData.adaptability},
            {"title": "affectionLevel", "rate": modelData.affectionLevel},
            {"title": "childFriendly", "rate": modelData.childFriendly},
            {"title": "grooming", "rate": modelData.grooming},
            {"title": "intelligence", "rate": modelData.intelligence},
            {"title": "healthIssues", "rate": modelData.healthIssues},
            {"title": "socialNeeds", "rate": modelData.socialNeeds},
            {"title": "strangerFriendly", "rate": modelData.strangerFriendly}],
            "otherPhotos": modelData.otherPhotos.split(','),
            
        }
    

        return JsonResponse(data, status=200)


#search for cat breed 
def cat_breed_search(request, catBreeed):
    searched_breeds = CatBreed.objects.filter(Q(breed__icontains=catBreeed)).values('id', 'breed')

    if searched_breeds:
        data = {breed['breed']: breed for breed in searched_breeds}
        return JsonResponse(data, status=200)
    
    else:
        raise Http404("No such a breed")
