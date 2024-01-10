from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from bson.json_util import dumps
import json
from .serializer import ProductSerializer
from .models import product_collection


# POST one Product or GET All Products
class ProductView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product_instance = serializer.save()
            
            # Get UUID of each product
            uid = product_instance.id
            # Get the image url
            url = product_instance.image.url
            # store request data as dictionary
            data = dict(request.data)
            # Remove the image as will strore image url
            data.pop('image')
            # Set the UUID and Image url to data
            data["_id"] = str(uid)
            data["url"] = url
            #Insert the data into collection
            product_collection.insert_one(data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            product_list = product_collection.find()
            data = json.loads(dumps(product_list))
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class ProductViewByIds(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            product = product_collection.find_one({"_id": pk})
            data = json.loads(dumps(product))
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        # Incase of changes in image
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            productInstance = serializer.save()
            product_data = dict(request.data)
            product_data.pop('image')
            product_data['url'] = productInstance.image.url
            
            product_collection.update_one({"_id": pk}, {"$set": product_data})
            return Response({"message": "Product Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request, pk):
        try:
            product_collection.delete_one({"_id": pk})
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)