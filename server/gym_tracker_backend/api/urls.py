from django.urls import path
from api.views import (
    ListCreateTemplate, 
    RetrieveUpdateDestroyTemplate, 
    WorkoutListCreateView,
    WorkoutRetrieveUpdateDestroyView,
    WorkoutExerciseListCreateView,
    WorkoutExerciseRetrieveUpdateDestroyView,
    SetListCreateView,
    SetRetrieveUpdateDestroyView
)


urlpatterns = [
    path('workouts/', WorkoutListCreateView.as_view(), name='workout-list'),
    path('workouts/<int:workout_id>/', WorkoutRetrieveUpdateDestroyView.as_view(), name='workout-detail'),

    path('workouts/<int:workout_id>/exercises/', WorkoutExerciseListCreateView.as_view(), name='exercise-list'),
    path('workouts/<int:workout_id>/exercises/<int:exercise_id>/', WorkoutExerciseRetrieveUpdateDestroyView.as_view(), name='exercise-update-destroy'),

    path('workouts/<int:workout_id>/exercises/<int:exercise_id>/sets/', SetListCreateView.as_view(), name='set-list'),
    path('workouts/<int:workout_id>/exercises/<int:exercise_id>/sets/<int:set_id>/', SetRetrieveUpdateDestroyView.as_view(), name='set-update-destroy'),

    path('templates/', ListCreateTemplate.as_view(), name='template-list'),
    path('templates/<int:template_id>/', RetrieveUpdateDestroyTemplate.as_view(), name='template-detail'),
]