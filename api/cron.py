from fcm_django.models import FCMDevice
from datetime import date
from ummalqura.hijri import Umalqurra
from threading import *
import time
import datetime 
from time import sleep
from ummalqura.hijri_date import HijriDate

def run(self):
    devices = FCMDevice.objects.all()
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
 
