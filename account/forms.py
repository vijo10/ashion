from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account,UserProfile

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name','phone_number', 'password1', 'password2')

    def __init__(self,*args,**kwargs):
        super(MyUserCreationForm, self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder']="Enter First Name" 
        self.fields['last_name'].widget.attrs['placeholder']="Enter Last Name" 
        self.fields['email'].widget.attrs['placeholder']="Enter Email" 
        self.fields['phone_number'].widget.attrs['placeholder']="Enter Phone Number" 
        self.fields['password1'].widget.attrs['placeholder']="Enter Password" 
        self.fields['password2'].widget.attrs['placeholder']="Re-Enter Password" 
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'

class UserForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=('first_name','last_name','phone_number')
    def __init__(self,*args,**kwargs):
        super(UserForm, self).__init__(*args,**kwargs)  
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'  

class UserProfileForm(forms.ModelForm):
    profile_pic=forms.ImageField(required=False,error_messages={'invalid':('Image File Only')}, widget=forms.FileInput)
    class Meta:
        model=UserProfile
        fields=('address_line_1','address_line_2','city','state','country','profile_pic')
    def __init__(self,*args,**kwargs):
        super(UserProfileForm, self).__init__(*args,**kwargs)  
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'     