from lettuce import world, before, after
from lettuce.django import django_url
from django.test.client import Client
from django.test.utils import setup_test_environment
from django.core.management import call_command
from selenium import selenium

world.browser = Client()

@before.runserver
def initial_setup(server):
    call_command('syncdb', interactive=False)
    call_command('flush', interactive=False)
    call_command('loaddata', 'all')
    setup_test_environment()

@before.harvest
def prepare_browser_driver(variables):
    if variables.get('run_server', False) is True:
        print 'Starting Selenium...'
        world.browser = selenium('localhost', 4444, '*firefox', django_url('/'))
        world.browser.start()
        print 'Selenium started.'

@after.harvest
def shutdown_browser_driver(results):
    world.browser.stop()

