from django.urls import path

from .views import homePageView, passwordUpdateSuccessView, transferView, createAccountView, accountCreateSuccessView, updatePasswordView

urlpatterns = [
    path('', homePageView, name='home'),
    path('transfer/', transferView, name='transfer'),
    # path('createaccount/', createAccountView, name='createaccount'),
    path('createaccount/', createAccountView, name='createaccount'),
    path('accountcreatesuccess/', accountCreateSuccessView, name="accountcreated"),
    path('updatepassword/', updatePasswordView, name="updatepassword"),
    path('passwordupdatesuccess/', passwordUpdateSuccessView, name="passwordupdated")
]
