from django.urls import path, include
from rest_framework import routers

from todo import views


router = routers.DefaultRouter()
router.register('category', views.CategoryViewset)
router.register('tache', views.TacheViewset)


urlpatterns = [
    path('', include(router.urls)),
]