# Generated by Django 4.2.18 on 2025-01-31 14:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0557_add_tags_to_experiment_saved_metrics"),
    ]

    operations = [
        migrations.AlterField(
            model_name="integration",
            name="kind",
            field=models.CharField(
                choices=[
                    ("slack", "Slack"),
                    ("salesforce", "Salesforce"),
                    ("hubspot", "Hubspot"),
                    ("google-pubsub", "Google Pubsub"),
                    ("google-cloud-storage", "Google Cloud Storage"),
                    ("google-ads", "Google Ads"),
                    ("snapchat", "Snapchat"),
                    ("linkedin-ads", "Linkedin Ads"),
                ],
                max_length=20,
            ),
        ),
    ]
