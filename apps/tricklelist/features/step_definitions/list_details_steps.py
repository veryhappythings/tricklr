# -*- coding: utf-8 -*-
from lettuce import step, world
from lettuce.django import django_url
from nose.tools import assert_true

from tricklelist.models import TrickleList

@step(u'And I go to the list details page for "(.*)"')
def and_i_go_to_the_list_details_page_for_name(step, name):
    tl = TrickleList.objects.get(name=name)
    world.browser.open(django_url(tl.get_absolute_url()))
    world.browser.wait_for_page_to_load(3000)


@step(u'Then I should see the items "(.*)" and "(.*)"')
def then_i_should_see_the_items_group1_and_group2(step, group1, group2):
    assert_true(world.browser.is_text_present(group1))
    assert_true(world.browser.is_text_present(group2))

