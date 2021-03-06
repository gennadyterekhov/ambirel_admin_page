# Generated by Django 2.2.12 on 2020-06-25 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opencart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='attribute_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opencart.AttributeGroup'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opencart.Category'),
        ),
    ]
