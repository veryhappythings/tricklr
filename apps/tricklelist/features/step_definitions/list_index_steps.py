# -*- coding: utf-8 -*-
from lettuce import step, world
from lettuce.django import django_url
from nose.tools import assert_equal



@step(u'And I go to the list index')
def and_i_go_to_the_list_index(step):
    world.browser.open(django_url('/trickle/'))
    world.browser.wait_for_page_to_load(30000)

@step(u'Then I should see (\d+) lists?')
def then_i_should_see_n_lists(step, quantity):
    quantity = int(quantity)
    count = int(world.browser.get_xpath_count('//li[@class="tricklelist"]'))
    assert_equal(count, quantity)


