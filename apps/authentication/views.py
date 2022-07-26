from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
import logging
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


def response_json(status=200, data=None, message=None):
    return {
        "data":data,
        "message":message,
        "status":status
    }

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class TestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "Hello World!"})


logger = logging.getLogger(__name__)


class LogoutView(APIView):
    """Logout view class.

    This view logouts the logged user and expires the user token.

    Parameters
    ----------
    APIView : rest_framework.views
    """

    permission_classes = (IsAuthenticated,)

    # pylint: disable=R0201
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "refresh_token": openapi.Schema(type=openapi.TYPE_STRING, description="user refresh token"),
            },
            responses={
                205: "Reset Content",
                500: "Internal Server Error",
            },
        ),
    )
    def post(self, request):
        """HTTP POST request.

        A HTTP api endpoint that logouts the user.

        Parameters
        ----------
        request : django.http.request

        Returns
        -------
        rest_framework.response.Response
            returns success message if user successfully logouts, error message otherwise
        """
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as err:
            message = "Error occurred while logging out the user."
            logger.exception(message, str(err))
            return Response(
                response_json(status=False, data=None, message=message), status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        else:
            return Response(
                response_json(status=True, data=None, message="User logout successfully."),
                status=status.HTTP_205_RESET_CONTENT,
            )
