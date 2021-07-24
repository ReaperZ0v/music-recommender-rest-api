from rest_framework.views import APIView
from accounts.models import Account 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status 
from . import serializers 
from . import models 
import joblib

# Create your views here.
class RecommenderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        loaded_model = joblib.load('./model/music-recommender.joblib')
        authenticated_user = self.request.user

        if authenticated_user.gender == "Male":
            predictions1 = loaded_model.predict([
                [authenticated_user.age, 1]
            ])

            recommendations1 = models.Album.objects.filter(genre=predictions1[0])
            serializer1 = serializers.RecommenderSerializer(recommendations1, many=True)

            return Response(serializer1.data, status=status.HTTP_200_OK)

        else:
            predictions2 = loaded_model.predict([
                [authenticated_user.age, 0]
            ])

            recommendations2 = models.Album.objects.filter(genre=predictions2[0])
            serializer2 = serializers.RecommenderSerializer(recommendations2, many=True)

            return Response(serializer2.data, status=status.HTTP_200_OK)

