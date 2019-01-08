from django.core.management.base import BaseCommand, CommandError
from pyquery import PyQuery as pq

import os
import re


class Command(BaseCommand):
    help = 'update Comic'

    def handle(self, *args, **options):
        Comic = pq(url='https://www.tohomh.com/quanzhifashi/')
        
