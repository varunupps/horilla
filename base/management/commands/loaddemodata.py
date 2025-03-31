"""
Horilla management command to load demo data.
"""

import os

from django.apps import apps
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Horilla management command to load demo data.
    """

    help = "Loads demo data into the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force", 
            action="store_true", 
            help="Force load demo data even if users exist"
        )

    def handle(self, *args, **options):
        # Check if there are any users
        if not options["force"] and User.objects.exists():
            self.stdout.write(
                self.style.WARNING("Users already exist in the database. Use --force to override.")
            )
            return

        # Load demo data
        self.stdout.write(self.style.NOTICE("Loading demo data..."))
        
        data_files = [
            "user_data.json",
            "employee_info_data.json",
            "base_data.json",
            "work_info_data.json",
        ]
        
        optional_apps = [
            ("attendance", "attendance_data.json"),
            ("leave", "leave_data.json"),
            ("asset", "asset_data.json"),
            ("recruitment", "recruitment_data.json"),
            ("onboarding", "onboarding_data.json"),
            ("offboarding", "offboarding_data.json"),
            ("pms", "pms_data.json"),
            ("payroll", "payroll_data.json"),
            ("payroll", "payroll_loanaccount_data.json"),
            ("helpdesk", "faqs.json"),
        ]

        # Add data files for installed apps
        data_files += [
            file for app, file in optional_apps if apps.is_installed(app)
        ]

        # Load all data files
        for file in data_files:
            file_path = os.path.join(settings.BASE_DIR, "load_data", file)
            if os.path.exists(file_path):
                self.stdout.write(self.style.NOTICE(f"Loading {file}..."))
                try:
                    call_command("loaddata", file_path)
                    self.stdout.write(self.style.SUCCESS(f"Successfully loaded {file}"))
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f"Error loading {file}: {str(e)}")
                    )
            else:
                self.stdout.write(
                    self.style.WARNING(f"File {file_path} does not exist, skipping")
                )

        self.stdout.write(self.style.SUCCESS("Demo data loaded successfully"))