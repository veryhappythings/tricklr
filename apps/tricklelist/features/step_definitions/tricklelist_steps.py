# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from lettuce import step, world
from lettuce.django import django_url
from tricklelist.models import TrickleList

@step(u'Given that I am logged in')
def given_that_i_am_logged_in(step):
    username = 'test_user'
    password = 'test_password'
    user = User(username=username)
    user.set_password(password)
    user.save()

    world.browser.open(django_url('/accounts/login'))
    world.browser.wait_for_page_to_load(30000)
    world.browser.type('username', username)
    world.browser.type('password', password)
    world.browser.click('submit')
    world.browser.wait_for_page_to_load(30000)

@step(u'And I have (\d+) lists?')
def and_i_have_n_lists(step, quantity):
    quantity = int(quantity)
    for i in range(quantity):
        TrickleList.objects.create(name='Test List {0}'.format(quantity))

@step(u'And I have a list called "(.*)"')
def and_i_have_a_list_called_name(step, name):
    TrickleList.objects.create(name=name)

@step(u'And the list "(.*)" contains the item "(.*)"')
def and_the_list_listname_contains_the_item_itemname(step, listname, itemname):
    tl = TrickleList.objects.get(name=listname)
    tl.listitem_set.create(name=itemname)

