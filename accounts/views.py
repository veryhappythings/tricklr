from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User

def user_detail(request, user_id=None):
    if user_id == None:
        if request.user.is_authenticated():
            user = request.user
        else:
            return HttpResponseNotFound()
    else:
        user = get_object_or_404(User, pk=user_id)
    return render_to_response('registration/profile.html', {'user': user})