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
            return redirect('contact')
        else:
            messages.error(request, "please correct the error below.")
    else:
        form = ContactForm()
    return render(request, 'contact', {'form': form})

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})


def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()  # Save the contact to the database
            messages.success(request, f"Contact '{contact.name}' was created successfully!")
            return redirect('contact_list')  # Replace with your contact list URL name
        else:
            messages.error(request, "There was an error creating the contact. Please try again.")
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save()
            messages.success(request, f"Contact '{contact.name}' was updated successfully!")
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_form.html', {'form': form})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        contact_name = contact.name
        contact.delete()
        messages.success(request, f"The contact '{contact_name}' has been deleted successfully!")
        return redirect('contact_list')
    return render(request, 'contact_confirm_delete.html', {'contact': contact})


