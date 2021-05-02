from django import forms
from .models import Donor





class donorForm(forms.ModelForm):

    class Meta:
        model = Donor
        fields = ('fullname','address','mobile','bloodgroup','medicalproblem')
        labels = {
            'fullname':'Full Name',
            #'_code':'EMP. Code'
        }

    def __init__(self, *args, **kwargs):
        super(donorForm,self).__init__(*args, **kwargs)
        self.fields['medicalproblem'].empty_label = "Select"
        #self.fields['emp_code'].required = False

from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=("caption","image")
        widgets={'image' : forms.FileInput(attrs={'required':True}),
}
