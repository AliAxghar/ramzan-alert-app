from django.shortcuts import render
from rest_framework import viewsets
from .models import Ayat,Hadees,Dua,RamzanHadees,SehrHadees,IftarHadees,LailaTulQadarHadees,Eid,Quran
from .serializers import AyatSerializer,QuranSerializer,EidSerializer,RamzanHadeesSerializer,SehrHadeesSerializer,IftarHadeesSerializer,LailaTulQadarHadeesSerializer,HadeesSerializer,DuaSerializer,FCMDeviceSerializer
from fcm_django.models import FCMDevice
from datetime import date
from ummalqura.hijri import Umalqurra
import time
import datetime 
from ummalqura.hijri_date import HijriDate
import boto3


class Ramzanalert():
    def run(self):
        devices = FCMDevice.objects.all()
        if date.today().weekday():
            devices.send_message("Ramzan Alert", "Narrated Abu Huraira: I heard Allah's Apostle saying, Before Allah created the creations, He wrote a Book (wherein He has written): My Mercy has preceded my Anger. and that (Book) is written with Him over the Throne.")
        um = HijriDate.today()
        if HijriDate.current_month()==12:
            if um.day-1 == 1:
                if date.today().weekday():
                    devices.send_message("Ramzan Alert","you can fast on first 9 days of Zilhajj")
            elif um.day-1 == 10:
                if date.today().weekday():
                    devices.send_message("Ramzan Alert","fasting on 10th 11th 12th Zilhajj is forbidden by our prophet(PBUH)")
            elif um.day-1 != 10 and um.day-1 != 1 :
                if date.today().weekday() == 3 or date.today().weekday() == 0:
                    devices.send_message("Ramzan Alert","Aishah narrated:The Prophet used to try to fast on Mondays and Thursdays. [Tirmidhi, Nasai, and Ibn Majah].It is Sunnah to fast today")
                elif date.today().weekday() == 4:
                    devices.send_message("Ramzan Alert","you should not fast Friday alone, but in combination with Thursday or Saturday.")
        elif HijriDate.current_month()==1:
            if um.day-1 == 9:
                if date.today().weekday():
                    devices.send_message("Ramzan Alert","It is Sunnah to fast on 9th and 10th muharram")
            else:
                if date.today().weekday() == 4:
                    devices.send_message("Ramzan Alert","you should not fast Friday alone, but in combination with Thursday or Saturday.")
                elif date.today().weekday() == 3 or date.today().weekday() == 0:
                    devices.send_message("Ramzan Alert","Aishah narrated:The Prophet used to try to fast on Mondays and Thursdays. [Tirmidhi, Nasai, and Ibn Majah].It is Sunnah to fast today")
        elif HijriDate.current_month()==8:
            if um.day-1 == 1:
                devices.send_message("Ramzan Alert","It is Sunnah to fast on first 15 days of Shaban")
            else:
                if date.today().weekday() == 4:
                    devices.send_message("Ramzan Alert","you should not fast Friday alone, but in combination with Thursday or Saturday.")
                elif date.today().weekday() == 3 or date.today().weekday() == 0:
                    devices.send_message("Ramzan Alert","Aishah narrated:The Prophet used to try to fast on Mondays and Thursdays. [Tirmidhi, Nasai, and Ibn Majah].It is Sunnah to fast today")
        elif HijriDate.current_month()== 10:
            if um.day-1 == 1:
                if date.today().weekday():
                    devices.send_message("Ramzan Alert","fasting is prohibited on beginning the day after Eid ul-Fitr.These six days of fasting together with the Ramadan fasts.")
            else:
                if date.today().weekday() == 4:
                    devices.send_message("Ramzan Alert","you should not fast Friday alone, but in combination with Thursday or Saturday.")
                elif date.today().weekday() == 3 or date.today().weekday() == 0:
                    devices.send_message("Ramzan Alert","Aishah narrated:The Prophet used to try to fast on Mondays and Thursdays. [Tirmidhi, Nasai, and Ibn Majah].It is Sunnah to fast today")

        elif HijriDate.current_month()== 9:
            if um.day-1 == 1:
                if date.today().weekday():
                    devices.send_message("Ramzan Alert","During the entire month of Ramadan, Every qualified Muslims is obligated to fast")

        else:
            if um.day-1 == 13:
                if date.today().weekday():
                    devices.send_message("Ramzan Alert","you can fast on 13th,14th and 15th days of moon")
            else:
                if date.today().weekday() == 4:
                    devices.send_message("Ramzan Alert","you should not fast Friday alone, but in combination with Thursday or Saturday.")
                elif date.today().weekday() == 3 or date.today().weekday() == 0:
                    devices.send_message("Ramzan Alert","Aishah narrated:The Prophet used to try to fast on Mondays and Thursdays. [Tirmidhi, Nasai, and Ibn Majah].It is Sunnah to fast today")
obj = Ramzanalert()
obj.run()

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



# class FCMdevicesViewSet(viewsets.ModelViewSet):

#     queryset = FCMdevices.objects.all().first()
#     serializer_class = FCMdevicesSerializer




















def sendMessage():
    # Create an SNS client
    client = boto3.client(
        "sns",
        aws_access_key_id="AKIAIPRRJYYIR6FS2GDQ",
        aws_secret_access_key="Tzv3tQyIWRrXy1KNxVbLaya4fMdcMMNIqnjt/mCb",
        region_name="us-east-1"
    )
    # Send your sms message.
    client.publish(
        PhoneNumber="+923224277699",
        Message="code"
    )