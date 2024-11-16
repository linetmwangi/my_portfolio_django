from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('contact.html')
        else:
            messages.error(request, "please correct the error below.")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_form.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Your contact has been deleted successfully.')
        return redirect('contact_list')
    return render(request, 'contact_confirm_delete.html', {'contact': contact})
