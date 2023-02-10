# Generated by Django 4.1.5 on 2023-02-10 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('year', models.PositiveIntegerField()),
                ('month', models.PositiveIntegerField()),
                ('version', models.CharField(max_length=128)),
                ('model', models.ManyToManyField(to='ticket.model')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.ticket')),
            ],
        ),
    ]
