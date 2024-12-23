# Generated by Django 5.1.2 on 2024-11-02 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('streaming', models.CharField(choices=[('AK', 'Amazon Kindle'), ('F', 'Físico')], max_length=2)),
                ('notice', models.IntegerField(blank=True, null=True)),
                ('coments', models.TextField(blank=True, null=True)),
                ('category', models.ManyToManyField(to='livros.category')),
            ],
        ),
    ]
