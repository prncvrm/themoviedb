from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class AccountManager(BaseUserManager):
	def create_user(self, email, password=None, **kwargs):
		if not email:
			raise ValueError('User must have a valid email address.')

		if not kwargs.get('username'):
			raise ValueError('User must have a valid username.')

		account = self.model(
			email=self.normalize_email(email), username=kwargs.get('username')
			)

		account.set_password(password)
		account.save()

		return account


class Account(AbstractBaseUser):
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=40,unique=True)

	name = models.CharField(max_length=60,blank=True)

	created_at = models.DateTimeField(auto_now_add=True)

	objects = AccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __unicode__(self):
		return self.email

	def get_name(self):
		return self.name;

