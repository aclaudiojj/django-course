from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Ead
from .forms import ContactEad


def index(request):
    eads = Ead.objects.all()

    return render(request, 'ead/index.html', {
        'eads': eads
    })


def detail(request, slug):
    data = {}
    ead = get_object_or_404(Ead, slug=slug)

    if request.method == 'POST':
        form = ContactEad(request.POST)

        if form.is_valid():
            data['is_valid'] = True
            # form.cleaned_data['nome_do_campo']
            form.send_email(ead)
            form = ContactEad()

    else:
        form = ContactEad()

    data['ead'] = ead
    data['form'] = form

    return render(request, 'ead/detail.html', data)
