from django.http import HttpResponse
from django.shortcuts import render
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
from django.utils import timezone
from .models import Post

request_timestamp = Signal(providing_args=['timestamp'])


def home(request):
    request_timestamp.send(sender=Post, timestamp=timezone.now())
    return HttpResponse("This is the response")


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("request finished")


@receiver(request_timestamp)
def my_callback(sender, **kwargs):
    print("custom signals works")
    print(kwargs)

