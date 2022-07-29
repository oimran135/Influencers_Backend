from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user: User):
        token =  super().get_token(user)
        token['name'] = user.username
        token['email'] = user.email
        token['user_id'] = user.id
        token["is_staff"] = user.is_staff
        token["is_superuser"] = user.is_superuser
        
        return token