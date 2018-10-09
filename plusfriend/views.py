from os.path import basename
import requests
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, resolve_url
from .decorators import bot
from .models import KakaoPost

@bot
def on_init(request):
    return {'type': 'text'}

@bot
def on_message(request):
    user_key = request.JSON['user_key']
    type = request.JSON['type']
    content = request.JSON['content'] # photo 타입일 경우에는 이미지 url

    if type == 'photo':
        img_url = content
        img_data  = requests.get(img_url).content
        img_name = basename(img_url)
        post = KakaoPost(user=request.user)
        post.photo.save(img_name, ContentFile(img_data), save=False)
        post.save()

        response = '사진을 저장했습니다.'

    else:
        if content == '!웹주소':
            web_url = request.build_absolute_uri(resolve_url('plusfriend:post_list'))
            print(resolve_url('plusfriend:post_list'))
            response = '{} 로 접속하세요'.format(web_url)            
        elif content.startswith('!내암호:'):
            password = content[5:]
            request.user.set_password(password)
            request.user.save()
            response = '암호를 설정했습니다.'
        else:
            post = KakaoPost.objects.create(user=request.user, message=content)
            response = '포스팅을 저장했습니다.'

    return {
        'message': {
            'text': response,
        }
    }

@bot
def on_added(request):
    user_key = request.JSON['user_key']

@bot
def on_block(request, user_key):
    pass

@bot
def on_leave(request, user_key):
    pass

@login_required
def post_list(request):
    qs = Post.objects.filter(user=request.user)
    #qs = Post.objects.all()
    print(qs)
    return render(request, 'plusfriend/post_list.html', {
        'post_list': qs,
    })