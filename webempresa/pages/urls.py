from django.urls import path
from . import views

urlpatterns = [
    #path del core
    path("<int:page_id>/<slug:page_slug>/", views.page, name='page')
]