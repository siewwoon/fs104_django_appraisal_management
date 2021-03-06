# Generated by Django 3.1.7 on 2021-03-30 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='manager',
            fields=[
                ('manager_ID', models.AutoField(primary_key=True, serialize=False)),
                ('manager_name', models.CharField(max_length=50, verbose_name='manager name')),
            ],
            options={
                'verbose_name': 'manager',
                'verbose_name_plural': 'managers',
            },
        ),
        migrations.CreateModel(
            name='Appraisal',
            fields=[
                ('appraisal_ID', models.AutoField(primary_key=True, serialize=False)),
                ('objective', models.CharField(max_length=40, verbose_name='objective')),
                ('review_year', models.CharField(max_length=4, verbose_name='review year')),
                ('rating', models.IntegerField()),
                ('department_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
            options={
                'verbose_name': 'Appraisal',
                'verbose_name_plural': 'Appraisals',
            },
        ),
    ]
