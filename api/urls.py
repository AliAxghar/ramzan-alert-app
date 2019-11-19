from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ayat', views.AyatViewSet)
router.register('dua', views.DuaViewSet)
router.register('hadees', views.HadeesViewSet)
router.register('quran', views.QuranViewSet)
router.register('ramzan', views.RamzanHadeesViewSet)
router.register('ramzan-sehr',views.SehrHadeesViewSet)
router.register('ramzan-iftar', views.IftarHadeesViewSet)
router.register('ramzan-laila-tul-qadar', views.LailaTulQadarHadeesViewSet)
router.register('eid', views.EidViewSet)

urlpatterns = [
    path('', include(router.urls))
]