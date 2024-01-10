from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import UserSerializer

# On / path
class HomeView(APIView):
    def get(self, request):
        return Response({"message":"Welcome to HomeView"}, status = status.HTTP_200_OK)

# on /accounts/auth/ path
class UserLoginLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            return Response({'error' : 'Refresh token not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message':'Loged out successfully'}, status=status.HTTP_200_OK)


#on /accounts/register/
class UserRegistrationsView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status = status.HTTP_400_BAD_REQUEST)