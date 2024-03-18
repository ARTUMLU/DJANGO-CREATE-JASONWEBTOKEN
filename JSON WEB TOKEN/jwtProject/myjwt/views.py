from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import status
from django.contrib.auth import authenticate

class LoginView(APIView):
    def post(self, request):
        # Kullanıcı adı ve parolayı alın
        username = request.data.get('username')
        password = request.data.get('password')

        # Kullanıcıyı doğrula
        user = authenticate(username=username, password=password)
        if user:
            # Kullanıcı doğrulandıysa JWT oluştur
            access_token = AccessToken.for_user(user)
            return Response({'access_token': str(access_token)}, status=status.HTTP_200_OK)
        else:
            # Kullanıcı doğrulanamadıysa hata mesajı döndür
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
