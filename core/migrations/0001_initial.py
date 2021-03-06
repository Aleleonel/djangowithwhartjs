# Generated by Django 3.2.9 on 2021-11-07 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='categoria')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='título')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='preço')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='core.category', verbose_name='categoria')),
            ],
            options={
                'verbose_name': 'produto',
                'verbose_name_plural': 'produtos',
                'ordering': ('title',),
            },
        ),
    ]
