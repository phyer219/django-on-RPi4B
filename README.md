# A Django project on Raspberry Pi 4B

use DHT22 senser, get the temperature and humidity.

uas archlinux arm, apache2, SQLite

Just for fun :)

# Notes

### Not running on a RPi!

you may got error: RuntimeError: Not running on a RPi!

This is because Django does not have right to read `/dev/gpiomem` 

Ref: https://github.com/adafruit/Adafruit_Blinka/issues/150

