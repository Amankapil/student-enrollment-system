from django import forms


class stude(forms.Form):
    Name = forms.CharField(max_length=33)
    enrollment_no = forms.IntegerField()



class searchF(forms.Form):
    Name = forms.CharField(max_length=33)