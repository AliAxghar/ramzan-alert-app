from rest_framework import serializers
from .models import Dua,Ayat,Hadees,Quran,RamzanHadees,SehrHadees,IftarHadees,LailaTulQadarHadees,Eid

class AyatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ayat
        fields = ['url', 'id','reference','arabic_text', 'urdu_text', 'english_text']

class HadeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hadees
        fields = ['url', 'id', 'reference','arabic_text','urdu_text', 'english_text']

class DuaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dua
        fields = ['url', 'id','title','arabic_text', 'urdu_text', 'english_text']

class QuranSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quran
        fields = ['url', 'id', 'arabic', 'urdu_arabic']

class EidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eid
        fields = ['url', 'id','reference','arabic_hadees', 'urdu_hadees', 'english_hadees']


class RamzanHadeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RamzanHadees
        fields = ['url', 'id','reference','arabic_text', 'urdu_text', 'english_text']

class SehrHadeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SehrHadees
        fields = ['url', 'id','reference','arabic_text', 'urdu_text', 'english_text']

class IftarHadeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IftarHadees
        fields = ['url', 'id','reference','arabic_text', 'urdu_text', 'english_text']

class LailaTulQadarHadeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LailaTulQadarHadees
        fields = ['url', 'id','reference','arabic_text', 'urdu_text', 'english_text']
        
        
        

