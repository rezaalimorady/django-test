from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/login')
def inbox(request):
    current_user = request.user.id
    message = Message.objects.filter(send_to=current_user).order_by('-update')
    # user = User.objects.all()
    return render(request, 'message/list.html', {'message': message, 'current_user': current_user})