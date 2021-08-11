from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name="quotepage"),
    path('generate/', views.generateQuote, name="generatequote"),
    path('translate/<id>/<lang>', views.translate, name="tanslateQuote"),
]
