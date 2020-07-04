from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadForm
from .models import Upload
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/login')
def UploadView(request):
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if UploadForm.is_valid(form):
            f = form.save(commit=False)
            f.request_user = request.user
            f.save()
            return redirect('/upload')

    return render(request, 'upload/new.html', {'form': form})


@login_required(login_url='/login')
def index_upload(request):
    current_user = request.user
    list_upload = Upload.objects.filter(request_user=request.user).order_by('-date')
    return render(request, 'upload/index.html', {'user': current_user, 'list': list_upload})
