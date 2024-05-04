# Code wrote in order to execute the scraping script once every day


import logging
from django.core.management.base import BaseCommand
from subprocess import run, PIPE
import os

user_actions_logger = logging.getLogger('user_actions')


class Command(BaseCommand):
    help = 'Scrape data from the web once a day'

    def handle(self, *args, **options):
        
        script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scraping_script', 'script.py'))
        
        try:
            result = run(['python',  script_path], stdout=PIPE, stderr=PIPE, check=True, text=True)
            user_actions_logger.info(f"Daily task for scraping data from web is now executed")
            self.stdout.write(self.style.SUCCESS('Scraping script executed successfully'))
            self.stdout.write(result.stdout)
        except Exception as e:
            user_actions_logger.info(f"Daily task for scraping data from web for today has this issue: {e}")
            self.stderr.write(self.style.ERROR(f'Error executing scraping script: {e}'))
