# Generated by Django 4.0.5 on 2022-11-04 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MaesCarentes', '0003_alter_evento_dinheiro_alter_evento_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='dinheiro',
            field=models.ForeignKey(blank=True, limit_choices_to={'confirmacao': True, 'doado': False}, null=True, on_delete=django.db.models.deletion.PROTECT, to='MaesCarentes.doacaodinheiro'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='produto',
            field=models.ForeignKey(blank=True, limit_choices_to={'confirmacao': True, 'doado': False}, null=True, on_delete=django.db.models.deletion.PROTECT, to='MaesCarentes.doacaoitem'),
        ),
    ]
