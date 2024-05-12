from django.urls import path

from .apps import CoreConfig
from .views import (
    HabitCreateAPIView,
    HabitsOwnerListAPIView,
    HabitsListAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView
)

app_name = CoreConfig.name


urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('my_habits/', HabitsOwnerListAPIView.as_view(), name='my_habits-list'),
    path('habits/', HabitsListAPIView.as_view(), name='habits-list'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),
]
