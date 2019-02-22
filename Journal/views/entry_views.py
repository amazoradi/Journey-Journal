from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from Journal.forms import EntryForm
from Journal.models import *



def entry(request, pk):

    if request.method == 'GET':
        entry_form = EntryForm()
        context = {'entry_form': entry_form}
        return render(request, 'entry_add.html', context)

    if request.method == 'POST':
    
        title = request.POST['title']
        location = request.POST['location']
        content = request.POST['content']
        date = request.POST['date']
        image = request.POST['image']
        # pk = User.id
        print(pk, "++++++++++++++++++++")
        
        
        new_entry = Entry(title=title, location=location, content=content, date=date, image=image, customer_id=request.user.id)
        new_entry.save()

        return HttpResponseRedirect(reverse('Journal:landing_page'))

def entry_list(request, pk):
    
    entry_list = Entry.objects.filter(customer_id=pk)
    context = {'entry_list': entry_list}
    return render(request, 'entry_list.html', context)


