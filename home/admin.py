from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import PlaylistNode

class MyAdmin(TreeAdmin):
    form = movenodeform_factory(PlaylistNode)

admin.site.register(PlaylistNode, MyAdmin)