from django.urls import include, path
from rest_framework import routers
from user import views

router = routers.DefaultRouter()
router.register(r'user', views.RestUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]