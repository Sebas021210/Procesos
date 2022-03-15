'''
Programa para la simulación  de  corrida  de  programas  en  un  sistema  operativo  
de  tiempo  compartido.

Programado por:  Sebastián Solorzano

Fecha:  14 marzo de 2022
'''

# Importar funciones necesarias

import simpy
import random

# Iniciar funciones

def proceso(num, env, cpu, llegada):
    global tiempo_final
    yield env.timeout(llegada)
    tiempo_inicial = env.now
    inTime = random.randint(1, 10)
    print ("%s - tiempo inicial %f - utiliza %d pasos para CPU" % (num, tiempo_inicial, inTime))

    with cpu.request() as req:
        yield req
        yield env.timeout(inTime)
        print ("%s - libre al %f" % (num, env.now))

    tiempo_final = env.now - tiempo_inicial
    print ("%s - el tiempo final es %f" % (num, tiempo_final))
    tiempo_final = tiempo_final + tiempo_final

random.seed(3)
env = simpy.Environment() 
initial_cpu = simpy.Resource(env, capacity=1)
tiempo_final = 0
initial_procesos = 50  

for i in range(initial_procesos):
    llegada = 0 
    env.process(proceso('proceso %d' % i, env, initial_cpu, llegada))

# correr la simulacion
env.run(until = 500)
print('tiempo promedio %d ' % (tiempo_final / initial_procesos))
