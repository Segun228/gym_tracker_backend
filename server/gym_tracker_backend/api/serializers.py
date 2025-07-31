from rest_framework import serializers
from .models import ExerciseTemplate, Workout, WorkoutExercise, Set






class ExerciseTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseTemplate
        fields = ["name", "muscle_group"]


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ["weight", "reps", "duration", "order"]


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercise
        fields = ["template", "workout", "order"]


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ["note", "duration"]






class SetReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ["weight", "reps", "duration", "order", "created_at"]


class WorkoutExerciseReadSerializer(serializers.ModelSerializer):
    sets = SetReadSerializer(many=True, read_only=True)
    template = ExerciseTemplateSerializer(source="template_id", read_only=True)

    class Meta:
        model = WorkoutExercise
        fields = ["template", "order", "sets", "created_at"]


class WorkoutReadSerializer(serializers.ModelSerializer):
    workout_exercises = WorkoutExerciseReadSerializer(many=True, read_only=True)

    class Meta:
        model = Workout
        fields = ["note", "duration", "workout_exercises", "created_at"]