from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Announcement, Respond
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import AnnouncementForm, RespondForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.conf import settings


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcement/home.html'
    context_object_name = 'news'


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcement/detail.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RespondForm()
        return context

    def get_success_url(self):
        return redirect('detail', self.id)


class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    template_name = 'announcement/create.html'
    form_class = AnnouncementForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
        return redirect('detail', form.id)


class AnnouncementDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'announcement/delete.html'
    queryset = Announcement.objects.all()
    success_url = '/'
    context_object_name = 'news'


class AnnouncementUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'announcement/create.html'
    form_class = AnnouncementForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Announcement.objects.get(pk=id)

    success_url = '/'


@login_required
def add_respond(request, pk):
    form = RespondForm(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        form.user = request.user
        form.announcement = Announcement.objects.get(id=pk)
        send_mail(f'Отклик на ваше объявление {form.announcement} от пользователя {form.user}',
                  f'{form.text}', settings.DEFAULT_FROM_EMAIL, [f'{form.announcement.user.email}'])
        form.save()
    return redirect('detail', pk)


class RespondListView(LoginRequiredMixin, ListView):
    model = Respond
    template_name = 'announcement/responds.html'
    context_object_name = 'responds'

    def get_queryset(self):
        return Respond.objects.filter(announcement__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['announcement'] = Announcement.objects.filter(user=self.request.user).exclude(announcements=None)
        return context


class RespondDetailView(LoginRequiredMixin, DetailView):
    model = Respond
    template_name = 'announcement/respond_detail.html'
    context_object_name = 'respond'


class RespondAnnouncementListView(LoginRequiredMixin, ListView):
    model = Respond
    template_name = 'announcement/responds.html'
    context_object_name = 'responds'

    def get_queryset(self):
        return Respond.objects.filter(announcement__user=self.request.user).filter(announcement__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['announcement'] = Announcement.objects.filter(user=self.request.user).exclude(announcements=None)
        return context


def delete_respond(request, pk):
    subject = Respond.objects.get(id=pk)
    subject.delete()
    return redirect('responds')

def accept_respond(request, pk):
    subject = Respond.objects.get(id=pk)
    subject.accept = True
    subject.save()
    send_mail(f'Отклик принят', f'Ваш отклик на объявление {subject.announcement} пользователя {subject.announcement.user} принят',
              settings.DEFAULT_FROM_EMAIL, [f'{subject.user.email}'])
    return redirect('responds')