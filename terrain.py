from lettuce import world, before
from django.test.client import Client
from django.test.utils import setup_test_environment
from django.core.management import call_command

world.browser = Client()

@before.runserver
def initial_setup(server):
    call_command('syncdb', interactive=False)
    call_command('flush', interactive=False)
    call_command('loaddata', 'all')
    setup_test_environment()
