from django.db import models
from users.models import AppUser
import datetime

class ExerciseTemplate(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='exercise_templates')
    name = models.CharField(max_length=100, null=False, blank=False, default="Exercise")
    muscle_group = models.CharField(max_length=100, default="Muscle")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'шаблон упражнения'
        verbose_name_plural = 'шаблоны упражнений'

    def __str__(self):
        return self.name


class Workout(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='workouts')
    date = models.DateField(auto_now_add=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.TimeField(default=datetime.time(0, 0))
    updated_at = models.DateTimeField(auto_now=True)
    callories_burnt = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'тренировка'
        verbose_name_plural = 'тренировки'

def __str__(self):
    return f"Exercise for workout on {self.workout.date}"


class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='workout_exercises')
    template = models.ForeignKey(ExerciseTemplate, on_delete=models.CASCADE, related_name='workout_exercise')
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'упражнение'
        verbose_name_plural = 'упражнения'

    def __str__(self):
        return f"{self.template.name} (Workout #{self.workout})"


class Set(models.Model):
    workout_exercise = models.ForeignKey(WorkoutExercise, on_delete=models.CASCADE, related_name='sets')
    weight = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    duration = models.TimeField(default=datetime.time(0, 0), null=True, blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'подход'
        verbose_name_plural = 'подходы'

    def __str__(self):
        return f"Set"