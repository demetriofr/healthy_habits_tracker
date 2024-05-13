from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from .models import Habit
from .serializers import HabitSerializer
from .paginators import HabitsListPagination
from .permissions import IsOwnerCRUDEnabled


class HabitCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """Create a new Habit object with the current user's id."""

        serializer.save(user=self.request.user)


class HabitsOwnerListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitsListPagination

    def get_queryset(self):
        """Return a queryset of Habit objects filtered by the current user's id."""

        return Habit.objects.filter(user=self.request.user.id)


class HabitsListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitsListPagination

    def get_queryset(self):
        """Return a queryset of Habit objects filtered by the 'is_public' field."""

        return Habit.objects.filter(is_public=True)


class HabitUpdateAPIView(UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerCRUDEnabled]


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerCRUDEnabled]
