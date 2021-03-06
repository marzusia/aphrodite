# Generated by Django 3.2.8 on 2021-10-20 19:37

import aphrodite.models.base.mixins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aphrodite', '0007_auto_20211020_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('name', models.CharField(help_text='The name of this course.', max_length=128)),
                ('accreditation', models.CharField(help_text='The accreditation achieved by this course, e.g BA (Hons), PhD, etc.', max_length=32)),
                ('code', models.CharField(help_text='A short unique code for this course, usually an uppercase abbreviation, such as LING for Linguistics.', max_length=32)),
                ('slug', models.SlugField(blank=True, help_text='How this article will appear in URLs (leave blank for auto).', max_length=128, unique=True)),
                ('level', models.CharField(choices=[('undergrad', 'Undergraduate'), ('postgrad', 'Postgraduate')], help_text='The degree level of this qualification.', max_length=128)),
                ('length', models.IntegerField(help_text='The length of this course in years.')),
                ('description', models.TextField(help_text='A short introduction to this course.')),
                ('requirements', models.TextField(help_text='A short description of the academic/other requirements for admission to this course.')),
                ('promo_image', models.ImageField(blank=True, help_text='A small image exemplifying this course, to appear on the course page.', null=True, upload_to='course/')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, aphrodite.models.base.mixins.AutoSlugMixin),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('name', models.CharField(help_text='The short, friendly name of this department, e.g Science.', max_length=128)),
                ('full_name', models.CharField(help_text='The full name of this department, e.g Department of Science.', max_length=128)),
                ('slug', models.SlugField(blank=True, help_text='How this article will appear in URLs (leave blank for auto).', max_length=128, unique=True)),
                ('description', models.TextField(help_text='A short introduction to this department.')),
                ('promo_image', models.ImageField(blank=True, help_text='A small image exemplifying this department, to appear on the department page.', null=True, upload_to='department/')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, aphrodite.models.base.mixins.AutoSlugMixin),
        ),
        migrations.CreateModel(
            name='QuickLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('label', models.CharField(help_text='The label for this link.', max_length=128)),
                ('index', models.IntegerField(help_text='The index (order) that this link should appear in the menu.', unique=True)),
                ('page', models.ForeignKey(help_text='The page this link should navigate to.', on_delete=django.db.models.deletion.CASCADE, to='aphrodite.page')),
            ],
            options={
                'ordering': ['index'],
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('code', models.CharField(help_text='A short code unique to this module. Typically made up of the course abbreviation (e.g LING for Linguistics) followed by a three-digit number, whereby the first is the course year and the second two are arbitrary and unique. An example would be LING102 as a first-year module for Semantics, and LING204 as a second-year module for Pragmatics.', max_length=32, unique=True)),
                ('name', models.CharField(help_text='The friendly name of the module, e.g Reinassance Art.', max_length=128)),
                ('description', models.TextField(help_text='A short introduction to this module.')),
                ('course', models.ForeignKey(help_text='The course to which this module belongs.', on_delete=django.db.models.deletion.CASCADE, to='aphrodite.course')),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(help_text='The department that provides this course.', on_delete=django.db.models.deletion.CASCADE, to='aphrodite.department'),
        ),
    ]
