from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Seeds the project'

    def handle(self, *args, **options):
        print('Seeding teams')
        call_command('seed_teams')
        print('Getting all games for this week')
        call_command('grab_new_games')
        print('Saving comments...')
        call_command('save_media_comments')
        try:
            site = Site.objects.get(name='example.com')
            site.domain = 'sportsForecast.com'
            site.name = 'sportsForecast.com'
            print('Updating default site...')
            site.save()
        except Site.DoesNotExist:
            pass
