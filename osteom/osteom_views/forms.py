from django import forms


class AppointmentForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=30)
    mail = forms.EmailField(label='Контактная почта', required=False)
    phone = forms.CharField(label='Номер телефона для связи')


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=15)
    surname = forms.CharField(label='Фамилия', max_length=15)
    content = forms.CharField(label='Ваши впечатления', max_length=800)


class SearchForm(forms.Form):
    filter = forms.CharField(label='Поисковая строка', required=False)

