"""showMovieNames URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from . import view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #安卓
    url(r'^getStore/',view.getStore),
    url(r'^getFood/',view.getFood),
    url(r'^getShoppingCar/',view.getShoppingCar),
    url(r'^getUser/',view.getUser),
    url(r'^getServe/',view.getServe),
    url(r'^setUser/',view.setUser),
    url(r'^insertShoppingCar/',view.insertShoppingCar),
    url(r'^deleteShoppingCar/',view.deleteShoppingCar),
    url(r'^updateShoppingCar/',view.updateShoppingCar),
    #学习app
    url(r'^works/',include('works.urls'))
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
