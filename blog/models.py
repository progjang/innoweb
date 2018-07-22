from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)

class Device(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Resource(models.Model):
    CATEGORY_CHOICES = (
        ('M', '마케팅'),
        ('C', '임상'),
    )
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=1,
        choices=CATEGORY_CHOICES, default='M')
    device = models.ManyToManyField(Device)
    contenturl = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('category',)

    def __str__(self):
        return self.title
