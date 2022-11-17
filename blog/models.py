from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Topic(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
    

class Post(models.Model):
    topic = models.ForeignKey(Topic, models.PROTECT, related_name='posts')
    title = models.CharField(max_length=150, null=True, blank=True)
    content = RichTextUploadingField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='media/posts/')
    slug = models.SlugField(null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at', 'title', 'views']

    def __str__(self) -> str:
        return self.title


class About(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    content = RichTextUploadingField(null=True, blank=True)


class Contact(models.Model):
    full_name = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=150, null=True, blank=True)
    content = models.TextField()
    sent_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-sent_at', 'full_name']

    def __str__(self):
        return f'{self.full_name} on date: {self.sent_at}'
    

class Info(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    surname = models.CharField(max_length=150, null=True, blank=True)
    bio = RichTextUploadingField(null=True, blank=True,)
    image = models.ImageField(null=True, blank=True, upload_to='media/info/')
    linkedin = models.URLField(null=True, blank=True,)
    resume = models.FileField(null=True, blank=True, upload_to='media/resume/')
