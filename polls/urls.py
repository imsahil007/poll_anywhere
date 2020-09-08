
from django.urls import path
from . import views
from .views import PollCreateView, PollDeleteView, PollDeleteView, PollUpdateView,PollDetailView
urlpatterns = [
    path('poll/new',PollCreateView.as_view(), name='poll-create'),
    path('',views.home, name='home'),
    # path('user/<str:username>',PollListView.as_view(), name='user-poll'),
    path('poll/<str:link>',PollDetailView.as_view(), name='poll-detail'),
    path('poll/<str:link>/result',PollDetailView.as_view(), name='poll-result'),
    path('poll/<int:pk>/delete',PollDeleteView.as_view(), name='poll-delete'),
    path('poll/<int:pk>/update',PollUpdateView.as_view(), name='poll-update'),
]
