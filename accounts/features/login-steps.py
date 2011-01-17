# -*- coding: utf-8 -*-
from lettuce import world
from lettuce import step
from lettuce.django import django_url

from django.contrib.auth.models import User

@step(u'Given that I have an account')
def given_that_i_have_an_account(step):
    user = User(
        username='test_user1',
        password='test_password'
    )
    user.save()

@step(u'When I go to the log in page')
def when_i_go_to_the_log_in_page(step):
    world.browser.get(django_url('/accounts/login'))

@step(u'And I login with valid credentials')
def and_i_login_with_valid_credentials(step):
    world.browser.post(
        django_url('/accounts/login'),
        {'username': 'test_user1', 'password': 'test_password'}
    )

@step(u'Then I should see "(.*)"')
def then_i_should_see_group1(step, group1):
    assert False, 'This step must be implemented'

