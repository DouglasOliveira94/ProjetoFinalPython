from django.contrib import admin
from django.urls import path
from stock_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('prediction/', views.prediction, name='prediction'),
]
