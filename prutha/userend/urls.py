from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView


app_name="userend"
urlpatterns=[
path("",TemplateView.as_view(template_name="userend/index.html"),name="home"),
# path("register",views.register.as_view(), name="register"),
# path("login", views.login.as_view(), name="login"),
path("know_more",views.know_more,name="know_more"),
path("appointment",views.appointment.as_view(),name="appointment"),
path("appointment/success",views.appointment_success,name="appointment_success"),
# path("counsellor",views.counsellor.as_view(),name="counsellor"),
# path("intern",views.intern.as_view(),name="intern"),
]

