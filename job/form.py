from django.forms import ModelForm
from .models import Apply,Job


class Applyform(ModelForm):
    class Meta:
        model = Apply
        fields = ['name','email','website','cv','cover_letter']


class Jobform(ModelForm):
     class Meta:
         model = Job
         fields = '__all__'
         exclude = ('slug','owner',)