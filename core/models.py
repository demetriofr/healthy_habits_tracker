from django.db import models

from config.settings import AUTH_USER_MODEL, NULLABLE


class Habit(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.CharField(max_length=100, verbose_name='время')
    action = models.CharField(max_length=150, verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='связанная привычка')
    periodicity = models.PositiveSmallIntegerField(default=1, verbose_name='периодичность')
    reward = models.CharField(max_length=150, verbose_name='вознаграждение', **NULLABLE)
    execution_time = models.PositiveSmallIntegerField(verbose_name='время выполнения')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        """
        Return a string representation of the object.

        Returns:
            str: The string with user, action, time and place.
        """
        return f'{self.user} - {self.action} - {self.time} - {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
