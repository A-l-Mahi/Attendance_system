'''
    When I wrote this code Only Allah and Me knows,
    Now Only Allah Knows.
'''


from django.shortcuts import render, redirect
import cv2
import pyzbar.pyzbar as pyzbar
import numpy as np
from .models import save
"""from django.http import HttpResponse
from django.views.generic import View
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
"""
"""from yourproject.utils import render_to_pdf #created in step 4"""

#from Qrscanner.models import *

# Create your views here.m
 
#opening Camera
cap = cv2.VideoCapture(0)

#font

font = cv2.FONT_HERSHEY_PLAIN



# Create your views here.
def scanner():
  #loop

    while True:

        #reading Qr
        _, frame = cap.read()

        #Qr Detection

        decodedObjects = pyzbar.decode(frame)
        #collecting data
        for obj in decodedObjects: 
            #processing data
            res = obj.data.decode('ascii')
            
            #converting data to string 
            a = str(res)

                #spliting data
            res = a.split()

            #printing info to the  console
            
            if len(res) == 4:
                Name = res[0]+" " + res[1]+ " " +res[2]
                Regno = res[3]
                obj1 = save(Name = Name, Regno = Regno)
                if save.objects.filter(Name = Name).exists():
                    cv2.putText(frame , "SAVED", (50, 50), font, 3, (255, 0 , 0)
                                                , 1)
                   
                else:
                    obj1.save()
                
            elif len(res) == 3:
                Name = res[0]+" " + res[1]
                Regno = res[2]
                obj1 = save(Name = Name, Regno = Regno)
                if save.objects.filter(Name = Name).exists():
                    cv2.putText(frame , "SAVED", (50, 50), font, 3, (255, 0 , 0), 1)
                    print("\a")
                                                
                   
                else:
                    obj1.save()
            else:
                cv2.putText(frame , "QR NOT VALID", (50, 50), font, 3, (255, 0 , 0), 1)
                

            #outputing text

            
        #Displaying Camera
                        
        cv2.imshow("QrScanner", frame)

        #Breaking loop
        key = cv2.waitKey(1)

        if key == ord("q"):
            return redirect("/current/")
            break


def scan(request):

    obj = scanner()
    context = {

    'info' : scanner()
  }

    return render(request, "scanning.html", context)

def att(request):

 
    return render(request, "attendance.html",)
 
def index(request):

    info = save.objects.all()
 
    return render(request, "index.html", {'info': info})
def about(request):
 
    return render(request, "about.html")

def contact(request):

    return render(request, "contact.html")

def current(request):

    info = save.objects.all()

    return render(request, "current.html", {'info': info})

def view(request):

    return render(request, "viewattendance.html")
def id_card(request):

    return render(request, "id-card.html")
'''def contact(request):

    return render(request, "scanner.html")
def contact(request):

    return render(request, "tables.html")'''
