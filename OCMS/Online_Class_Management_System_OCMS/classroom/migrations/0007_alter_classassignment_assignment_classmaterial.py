# Generated by Django 4.0 on 2022-03-27 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_classtest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classassignment',
            name='assignment',
            field=models.FileField(upload_to='materials'),
        ),
        migrations.CreateModel(
            name='ClassMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('material_name', models.CharField(max_length=250)),
                ('material', models.FileField(upload_to='assignments')),
                ('student', models.ManyToManyField(related_name='student_material', to='classroom.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_material', to='classroom.teacher')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
