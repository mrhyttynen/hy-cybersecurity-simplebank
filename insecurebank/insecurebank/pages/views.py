from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from .models import Account

def createAccountView(request):
	
	if request.method == 'POST':
		request_username = request.POST.get('username')
		try:
			print("CREATING ACCOUNT")
			# FIX A02
			# user = User.objects.create_user(username=request_username, password=request.POST.get('password'))
			user = User.objects.create_user(username=request_username, password="12345")
			Account.objects.create(user=user, balance=100)
			return redirect('/accountcreatesuccess/')
		except IntegrityError:
			return render(request, 'pages/accountCreateFailed.html', {'username': request_username})
	else:
		return redirect('/')

def accountCreateSuccessView(request):
	return render(request, 'pages/accountCreateSuccess.html')

@login_required
def updatePasswordView(request):
	if request.method == 'POST':
		new_password = request.POST.get('newpassword')
		request_username = request.user.username
		user = User.objects.get(username=request_username)
		print("UPDATING PASSWORD FOR", request_username, "as", new_password)
		try:
			user.set_password(new_password)
			user.save()
			return redirect('/passwordupdatesuccess/')
		except:
			return render(request, 'pages/passwordUpdateFailed.html', {'username': request_username})
	else:
		return redirect('/')

def passwordUpdateSuccessView(request):
	return render(request, 'pages/passwordUpdateSuccess.html')

def transfer(sender_name, receiver_name, amountRaw):
	with transaction.atomic():

		sender_acc = Account.objects.get(user__username=sender_name)
		receiver_acc = Account.objects.get(user__username=receiver_name)

		# validation
		if amountRaw < 0 or sender_acc == receiver_acc or sender_acc.balance - amountRaw < 0:
			amount = 0
		else:
			amount = amountRaw

		sender_acc.balance -= amount
		receiver_acc.balance += amount

		sender_acc.save()
		receiver_acc.save()

# login_url="/accounts/login" (default param)
@login_required
def transferView(request):
	
	if request.method == 'POST':
		print("POSTING")
		sender_name = request.user.username
		receiver_name = request.POST.get('to')
		amount = int(request.POST.get('amount'))
		print(amount, "from", sender_name, "to", receiver_name)
		transfer(sender_name, receiver_name, amount)
	
	return redirect('/')

# login_url="/accounts/login"
@login_required
def homePageView(request):
	accounts = Account.objects.exclude(user_id=request.user.id)
	return render(request, 'pages/index.html', {'accounts': accounts})
