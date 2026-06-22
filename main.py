from machine import Pin
import dht
import time

sensor = dht.DHT22(Pin(15))

print("IOT WEATHER STATION")
print("-------------------")

while True:
    try:
        sensor.measure()

        temp = sensor.temperature()
        hum = sensor.humidity()

        print("Temperature:", temp, "°C")
        print("Humidity:", hum, "%")
        print("-------------------")

    except Exception as e:
        print("Error:", e)

    time.sleep(2)