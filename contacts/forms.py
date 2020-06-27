from django import forms


class EmailForm(forms.Form):
    name = forms.CharField(label='Введите имя', max_length=100)
    subject = forms.CharField(label='Введите тему', max_length=100)
    email = forms.EmailField(label='Введите email', max_length=100)
    text = forms.CharField(label='Введите текст собщения')

    name.widget.attrs.update({'class': 'form-control'})
    subject.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    text.widget = forms.Textarea()
    text.widget.attrs.update({'class': 'form-control'})
