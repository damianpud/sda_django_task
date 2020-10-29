# Generated by Django 3.0.10 on 2020-10-29 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
                ('starts', models.DateField()),
                ('finishes', models.DateField()),
                ('max_atendees_counts', models.IntegerField()),
                ('price', models.FloatField()),
                ('remote', models.BooleanField()),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.Technology')),
            ],
        ),
    ]
