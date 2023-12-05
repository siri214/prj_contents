from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse
from django.conf import settings
from prjwk_contents.models import VideoContents as vc, VideoSeoul as vs
from .models import DownloadedVideo
import os
import json
from cryptography.fernet import Fernet
from django.http import JsonResponse
import datetime
from .models import VideoSeoul
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



def index(request):
    return render(request, "prjwk_contents/index.html")

@login_required
def busan(request):
    return render(request, "prjwk_contents/busan.html")

@login_required
def daegu(request):
    return render(request, "prjwk_contents/daegu.html")

@login_required
def incheon(request):
    return render(request, "prjwk_contents/incheon.html")

@login_required
def gwangju(request):
    return render(request, "prjwk_contents/gwangju.html")

@login_required
def daejeon(request):
    return render(request, "prjwk_contents/daejeon.html")

@login_required
def ulsan(request):
    return render(request, "prjwk_contents/ulsan.html")

@login_required
def gyeonggi(request):
    return render(request, "prjwk_contents/gyeonggi.html")

@login_required
def gangwon(request):
    return render(request, "prjwk_contents/gangwon.html")

@login_required
def northchungcheong(request):
    return render(request, "prjwk_contents/northchungcheong.html")

@login_required
def southchungcheong(request):
    return render(request, "prjwk_contents/southchungcheong.html")

@login_required
def northjeolla(request):
    return render(request, "prjwk_contents/northjeolla.html")

@login_required
def southjeolla(request):
    return render(request, "prjwk_contents/southjeolla.html")

@login_required
def northgyeongsang(request):
    return render(request, "prjwk_contents/northgyeongsang.html")

@login_required
def southgyeongsang(request):
    return render(request, "prjwk_contents/southgyeongsang.html")

@login_required
def jeju(request):
    return render(request, "prjwk_contents/jeju.html")

@login_required
def sejong(request):
    return render(request, "prjwk_contents/sejong.html")



#healthCheck API 생성, POSTMAN TEST 목적. 코드와 상관 X
def healthCheck(request):
    result = "Hello jasil"
    return HttpResponse(result)


#회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name']
                )
            auth.login(request, user)
            return redirect('/prjwk_contents/')
        return render(request, 'prjwk_contents/signup.html')
    return render(request, 'prjwk_contents/signup.html')


#로그인 기능
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/prjwk_contents/')
        else:
            return render(request, 'prjwk_contents/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'prjwk_contents/login.html')

        
def logout(request):
    auth.logout(request)
    return redirect("/prjwk_contents/")
        

@login_required
def seoul(request):
    video_seoul = VideoSeoul.objects.all().order_by('vid')
    paginator = Paginator(video_seoul, 10) #페이지당 10개의 동영상 표시
    page = request.GET.get('page')
    video_seoul = paginator.get_page(page)
    video_number = [(num + (video_seoul.number - 1) * 10) for num in video_seoul.paginator.page_range]
    return render(request, "prjwk_contents/seoul.html", {'video_seoul': video_seoul, 'video_number':video_number})

#비디오 다운로드 기능
@login_required
def download_video(request):
    video_name = request.GET.get('videoName')
    video = vs.objects.filter(contents_name=video_name).first()
    user = request.user

    if DownloadedVideo.objects.filter(user=user, video_name = video_name).exists():
        return render(request, "prjwk_contents/already_download.html")
    
    DownloadedVideo.objects.create(user = user, video_name = video_name)


    video_path = os.path.join(settings.MEDIA_ROOT, video.contents_path)

    with open(video_path, 'rb') as file:
        file_contents = file.read()
        response = HttpResponse(file_contents, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(video.contents_path)}"'
        return response


@login_required
def update_download_status(request):
    if request.method == 'POST':
        video_name = request.POST.get('videoName')
        user = request.user

        # 이미 다운로드한 동영상인지 확인
        if DownloadedVideo.objects.filter(user=user, video_name=video_name).exists():
            return JsonResponse({'status': '이미 다운로드한 동영상입니다. 결제 후에 이용해주세요'})

        # 다운로드 기록 저장
        DownloadedVideo.objects.create(user=user, video_name=video_name)

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})


# @login_required
# def video_detail(request, vid):
#     video = get_object_or_404(VideoSeoul, vid=vid)
#     user = request.user

#     can_download = video.can_be_downloaded(user)

#     return render(request, 'video_detail.html', {'video': video, 'can_download': can_download})


#비디오 플레이 기능, 사용X
# def play_video(request, video_id):
#     video = VideoSeoul.objects.get(vid=video_id)
#     video_path = os.path.join(settings.MEDIA_ROOT, video.contents_path)

#     with open(video_path, 'rb') as video_file:
#         response = HttpResponse(video_file.read(), content_type='video/mp4')
#         response['Content-Disposition'] = f'inline; filename="{os.path.basename(video.contents_path)}"'
#         return response
    




