# -*- coding: utf-8 -*-
from lettuce import step, world
from lettuce.django import django_url
from nose.tools import assert_equal

from tricklelist.models import TrickleList

# Ands
@step(u'And I go to the list index')
def and_i_go_to_the_list_index(step):
    world.browser.open(django_url('/trickle/'))
    world.browser.wait_for_page_to_load(3000)

@step(u'And I click on the first list')
def and_i_click_on_the_first_list(step):
    world.browser.click('xpath=//li[@class="tricklelist"]/a')
    world.browser.wait_for_page_to_load(3000)

# Thens
@step(u'Then I should see (\d+) lists?')
def then_i_should_see_n_lists(step, quantity):
    quantity = int(quantity)
    count = int(world.browser.get_xpath_count('//li[@class="tricklelist"]'))
    assert_equal(count, quantity)

@step(u'Then I should see that list on the list display page')
def then_i_should_see_that_list_on_the_list_display_page(step):
    lists = TrickleList.objects.all()
    world.browser.is_text_present(lists[0].name)

