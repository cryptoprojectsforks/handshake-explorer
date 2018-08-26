# Generated by Django 2.1 on 2018-08-26 16:08

import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('height', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('hash', models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(code='nomatch', message='Must be a 64 character hex string', regex='^.[a-f0-9]{64}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tx_hash', models.CharField(max_length=64, validators=[django.core.validators.RegexValidator(code='nomatch', message='Must be a 64 character hex string', regex='^.[a-f0-9]{64}$')])),
                ('output_index', models.PositiveIntegerField()),
                ('action', models.PositiveIntegerField(choices=[('NONE', 0), ('CLAIM', 1), ('OPEN', 2), ('BID', 3), ('REVEAL', 4), ('REDEEM', 5), ('REGISTER', 6), ('UPDATE', 7), ('RENEW', 8), ('TRANSFER', 9), ('FINALIZE', 10), ('REVOKE', 11)])),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('value', models.BigIntegerField(blank=True, null=True)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='block', to='explorer.Block')),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('hash', models.CharField(max_length=64, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[a-f0-9]{64}$', 'Must be a 64 character hex string')])),
                ('name', models.CharField(max_length=500, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explorer.Name'),
        ),
        migrations.AddField(
            model_name='event',
            name='start_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='start_height', to='explorer.Block'),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together={('tx_hash', 'output_index')},
        ),
    ]
