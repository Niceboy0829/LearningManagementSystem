# Generated by Django 2.1 on 2018-11-08 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0007_auto_20181108_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabustemplate',
            name='lecturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classes_in_template_set', to=settings.AUTH_USER_MODEL, verbose_name='Lecturer'),
        ),
        migrations.AlterField(
            model_name='syllabustemplate',
            name='own_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lecturers_in_template_set', to='course.Class', verbose_name='Class'),
        ),
        migrations.AlterModelTable(
            name='syllabustemplate',
            table='syllabus_template',
        ),
    ]
