from django.http.response import HttpResponse, FileResponse,JsonResponse
import os
from django.shortcuts import render


def product_hello_page(request):
    return HttpResponse("Hello this is hello page")


def display_name(request, name):
    return HttpResponse(f"Hello {name} welcome!")



def download_Dorcci(request):
    file_music = os.path.join("/home/amirykta/Desktop/Fidibo/env/Fidibo/product/10.Dorcci - Addi (320).mp3")
    return FileResponse(
        open(file_music, "rb"),
        as_attachment=True
    )
    

def your_info(request):
    your_info = {
        "name":"amirhosein",
        "age":21,
        "code":"021"
    }
    return JsonResponse(your_info)



 






