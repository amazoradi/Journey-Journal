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
      
        
        new_entry = Entry(title=title, location=location, content=content, date=date, image=image, customer_id=request.user.id)
        new_entry.save()

        return HttpResponseRedirect(reverse('Journal:landing_page'))

def entry_list(request, pk):
    
    entry_list = Entry.objects.filter(customer_id=pk)
    context = {'entry_list': entry_list}
    return render(request, 'entry_list.html', context)


def entry_edit(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    edit_form =  EntryForm(initial={'title': entry.title, 'location': entry.location, 'content': entry.content, 'date':entry.date, 'image':entry.image, 'customer_id':request.user.id})
    context = {"entry": entry, "edit_form": edit_form}
    return render(request, 'entry_edit_form.html', context)

def entry_update(request, entry_id):
    entry_details = Entry(id=request.POST['entry_id'],title=request.POST['title'], location=request.POST['location'], content=request.POST['content'], date=request.POST['date'], image=request.POST['image'], customer_id=request.user.id)
    entry_details.save()
    return HttpResponseRedirect(reverse('Journal:entry_list', args=(request.user.id,)))

