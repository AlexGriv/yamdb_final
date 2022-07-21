import datetime as dt

from rest_framework import serializers


def validate_year(value):
    year = dt.date.today().year
    if value > year:
        raise serializers.ValidationError('Произведение еще не издано!')
