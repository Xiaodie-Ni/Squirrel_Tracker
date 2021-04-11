from django.db import models


# Create your models here.
class Sighting(models.Model):
    SHIFT_CHOICES = [
        ("AM", "A.M."),
        ("PM", "P.M."),
    ]

    AGE_CHOICES = [
        ("Adult", "Adult"),
        ("Juvenile", "Juvenile"),
        ("Unknown", "?"),
    ]

    PRIMARY_FUR_COLOR_CHOICES = [
        ("Black", "Black"),
        ("Gray", "Gray"),
        ("Cinnamon", "Cinnamon"),
    ]

    LOCATION_CHOICE = [
        ("Ground Plane", "Ground Plane"),
        ("Above Ground", "Above Ground"),
    ]

    longitude = models.FloatField(
        help_text="The longitude of the sight",
    )

    latitude = models.FloatField(
        help_text="The latitude of the sight",
    )

    unique_squirrel_id = models.CharField(
        help_text="The unique ID of the squirrel",
        max_length=16,
    )

    shift = models.CharField(
        help_text="Whether the squirrel observed in the before noon or after noon.",
        max_length=8,
        choices=SHIFT_CHOICES,
        blank=True
    )

    date = models.DateField(
        help_text="The date the squirrel was observed.",
        null=True,
        blank=True
    )

    age = models.CharField(
        help_text="The age of the squirrel.",
        max_length=16,
        choices=AGE_CHOICES,
        blank=True
    )

    primary_fur_color = models.CharField(
        help_text="The fur color of the squirrel.",
        max_length=16,
        choices=PRIMARY_FUR_COLOR_CHOICES,
        blank=True
    )
    location = models.CharField(
        help_text="The location of the squirrel.",
        max_length=128,
        choices=LOCATION_CHOICE,
        blank=True
    )
    specific_location = models.CharField(
        help_text="The additional notes to the location",
        max_length=128,
        blank=True,
    )
    running = models.BooleanField(
        help_text="Is running?",
        blank=True,
    )
    chasing = models.BooleanField(
        help_text="Is chasing?",
        blank=True,
    )
    climbing = models.BooleanField(
        help_text="Is climbing?",
        blank=True,
    )
    eating = models.BooleanField(
        help_text="Is eating?",
        blank=True,
    )
    foraging = models.BooleanField(
        help_text="Is foraging?",
        blank=True,
    )
    other_activities = models.CharField(
        help_text="Other Activities",
        max_length=128,
        null=True,
        blank=True
    )
    kuks = models.BooleanField(
        help_text="Kuks",
        blank=True,
    )
    quaas = models.BooleanField(
        help_text="Quaas",
        blank=True,
    )
    moans = models.BooleanField(
        help_text="Moans",
        blank=True,
    )
    tail_flags = models.BooleanField(
        help_text="Tail flags",
        blank=True,
    )
    tail_twitches = models.BooleanField(
        help_text="Tail twitches",
        blank=True,
    )
    approaches = models.BooleanField(
        help_text="Approaches",
        blank=True,
    )
    indifferent = models.BooleanField(
        help_text="Indifferent",
        blank=True,
    )
    runs_from = models.BooleanField(
        help_text="Runs from",
        blank=True,
    )
