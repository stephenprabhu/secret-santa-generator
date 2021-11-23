from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name="main"

urlpatterns = [
    path('',TemplateView.as_view(template_name='main/home.html'),name='all'),
    path('manage/',views.PersonListView.as_view(),name='list'),
    path('members/add/',views.PersonCreateView.as_view(),name='add'),
    path('members/<int:pk>/delete/',views.PersonDeleteView.as_view(),name='remove'),
    path('members/<int:pk>/update/',views.PersonUpdateView.as_view(),name='update'),
    path('members/view/',views.PersonChooseView.as_view(),name='view'),
]