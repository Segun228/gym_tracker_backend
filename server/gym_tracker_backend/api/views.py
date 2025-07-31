from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from .models import Workout, WorkoutExercise, Set, ExerciseTemplate
from .serializers import (
    WorkoutSerializer, WorkoutReadSerializer,
    WorkoutExerciseSerializer, WorkoutExerciseReadSerializer,
    SetSerializer, SetReadSerializer,
    ExerciseTemplateSerializer
)


# ===== ExerciseTemplate Views =====

class ListCreateTemplate(ListCreateAPIView):
    serializer_class = ExerciseTemplateSerializer
    permission_classes = [IsAuthenticated]
    queryset = ExerciseTemplate.objects.all()
    def perform_create(self, serializer):
            serializer.save(user=self.request.user)


class RetrieveUpdateDestroyTemplate(RetrieveUpdateDestroyAPIView):
    serializer_class = ExerciseTemplateSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "template_id"
    queryset = ExerciseTemplate.objects.all()


# ===== Workout Views =====

class WorkoutListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return WorkoutReadSerializer
        return WorkoutSerializer


class WorkoutRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "workout_id"

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return WorkoutReadSerializer
        return WorkoutSerializer


# ===== WorkoutExercise Views =====

class WorkoutExerciseListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WorkoutExercise.objects.filter(
            workout_id=self.kwargs['workout_id'],
            workout__user=self.request.user
        )

    def perform_create(self, serializer):
        workout = get_object_or_404(
            Workout,
            pk=self.kwargs['workout_id'],
            user=self.request.user
        )
        serializer.save(workout=workout)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return WorkoutExerciseReadSerializer
        return WorkoutExerciseSerializer


class WorkoutExerciseRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "exercise_id"

    def get_queryset(self):
        return WorkoutExercise.objects.filter(
            pk=self.kwargs['exercise_id'],
            workout__user=self.request.user
        )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return WorkoutExerciseReadSerializer
        return WorkoutExerciseSerializer


# ===== Set Views =====

class SetListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Set.objects.filter(
            workout_exercise_id=self.kwargs['exercise_id'],
            workout_exercise_id__workout__user=self.request.user
        )

    def perform_create(self, serializer):
        exercise = get_object_or_404(
            WorkoutExercise,
            pk=self.kwargs['exercise_id'],
            workout__user=self.request.user
        )
        serializer.save(workout_exercise=exercise)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SetReadSerializer
        return SetSerializer


class SetRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "set_id"

    def get_queryset(self):
        return Set.objects.filter(
            pk=self.kwargs['set_id'],
            workout_exercise_id__workout__user=self.request.user
        )

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SetReadSerializer
        return SetSerializer