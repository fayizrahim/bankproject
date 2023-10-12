# Generated by Django 4.2.5 on 2023-10-05 17:40

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0003_alter_persondetails_account_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persondetails',
            name='material_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('debit card', 'debit card'), ('credit card', 'credit card'), ('other', 'other')], default='', max_length=220),
        ),
    ]
