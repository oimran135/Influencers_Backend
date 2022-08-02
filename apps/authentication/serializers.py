from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from .models import Influencer, User


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

class InfluencerSerializer(ModelSerializer):

    class Meta:
        model = Influencer
        fields = '__all__'