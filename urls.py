from django.conf.urls import url
from . import api


urlpatterns = [
    url(r'api/tables$', api.get_tables_brief),
    url(r'api/table/([0-9]+)$', api.get_table),
    url(r'api/table/entries/by_symbol/([0-9]+)$', api.entries_by_symbol),
    url(r'api/table/entries/by_date/([0-9]+)$', api.entries_by_date)
]
