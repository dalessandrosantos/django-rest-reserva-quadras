from django.urls import path
from .views import QuadraListCreateView

urlpatterns = [
    path('quadras/', QuadraListCreateView.as_view(), name='quadra-list-create'),
]
