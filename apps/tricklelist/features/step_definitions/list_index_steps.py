# -*- coding: utf-8 -*-
from lettuce import step, world
from lettuce.django import django_url
from django.contrib import auth
from django.contrib.auth.models import User
from nose.tools import assert_equal

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
        tl = TrickleList(
            name='Test List {0}'.format(quantity)
        )
        tl.save()

@step(u'And I go to the list index')
def and_i_go_to_the_list_index(step):
    world.browser.open(django_url('/trickle/'))
    world.browser.wait_for_page_to_load(30000)

@step(u'Then I should see (\d+) lists?')
def then_i_should_see_n_lists(step, quantity):
    quantity = int(quantity)
    count = int(world.browser.get_xpath_count('//li[@class="tricklelist"]'))
    assert_equal(count, quantity)


