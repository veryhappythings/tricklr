from django.shortcuts import render_to_response, get_object_or_404
from models import TrickleList

def index(request):
    trickle_lists = TrickleList.objects.all()
    return render_to_response(
        'tricklelist/index.html',
        {'trickle_lists': trickle_lists}
    )

