from ckeditor.widgets import CKEditorWidget
from django import forms
from courses.models import Course
from university.widgets.DatePickerInput import DatePickerInput


class CourseForm(forms.ModelForm):
    def cleaned_data(self):
        cleaned_data = super(CourseForm, self).clean()
        from_time = cleaned_data.get("started_at")
        end_time = cleaned_data.get("finished_at")

        if from_time and end_time:
            if end_time < from_time:
                raise forms.ValidationError("Дата окончания курса не может быть раньше даты начала")
        return cleaned_data

    class Meta:
        model = Course
        fields = "__all__"
        exclude = ('created_by', 'updated_by')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': CKEditorWidget(config_name='awesome_ckeditor'),
            'preview': forms.FileInput(),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'has_certificate': forms.Select(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'started_at': DatePickerInput(attrs={'class': 'form-control'}),
            'finished_at': DatePickerInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
