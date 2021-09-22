# Generated by Django 2.2.5 on 2021-09-22 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': '보유 시설',
            },
        ),
        migrations.CreateModel(
            name='Fitness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=140, verbose_name='헬스장 이름')),
                ('description', models.TextField(blank=True, null=True, verbose_name='소개')),
                ('province', models.CharField(blank=True, choices=[('경기도', '경기도'), ('강원도', '강원도'), ('충청남도', '충청남도'), ('충청북도', '충청북도'), ('전라남도', '전라남도'), ('전라북도', '전라북도'), ('경상남도', '경상남도'), ('경상북도', '경상북도'), ('제주도', '제주도')], max_length=20, null=True, verbose_name='위치한 지역(도)')),
                ('city', models.CharField(max_length=80, null=True, verbose_name='지역(시)')),
                ('price', models.IntegerField(verbose_name='월정액 가격')),
                ('guests', models.IntegerField(verbose_name='회원 수')),
                ('open_time', models.TimeField(verbose_name='오픈시간')),
                ('close_time', models.TimeField(verbose_name='마감시간')),
                ('facilities', models.ManyToManyField(blank=True, related_name='fitness', to='fitnesscenters.Facility')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fitnessequipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': '보유 기구',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': '헬스장 옵션',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('caption', models.CharField(max_length=80)),
                ('file', models.ImageField(upload_to='fitness_photos')),
                ('fitness', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='fitnesscenters.Fitness')),
            ],
            options={
                'verbose_name_plural': '헬스장 사진',
            },
        ),
        migrations.AddField(
            model_name='fitness',
            name='fitnessequipments',
            field=models.ManyToManyField(blank=True, related_name='fitness', to='fitnesscenters.Fitnessequipment'),
        ),
        migrations.AddField(
            model_name='fitness',
            name='options',
            field=models.ManyToManyField(blank=True, related_name='fitness', to='fitnesscenters.Option'),
        ),
    ]
