# Generated by Django 2.1 on 2018-10-19 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('syllabus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="Class's Name")),
                ('time_start', models.DateTimeField(verbose_name="Class's start time")),
                ('time_end', models.DateTimeField(verbose_name="Class's end time")),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
                'db_table': 'class',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ClassSyllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Class', verbose_name='Class')),
                ('syllabus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus.Syllabus', verbose_name='Syllabus')),
            ],
            options={
                'verbose_name': 'Class - Syllasbus',
                'verbose_name_plural': 'Classes - Syllabus',
                'db_table': 'class_syllabus',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ClassUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Class', verbose_name='Class')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Class - User',
                'verbose_name_plural': 'Classes - Users',
                'db_table': 'class_user',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="Course's Name")),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'db_table': 'courses',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='class',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course', verbose_name='Course'),
        ),
    ]
