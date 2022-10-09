from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ('ism' ,'id')
    list_display = ("id", "ism", "jins", "kitob_soni")
    list_display_links = ("ism", "jins")
    list_editable = ('kitob_soni',)
    list_filter = ('jins',)
    list_per_page = 4
    # list_max_show_all = 5

@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    search_fields = ('ism', 'id')
    list_display = ('ism', 'tirik', 'kitob_soni', 'tugilgan_yil')
    list_display_links = ("ism",)
    list_editable = ('kitob_soni', 'tirik')
    list_filter = ('tirik',)

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    search_fields = ('id', 'student__ism', 'kitob__nom')
    list_filter = ('qaytardi',)

@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    search_fields = ('id', 'nom', 'muallif__ism','janr')
    list_filter = ('janr',)
    list_display = ("id", "nom", "sahifa", "janr")
    list_display_links = ("nom", "janr")
    list_editable = ('sahifa',)

@admin.register(Fan)
class FanAdmin(admin.ModelAdmin):
    search_fields = ('id', "nom", "yonalish")
    list_filter = ("asosiy",)
    list_display = ("id", "nom", "yonalish", "asosiy")
    list_display_links = ("nom",)
    list_editable = ('yonalish',)


@admin.register(Yonalish)
class YonalishAdmin(admin.ModelAdmin):
    search_fields = ("id", "nom")
    list_filter = ("aktiv",)

@admin.register(Ustoz)
class UstozAdmin(admin.ModelAdmin):
    search_fields = ("id", "ism", "yosh")
    list_filter = ("jins", "daraja")


# admin.site.register(Muallif)
# admin.site.register(Muallif)
# admin.site.register(Kitob)
# admin.site.register(Record)
# admin.site.register(Fan)
# admin.site.register(Yonalish)
# admin.site.register(Ustoz)