from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import transaction
from .models import Account

def createAccountView(request):
	
	if request.method == 'POST':
		print("CREATING ACCOUNT")
		user = User.objects.create_user(username=request.POST.get('username'), password=request.POST.get('password'))
		# user.save() # may not be needed
		Account.objects.create(user=user, balance=100)
	
	return redirect('/accountCreateSuccess/')

def accountCreateSuccessView(request):
	return render(request, 'pages/accountCreateSuccess.html')

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
