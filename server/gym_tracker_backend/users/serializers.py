from rest_framework.serializers import ModelSerializer
from users.models import AppUser


class AppUserSerializer(ModelSerializer):
    class Meta:
        model = AppUser
        fields = ["username", "vk_user_id", "height", "weight" ]