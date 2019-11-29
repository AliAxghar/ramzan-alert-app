from django.shortcuts import render
from rest_framework import viewsets
from .models import Ayat,Hadees,Dua,RamzanHadees,SehrHadees,IftarHadees,LailaTulQadarHadees,Eid,Quran
from .serializers import AyatSerializer,QuranSerializer,EidSerializer,RamzanHadeesSerializer,SehrHadeesSerializer,IftarHadeesSerializer,LailaTulQadarHadeesSerializer,HadeesSerializer,DuaSerializer,FCMDeviceSerializer
from fcm_django.models import FCMDevice
from datetime import date
from ummalqura.hijri import Umalqurra
# from threading import *
import time
from time import sleep
from ummalqura.hijri_date import HijriDate

device = FCMDevice.objects.all().first()
if date.today().weekday() == 4:
    device.send_message("Ramzan Alert", "It is sunnat to fast today ")

# list  = []
# for d in device:
#     list.append(d.registration_id)
#     print(list)
um = HijriDate.today()
if HijriDate.current_month()==12:
    if um.day-1 == 1:
        if date.today().weekday():
            device.send_message("Ramzan Alert","you can fast on first 9 days of Zilhajj")
    elif um.day-1 == 10:
        if date.today().weekday():
            device.send_message("Ramzan Alert","fasting on 10th 11th 12th Zilhajj is forbidden by our prophet(PBUH)")
    elif um.day-1 != 10 and um.day-1 != 1 :
        if date.today().weekday() == 3 or date.today().weekday() == 0:
            device.send_message("Ramzan Alert","Aishah narrated:The Prophet used to try to fast on Mondays and Thursdays. [Tirmidhi, Nasai, and Ibn Majah].It is Sunnah to keep fast today")
        elif date.today().weekday() == 4:
            device.send_message("Ramzan Alert","you should not fast Friday alone, but in combination with Thursday or Saturday.")
elif HijriDate.current_month()==1:
    if um.day-1 == 9:
        if date.today().weekday():
            device.send_message("Ramzan Alert","It is Sunnah to fast on 9th and 10th muharram")
    else:
        if date.today().weekday() == 4:
            device.send_message("Ramzan Alert","you should not fast Friday alone, but in combination with Thursday or Saturday.")
        elif date.today().weekday() == 3 or date.today().weekday() == 0:
            device.send_message("Ramzan Alert","Aishah narrated:The Prophet used to try to fast on Mondays and Thursdays. [Tirmidhi, Nasai, and Ibn Majah].It is Sunnah to keep fast today")
elif HijriDate.current_month()==8:
    if um.day-1 == 1:
        device.send_message("Ramzan Alert","It is Sunnah to fast on first 15 days of Shaban")
    else:
        if date.today().weekday() == 4:
            device.send_message("Ramzan Alert","you should not fast Friday alone, but in combination with Thursday or Saturday.")
        elif date.today().weekday() == 3 or date.today().weekday() == 0:
            device.send_message("Ramzan Alert","Aishah narrated:The Prophet used to try to fast on Mondays and Thursdays. [Tirmidhi, Nasai, and Ibn Majah].It is Sunnah to keep fast today")
elif HijriDate.current_month()== 10:
    if um.day-1 == 1:
        if date.today().weekday():
            device.send_message("Ramzan Alert","fasting is prohibited on beginning the day after Eid ul-Fitr.These six days of fasting together with the Ramadan fasts.")
    else:
        if date.today().weekday() == 4:
            device.send_message("Ramzan Alert","you should not fast Friday alone, but in combination with Thursday or Saturday.")
        elif date.today().weekday() == 3 or date.today().weekday() == 0:
            device.send_message("Ramzan Alert","Aishah narrated:The Prophet used to try to fast on Mondays and Thursdays. [Tirmidhi, Nasai, and Ibn Majah].It is Sunnah to keep fast today")

elif HijriDate.current_month()== 9:
    if um.day-1 == 1:
        if date.today().weekday():
            device.send_message("Ramzan Alert","During the entire month of Ramadan, Every qualified Muslims is obligated to fast")

else:
    if um.day-1 == 13:
        if date.today().weekday():
            device.send_message("Ramzan Alert","you can fast on 13th,14th and 15th days of moon")
    else:
        if date.today().weekday() == 4:
            device.send_message("Ramzan Alert","you should not fast Friday alone, but in combination with Thursday or Saturday.")
        elif date.today().weekday() == 3 or date.today().weekday() == 0:
            device.send_message("Ramzan Alert","Aishah narrated:The Prophet used to try to fast on Mondays and Thursdays. [Tirmidhi, Nasai, and Ibn Majah].It is Sunnah to keep fast today")


# class Ramzanalert(Thread):
#     def run(self):
#         while True:
#             # device = FCMDevice.objects.all().first()
#             if date.today().weekday() == 0 or 3:
#                 # device.send_message("Ramzan Alert", "It is sunnat to fast today")
#                 # time.sleep(2000)
#                 print('Hola')
#                 sleep(10)
#             else:
#                 continue
# time.sleep(20)
# t1 = Ramzanalert()
# t1.start()


class AyatViewSet(viewsets.ModelViewSet):

    queryset = Ayat.objects.all()
    serializer_class = AyatSerializer

class HadeesViewSet(viewsets.ModelViewSet):

    queryset = Hadees.objects.all()
    serializer_class = HadeesSerializer

class DuaViewSet(viewsets.ModelViewSet):

    queryset = Dua.objects.all()
    serializer_class = DuaSerializer


class QuranViewSet(viewsets.ModelViewSet):

    queryset = Quran.objects.all()
    serializer_class = QuranSerializer

class RamzanHadeesViewSet(viewsets.ModelViewSet):

    queryset = RamzanHadees.objects.all()
    serializer_class = RamzanHadeesSerializer
class SehrHadeesViewSet(viewsets.ModelViewSet):

    queryset = SehrHadees.objects.all()
    serializer_class = SehrHadeesSerializer

class IftarHadeesViewSet(viewsets.ModelViewSet):

    queryset = IftarHadees.objects.all()
    serializer_class = IftarHadeesSerializer

class LailaTulQadarHadeesViewSet(viewsets.ModelViewSet):

    queryset = LailaTulQadarHadees.objects.all()
    serializer_class = LailaTulQadarHadeesSerializer

class EidViewSet(viewsets.ModelViewSet):

    queryset = Eid.objects.all()
    serializer_class = EidSerializer


class FCMDeviceViewSet(viewsets.ModelViewSet):

    queryset = FCMDevice.objects.all().first()
    serializer_class = FCMDeviceSerializer

