# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import UserMessage
# from django.views.decorators.csrf import csrf_exempt,csrf_protect

# Create your views here.

def getform(request):
    message = None
    all_messages = UserMessage.objects.filter(name='mx', address=u'重庆')
    if all_messages:
        message = all_messages[0]

    # all_messages.delete()
    # for message in all_messages:
    #     print message.name

    # if request.method == 'POST':
    #     name = request.POST.get(u'name', '')
    #     message = request.POST.get(u'message', '')
    #     address = request.POST.get(u'address', '')
    #     email = request.POST.get(u'email', '')
    #
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = 'hlwd3'
    #
    #     user_message.save()

    return render(request, 'message_form.html',{
        'my_message':message
    })
