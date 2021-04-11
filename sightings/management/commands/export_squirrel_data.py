import pandas as pd

from django.core.management.base import BaseCommand
from sightings.models import Sighting


def save2Csv(file_path):
    data = [[row.longitude,
             row.latitude,
             row.unique_squirrel_id,
             row.shift,
             row.date.strftime('%m%d%Y'),
             row.age,
             row.primary_fur_color,
             row.location,
             row.specific_location,
             row.running,
             row.chasing,
             row.climbing,
             row.eating,
             row.foraging,
             row.other_activities,
             row.kuks,
             row.quaas,
             row.moans,
             row.tail_flags,
             row.tail_twitches,
             row.approaches,
             row.indifferent,
             row.runs_from
             ] for row in Sighting.objects.all()[:20]]
    df = pd.DataFrame(data,
                      columns=["X", 'Y', 'Unique Squirrel ID', 'Shift', 'Date', 'Age', 'Primary Fur Color', 'Location',
                               'Specific Location', 'Running', 'Chasing', 'Climbing', 'Eating', 'Foraging',
                               'Other Activities', 'Kuks', 'Quaas', 'Moans', 'Tail flags', 'Tail twitches',
                               'Approaches', 'Indifferent', 'Runs from'])
    df.replace("nan", "", inplace = True)
    df.to_csv(file_path, na_rep='', index=None)


class Command(BaseCommand):
    help = 'Export squirrel data to csv file.'

    def add_arguments(self, parser):
        parser.add_argument('csv_data')

    def handle(self, *args, **options):
        csv_path = options['csv_data']
        save2Csv(csv_path)
