# Generated by Django 4.2.6 on 2023-11-02 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_comboproducts_products_author_shoppingcartcombo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcartcombo',
            name='combo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.comboproducts'),
        ),
    ]