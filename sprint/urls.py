from django.urls import path 
from .views import SprintListView, SprintCreate, SprintViewSet, SprintUpdate, SprintDeleteView, SprintDetail    

urlpatterns = [
    path('', SprintListView.as_view(), name='sprints'),
    path('sprint-create/', SprintCreate.as_view(), name='sprint_form'), 
    path('sprint/<int:pk>/', SprintDetail.as_view(), name='sprint_detail'),
    path('sprint-update/<int:pk>/', SprintUpdate.as_view(), name='sprint_update'), 
    path('sprint-delete/<int:pk>/', SprintDeleteView.as_view(), name='sprint_delete'),

]