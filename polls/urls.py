
from django.urls import path
from . import views
from .views import PollDeleteView, PollDeleteView, PollUpdateView, UserPollListView
urlpatterns = [
    path('poll/new/',views.add_poll, name='poll-create'),
    path('',views.home, name='home'),
    path('user/<str:username>/',UserPollListView.as_view(), name='user-polls'),
    path('poll/<str:link>/',views.poll_detail, name='poll-detail'),
    path('poll/<str:link>/result/',views.result, name='poll-result'),
    path('poll/<int:pk>/delete/',PollDeleteView.as_view(), name='poll-delete'),
    path('poll/<int:pk>/update/',PollUpdateView.as_view(), name='poll-update'),
]
