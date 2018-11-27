from rest_framework import permissions, viewsets

from authentication.models import Account
from authentication.permissions import IsAccountOwner
from authentication.serializers import AccountSerializer

from django.shortcuts import render

# Create your views here.


class AccountViewSet(viewsets.ModelViewSet):
	lookup_field = 'username'
	queryset = Account.objects.all()
	serializer_class = AccountSerializer

	def get_permissions(self):
		if self.request.method in permissions.SAFE_METHODS:
			return (permissions.AllowAny(),)

		if self.request.method == 'POST':
			return (permissions.AllowAny(),)

		return (permissions.IsAuthenticated(), IsAccountOwner(),)

	def create(self,request):
		serializers = self.serializer_class(data=request.data)

		if serializers.is_valid():
			Account.objects.create_user(**serializers.validated_data)

			return Response(serializers.validated_data,status=status.HTTP_201_CREATED)

		return Response({
			'status': 'Bad request',
			'message': 'Account Could not be created with received data.'
			},status=status.HTTP_400_BAD_REQUEST)
