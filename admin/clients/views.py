from copy import deepcopy

from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView

from admin.clients.models import Clients

from .forms import ClientForm, ClientUpdate


class ClientsList(LoginRequiredMixin, ListView):
    model = Clients
    login_url = '/'
    context_object_name = 'clients'
    template_name = 'client/clients_list.html'
    paginate_by = 10
    extra_context = {"title": "Clients", 'page_by': paginate_by}

    def get_queryset(self):
        self.extra_context['search_name'] = ""
        name = self.request.GET.get('name')
        object_list = self.model.objects.all()
        if name:
            object_list = object_list.filter(businessName__icontains=name)
            self.extra_context['search_name'] = name
        return object_list


class ClientAdd(LoginRequiredMixin, CreateView):
    form_class = ClientForm
    login_url = '/'
    template_name = 'client/add_clients.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'title': 'Add Client', 'form': ClientForm()})

    def post(self, request, *args, **kwargs):
        title = 'Add Client'
        data = deepcopy(request.POST)
        data['username'] = request.POST.get('personEmail')
        form = self.form_class(data)
        if form.is_valid():
            user = form.save()
            user.username = user.personEmail
            user.password = make_password(user.password)
            user.save()
            messages.success(request, "Client Added Successfully.")
            return redirect(reverse('clients'))
        else:
            for key, value in form.errors.items():
                messages.warning(request, value[0])
                return render(request, 'client/add_clients.html', locals())
        return render(request, 'client/add_clients.html', locals())


class ClientUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Clients
    form_class = ClientUpdate
    login_url = '/'
    success_message = 'Client Updated Successfully'
    success_url = '/client'
    template_name = 'client/update_clients.html'
    extra_context = {"title": "Update Client"}


def clientdel(request, pk):
    if request.method == 'POST':
        client_del = Clients.objects.get(pk=pk)
        client_del.delete()
        messages.success(request, "Client Deleted successfully.")
        return redirect(reverse('clients'))
    messages.error(request, "Method not allowed.")
    return redirect(reverse('clients'))


def changeStatus(request, pk):
    if request.method == 'POST':
        try:
            client = Clients.objects.get(pk=pk)
            if client.status == True:
                client.status = False
                client.save()
                messages.success(request, 'Account Deactivated Successfully')
            else:
                client.status = True
                client.save()
                messages.success(request, 'Account Activated Successfully')
        except:
            messages.error(request, 'Something went wrong')
    else:
        messages.error(request, 'Method Not allowed')
    return redirect(reverse('clients'))
