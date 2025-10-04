from django.urls import path ,include
from . import views

urlpatterns = [
    path('',include('rest_framework.urls')),
    path("register/", views.Reister.as_view(), name="register"),
    path("writenote/", views.WriteNote.as_view(), name="writenote"),
    path("crud-note/", views.CrudNote.as_view(), name="crud-note"),

]
