from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Player, Franchise, Team
from .serializers import *


@api_view(['GET', 'POST'])
def players_list(request):
    if request.method == 'GET':
        data = Player.objects.all()

        serializer = PlayerSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
def franchise_list(request):
    if request.method == 'GET':
        data = Franchise.objects.all()

        serializer = FranchiseSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
def team_list(request):
    if request.method == 'GET':
        data = Team.objects.all()

        serializer = TeamSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
