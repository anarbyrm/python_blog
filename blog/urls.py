from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home-page"),
    path("about/", views.AboutView.as_view(), name="about-page"),
    path("contact/", views.ContactView.as_view(), name="contact-page"),
    # path("", views.HomeView.as_view(), name="home-page"),
    # path("", views.HomeView.as_view(), name="home-page"),
    #
]