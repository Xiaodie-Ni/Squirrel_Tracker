import pandas as pd
import datetime


from django.core.management.base import BaseCommand, CommandError
from sightings.models import Sighting


def convertStr2Boolean(string):
    string = str(string).lower()
    if string == "true":
        return True
    elif string == "false":
        return False
    else:
        return None


def loadCsv(file_path):
    def getItem(row, key):
        if key in row:
            return row[key]
        else:
            print("Error: the key is not in the index!")
            return None

    try:
        data_frame = pd.read_csv(file_path)
    except FileNotFoundError:
        print("Error: the file is not found")
        raise CommandError("Error: the file is not found")

    for index, row in data_frame.iterrows():
        sighting = Sighting(
            longitude=getItem(row, "X"),
            latitude=getItem(row, 'Y'),
            unique_squirrel_id=getItem(row, 'Unique Squirrel ID'),
            shift=getItem(row, 'Shift'),
            date=datetime.datetime.strptime(str(getItem(row, 'Date')), '%m%d%Y'),
            age=getItem(row, 'Age'),
            primary_fur_color=getItem(row, 'Primary Fur Color'),
            location=getItem(row, 'Location'),
            specific_location=getItem(row, 'Specific Location'),
            running=convertStr2Boolean(getItem(row, 'Running')),
            chasing=convertStr2Boolean(getItem(row, 'Chasing')),
            climbing=convertStr2Boolean(getItem(row, 'Climbing')),
            eating=convertStr2Boolean(getItem(row, 'Eating')),
            foraging=convertStr2Boolean(getItem(row, 'Foraging')),
            other_activities=getItem(row, 'Other Activities'),
            kuks=convertStr2Boolean(getItem(row, 'Kuks')),
            quaas=convertStr2Boolean(getItem(row, 'Quaas')),
            moans=convertStr2Boolean(getItem(row, 'Moans')),
            tail_flags=convertStr2Boolean(getItem(row, 'Tail flags')),
            tail_twitches=convertStr2Boolean(getItem(row, 'Tail twitches')),
            approaches=convertStr2Boolean(getItem(row, 'Approaches')),
            indifferent=convertStr2Boolean(getItem(row, 'Indifferent')),
            runs_from=convertStr2Boolean(getItem(row, 'Runs from')),
        )
        sighting.save()


class Command(BaseCommand):
    help = 'Import squirrel data from csv file.'

    def add_arguments(self, parser):
        parser.add_argument('csv_data')

    def handle(self, *args, **options):
        csv_path = options['csv_data']
        loadCsv(csv_path)
