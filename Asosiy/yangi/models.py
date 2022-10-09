from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    ism = models.CharField(max_length=30)
    jins = models.CharField(max_length=10)
    bitiruvchi = models.BooleanField(default=False)
    kitob_soni = models.PositiveSmallIntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.ism

class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    tirik = models.BooleanField(default=True)
    kitob_soni = models.PositiveSmallIntegerField()
    tugilgan_yil = models.DateField()

    def __str__(self): return self.ism

    # class Meta:
    #     ordering = ['kitob_soni']

class Kitob(models.Model):
    nom = models.CharField(max_length=70)
    sahifa = models.IntegerField()
    janr = models.CharField(max_length=30)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Record(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    olingan_sana = models.DateField()
    qaytardi = models.BooleanField(default=False)
    qaytargan_sana = models.DateField(null=True, blank=True)

    def __str__(self):
         return f"{self.student.ism}, {self.kitob.nom}"



class Yonalish(models.Model):
    nom = models.CharField(max_length=30)
    aktiv = models.BooleanField(default=True)

    def __str__(self):
        return self.nom
class Fan(models.Model):
    nom = models.CharField(max_length=50)
    yonalish = models.ForeignKey(Yonalish,on_delete=models.CASCADE)
    asosiy = models.BooleanField(default=True)

    def __str__(self):
        return self.nom
class Ustoz(models.Model):
    D = [
        ("Bakalavr","Bakalavr"),
        ("Magistr","Magistr"),
    ]
    ism = models.CharField(max_length=30)
    jins = models.CharField(max_length=10)
    yosh = models.PositiveSmallIntegerField()
    daraja = models.CharField(max_length=30,choices=D)
    fan = models.ForeignKey(Fan,on_delete=models.CASCADE)


    def __str__(self):
        return self.ism

