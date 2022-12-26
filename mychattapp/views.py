import json

from django.http import JsonResponse
from django.shortcuts import redirect, render

from .forms import ChatMessageForm
from .models import Chattmessage, Friend, Profile


# Create your views here.
def index(request):
    user=request.user.profile
    friends=request.user.profile.friends.all()
    context={"user":user ,"friends":friends}
    return render(request, "index.html" ,context)

def detail(request,pk):
    friend=Friend.objects.get(profile_id=pk)
    user=request.user.profile
    profile=Profile.objects.get(id=friend.profile.id)
    chats=Chattmessage.objects.all()
    rec_chats=Chattmessage.objects.filter(msg_sender=profile, msg_receiver=user)
    rec_chats.update(seen=True)
    form=ChatMessageForm()
    if request.method =="POST":
        form=ChatMessageForm(request.POST)
        if form.is_valid():  
            chat_message=form.save(commit=False)
            chat_message.msg_sender=user
            chat_message.msg_receiver=profile
            chat_message.save()
            return redirect("detail",pk=friend.profile.id)
    context={"friend":friend,"form":form, "user":user, "profile":profile, "chats":chats,"rec":rec_chats.count() }
    return render(request,"detail.html",context)  


def SendMessages(request,pk):
    sender=request.user.profile
    friend=Friend.objects.get(profile_id=pk)
    reciever=Profile.objects.get(id=friend.profile.id)
    data=json.loads(request.body)
    new_chat=data["msg"]
    new_chat_message=Chattmessage.objects.create(body=new_chat,msg_sender=sender,msg_receiver=reciever)

    print(new_chat)
    
    return JsonResponse(new_chat_message.body, safe=False)

def receivedMessages(request,pk):
    friend=Friend.objects.get(profile_id=pk)
    user=request.user.profile
    profile=Profile.objects.get(id=friend.profile.id)
    arr=[]
    chats=Chattmessage.objects.filter(msg_sender=profile , msg_receiver=user)
    for chat in chats:
        arr.append(chat.body)
    return JsonResponse(arr,safe=False)
    
def notification(request):
    user=request.user.profile
    friends=user.friends.all()
    arr=[]
    for friend in friends:

        chats=Chattmessage.objects.filter(msg_sender__id=friend.profile.id,msg_receiver=user,seen=False)
        arr.append(chats.count())
   

    return JsonResponse(arr,safe=False)