from django.db import models

# Create your models here.
class DataTable(models.Model):
    table_code = models.CharField(max_length=100, unique=True)


class Symbol(models.Model):
    symbol = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=350, blank=False)
    location = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=350, blank=False)
    unit = models.CharField(max_length=100, blank=False)

    data_table = models.ForeignKey(DataTable, on_delete=models.CASCADE)


class Date(models.Model):
    date = models.CharField(max_length=100, blank=False)

    data_table = models.ForeignKey(DataTable, on_delete=models.CASCADE)


class Entry(models.Model):
    data = models.FloatField(null=True)

    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE)

