from django.shortcuts import render
from .forms import UserInfo, CompanyInfo
from formtools.wizard.views import SessionWizardView

class FormWizardView(SessionWizardView):
    template_name = "wizard_form.html"
    form_list = [UserInfo, CompanyInfo]

    def done(self, form_list, **kwargs):
        user_form = form_list[0]
        user = user_form.save()
        company_model = form_list[1].save(commit=False)
        company_model.user = user
        company_model.save()
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })