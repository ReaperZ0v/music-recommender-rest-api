from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from . import serializers 
from . import models 

# Create your views here.
class RegistrationAPIView(APIView):
    serializer_class = serializers.AccountSerializer

    def get(self, request):
        message = "Welcome to the Music Recommender, Sign up to get started!"
        return Response(message, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(f"Thank you for signing up {serializer.validated_data['first_name']}!")

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)