# Generated by Django 2.1 on 2018-10-25 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20181025_1131'),
        ('syllabus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassSyllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='course.Class', verbose_name='Class')),
            ],
            options={
                'verbose_name': 'Class - Syllasbus',
                'verbose_name_plural': 'Classes - Syllabus',
                'db_table': 'class_syllabus',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SyllabusTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='course.Class', verbose_name='Class')),
            ],
            options={
                'verbose_name': 'Syllabus Template',
                'verbose_name_plural': 'Syllabus Templates',
                'db_table': 'syllbus_template',
                'ordering': ['id'],
            },
        ),
        migrations.RemoveField(
            model_name='syllabus',
            name='name',
        ),
        migrations.AddField(
            model_name='material',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='class_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='course.Class', verbose_name='Class'),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='content',
            field=models.TextField(default='', verbose_name="Syllabus's content"),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='title',
            field=models.CharField(default='', max_length=100, verbose_name="Syllabus's title"),
        ),
        migrations.AddField(
            model_name='syllabus',
            name='week',
            field=models.CharField(default='', max_length=10, verbose_name='Week'),
        ),
        migrations.AddField(
            model_name='classsyllabus',
            name='syllabus_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='syllabus.Syllabus', verbose_name='Syllabus'),
        ),
    ]