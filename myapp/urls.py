from django.urls import path
from myapp import views # 내가 만든 views 내부의 함수를 이용하도록 import
urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>/', views.read), # <>로 들어오는 부분은 변수로 가변적이다.
    path('delete/', views.delete),
    path('update/<id>/', views.update)
]
