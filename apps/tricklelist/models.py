import datetime
from django.db import models

# TrickleList has many items
# items are done by a user, on a day

class TrickleList(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def items_for_date(self, date=None):
        if date == None:
            date = datetime.datetime.utcnow()
        return False

    @models.permalink
    def get_absolute_url(self):
        return ('tricklelist.views.details', [str(self.id)])

class ListItem(models.Model):
    trickle_list = models.ForeignKey(TrickleList)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    def complete(self, date=None):
        if date == None:
            date = datetime.datetime.utcnow()
        done = self.doneitem_set.create(date=date)
        done.save()

    def is_done(self, date=None):
        if date == None:
            date = datetime.datetime.utcnow()
        return len(self.doneitem_set.filter(date__day=date.day)) > 0

class DoneItem(models.Model):
    list_item = models.ForeignKey(ListItem)
    date = models.DateTimeField()

    def __unicode__(self):
        return unicode(self.list_item) + ' ' + unicode(self.date)

