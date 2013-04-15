from django.core.management.base import BaseCommand
import time
import json
from drinks.models import Drink
from django.utils.html import strip_tags

class Command(BaseCommand):
    args = 'takes no args'
    help = 'reduces the polgyon count'

    def handle(self, *args, **options):
        time_start = time.time()
        file = open("/home/dotcloud/current/tbldata.txt", "r+")
        #file = open("tbldata.txt", "r+")
        contents = file.read()
        contents = json.loads(contents)
        for content in contents:
            drink = Drink.objects.create(name=strip_tags(content[0]), volume=content[1], caffeine=content[2])
            print drink
        
        time_end = time.time()
        time_diff = time_end - time_start
        print "%s seconds" % time_diff
            
                
                