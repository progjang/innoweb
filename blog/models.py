from django.db import models
from datetime import timezone, timedelta, datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)

class Maker(models.Model):
    name = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', 'id')

    def __str__(self):
        return self.name

class Device(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('maker', 'id')

    def __str__(self):
        return self.name
def upload_location(instance, filename):
    tz = timezone(timedelta(hours=9)) # 9_timezone
    dt = datetime.now(timezone.utc).astimezone(tz)
    timestamp_month = dt.strftime("%Y-%m")
    filebase,extension = filename.split(".")
    filename = filebase + "_" + str(dt) + "." + extension
    return "{}/{}".format(timestamp_month, filename)
    
class Resource(models.Model):
    CATEGORY_CHOICES = (
        ('M', '마케팅'),
        ('C', '임상'),
    )
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=1,
        choices=CATEGORY_CHOICES, default='M')
    device = models.ManyToManyField(Device)
    resource = models.FileField(upload_to = upload_location,
        null=True, blank=True)
    contenturl = models.TextField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('category',)

    def __str__(self):
        return self.title
