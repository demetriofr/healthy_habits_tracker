from rest_framework.serializers import ModelSerializer

from .models import Habit
from .validators import (RewardOrRelatedHabitValidator,
                         ExecutionTimeValidator,
                         RelatedHabitIsPleasantTrueValidator,
                         PleasantHabitIsNotRewardOrRelatedHabitValidator,
                         PeriodicityIsNotZeroOrAboveSevenDaysValidator)


class HabitSerializer(ModelSerializer):
    """Serializer for Habit model."""

    class Meta:
        model = Habit
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}  # read-only field for user id in the request
        validators = [
            RewardOrRelatedHabitValidator(),
            ExecutionTimeValidator(),
            RelatedHabitIsPleasantTrueValidator(),
            PleasantHabitIsNotRewardOrRelatedHabitValidator(),
            PeriodicityIsNotZeroOrAboveSevenDaysValidator()
        ]
