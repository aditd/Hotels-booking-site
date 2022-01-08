from django.urls import path

from . import views

app_name='hotels'

urlpatterns = [
    #path('', views.all_hotels_view, name='search'),
    path('<int:my_id>/', views.details_view, name='details')
]
