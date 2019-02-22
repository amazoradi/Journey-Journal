from django.shortcuts import render
from Journal.forms import EntryForm
from Journal.models import *



def entry(request):


    if request.method == 'GET':
        entry_form = EntryForm()
        context = {'entry_form': entry_form}
        return render(request, 'entry_add.html', context)

