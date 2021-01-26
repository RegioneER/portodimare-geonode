# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-04 08:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    replaces = [(b'services', '0026_auto_20171130_0600'), (b'services', '0027_harvestjob_details'), (b'services', '0028_auto_20171201_0640'), (b'services', '0029_auto_20171203_1624'), (b'services', '0030_auto_20171212_0518'), (b'services', '0031_auto_20180301_1947'), (b'services', '0032_auto_20180302_0430'), (b'services', '0031_service_proxy_base'), (b'services', '0033_merge'), (b'services', '0034_auto_20180309_0917'), (b'services', '0035_auto_20180327_0846'), (b'services', '0036_auto_20180331_1039'), (b'services', '0037_auto_20180409_1238'), (b'services', '0038_auto_20180412_0822'), (b'services', '0039_auto_20180414_2120'), (b'services', '0040_auto_20190329_1652'), (b'services', '0041_auto_20190404_0820')]

    dependencies = [
        ('services', '0025_harvestjob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvestjob',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service'),
        ),
        migrations.AddField(
            model_name='harvestjob',
            name='details',
            field=models.TextField(blank=True, default='Resource is queued', null=True),
        ),
        migrations.RemoveField(
            model_name='servicelayer',
            name='description',
        ),
        migrations.RemoveField(
            model_name='servicelayer',
            name='styles',
        ),
        migrations.RemoveField(
            model_name='servicelayer',
            name='title',
        ),
        migrations.RemoveField(
            model_name='servicelayer',
            name='typename',
        ),
        migrations.RemoveField(
            model_name='servicelayer',
            name='layer',
        ),
        migrations.RemoveField(
            model_name='servicelayer',
            name='service',
        ),
        migrations.DeleteModel(
            name='ServiceLayer',
        ),
        migrations.RemoveField(
            model_name='webserviceharvestlayersjob',
            name='service',
        ),
        migrations.DeleteModel(
            name='WebServiceRegistrationJob',
        ),
        migrations.AlterField(
            model_name='harvestjob',
            name='status',
            field=models.CharField(choices=[(b'QUEUED', b'QUEUED'), (b'CANCELLED', b'QUEUED'), (b'IN_PROCESS', b'IN_PROCESS'), (b'PROCESSED', b'PROCESSED'), (b'FAILED', b'FAILED')], default=b'QUEUED', max_length=15),
        ),
        migrations.DeleteModel(
            name='WebServiceHarvestLayersJob',
        ),
        migrations.AlterModelManagers(
            name='service',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='proxy_base',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(choices=[(b'AUTO', 'Auto-detect'), (b'OWS', 'Paired WMS/WFS/WCS'), (b'WMS', 'Web Map Service'), (b'CSW', 'Catalogue Service'), (b'REST', 'ArcGIS REST Service'), (b'OGP', 'OpenGeoPortal'), (b'HGL', 'Harvard Geospatial Library'), (b'GN_WMS', 'GeoNode (Web Map Service)'), (b'GN_CSW', 'GeoNode (Catalogue Service)')], max_length=10),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(choices=[(b'AUTO', 'Auto-detect'), (b'OWS', 'Paired WMS/WFS/WCS'), (b'WMS', 'Web Map Service'), (b'CSW', 'Catalogue Service'), (b'REST_MAP', 'ArcGIS REST MapServer'), (b'REST_IMG', 'ArcGIS REST ImageServer'), (b'OGP', 'OpenGeoPortal'), (b'HGL', 'Harvard Geospatial Library'), (b'GN_WMS', 'GeoNode (Web Map Service)'), (b'GN_CSW', 'GeoNode (Catalogue Service)')], max_length=10),
        ),
        migrations.AlterModelManagers(
            name='service',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
