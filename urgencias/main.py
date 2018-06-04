#-*- coding: latin-1 -*-
'''
Created on Jun 3, 2018

@author: Jesús Molina
'''

import time
import random

from faker import Faker

from pacientes import Pacientes
from cola_pacientes import ColaPacientes
from recepcion import Recepcion


generador = Faker('en_GB')
cola_recepcion = ColaPacientes()
recepcion_urgencias = Recepcion()

if __name__ == '__main__':
    
    #Creación de pacientes en recepción iniciales.
    for repeticiones in range(6):
        
        paciente = Pacientes()
        paciente.generar_paciente()
        cola_recepcion.nuevo_paciente(paciente)
        
    #Creación de médicos
    for repeticiones in range(3):
        
        medico =  generador.name()
        recepcion_urgencias.diccionario_medicos[medico] = ColaPacientes()
        
    while True:
        
        print "Lista de pacientes en recepción:" #Imprime la lista de pacientes en recepción.
        for paciente in cola_recepcion.lista:
            print "[ " + str(paciente) + " ]"
        print ""
        
        simular = random.randint(0,1)
        if simular > 0:
            paciente_ingresado = recepcion_urgencias.ingreso_paciente() #Comprueba si un paciente entra en urgencias.
            if paciente_ingresado:
                print "Paciente entra en urgencias: "
                print paciente
            cola_recepcion.nuevo_paciente(paciente_ingresado) #Añade el nuevo paciente a la cola de recepción.
            print ""
            
        #Simulacion medico cura a paciente:
        simular = random.randint(0,3)
        if simular > 0:    
            paciente = recepcion_urgencias.medico_cura_paciente()
            if paciente:
                print "El paciente " + str(paciente.get_nombre()) + " ha sido dado de alta"
            
        #Simulación de asignacion de paciente a médico:
        simular = random.randint(0,3)
        if simular > 0:
            
            paciente_asignar = cola_recepcion.proximo_paciente()
            if paciente_asignar:
                medico = recepcion_urgencias.asignar_paciente_medico(paciente_asignar)
                print "El paciente " + str(paciente_asignar.get_nombre()) + " ha sido asignado a " + str(medico) + "\n"
                       
        #Mostrar lista de pacientes de cada médico:
        recepcion_urgencias.mostrar_diccionario()
        
        print "########################################################################"
        time.sleep(2)