from django.urls import path

from .views import homePageView, transferView, createAccountView, accountCreateSuccessView

urlpatterns = [
    path('', homePageView, name='home'),
    path('transfer/', transferView, name='transfer'),
    # path('createaccount/', createAccountView, name='createaccount'),
    path('createaccount/', createAccountView, name='createaccount'),
    path('accountCreateSuccess/', accountCreateSuccessView, name="accountcreated")
]
