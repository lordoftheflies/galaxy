# NOTE(cutwater): This migration is replaced by v2_4_0 and should be
#   deleted once superseding migration is merged into master.
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [('main', '0016_auto_20150922_1041')]

    operations = [
        migrations.RemoveField(model_name='role', name='authors'),
        migrations.AddField(
            model_name='role',
            name='namespace',
            field=models.CharField(
                max_length=256,
                null=True,
                verbose_name='Namespace',
                blank=True,
            ),
        ),
        migrations.AlterUniqueTogether(
            name='role', unique_together={('namespace', 'name')}
        ),
    ]
