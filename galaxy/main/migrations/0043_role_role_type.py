# NOTE(cutwater): This migration is replaced by v2_4_0 and should be
#   deleted once superseding migration is merged into master.
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [('main', '0042_auto_20160721_2318')]

    operations = [
        migrations.AddField(
            model_name='role',
            name='role_type',
            field=models.CharField(
                default='ANS',
                max_length=3,
                editable=False,
                choices=[
                    ('ANS', 'Ansible'),
                    ('CON', 'Container Role'),
                    ('APP', 'Container App'),
                ],
            ),
        )
    ]
