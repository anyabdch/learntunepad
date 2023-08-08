from django.db import models
from treebeard.mp_tree import MP_Node
from django.urls import reverse


# Create your models here.
class TestDb(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    desc = models.CharField(max_length=1000, null=True)
    tags = models.CharField(max_length=1000, null=True)
    t = models.BooleanField(null=True)

class PlaylistNode(MP_Node):
    node_order_by = ['ordering', 'title']

    ordering = models.IntegerField()
    title = models.CharField(max_length=255)

    desc = models.TextField(null=True) #could include keywords in desc?
    slug = models.SlugField(null=False, unique=True)
    type = models.CharField(max_length=3, default='/g/')

    # tunepad project_id to display an embedded project
    project_id = models.CharField(null=True, blank=True, default='1200', verbose_name='TunePad Project ID', max_length=15)

    # URL to display external content (e.g. Google doc)
    url = models.URLField(max_length=512, default=None, blank=True, null=True, verbose_name='External URL')

    # markdown text to display markdown
    text = models.TextField(verbose_name='Markdown Text', default=None, blank=True, null=True)

    # MartorField?

    def __str__(self):
        return "{}: {} ({})".format(self.title, self.desc, self.id)

    def get_absolute_url(self):
        return reverse("content", kwargs={"slug": self.slug})