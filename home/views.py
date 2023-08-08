import json
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import PlaylistNode
from django.db.models import Q

# Create your views here.

def get(name):
    return PlaylistNode.objects.get(title=name)


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def tester(request):
    temp = loader.get_template('test.html')
    context = {'collections': PlaylistNode.objects.all().values(), 'results' : []}
    return HttpResponse(temp.render(context, request))

queryset = PlaylistNode.objects.all().exclude(Q(depth=1) | Q(title__icontains="Lesson") | Q(title__icontains="Overview"))
filters = [{'name': 'Curriculum', 'key': 'urricul'},
           {'name': 'Activity Sets', 'key': 'ctivit'},
           {'name': 'Tutorials', 'key': 'utorial'}]

@csrf_exempt
def filtersSet(request, loaded=0):
    global queryset
    global filters
    lst = []
    temp = loader.get_template('search.html')
    if loaded == 0:
        for f in request.POST.values():
            print(f)
            lst.append(request.POST[f])
        for filter in filters:
            key = filter['key']
            if key not in lst:
                queryset = queryset.exclude(Q(title__icontains=key) | Q(desc__icontains=key))
    return HttpResponse(temp.render({'collection' : queryset}, request))


@csrf_exempt
def gridLayout(request, data=None, load=0):
    global queryset
    global filters
    filters = [{'name': 'Curriculum', 'key': 'urricul'},
               {'name': 'Activity Sets', 'key': 'ctivit'},
               {'name': 'Tutorials', 'key': 'utorial'}]
    queryset = PlaylistNode.objects.get(title='Activity Sets').get_descendants() | PlaylistNode.objects.get(title='Tutorials').get_descendants() | PlaylistNode.objects.get(title='Curriculum').get_children()
    queryset = queryset.order_by("title")
    temp = loader.get_template('grid.html')
    model = PlaylistNode
    context = {}
    context['title'] = "All Content"
    context['overview'] = "This is a collection of all the TunePad curriculum, activity sets, and tutorials, including specific activities and lessons. Use the search by in the upper right corner to populate results based on titles or topics of your choice. Use the filter button on the left to restrict results to specific types of items."
    query = request.GET.get("q")
    context['noresults'] = False
    context['search'] = None
    if query != None:
        context['search'] = query
        queryset = queryset.filter(Q(title__icontains=query) | Q(desc__icontains=query))
    if data:
        target = get_object_or_404(model, slug=data)
        queryset = target.get_children()
        context['title'] = target.title
        context['overview'] = target.desc
        if "activity" in target.desc:
            filters = [{'name': 'Beginner', 'key': 0},
                       {'name': 'Intermediate', 'key': 1},
                       {'name': 'Advanced', 'key': 2}]
        else:
            filters = None
    if not queryset:
        context['noresults'] = True
    context['collection'] = queryset.values()
    context['filters'] = filters
    return HttpResponse(temp.render(context, request))

def landing(request):
    temp = loader.get_template('home.html')
    context = {'loggedin': False,
               'collections': PlaylistNode.get_root_nodes(),
               'libraries' : [get('Curriculum').get_children(), get('Activity Sets').get_children(), get('Tutorials').get_children()],}
    return HttpResponse(temp.render(context))

def searchResults(request):
    if 'term' in request.GET:
        query = PlaylistNode.objects.get(title='Activity Sets').get_descendants() | PlaylistNode.objects.get(title='Tutorials').get_descendants() | PlaylistNode.objects.get(title='Curriculum').get_children()
        query = query.order_by("title")
        qs = query.filter(Q(title__icontains=request.GET.get('term')) | Q(desc__icontains=request.GET.get('term')))
        result = list()
        for idx, obj in enumerate(qs):
            if idx == 5:
                break
            result.append(obj.title)
        return JsonResponse(result, safe=False)


def sidebarLayout(request, data):
    target = get_object_or_404(PlaylistNode, slug=data)
    temp = loader.get_template('sidebar.html')
    return HttpResponse(temp.render({'curriculum' : target}))

def embed(request, data):
    target = get_object_or_404(PlaylistNode, slug=data)
    temp = loader.get_template('embed.html')
    context = {'video' : target,
               'collection' : target.get_siblings().exclude(slug__icontains=data)}
    return HttpResponse(temp.render(context))
