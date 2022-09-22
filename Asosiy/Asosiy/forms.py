from django import forms
from django.core.exceptions import ValidationError
from .models import Kitob
class StudentForm(forms.Form):
    i = forms.CharField(label="Ism")
    j = forms.CharField(label="Jins")
    bitiruvchi = forms.BooleanField()
    kitoblari_soni = forms.IntegerField()

    def clean_i(self):
        qiymat = self.cleaned_data.get('i')
        if not qiymat.endswith('jon') and not qiymat.endswith('bek'):
            raise ValidationError("Ism oz'bekcha emas")
        return qiymat

    def clean_kitoblari_soni(self):
        qiymat = self.cleaned_data.get('kitoblari_soni')
        if qiymat > 5 or qiymat < 0:
            raise ValidationError("Nato'g'ri qiymat")
        return qiymat


class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = ('nom', 'sahifa', 'janr', 'muallif')


