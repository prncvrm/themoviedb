from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from authentication.models import Account

class AccountSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=False)
	confirm_password = serializers.CharField(write_only=True, required=False)

	class Meta:
			model = Account
			fields = ('id','email','username','created_at','name','password','confirm_password',)
			read_only_fields = ('created_at')

			def create(self, validated_data):
				return Account.objects.create(**validated_data)
