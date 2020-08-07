from .forms import FileUploadForm
from .models import BackgroundFile
from . import background_utility

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def background_home(request):
    background_list = BackgroundFile.objects.filter(
        background_owner=request.user.profile
        )
    return render(
        request,
        'background_app/background_home.html',
        {'background_list': background_list}
        )


@login_required(login_url='login')
def add_background(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.get('background_file')
            title = request.POST.get('background_title')
            file_instance = BackgroundFile(
                background_file=files,
                background_title=title,
                background_owner=request.user.profile
                )
            file_instance.save()
            if background_utility.resolution_checker(file_instance.background_file.path):
                file_instance.background_thumbnail = background_utility.image_resizer(file_instance.background_file.path)
                file_instance.save()
                print(file_instance.background_thumbnail.url)
                messages.success(request, 'background added')
                return redirect('background-home')
            else:
                file_instance.delete()
                messages.error(request, "image resolution too low or '.' in file name")
                return redirect('add-background')
    else:
        form = FileUploadForm()
    return render(
        request,
        'background_app/add_background.html',
        {
            'form': form
        }
        )


@login_required(login_url='login')
def delete_background(request, pk):
    to_be_deleted_background = BackgroundFile.objects.get(pk=pk)
    if request.method == 'POST':
        # print(to_be_deleted_background.background_thumbnail)
        # to_be_deleted_background.background_thumbnail.delete()
        to_be_deleted_background.delete()
        messages.success(request, 'background image deleted')
        return redirect('background-home')
    return redirect('background-home')


@login_required(login_url='login')
def use_background(request, pk):
    to_be_used_background_file = BackgroundFile.objects.get(pk=pk)
    if request.method == 'POST':
        messages.success(request, f'background changed to {to_be_used_background_file.background_title}')
        return redirect('background-home')
    return redirect('background-home')
