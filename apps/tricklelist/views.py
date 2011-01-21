from django.shortcuts import render_to_response, get_object_or_404
from models import TrickleList

def index(request):
    trickle_list = TrickleList.objects.all()[0]
    return render_to_response(
        'tricklelist/index.html',
        {'trickle_list': trickle_list}
    )

