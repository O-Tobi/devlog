from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status



# The register/signup view
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

# Logout endpoint view
class LogoutView(generics.APIView):
    # allow only authenticated user to call this function
    permission_classes = (IsAuthenticated,)

    # get refresh token from the client
    def post( self, request):
        try:

            refresh_token = request.data.get("refresh")

            # convert the token string into a proper SimpleJWT RefreshToken object
            token = RefreshToken(refresh_token)

            # blacklist the token to prevent future use
            token.blacklist()

            # return a success response to the client
            return Response({"status": "Success"}, status=status.HTTP_205_RESET_CONTENT)
        #handle errors if the token is invalid or expired
        except Exception as e:
            return Response({"status": "Failed", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
