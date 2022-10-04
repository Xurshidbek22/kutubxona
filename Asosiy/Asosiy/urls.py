from django.contrib import admin
from django.urls import path
from yangi.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginView),
    path('logout/', logoutView),

    path('about/', about),
    path('amaliyot/', amaliyot),
    #record
    path('record/', record),
    path('recordni_ochir/<int:son>/', recordni_ochir),
    path('recordni_tasdiqlash/<int:son>/', recordni_tasdiqlash),
    path('record_edit/<int:son>/', record_tahrirlash),

    #mualliflar
    path('muallif_batafsil/<int:son>/', muallif_batafsil),

    path('muallif/', mualliflar),
    path('muallifni_ochir/<int:son>/', muallifni_ochir),
    path('muallif_edit/<int:son>/', muallif_tahrirlash),
    path('muallifni_tasdiqlash/<int:son>/', muallifni_tasdiqlash),
    #studentlar
    path('student/',student),
    path('studentni_ochir/<int:son>/',studentni_ochir),
    path('student_edit/<int:son>/', student_tahrirlash),
    path('student_tasdiqlash/<int:son>/', student_tasdiqlash),

    path('mashq/', mashq),
    path('',boshSahifa),
    path('vazifa/',vazifa),

    path('bitiruvchi/',bitiruvchi),
    path('kitob/',kitoblar),
    path('kitobni_ochir/<int:son>/',kitobni_ochir),
    path('kitobni_tasdiqlash/<int:son>/',kitobni_tasdiqlash),

    path('talaba/<int:son>/',talaba),
    #fanlar
    path('fan/',fanlar),
    path('fanni_ochir/<int:son>/',fanni_ochir),
    path('fan_edit/<int:son>/',fanni_tahrirlash),
    path('fanni_tasdiqlash/<int:son>/', fanni_tasdiqlash),

    #yonalishlar
    path('yonalish/', yonalishlar),
    path('yonalishni_ochir/<int:son>/', yonalishni_ochir),
    path('yonalish_edit/<int:son>/', yonalishni_tahrirlash),
    #ustozlar
    path('ustoz/',ustozlar),
    path('ustozni_ochir/<int:son>/',ustozni_ochir),
    path('ustoz_edit/<int:son>/',ustozni_tahrirlash),

]
