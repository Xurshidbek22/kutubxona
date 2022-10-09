from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import *
from .forms import StudentForm,KitobForm,MuallifForm,RecordForm,FanForm,YonalishForm,UstozForm

# def student(request):
#     if request.user.is_authenticated:
#         t = {
#             'ismlar':Student.objects.all()
#         }
#         return render(request, 'student.html', t)
#     else:
#         return redirect('/')




def loginView(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('l'),password=request.POST.get('p'))
        if user is None:
            return redirect('/ustoz/')
        login(request, user)
        return redirect('/')
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect('/login/')

def registerView(request):
    if request.method == "POST":
        user = authenticate(username=request.POST.get('l'), password=request.POST.get('p'))
        login(request, user)
        return redirect('/login/')
    return render(request, 'register.html')

def about(request):
    return render(request, 'about.html')

def amaliyot(request):
    return render(request, 'amaliyot.html')


def mashq(request):
    return HttpResponse,("Hello World")

def boshSahifa(request):
    return render(request, 'home.html')

def vazifa(request):
    data = {
        'ism':'Husniddin',
    }
    return render(request,'vazifa.html',data)



def student(request):
    if request.method == 'POST':
        f = StudentForm(request.POST)
        if f.is_valid():
            Student.objects.create(
                ism=f.cleaned_data.get('i'),
                jins=f.cleaned_data.get('j'),
                kitob_soni=f.cleaned_data.get('kitoblari_soni'),
                bitiruvchi = f.cleaned_data.get('bitiruvchi')
            )
        return redirect('/student/')

    soz = request.GET.get('q_sozi')
    if soz is None:
        s = Student.objects.all()
    else:
        s = Student.objects.filter(ism__contains=soz)

    std = {
        'ismlar':s,
        'forma':StudentForm

    }
    return render(request,'student.html',std)




def studentni_ochir(request, son):
    Student.objects.get(id=son).delete()
    return redirect('/student/')

def student_tasdiqlash(request, son):
    data = {
        'student':Student.objects.get(id=son)
    }
    return render(request, 'student_ochir.html', data)

#recordlar
def record(request):
    if request.method == 'POST':
        forma = RecordForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect('/record/')
    soz = request.GET.get('r_sozi')
    if soz is None:
        r = Record.objects.all()
    else:
        r = Record.objects.filter(student__ism__contains=soz)

    rec = {
        'sozlar':r,
        'studentlar':Student.objects.all(),
        'kitoblar':Kitob.objects.all(),
        'forma':RecordForm
    }
    return render(request,'record.html',rec)

def recordni_ochir(request, son):
    Record.objects.get(id=son).delete()
    return redirect('/record/')

def recordni_tasdiqlash(request, son):
    data = {
        'record':Record.objects.get(id=son),
        'studentlar': Record.objects.filter(id=son),

    }
    return render(request, 'recordni_ochir.html', data)


def record_tahrirlash(request, son):
    if request.method == 'POST':
        if request.POST.get('qaytar') == 'on':
            natija = True
        else:
            natija = False
        Record.objects.filter(id=son).update(
            olingan_sana=request.POST.get('olingan_s'),
            qaytardi=natija,
            qaytargan_sana=request.POST.get('qaytargan_s'),
        )
        return redirect('/record/')
    data = {
        'record':Record.objects.get(id=son),
    }

    return render(request, 'record_edit.html', data)


#3 mualliflar

def mualliflar(request):
    if request.method == 'POST':
        forma = MuallifForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect('/muallif/')

    soz = request.GET.get('m_sozi')
    if soz is None:
        m = Muallif.objects.all()
    else:
        m = Muallif.objects.filter(ism=soz)

    i = {
        'ismlar':m,
        'forma':MuallifForm
    }
    return render(request, 'mualliflar.html', i)

def muallif_tahrirlash(request, son):
    if request.method == 'POST':
        if request.POST.get('Tirik') == 'on':
            natija = True
        else:
            natija = False
        Muallif.objects.filter(id=son).update(
            ism=request.POST.get('ismi'),
            tirik=natija,
            kitob_soni=request.POST.get('k_soni'),
            tugilgan_yil=request.POST.get('tugilgan')
        )
        return redirect('/muallif/')
    data = {
        'muallif':Muallif.objects.get(id=son)
    }

    return render(request, 'muallif_edit.html', data)

def muallifni_ochir(request, son):
    Muallif.objects.get(id=son).delete()
    return redirect('/muallif/')


def muallifni_tasdiqlash(request, son):
    data = {
        'muallif':Muallif.objects.get(id=son)
    }
    return render(request, 'muallifni_ochir.html', data)

def muallif_batafsil(request, son):
    tal = {
        'muallif':Muallif.objects.get(id=son)
    }
    return render(request,'muallif_batafsil.html',tal)

