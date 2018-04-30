from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Cart, Product
from .serializers import UserSerializer, CartSerializer, ProductSerializer
from django.http import Http404

# Create your views here.

class UserList(APIView):
	def get(self, request):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
	def get_object(self, pk):
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		user = self.get_object(pk)
		serializer = UserSerializer(user)
		return Response(serializer.data)

	def patch(self, request, pk):
		user = self.get_object(pk)
		serializer = UserSerializer(user, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		user = self.get_object(pk)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class ProductList(APIView):
	def get(self, request):
		products = Product.objects.all()
		serializer = ProductSerializer(products, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
	def get_object(self, pk):
		try:
			return Product.objects.get(pk=pk)
		except Product.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		product = self.get_object(pk)
		serializer = ProductSerializer(product)
		return Response(serializer.data)

	def patch(self, request, pk):
		product = self.get_object(pk)
		serializer = ProductSerializer(product, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		product = self.get_object(pk)
		product.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class CartList(APIView):
	def get(self, request):
		carts = Cart.objects.all()
		serializer = CartSerializer(carts, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = CartSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartDetail(APIView):
	def get_object(self, pk):
		try:
			return Cart.objects.get(pk=pk)
		except Product.DoesNotExist:
			raise Http404

	def get(self, request, pk):
		cart = self.get_object(pk)
		serializer = CartSerializer(cart)
		return Response(serializer.data)

	def patch(self, request, pk):
		cart = self.get_object(pk)
		serializer = CartSerializer(cart, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		cart = self.get_object(pk)
		cart.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)