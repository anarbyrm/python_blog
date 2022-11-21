from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home-page"),
    path("about/", views.AboutView.as_view(), name="about-page"),
    path("contact/", views.ContactView.as_view(), name="contact-page"),
    path("posts/", views.PostListView.as_view(), name="post-list-page"),
    path("posts/<slug:slug>/", views.PostDetailView.as_view(), name="post-detail-page"),
    path("tutorials/", views.TutorialListView.as_view(), name="tutorial-list-page"),
    path("tutorials/<slug:slug>/", views.TutorialDetailView.as_view(), name="tutorial-detail-page"),
    path("lessons/<slug:slug>/", views.LessonDetailView.as_view(), name="lesson-detail-page"),

]