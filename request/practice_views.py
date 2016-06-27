from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from request.models import PERRequest


# Create your views here.
def hello(request):
    name = 'merps'
    html = "<html><body>Hi %s, this bloody thing has worked!</body></html>" % name
    return HttpResponse(html)


def hello_template(request):
    name = "merps"
    t = get_template('hello.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)


def hello_template_simple(request):
    name = 'merps'
    return render_to_response('hello.html', {'name': name})


class HelloTemplate(TemplateView):

    template_name = 'hello_class.html'

    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'merps'
        return context


def request(request):
    return render_to_response('requests.html',
                             {'requests': PERRequest.objects.all()})
