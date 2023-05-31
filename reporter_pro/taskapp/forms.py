from django import forms
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tasks,Leave_apply


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class TaskForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = Tasks
        fields = ['tid', 'user', 'desc', 'start_date', 'end_date']# field which you want to show for now status not shown for admin
        widgets = {
            'tid': forms.NumberInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            #'status': forms.Select(attrs={'class': 'form-control'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields= ['status']
        widgets={
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class ApplyLeaveForm(forms.ModelForm):
    class Meta:
        model = Leave_apply
        exclude=('status','user','lid',)
        fields='__all__'
        

class LeaveApprovalForm(forms.ModelForm):
    class Meta:
        model = Leave_apply
        fields= ['status']
        widgets={
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

