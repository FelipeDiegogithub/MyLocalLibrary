# Generated by Django 3.1.3 on 2020-11-08 18:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camisetas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('país', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('Rut', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['apellido', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Liga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CamisetasInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID único para cada camiseta en la tienda', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('status', models.CharField(blank=True, choices=[('l', 'La Liga'), ('pl', 'Premier League'), ('a', 'Serie A')], default='l', help_text='Camisetas disponibles', max_length=100)),
                ('camiseta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.camisetas')),
            ],
            options={
                'ordering': ['camiseta'],
            },
        ),
        migrations.AddField(
            model_name='camisetas',
            name='equipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.liga'),
        ),
    ]
