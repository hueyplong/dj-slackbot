# Generated by Django 2.2.12 on 2020-05-29 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack_client_id', models.CharField(max_length=100)),
                ('slack_client_secret', models.CharField(max_length=100)),
                ('slack_verification_token', models.CharField(max_length=100)),
                ('slack_bot_user_token', models.CharField(max_length=100)),
            ],
        ),
    ]
