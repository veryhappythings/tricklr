# -*- coding: utf-8 -*-
import re
from lettuce import world
from lettuce import step
from lettuce.django import django_url

from django.contrib.auth.models import User

@step(u'Given that I have an account with username "(.*)" and password "(.*)"')
def given_that_i_have_an_account(step, username, password):
    user = User(username=username)
    user.set_password(password)
    user.save()

@step(u'When I go to the log in page')
def when_i_go_to_the_log_in_page(step):
    world.browser.get(django_url('/accounts/login'))

@step(u'And I login with valid credentials')
def and_i_login_with_valid_credentials(step):
    world.response = world.browser.post(
        django_url('/accounts/login'),
        {'username': 'test_user1', 'password': 'test_password', 'next': '/accounts/profile'}
    )

@step(u'Then I should see "(.*)"')
def then_i_should_see_(step, phrase):
    assert re.search(phrase, world.response.content)

@step(u'Then I should be redirected')
def then_i_should_be_redirected(step):
    assert world.response.status_code == 301

