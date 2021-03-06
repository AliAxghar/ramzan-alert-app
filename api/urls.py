from django.urls import path, include
from . import views
from fcm_django.api.rest_framework import FCMDeviceViewSet
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view()

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
router.register('devices', FCMDeviceViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('swagger-docs/', schema_view),
]
