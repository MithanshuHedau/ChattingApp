from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Room, Message


def index(request):
    return render(request, 'index.html')


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    room = request.POST.get('room_name')
    username = request.POST.get('username')

    if Room.objects.filter(name=room).exists():
        return redirect(f'/{room}/?username={username}')
    else:
        new_room = Room.objects.create(name=room)
        return redirect(f'/{room}/?username={username}')


def send(request):
    message = request.POST.get('message')
    username = request.POST.get('username')
    room_id = request.POST.get('room_id')

    room = Room.objects.get(id=room_id)
    Message.objects.create(value=message, user=username, room=room)

    return JsonResponse({"status": "success"})


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details).order_by('date')

    return JsonResponse({
        "messages": [
            {
                "user": msg.user,
                "value": msg.value,
                "date": msg.date.strftime("%d %b, %Y %I:%M %p")
            } for msg in messages
        ]
    })
