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
    world.browser.open(django_url('/accounts/login'))

@step(u'And I login with username "(.*)" and password "(.*)"')
def and_i_login_with_valid_credentials(step, username, password):
    world.browser.type('username', username)
    world.browser.type('password', password)
    world.browser.click('submit')
    world.browser.wait_for_page_to_load(30000)

@step(u'Then I should see "(.*)"')
def then_i_should_see_(step, phrase):
    assert world.browser.is_text_present(phrase)

@step(u'Then I should be redirected')
def then_i_should_be_redirected(step):
    assert world.response.status_code == 301

