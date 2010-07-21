from django.test import TestCase
from django.test.client import Client

from models import TrickleList, ListItem, DoneItem

class TestTrickleListApp(TestCase):
    def setup(self):
        self.client = Client()

    def test_404(self):
        response = self.client.get('/this_does_not_exist!/')
        self.assertEqual(response.status_code, 404)

    def test_that_index_page_exists(self):
        response = self.client.get('/trickle/')
        self.assertEqual(response.status_code, 200)

class TestTrickleList(TestCase):
    def test_adding_list_items(self):
        tl = TrickleList(name='Test List')
        tl.save()
        li = ListItem(name='Test Item', trickle_list=tl)
        li.save()
        self.assertEqual(li.trickle_list.id, tl.id)

        li = tl.listitem_set.create(name='Another test item')
        li.save()
        self.assertEqual(li.trickle_list.id, tl.id)

        self.assertEqual(
            map(lambda i: i.name, tl.listitem_set.all()),
            [u'Test Item', u'Another test item']
        )

class TestListItem(TestCase):
    def test_that_new_items_are_not_done_today(self):
        tl = TrickleList(name='Test List')
        tl.save()
        li = tl.listitem_set.create(name='Test item')
        li.save()
        self.assertFalse(li.is_done())

    def test_completing_an_item_today(self):
        tl = TrickleList(name='Test List')
        tl.save()
        li = tl.listitem_set.create(name='Test item')
        li.complete()
        li.save()
        self.assertTrue(li.is_done())

class TestDoneItem(TestCase):
    pass

