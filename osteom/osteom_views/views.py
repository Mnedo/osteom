import random

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect
import smtplib
import datetime as dt
# Create your views here.
from django.views.generic import TemplateView, CreateView, UpdateView, FormView
from .forms import AppointmentForm, FeedbackForm, SearchForm
from .models import Tag, Feedback, Posts, Certificate, Bio, Jobs, ServicePrices, BlogAbout


def sendmail(dct):
    loginn, password = Bio.objects.all()[0].mail, ''
    # login - мэйл
    text_data = ''
    for key in dct.keys():
        text_data += dct[key]
        text_data += ' - '
        text_data += key
        text_data += '\n'
        if key == 'mail':
            mail = dct[key]
    if password != '':
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login(loginn, password)
        smtpObj.sendmail(loginn, mail, text_data)
        smtpObj.quit()


class MainView(TemplateView):
    template_name = 'landing.html'

    def get(self, request):
        prices = ServicePrices.objects.all()
        for price in prices:
            if price.free:
                price.price = 0
        prices = sorted(prices, key=lambda x: int(x.price))
        jobs = Jobs.objects.all()
        for job in jobs:
            job.location = '/'.join(str(job.location).split('/')[1:])
            if ';' in str(job.phones):
                job.phones = str(job.phones).split(';')
            else:
                job.phones = [job.phones]
        feedback = list(Feedback.objects.filter(is_visible=True)[:5])
        for _ in range(5 - len(feedback)):
            feedback.append(0)
        certificates = Certificate.objects.all()
        visitka = Bio.objects.all()[0]
        visitka.image = '/'.join(str(visitka.image).split('/')[1:])
        certificates_result = []
        certificates_group = []
        for certificate in certificates:
            certificate.image = '/'.join(str(certificate.image).split('/')[1:])
            certificates_group.append(certificate)
            if len(certificates_group) > 5:
                certificates_result.append(certificates_group)
                certificates_group = []
        certificates_result.append(certificates_group)
        feedback1, feedback2, feedback3, feedback4, feedback5 = feedback
        ctx = {'title': 'Главная', 'certificates': certificates_result, 'visitka': visitka,
               'feedback1': feedback1, 'feedback2': feedback2, 'feedback3': feedback3,
               'feedback4': feedback4, 'feedback5': feedback5,
               'jobs': jobs, 'prices': prices}
        return render(request, self.template_name, ctx)


class AppointmentView(FormView):
    template_name = 'appointment.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            sendmail(form.cleaned_data)
            # for key in form.cleaned_data.keys():
            # print(form.cleaned_data[key])  # данные пользователя
            return redirect(self.success_url)

    def get(self, request, *args, **kwargs):
        form = AppointmentForm()
        visitka = Bio.objects.all()[0]
        visitka.image = '/'.join(str(visitka.image).split('/')[1:])
        return render(request, 'appointment.html', {'form': form, 'title': 'Записаться', 'visitka': visitka})


class GiveFeedback(FormView):
    template_name = 'add_feedback.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST)

        if form.is_valid():
            model = Feedback()
            model.name = form.cleaned_data['name']
            model.surname = form.cleaned_data['surname']
            model.content = form.cleaned_data['content']
            model.save()
            return redirect(self.success_url)

    def get(self, request, *args, **kwargs):
        form = FeedbackForm()
        return render(request, self.template_name, {'form': form, 'title': 'Оставь свой отзыв'})


