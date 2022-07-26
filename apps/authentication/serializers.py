from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user: User):
        token =  super().get_token(user)
        token['name'] = user.username
        token['email'] = user.email
        token['user_id'] = user.id
        
        return token