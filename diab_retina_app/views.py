

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from diab_retina_app import process
from diab_retina_app import vessels_remove
from diab_retina_app import detect_stains



@csrf_exempt
def display(request):
    if request.method == 'GET':
        return render(request, 'index.html')


@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        img = request.POST.get('image')
        vessels_remove.remove_vessels(img)
        detect_stains.draw_vessels(img)
        response = process.process_img(img)
        return HttpResponse(response, status=200)
