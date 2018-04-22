from django import forms

# our new form
class TeacherLoginForm(forms.Form):
    courseCode = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)


class TeacherRegisterForm(forms.Form):
    name = forms.CharField(required=True)
    courseCode = forms.CharField(required=True)
    course = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

class StudentLoginForm(forms.Form):
    prn= forms.CharField(required=True)
    password= forms.CharField(widget=forms.PasswordInput)

class StudentRegisterForm(forms.Form):
    prn= forms.CharField(required=True)
    name= forms.CharField(required=True)
    email= forms.EmailField(required=True)
    password= forms.CharField(widget=forms.PasswordInput)
