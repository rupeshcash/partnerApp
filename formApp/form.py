from django import forms
from formApp import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PartnerForm(forms.ModelForm):
    class Meta:
        model = models.Partner
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

class FacultyForm(forms.ModelForm):
    class Meta:
        model = models.Faculty
        fields = ['name', 'subject', 'experience', 'rating']
    def __init__(self, *args, **kwargs):
    		super(FacultyForm,self).__init__(*args, **kwargs)
    		for name, field in self.fields.items():
    			field.widget.attrs.update({'class':
    				'input'})

class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ['name', 'description', 'fee']
    def __init__(self, *args, **kwargs):
    		super(CourseForm,self).__init__(*args, **kwargs)
    		for name, field in self.fields.items():
    			field.widget.attrs.update({'class':
    				'input'})