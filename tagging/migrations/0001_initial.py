# Generated by Django 3.1.7 on 2021-04-26 06:53

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaggingResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_grouping', smart_selects.db_fields.ChainedManyToManyField(chained_field='geographical_scope', chained_model_field='geographical_scope', horizontal=True, to='categories.CountryGrouping', verbose_name='Countries grouping')),
                ('data_type', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.datatype')),
                ('data_type_sub', smart_selects.db_fields.ChainedManyToManyField(chained_field='data_type', chained_model_field='data_type', horizontal=True, to='categories.DataTypeSub', verbose_name='Data type subgroups')),
                ('geographical_scope', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.geographicalscope')),
                ('research_field', models.ManyToManyField(to='categories.ResearchField')),
                ('resource', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='resources.resource')),
                ('resource_type', models.ManyToManyField(to='categories.ResourceType')),
                ('specific_topic', models.ManyToManyField(to='categories.SpecificTopic')),
                ('stage_in_ds', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.stageinds', verbose_name='Stage in data sharing life cycle')),
            ],
            options={
                'verbose_name_plural': 'Waiting for tagging',
            },
        ),
    ]
