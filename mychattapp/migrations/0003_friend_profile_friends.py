# Generated by Django 4.1.3 on 2022-11-15 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mychattapp', '0002_delete_friend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mychattapp.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(related_name='my_friends', to='mychattapp.friend'),
        ),
    ]