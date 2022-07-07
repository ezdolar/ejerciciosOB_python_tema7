import time

# las 7pm en formato 24h es 19
# supongamos que la hora de salida puede cambiar
# por lo que se almacena en una constante
HORA_SALIDA = 19

# extrae la hora exacta en el momento de ejecucion
horas = time.localtime().tm_hour
minutos = time.localtime().tm_min

if horas >= HORA_SALIDA:
    print("Es hora de ir a casa")
else:
    # la hora de salida exacta no cuenta, por lo que se resta 1 hora
    print ("Le quedan %d horas y %d minutos de trabajo" % (HORA_SALIDA - horas - 1, 60 - minutos))