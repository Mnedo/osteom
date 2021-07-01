from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainView.as_view()),
    path('add_feedback', views.GiveFeedback.as_view()),
    path('appointment', views.AppointmentView.as_view()),
    path('blog', views.BlogView.as_view()),
    path('blogy', views.BlogViewYear.as_view()),
    path('blogm', views.BlogViewMonth.as_view()),
    path('blogw', views.BlogViewWeek.as_view())
]