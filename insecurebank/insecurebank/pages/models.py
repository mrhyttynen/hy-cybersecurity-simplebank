from django.db import models

from django.contrib.auth.models import User

from django_cryptography.fields import encrypt

# after any change to the code in this file, run 
# python3 ./manage.py makemigrations
# then
# python3 manage.py migrate
# before running the server again

class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# A02-2: sensitive data stored in unencrypted format
	email = models.CharField(max_length=100)
	balance = models.IntegerField()
	# A02-2 FIX: encrypting the data using symmetric key
	# email = encrypt(models.CharField(max_length=100))
	# balance = encrypt(models.IntegerField())
