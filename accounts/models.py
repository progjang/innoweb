from django.db import models
from blog.models import Device
from django.conf import settings
#from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    ROLE_CHOICES = (
        ('W', '원장'),
        ('M', '마케팅담당자'),
        ('S', '병원관계자'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=1,
        choices=ROLE_CHOICES, default='M')
    clinicname = models.CharField(max_length=100, blank=True)
    device = models.ManyToManyField(Device)

    def __str__(self):
        return self.user.username
'''
def on_post_save_for_user(sender, **kwargs):
    if kwargs['created']: # sender모델이 처음 생성되었을 때
        user = kwargs['instance']
        Profile.objects.create(user=user) #profile 레코드도 함께 생성됨

post_save.connect(on_post_save_for_user, sender=settings.AUTH_USER_MODEL)
'''