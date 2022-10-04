# Generated by Django 4.1 on 2022-09-05 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('yangi', '0002_delete_nashiryot_remove_sotuvchi_sotuv_delete_kitob_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=70)),
                ('sahifa', models.IntegerField()),
                ('janr', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('tirik', models.BooleanField(default=True)),
                ('kitob_soni', models.PositiveSmallIntegerField()),
                ('tugilgan_yil', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('jins', models.CharField(max_length=10)),
                ('bitiruvchi', models.BooleanField()),
                ('kitob_soni', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olingan_sana', models.DateField(auto_now_add=True)),
                ('qaytardi', models.BooleanField(default=False)),
                ('qaytargan_sana', models.DateField(blank=True, null=True)),
                ('kitob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yangi.kitob')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yangi.student')),
            ],
        ),
        migrations.AddField(
            model_name='kitob',
            name='muallif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yangi.muallif'),
        ),
    ]