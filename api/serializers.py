from rest_framework import serializers
from .models import Dua,Ayat,Hadees,Quran,RamzanHadees,SehrHadees,IftarHadees,LailaTulQadarHadees,Eid
from django.conf import settings
from fcm_django.models import FCMDevice
from django.db import models
class AyatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ayat
        fields = ['id','reference','arabic_text', 'urdu_text', 'english_text']

class HadeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hadees
        fields = ['id', 'reference','arabic_text','urdu_text', 'english_text']

class DuaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dua
        fields = ['id','title','reference','arabic_text', 'urdu_text', 'english_text']

class QuranSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quran
        fields = ['id', 'arabic', 'urdu_arabic']

class EidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eid
        fields = ['id','reference','arabic_text','urdu_text', 'english_text']


class RamzanHadeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RamzanHadees
        fields = ['id','reference','arabic_text', 'urdu_text', 'english_text']

class SehrHadeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SehrHadees
        fields = ['id','reference','arabic_text', 'urdu_text', 'english_text']

class IftarHadeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IftarHadees
        fields = ['id','reference','arabic_text', 'urdu_text', 'english_text']

class LailaTulQadarHadeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LailaTulQadarHadees
        fields = ['id','reference','arabic_text', 'urdu_text', 'english_text']
        
        
        

class FCMDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FCMDevice
        fields = ["id", "name", "registration_id", "device_id", "active","date_created", "type"]
        
        read_only_fields = ("date_created",)

        extra_kwargs = {"active": {"default": True}}