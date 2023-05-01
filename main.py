from machine import Pin
import time

# Led interno
led = Pin(25, Pin.OUT)
sen_1 = Pin(2, Pin.IN)

cont = 0
while True:
    t = time.localtime()
    # Mostrar la hora actual en formato HH:MM:SS
    hora_actual = "{:02d}:{:02d}:{:02d}".format(t[3], t[4], t[5])

    # Check sensor PIR
    if (sen_1.value() == 1):
        cont += 1
        led.value(1)
        print('Objeto detectado: ' + str(cont))
    else:
        led.value(0)
        print('No hay actividad')

    print("HORA:", hora_actual)

    time.sleep(1)