class BlogView(FormView):
    template_name = 'blog.html'
    success_url = '/blog'

    def post(self, request, *args, **kwargs):

        def smb(element):
            for zn in ['!', '?', '.', ',']:
                element = element.rstrip(zn)
            return element

        form = SearchForm(request.POST)
        if form.is_valid():
            key_word = form.cleaned_data['filter']
            about = BlogAbout.objects.all()[0]
            about.img = '/'.join(str(about.img).split('/')[1:])
            posts_main = Posts.objects.filter(is_urgent=True)
            posts_result = []
            for post in posts_main:
                post.image = '/'.join(str(post.image).split('/')[1:])
                if post.file:
                    post.file = '/'.join(str(post.file).split('/')[1:])
                if key_word == '':
                    posts_result.append(post)
                else:
                    if key_word in map(lambda x: smb(x), post.title.split()):
                        posts_result.append(post)
            posts_result = sorted(posts_result, key=lambda x: x.date_created, reverse=True)
            return render(request, self.template_name,
                          {'form': form, 'title': 'Личный блог', 'bio': about, 'posts': posts_result})

    def get(self, request, *args, **kwargs):
        form = SearchForm()
        about = BlogAbout.objects.all()[0]
        about.img = '/'.join(str(about.img).split('/')[1:])
        posts_main = Posts.objects.filter(is_urgent=True)
        for post in posts_main:
            post.image = '/'.join(str(post.image).split('/')[1:])
            if post.file:
                post.file = '/'.join(str(post.file).split('/')[1:])
        posts_main = sorted(posts_main, key=lambda x: x.date_created, reverse=True)
        return render(request, self.template_name,
                      {'form': form, 'title': 'Личный блог', 'bio': about, 'posts': posts_main})


class BlogViewYear(FormView):
    template_name = 'blog.html'
    success_url = '/blog'

    def post(self, request, *args, **kwargs):

        def smb(element):
            for zn in ['!', '?', '.', ',']:
                element = element.rstrip(zn)
            return element

        form = SearchForm(request.POST)
        if form.is_valid():
            key_word = form.cleaned_data['filter']
            about = BlogAbout.objects.all()[0]
            about.img = '/'.join(str(about.img).split('/')[1:])
            posts_main = Posts.objects.filter(is_urgent=True)
            posts_result = []
            for post in posts_main:
                post.image = '/'.join(str(post.image).split('/')[1:])
                if post.file:
                    post.file = '/'.join(str(post.file).split('/')[1:])
                if key_word == '':
                    posts_result.append(post)
                else:
                    if key_word in map(lambda x: smb(x), post.title.split()):
                        posts_result.append(post)
            posts_result = sorted(posts_result, key=lambda x: x.date_created, reverse=True)
            posts_res = []
            for post in posts_result:

                year = dt.datetime.now().date() + dt.timedelta()
                dd = post.date_created.date()
                delta = year - dd
                if 'days' in str(delta):
                    if int(str(delta).split()[0]) <= 365:
                        posts_res.append(post)
                else:
                    posts_res.append(post)
            return render(request, self.template_name,
                          {'form': form, 'title': 'Личный блог', 'bio': about, 'posts': posts_res})

    def get(self, request, *args, **kwargs):
        form = SearchForm()
        about = BlogAbout.objects.all()[0]
        about.img = '/'.join(str(about.img).split('/')[1:])
        posts_main = Posts.objects.filter(is_urgent=True)
        posts_main = sorted(posts_main, key=lambda x: x.date_created, reverse=True)
        posts_res = []
        for post in posts_main:
            post.image = '/'.join(str(post.image).split('/')[1:])
            if post.file:
                post.file = '/'.join(str(post.file).split('/')[1:])
            year = dt.datetime.now().date() + dt.timedelta()
            dd = post.date_created.date()
            delta = year - dd
            if 'days' in str(delta):
                if int(str(delta).split()[0]) <= 365:
                    posts_res.append(post)
            else:
                posts_res.append(post)
        return render(request, self.template_name,
                      {'form': form, 'title': 'Личный блог', 'bio': about, 'posts': posts_res})


