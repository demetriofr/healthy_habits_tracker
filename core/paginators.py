from rest_framework.pagination import PageNumberPagination


class HabitsListPagination(PageNumberPagination):
    """Custom pagination class for Habits list."""

    page_size = 5
