from rest_framework.serializers import ValidationError

from .models import Habit


class RewardOrRelatedHabitValidator:
    """Class to validate that only one of reward or related habit is set."""

    def __call__(self, data):
        if data.get('reward') and data.get('related_habit'):
            raise ValidationError('Only one of reward or related habit can be set.')


class ExecutionTimeValidator:
    """Class to validate that execution time is don't be above 120 seconds."""

    def __call__(self, data):
        execution_time = data.get('execution_time')
        if execution_time is not None:
            if data.get('execution_time') > 120:
                raise ValidationError('Execution time is don\'t be above 120 seconds.')


class RelatedHabitIsPleasantTrueValidator:
    """Class to validate that the related habit 'is_pleasant' field is True."""

    def __call__(self, data):
        related_habit = data.get('related_habit')
        if related_habit is not None:
            pleasant_habit = Habit.objects.filter(pk=related_habit.id, is_pleasant=True)
            if not pleasant_habit.exists():
                raise ValidationError('Related habit must have the \'is_pleasant\' field set to True.')


class PleasantHabitIsNotRewardOrRelatedHabitValidator:
    """Class to validate that pleasant habit doesn't have reward or related habit."""

    def __call__(self, data):
        if data.get('is_pleasant'):
            if data.get('reward') or data.get('related_habit'):
                raise ValidationError('Pleasant habit must not have reward or related habit.')


class PeriodicityIsNotZeroOrAboveSevenDaysValidator:
    """Class to validate that periodicity is not above 7 days."""

    def __call__(self, data):
        periodicity = data.get('periodicity')
        if periodicity is not None:
            if periodicity > 7 or periodicity < 1:
                raise ValidationError('Periodicity is not 0 or above 7 days.')
