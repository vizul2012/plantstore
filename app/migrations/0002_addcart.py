# Generated by Django 2.0 on 2021-08-16 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qun', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=1234)),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('usrg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User')),
            ],
        ),
    ]
