from django.contrib import admin
from django.urls import path,include
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Cliente.urls',namespace="servicios"))
]
