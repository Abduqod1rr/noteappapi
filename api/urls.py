from django.urls import path ,include
from . import views
from drf_spectacular.views import SpectacularAPIView ,SpectacularSwaggerView 

urlpatterns = [
    path('',include('rest_framework.urls')),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("register/", views.Reister.as_view(), name="register"),
    path("writenote/", views.WriteNote.as_view(), name="writenote"),
    path("crud-note/", views.CrudNote.as_view(), name="crud-note"),
    path("docs/", SpectacularSwaggerView.as_view(url_name='schema'), name="swagger-ui")

]
