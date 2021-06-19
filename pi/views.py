from gpiozero import CPUTemperature
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Temperature

import time
import board
import adafruit_dht
import RPi.GPIO as GPIO


def blink():
    LED_PIN = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()


def dht22():
    dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
    temp = dhtDevice.temperature
    humi = dhtDevice.humidity
    print_temp = f"Enviorment temperature is {temp:.1f} °C"
    print_humi = f"Enviorment humidity is {humi:.1f}%"
    # blink()
    return [print_temp, print_humi]


def temp_of_pi():
    cpu = CPUTemperature()
    return f"Raspberry Pi temperature is {cpu.temperature:.1f} °C"


def pi(request):
    pi_temp = temp_of_pi()
    dht = dht22()
    blink()
    temp = [pi_temp, dht[0], dht[1]]
    context = {'temp': temp}
    return render(request, 'pi/pi.html', context)
