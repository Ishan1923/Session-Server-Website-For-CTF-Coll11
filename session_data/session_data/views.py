from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import SessionData
from .serializers import SessionDataSerializer   

from django.shortcuts import render


class UpdateSessionData(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(request.data)
        team_name = request.data.get('team_name')
        team_score = request.data.get('team_score')
        questions_answered = request.data.get('questions_answered')

        if not all([team_name, team_score, questions_answered]):
            return Response({"error": "Null or invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        team, created = SessionData.objects.update_or_create(
            team_name=team_name,
            defaults={
                "team_score": team_score,
                "questions_answered": questions_answered
            }
        )

        return Response({"message": "data updated successfully"}, status=status.HTTP_200_OK)


class SessionDataView(ListAPIView):
    permission_classes = [AllowAny]
    def get(self, request):
        team_name = request.query_params.get('team_name')
        if team_name:
            try:
                session_data = SessionData.objects.get(team_name=team_name)
                serializer = SessionDataSerializer(session_data)
                wrapped_data = {
                    "items": [serializer.data]
                }
                return Response(wrapped_data, status=status.HTTP_200_OK)
            except SessionData.DoesNotExist:
                return Response({"error": "Team not found."}, status=status.HTTP_404_NOT_FOUND)
            
        else:
            # If no team is specified, return all session data
            session_data = SessionData.objects.order_by('-team_score')
            serializer = SessionDataSerializer(session_data, many=True)
            wrapped_data = {
                "items": serializer.data
            }   
            return Response(wrapped_data, status=status.HTTP_200_OK)


# class SessionDataDetail(APIView):
#     permission_classes = [AllowAny]

#     def get(self, request, team_name):
#         try:
#             # Retrieve the session data for the given team_name.
#             session_data = SessionData.objects.get(team_name=team_name)
#         except SessionData.DoesNotExist:
#             return Response(
#                 {"error": "Team not found."}, 
#                 status=status.HTTP_404_NOT_FOUND
#             )
        
#         # Serialize the data.
#         serializer = SessionDataSerializer(session_data)
        
#         # Optionally, if you want to wrap the object in a key (e.g., "item"), you could do:
#         # return Response({"item": serializer.data}, status=status.HTTP_200_OK)
#         # For simplicity with Unity's JsonUtility, return the object directly.
#         return Response(serializer.data, status=status.HTTP_200_OK)

    