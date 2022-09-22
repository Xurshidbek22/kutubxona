from django import forms
from django.core.exceptions import ValidationError
from .models import Kitob,Muallif,Record,Fan,Yonalish,Ustoz


class StudentForm(forms.Form):
    i = forms.CharField(label="Ism")
    j = forms.CharField(label="Jins")
    bitiruvchi = forms.BooleanField()
    kitoblari_soni = forms.IntegerField()

    def clean_i(self):
        qiymat = self.cleaned_data.get('i')
        if not qiymat.endswith('jon') or not qiymat.endswith('bek'):
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

# class MuallifForm(forms.Form):
#     i = forms.CharField(label="Ism")
#     tirik = forms.BooleanField()
#     kitob_soni = forms.IntegerField()
#     tugilgan_yil = forms.DateField()

class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = ('ism', 'tirik', 'kitob_soni', 'tugilgan_yil')

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('student', 'kitob', 'olingan_sana', 'qaytardi', 'qaytargan_sana')

class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = ('nom', 'yonalish', 'asosiy')

class YonalishForm(forms.ModelForm):
    class Meta:
        model = Yonalish
        fields = ('nom', 'aktiv')

class UstozForm(forms.ModelForm):
    class Meta:
        model = Ustoz
        fields = ('ism', 'jins', 'yosh', 'daraja', 'fan')