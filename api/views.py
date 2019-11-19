from django.shortcuts import render
from rest_framework import viewsets
from .models import Ayat,Hadees,Dua,RamzanHadees,SehrHadees,IftarHadees,LailaTulQadarHadees,Eid,Quran
from .serializers import AyatSerializer,QuranSerializer,EidSerializer,RamzanHadeesSerializer,SehrHadeesSerializer,IftarHadeesSerializer,LailaTulQadarHadeesSerializer,HadeesSerializer,DuaSerializer


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

