from django.shortcuts import render_to_response, get_object_or_404
from models import TrickleList

def index(request):
    trickle_lists = TrickleList.objects.all()
    return render_to_response(
        'tricklelist/index.html',
        {'trickle_lists': trickle_lists}
    )

def details(request, list_id):
    #TODO: authenticate
    trickle_list = get_object_or_404(TrickleList, pk=list_id)
    return render_to_response(
        'tricklelist/details.html',
        {'trickle_list': trickle_list}
    )
