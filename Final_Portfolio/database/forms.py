from django import forms
from .models import Profile,Professions,About,Educations,Contact,Services,Skills,Experiernces
class ProfileForm(forms.ModelForm):
   class Meta:
        model=Profile
        fields=['firstname','lastname']
        labels={'firstname':'Firstname','lastname':'Lastname'}
        widgets={'firstname':forms.TextInput(attrs={'class':'form-control'}),
        'lastname':forms.TextInput(attrs={'class':'form-control'}),}


class ProfessionsForm(forms.ModelForm):
    class Meta:
        model:Professions
        fields=['professions']
        labels={'professions':'Professions'}
        widgets={'professions':forms.TextInput(attrs={'class':'form-control'}),}

class AboutForm(forms.ModelForm):
    class Meta:
        model:About
        fields=['about']
        labels={'about':'About'}
        widgets={'about':forms.TextInput(attrs={'class':'form-control'}),}


class EducationsForm(forms.ModelForm):
    class Meta:Educations
    fields=['start_date','end_date','institution_name','institution_logo','education','CGPA','Out_of']
    labels={'start_date':'Start Date','end_date':'End Date','institution_name':'Institution Name',
             'institution_logo':'Institution Logo','education':'Education','CGPA':'CGPA','Out_of':'Out Of'}
    widgets={'start_date':forms.DateInput(attrs={'class':'form-control'}),
    'end_date':forms.DateInput(attrs={'class':'form-control'}),
    'institution_name':forms.TextInput(attrs={'class':'form-control'}),
    'institution_logo':forms.ImageInput(attrs={'class':'form-control'}),
    'education':forms.TextInput(attrs={'class':'form-control'}),
    'CGPA':forms.FloatInput(attrs={'class':'form-control'}),
    'Out_of':forms.FloatInput(attrs={'class':'form-control'}),}

class ContactForm(forms.ModelForm):
    class Meta:
        model:Contact
        fields=['phone','email','address']
        labels={'phone':'Phone','email':'Email','address':'Address'}
        widgets={'phone':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.TextInput(attrs={'class':'form-control'}),
        'address':forms.TextInput(attrs={'class':'form-control'}),}


class ServicesForm(forms.ModelForm):
    class Meta:
        model:Services
        fields=['service_name','description']
        labels={'service_name':'Service Name','description':'Description'}
        widgets={'service_name':forms.TextInput(attrs={'class':'form-control'}),
        'description':forms.TextInput(attrs={'class':'form-control'}),}


class SkillsForm(forms.ModelForm):
    class Meta:
        model:Skills
        fields=['skill']
        labels={'skill':'Skill'}
        widgets={'skill':forms.TextInput(attrs={'class':'form-control'}),}



class ExperierncesForm(forms.ModelForm):
    class Meta:
        model:Experiernces
        fields=['start_date','posision','company_name','address','description']
        labels={'start_date':'Start Date','posision':'Posision','company_name':'Company Name','address':'Address','description':'Description'}
        widgets={'start_date':forms.DateInput(attrs={'class':'form-control'}),
        'posision':forms.TextInput(attrs={'class':'form-control'}),
        'company_name':forms.TextInput(attrs={'class':'form-control'}),
        'address':forms.TextInput(attrs={'class':'form-control'}),
        'description':forms.TextInput(attrs={'class':'form-control'}),}