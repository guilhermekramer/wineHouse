import json
from django.http import JsonResponse
from ..models.wineModel import Wine
from ..serializers.wineSerializer import WineSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(["GET"])
def wine_list(request):

    if (request.method) == "GET":
        wines = Wine.objects.all()
        serializer = WineSerializer(wines, many=True)
        return JsonResponse({"Winery": serializer.data})


@api_view(["POST"])
def create_wine(request):
    if (request.method) == "POST":
        serializer = WineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def wine_detail(request, id):

    try:
        wine = Wine.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = WineSerializer(wine)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def find_wine(request):
    try:
        data = json.loads(request.body)
        name = data.get("name", "")
        keywords = data.get("keywords", "")

        print("Nome: ", name)
        print("keywords: ", keywords)

        if name:
            wine = Wine.objects.get(name__iexact=name)
            serializer = WineSerializer(wine)
            return Response(serializer.data)

        else:
            wines = Wine.objects.filter(name__icontains=keywords) | Wine.objects.filter(
                description__icontains=keywords
            )
            serializer = WineSerializer(wines, many=True)
            return Response(serializer.data)

    except Exception as e:
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["PUT"])
def update_wine(request, id):
    try:
        wine = Wine.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = WineSerializer(wine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["DELETE"])
def delete_wine(request, id):
    try:
        wine = Wine.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        wine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