class BlogViewMonth(FormView):
    template_name = 'blog.html'
    success_url = '/blog'

    def post(self, request, *args, **kwargs):

        def smb(element):
            for zn in ['!', '?', '.', ',']:
                element = element.rstrip(zn)
            return element

        form = SearchForm(request.POST)
        if form.is_valid():
            key_word = form.cleaned_data['filter']
            about = BlogAbout.objects.all()[0]
            about.img = '/'.join(str(about.img).split('/')[1:])
            posts_main = Posts.objects.filter(is_urgent=True)
            posts_result = []
            for post in posts_main:
                post.image = '/'.join(str(post.image).split('/')[1:])
                if post.file:
                    post.file = '/'.join(str(post.file).split('/')[1:])
                if key_word == '':
                    posts_result.append(post)
                else:
                    if key_word in map(lambda x: smb(x), post.title.split()):
                        posts_result.append(post)
            posts_result = sorted(posts_result, key=lambda x: x.date_created, reverse=True)
            posts_res = []
            for post in posts_result:
                year = dt.datetime.now().date() + dt.timedelta()
                dd = post.date_created.date()
                delta = year - dd
                if 'days' in str(delta):
                    if int(str(delta).split()[0]) <= 30:
                        posts_res.append(post)
                else:
                    posts_res.append(post)
            return render(request, self.template_name,
                          {'form': form, 'title': 'Личный блог', 'bio': about, 'posts': posts_res})

    def get(self, request, *args, **kwargs):
        form = SearchForm()
        about = BlogAbout.objects.all()[0]
        about.img = '/'.join(str(about.img).split('/')[1:])
        posts_main = Posts.objects.filter(is_urgent=True)
        for post in posts_main:
            if post.file:
                post.file = '/'.join(str(post.file).split('/')[1:])
            post.image = '/'.join(str(post.image).split('/')[1:])

        posts_main = sorted(posts_main, key=lambda x: x.date_created, reverse=True)
        posts_res = []
        for post in posts_main:
            year = dt.datetime.now().date() + dt.timedelta()
            dd = post.date_created.date()
            delta = year - dd
            if 'days' in str(delta):
                if int(str(delta).split()[0]) <= 30:
                    posts_res.append(post)
            else:
                posts_res.append(post)
        return render(request, self.template_name,
                      {'form': form, 'title': 'Личный блог', 'bio': about, 'posts': posts_res})


class BlogViewWeek(FormView):
    template_name = 'blog.html'
    success_url = '/blog'

    def post(self, request, *args, **kwargs):

        def smb(element):
            for zn in ['!', '?', '.', ',']:
                element = element.rstrip(zn)
            return element

        form = SearchForm(request.POST)
        if form.is_valid():
            key_word = form.cleaned_data['filter']
            about = BlogAbout.objects.all()[0]
            about.img = '/'.join(str(about.img).split('/')[1:])
            posts_main = Posts.objects.filter(is_urgent=True)
            posts_result = []
            for post in posts_main:
                if post.file:
                    post.file = '/'.join(str(post.file).split('/')[1:])
                post.image = '/'.join(str(post.image).split('/')[1:])
                if key_word == '':
                    posts_result.append(post)
                else:
                    if key_word in map(lambda x: smb(x), post.title.split()):
                        posts_result.append(post)
            posts_result = sorted(posts_result, key=lambda x: x.date_created, reverse=True)
            posts_res = []
            for post in posts_result:
                year = dt.datetime.now().date() + dt.timedelta()
                dd = post.date_created.date()
                delta = year - dd
                if 'days' in str(delta):
                    if int(str(delta).split()[0]) <= 7:
                        posts_res.append(post)
                else:
                    posts_res.append(post)
            return render(request, self.template_name,
                          {'form': form, 'title': 'Личный блог', 'bio': about, 'posts': posts_res})

    def get(self, request, *args, **kwargs):
        form = SearchForm()
        about = BlogAbout.objects.all()[0]
        about.img = '/'.join(str(about.img).split('/')[1:])
        posts_main = Posts.objects.filter(is_urgent=True)
        for post in posts_main:
            if post.file:
                post.file = '/'.join(str(post.file).split('/')[1:])
            post.image = '/'.join(str(post.image).split('/')[1:])
        posts_main = sorted(posts_main, key=lambda x: x.date_created, reverse=True)
        posts_res = []
        for post in posts_main:
            year = dt.datetime.now().date() + dt.timedelta()
            dd = post.date_created.date()
            delta = year - dd
            if 'days' in str(delta):
                if int(str(delta).split()[0]) <= 7:
                    posts_res.append(post)
            else:
                posts_res.append(post)
        return render(request, self.template_name,
                      {'form': form, 'title': 'Личный блог', 'bio': about, 'posts': posts_res})
