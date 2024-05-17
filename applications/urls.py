from django.urls import path

from applications.forms import UserInfo, CompanyInfo
from applications.views import FormWizardView

urlpatterns = [
    path('contact/', FormWizardView.as_view([UserInfo, CompanyInfo])),
]