# Generated by Django 4.0.3 on 2023-05-01 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Visibility')),
                ('order', models.IntegerField(default=10, verbose_name='Order')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=20, verbose_name='Menu title')),
                ('slug', models.SlugField(help_text='Use it in templatetag for displaying menu', max_length=255, null=True, verbose_name='Slug')),
                ('named_url', models.CharField(blank=True, help_text='Named url from your urls.py file', max_length=255, verbose_name='Named URL')),
            ],
            options={
                'verbose_name': 'menu',
                'verbose_name_plural': 'menu',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Visibility')),
                ('order', models.IntegerField(default=10, verbose_name='Order')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Item title')),
                ('url', models.CharField(blank=True, max_length=255, verbose_name='Link')),
                ('named_url', models.CharField(blank=True, help_text='Named url from your urls.py file', max_length=255, verbose_name='Named URL')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='menu.menu', verbose_name='menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='menu.menuitem', verbose_name='parent menu item')),
            ],
            options={
                'verbose_name': 'menu item',
                'verbose_name_plural': 'menu items',
                'ordering': ('order',),
            },
        ),
    ]
