import datetime
from django.db import models

# TrickleList has many items
# items are done by a user, on a day

class TrickleList(models.Model):
    name = models.CharField(max_length=100)

class ListItem(models.Model):
    trickle_list = models.ForeignKey(TrickleList)
    name = models.CharField(max_length=50)

    def complete(self, date=None):
        if date == None:
            date = datetime.datetime.utcnow()
        done = self.doneitem_set.create(date=date)
        done.save()

    def is_done(self, date=None):
        if date == None:
            date = datetime.datetime.utcnow()
        return len(self.doneitem_set.select_related().dates('date', 'day')) > 0

class DoneItem(models.Model):
    list_item = models.ForeignKey(ListItem)
    date = models.DateField()

