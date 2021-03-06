# Generated by Django 2.2.12 on 2020-05-30 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jeopardy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('answered_by', models.CharField(max_length=100)),
                ('answered_at', models.DateTimeField(null=True)),
                ('clue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jeopardy.Clue')),
            ],
        ),
    ]
