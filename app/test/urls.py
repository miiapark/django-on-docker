from django.urls import path, re_path, include
from test import views
from rest_framework.routers import DefaultRouter

app_name = "test"

router = DefaultRouter()
router.register("msg", views.TestViewSet)


urlpatterns = [
    re_path(r"^test/", include(router.urls)),

]
