from django.contrib import admin
from models import TrickleList, ListItem, DoneItem

class TrickleListAdmin(admin.ModelAdmin):
    pass
admin.site.register(TrickleList, TrickleListAdmin)

class ListItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(ListItem, ListItemAdmin)

class DoneItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(DoneItem, DoneItemAdmin)