def bitiruvchi(request):
    btd = {
        'bitiruvchilar':Student.objects.filter(bitiruvchi=True)
    }
    return render(request,'Mashq/bitiruvchi.html',btd)


def kitoblar(request):
    if request.method == 'POST':
        forma = KitobForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect('/kitob/')

    k = request.GET.get('k_sozi')
    if k is None:
        s = Kitob.objects.all()
    else:
        s = Kitob.objects.filter(nom__contains=k)

    ktb = {
        'kitoblar':s,
        'forma':KitobForm
    }
    return render(request,'kitob.html',ktb)

def kitobni_ochir(request, son):
    Kitob.objects.get(id=son).delete()
    return redirect('/kitob/')

def kitobni_tasdiqlash(request, son):
    data = {
        'kitob':Kitob.objects.get(id=son)
    }
    return render(request, 'kitobni_ochir.html', data)

def talaba(request, son):
    tal = {
        'student':Student.objects.get(id=son)
    }
    return render(request,'Mashq/talaba.html',tal)



def talaba_ochir(request, son):
    Student.objects.get(id=son).delete()
    return redirect('/student')
#fanlar

def fanlar(request):
    if request.method == 'POST':
        forma = FanForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect('/fan/')
    f = request.GET.get('f_soz')
    if f is None:
        s = Fan.objects.all()
    else:
        s = Fan.objects.filter(nom=f)

    f = {
        'fanlar':s,
        'yonalishlar': Yonalish.objects.all(),
        'forma' :FanForm
    }
    return render(request, 'fan.html',f)

def fanni_tahrirlash(request, son):
    if request.method == 'POST':
        if request.POST.get('fani') == 'on':
            natija = False
        else:
            natija = True
        Fan.objects.filter(id=son).update(
            nom=request.POST.get('nomi'),
            yonalish = request.POST.get('yonalishi'),
            asosiy=natija,
        )
        return redirect('/fan/')
    data = {
        'fan':Fan.objects.get(id=son),
        'fanlar':Yonalish.objects.all()
    }

    return render(request, 'fan_edit.html', data)


def fanni_tasdiqlash(request, son):
    data = {
        'fan':Fan.objects.get(id=son)
    }
    return render(request, 'fanni_ochir.html', data)

def fanni_ochir(request, son):
    Fan.objects.get(id=son).delete()
    return redirect('/fan/')
# yonalishlar
def yonalishlar(request):
    if request.method == 'POST':
        forma = YonalishForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect('/yonalish/')

    y = {
        'yonalishlar':Yonalish.objects.all(),
        'forma':YonalishForm
    }
    return render(request, 'yonalish.html',y)

def yonalishni_tahrirlash(request, son):
    if request.method == 'POST':
        if request.POST.get('akt') == 'on':
            natija = False
        else:
            natija = True
        Yonalish.objects.filter(id=son).update(
            nom=request.POST.get('nomi'),
            aktiv=natija,
        )
        return redirect('/yonalish/')
    data = {
        'yonalish':Yonalish.objects.get(id=son),
    }

    return render(request, 'yonalish_edit.html', data)



def yonalishni_ochir(request, son):
    Yonalish.objects.get(id=son).delete()
    return redirect('/yonalish/')

#ustozlar
def ustozlar(request):
    if request.method == 'POST':
        forma = UstozForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect('/ustoz/')
    f = request.GET.get('u_soz')
    if f is None:
        s = Ustoz.objects.all()
    else:
        s = Ustoz.objects.filter(ism=f)
    u = {
        'ustozlar':s,
        'fanlar': Fan.objects.all(),
        'forma':UstozForm

    }
    return render(request, 'ustoz.html', u)

def ustozni_ochir(request, son):
    Ustoz.objects.get(id=son).delete()
    return redirect('/ustoz/')


def ustozni_tahrirlash(request, son):
    if request.method == 'POST':
        Ustoz.objects.filter(id=son).update(
            ism=request.POST.get('ismi'),
            yosh=request.POST.get('yoshi'),
            daraja=request.POST.get('darajasi'),
            fan=Fan.objects.get(id=request.POST.get('fani')),
        )
        return redirect('/ustoz/')
    data = {
        'ustoz':Ustoz.objects.get(id=son),
        'fanlar':Fan.objects.all()
    }

    return render(request, 'ustoz_edit.html', data)


def student_tahrirlash(request, son):
    if request.method == 'POST':
        if request.POST.get('bitiradi') == 'on':
            natija = False
        else:
            natija = True
        Student.objects.filter(id=son).update(
            ism=request.POST.get('ismi'),
            bitiruvchi=natija,
            kitob_soni=request.POST.get('k_soni'),

        )
        return redirect('/student/')
    data = {
        'student':Student.objects.get(id=son)
    }

    return render(request, 'student_edit.html', data)




