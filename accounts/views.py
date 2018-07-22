from django.shortcuts import get_object_or_404, resolve_url, render, redirect
from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView, LoginView
from django.http import Http404
from django.utils.http import urlsafe_base64_decode
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, PlaceholderAuthForm
from django.views.generic import CreateView
from .models import Profile
from blog.models import Device
from django.core.mail import send_mail

# Create your views here.

@login_required
def profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    device_list = [device for device in profile.device.values_list('name', flat=True)]

    devices = Device.objects.all().filter(name__in=device_list)

    return render(request, 'accounts/profile.html', {
        'devices' : devices
    })

'''
def signup(request):
    if request.method == "POST":
        form = SignupFormForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            auth_login(request, user)  # 로그인 처리
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()

    return render(request, 'accounts/signup_form.html',{
        'form': form,
    })
'''

'''
signup = CreateView.as_view(model=User,
        form_class=SignupForm,
        template_name='accounts/signup_form.html',
        success_url=settings.LOGIN_URL)
'''
class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup_form.html'
    
    def get_success_url(self):
        return resolve_url('profile')

    def form_valid(self, form):
        user = form.save()
        auth_login(self.request, user)
        send_mail(
            '환영합니다.',
            'Here is the message.',
            'admin@innomed.co.kr',
            ['wooritobi@gmail.com'],
            fail_silently=False,
        )

        return redirect(self.get_success_url())

signup = SignupView.as_view()

class PlaceholderLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = PlaceholderAuthForm
    redirect_authenticated_user = True

login = PlaceholderLoginView.as_view()


class RequestLoginViaUrlView(PasswordResetView):
    template_name = 'accounts/request_login_via_url_form.html'
    title = '이메일을 통한 로그인'
    email_template_name = 'accounts/login_via_url.html'
    success_url = settings.LOGIN_URL


def login_via_url(request, uidb64, token):
    User = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        current_user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist, ValidationError):
        raise Http404

    if default_token_generator.check_token(current_user, token):
        auth_login(request, current_user)
        messages.info(request, '로그인이 승인되었습니다.')
        return redirect('root')

    messages.error(request, '로그인이 거부되었습니다.')
    return redirect('root')