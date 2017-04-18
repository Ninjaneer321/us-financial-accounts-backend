from .models import *
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import logging

from django.conf import settings

logger = logging.getLogger(__name__)

def maybe_dev(func):
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if settings.DEBUG:
            response['Access-Control-Allow-Origin'] = '*'
        return response
    return wrapper

@maybe_dev 
def get_tables_brief(request):
    '''
    get all tables
    :param request:
    :return: JsonResponse. on success
    {
        // list of ids of tables.
        tables: [{'id' :int, 'table_code': string},]
    }
    '''
    if request.method != 'GET':
        logger.warning('request method has to be GET')
        return JsonResponse({'msg': 'request method has to be GET'}, status=400)

    # getting all table symbols
    tables = []
    dj_tables = DataTable.objects.all()
    for table in dj_tables:
        tables.append({
            'id': int(table.id),
            'table_code': table.table_code
        })

    return JsonResponse({'tables': tables}, status=200)

'''FIXME'''
@maybe_dev
def get_table(request, id_):
    '''
    get symbols, and dates of a table. table id, request.GET['id'], is needed
    :param request:
    :return: JsonResponse. on success
    {
        data_table_id: int
        symbols [{
            symbol: string,
            id: int,
            location: string,
            category: string,
            unit: string,
        },],
        dates: [{
            id: int
            date: string
        },]
    }
    '''
    if request.method != 'GET':
        logger.warning('request method has to be GET')
        return JsonResponse({'msg': 'request method has to be GET'}, status=400)

    id_ = int(id_)
    try:
        table = DataTable.objects.get(pk=id_)
    except ObjectDoesNotExist as err:
        logger.warning('id does not exist')
        return JsonResponse({'msg': 'id does not exist'}, status=400)

    dj_symbols = Symbol.objects.filter(data_table_id=id_)
    symbols = []
    for s in dj_symbols:
        symbols.append({
            'symbol': s.symbol,
            'id': int(s.id),
            'location': s.location,
            'category': s.category,
            'unit': s.unit,
        })

    dj_dates = Date.objects.filter(data_table_id=id_)
    dates = []
    for d in dj_dates:
        dates.append({
            'date': d.date,
            'id': d.id
        })

    return JsonResponse({'data_table_id': int(table.id),
                         'symbols': symbols, 'dates': dates}, status=200)

@maybe_dev
def entries_by_symbol(request, id_):
    '''

    :param request:
    :param _id: int. id of a Symbol
    :return: JsonResponse. on success.
    {
        symbol_id: int
        entries: [{
            date_id: int // foreign key
            data: float or null
        }]
    }
    '''
    if (request.method != 'GET'):
        logger.warning('must be GET request')
        return JsonResponse({'msg': 'must be GET request'}, status=400)

    try:
        symbol = Symbol.objects.get(pk=id_)
    except ObjectDoesNotExist as err:
        logger.warning(err)
        return JsonResponse({'msg': 'invalid id'}, status=400)

    dj_entries = Entry.objects.filter(symbol_id=id_)
    entries = []
    for e in dj_entries:
        entries.append({
            'date_id': int(e.date_id),
            'data': e.data
        })
    return JsonResponse({'symbol_id': id_, 'entries': entries}, status=200)

@maybe_dev
def entries_by_date(request, id_):
    '''
    get entries by date. GET
    :param request:
    :param id_: int. id of Date
    :return: JsonResponse. on success
    {
        date_id: int,
        entries: [{
            symbol_id: int,
            data: float or null.
        }]
    }
    '''
    if request.method != 'GET':
        logger.warning('not a GET method')

    try:
        date = Date.objects.get(pk=id_)
    except ObjectDoesNotExist as err:
        logging.warning(err)
        return JsonResponse({'msg': 'invalid id'}, status=400)

    dj_entries = Entry.objects.filter(date=date)
    entries = []
    for e in dj_entries:
        entries.append({
            'symbol_id': e.symbol_id,
            'data': e.data
        })
    return JsonResponse({'date_id': date.id, 'entries': entries}, status=200)
