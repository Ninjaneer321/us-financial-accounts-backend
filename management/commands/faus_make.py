from os import path, listdir
import csv
import re

from financial_accounts_us.models import DataTable, Symbol, Entry, Date
from django.core.management.base import BaseCommand
from django.db import transaction

RD = path.join(path.dirname(__file__), '../../z1_csv_files')


class Command(BaseCommand):
    help = 'populate data into financial account us from ' + RD

    @transaction.atomic
    def process_table(self, fn, table_code):
        # create a DataTable, from a file in data_dictionary.
        data_table = DataTable.objects.create(table_code=table_code)
        data_table.save()

        # read symbols of the table
        table_file = open(fn, 'r')
        symbol_row = table_file.readline()
        symbols = {}
        while symbol_row != '':
            cols = symbol_row.split('\t')
            assert len(cols) == 5
            symbol_code = cols[0]
            description = cols[1]
            location = cols[2]
            category = cols[3]
            unit = cols[4].strip()
            symbol = Symbol.objects.create(symbol=symbol_code, description=description, location=location,
                                           category=category, unit=unit, data_table=data_table)
            symbol.save()
            symbols[symbol_code] = symbol
            symbol_row = table_file.readline()
        table_file.close()

        table_data_file = open(path.join(RD, 'csv/{0}.csv'.format(table_code)), 'r')
        table_data_reader = csv.DictReader(table_data_file)
        for table_data_row in table_data_reader:
            assert len(table_data_row) == len(symbols)+1
            date_str = table_data_row['date']
            date = Date.objects.create(date=date_str, data_table=data_table)
            date.save()
            for symbol_code, symbol in symbols.items():
                if symbol_code not in table_data_row:
                    raise Exception('?1')
                entry_raw = table_data_row[symbol_code]
                try:
                    entry_data = float(entry_raw)
                    entry = Entry.objects.create(data=entry_data, date=date, symbol=symbol)
                except ValueError as err:
                    entry = Entry.objects.create(date=date, symbol=symbol)
                entry.save()
        table_data_file.close()

    def handle(self, *args, **options):
        self.stdout.write('removing old data')
        DataTable.objects.all().delete()

        data_dict_path = path.join(RD, 'data_dictionary')
        for dt in listdir(data_dict_path):
            matched = re.match(r'([a-zA-Z0-9]+)\.txt$', dt)
            if matched:
                self.stdout.write('processing {0}'.format(dt), ending='\n')
                self.process_table(path.join(data_dict_path, dt), matched.group(1))
