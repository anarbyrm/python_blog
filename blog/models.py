from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
import readtime


class Tag(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        name = str(self.name)
        return name.lower()
    

class Post(models.Model):
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=150, null=True, blank=True)
    content = RichTextUploadingField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='posts/')
    slug = models.SlugField(null=True, blank=True, unique=True)
    views = models.ManyToManyField('blog.IPModel', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at', 'title']

    def __str__(self) -> str:
        return self.title

    def get_readtime(self):
        result = readtime.of_text(self.content, wpm=100)
        return result.text


class Tutorial(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    description = RichTextUploadingField()
    photo = models.ImageField(null=True, blank=True, upload_to="tutorial/")
    slug = models.SlugField(null=True, blank=True, unique=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at', '-created_at', 'name']

    def __str__(self) -> str:
        return self.name


class Lesson(models.Model):
    tutorial = models.ForeignKey(Tutorial, models.PROTECT, related_name='lessons')
    title = models.CharField(max_length=150, null=True, blank=True)
    content = RichTextUploadingField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    order = models.PositiveIntegerField(null=True, blank=True, unique=True)
    views = models.ManyToManyField('blog.IPModel', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self) -> str:
        return f"{self.tutorial.name}/lesson: {self.order}"

    def get_readtime(self):
        result = readtime.of_text(self.content, wpm=100)
        return result.text


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
    image = models.ImageField(null=True, blank=True, upload_to='info/')
    linkedin = models.URLField(null=True, blank=True,)
    resume = models.FileField(null=True, blank=True, upload_to='resume/')

    @property
    def get_full_name(self):
        return f"{self.name} {self.surname}"


class WebsiteSetting(models.Model):
    site_name = models.CharField(max_length=50, null=True, blank=True)
    site_title = models.CharField(max_length=200, null=True, blank=True)
    meta_keywords = models.CharField(max_length=200, null=True, blank=True)
    meta_description = models.CharField(max_length=600, null=True, blank=True)
    site_name_footer = models.CharField(max_length=100, null=True, blank=True)
    footer_caption = models.CharField(max_length=100, null=True, blank=True)


class IPModel(models.Model):
    address = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.address


