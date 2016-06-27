from .models import *
from django.shortcuts import render_to_response, get_object_or_404


# Create your views here.
def requests(request):
    return render_to_response('requests.html', {'requests': PERRequest.objects.all()})


def request(request, per_id):
    request = get_object_or_404(PERRequest, pk=per_id)
    return render_to_response('request.html', {'request': request})