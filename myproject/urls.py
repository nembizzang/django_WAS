"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('b1log/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # include는 특정 app으로 라우팅할 수 있게 해줌
# 사용자가 아래와 같은 경로들로 접속시에 특정 app으로 라우팅된다.
# http://127.0.0.1/
# http://127.0.0.1/app/
# http://127.0.0.1/create/
# http://127.0.0.1/read/1

# 위와 같은 url들을 라우팅하기 위해 urlpatterns에 담아준다.
urlpatterns = [
    path('admin/', admin.site.urls), # http://127.0.0.1/ 이후 admin으로 접속 시 django 관리자 모드로 위임
    path('', include('myapp.urls')) # http://127.0.0.1/ 이후 어떤 경로던지 접속 시 myapps의 urls.py로 위임
]