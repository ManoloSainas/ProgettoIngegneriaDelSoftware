# Generated by Django 4.2.3 on 2023-07-31 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrello',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrello', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prodotto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tipologia', models.CharField(max_length=100)),
                ('descrizione', models.CharField(max_length=500)),
                ('prezzo', models.FloatField()),
                ('quantita', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProdottoVenduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tipologia', models.CharField(max_length=100)),
                ('descrizione', models.CharField(max_length=500)),
                ('prezzo', models.FloatField()),
                ('quantita', models.IntegerField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prodotti_venduti', to='applicazione.stock')),
            ],
        ),
        migrations.CreateModel(
            name='ProdottoCarrello',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantita', models.IntegerField()),
                ('carrello', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prodotti', to='applicazione.carrello')),
                ('prodotto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicazione.prodotto')),
            ],
        ),
        migrations.AddField(
            model_name='prodotto',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prodotti', to='applicazione.stock'),
        ),
    ]