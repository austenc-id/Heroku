# Generated by Django 4.0.3 on 2022-03-17 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_resume', '0006_remove_entry_positions_entry_positions_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=48)),
                ('provider', models.CharField(max_length=48)),
                ('earned', models.DateField(default='2022-03-16')),
                ('expiration', models.DateField(blank=True, default='2022-03-16', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='entry',
            name='journal',
        ),
        migrations.RemoveField(
            model_name='position',
            name='entry',
        ),
        migrations.RemoveField(
            model_name='position',
            name='position_id',
        ),
        migrations.AddField(
            model_name='journal',
            name='entries',
            field=models.ManyToManyField(related_name='journal_entries', to='_resume.entry'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='positions',
            field=models.ManyToManyField(blank=True, null=True, related_name='entry_positions', to='_resume.position'),
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, max_length=48)),
                ('provider', models.CharField(blank=True, max_length=48)),
                ('street', models.CharField(blank=True, max_length=48)),
                ('city', models.CharField(blank=True, max_length=24)),
                ('state', models.CharField(blank=True, max_length=24)),
                ('start', models.DateField(default='2022-03-16')),
                ('end', models.DateField(default='2022-03-16')),
                ('certificates', models.ManyToManyField(blank=True, null=True, related_name='program_certs', to='_resume.certificate')),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='progams',
            field=models.ManyToManyField(blank=True, null=True, related_name='entry_programs', to='_resume.program'),
        ),
    ]
