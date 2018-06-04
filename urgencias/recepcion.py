#-*- coding: latin-1 -*-

'''
Created on Jun 3, 2018

@author: Jesús Molina
'''

import random

from pacientes import Pacientes


class Recepcion(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.diccionario_medicos = {}
        
        
    def ingreso_paciente(self):
        '''
        Crea un nuevo paciente y lo encola en la lista de recepción.
        '''
        paciente_ingresado = Pacientes()
        paciente_ingresado.generar_paciente()
        return paciente_ingresado
    
    
    def medico_aleatorio(self):
    
        lista_keys_diccionario = self.diccionario_medicos.keys()
        aleatorio_indice = random.randint(0,len(lista_keys_diccionario)-1)
        aleatorio_medico = lista_keys_diccionario[aleatorio_indice]
        return aleatorio_medico
    
    
    def decidir_medico_asignar(self):
        '''
        Decide si agregar un paciente a un médico si uno de los médicos del diccionario
        está libre, o si todos los médicos tienen pacientes en cola se escoge un médico
        al azar.
        '''
        for medico in self.diccionario_medicos:
            if len(self.diccionario_medicos[medico].lista) == 0:
                return medico
            else: 
                medico = self.medico_aleatorio()
                return medico
                
                
    def asignar_paciente_medico(self,paciente):
        '''
        Asigna el primer paciente de la lista de recepción al médico 
        devuelto por el método decidir_medico_asignar.
        '''
        medico = self.decidir_medico_asignar()
        self.diccionario_medicos[medico].nuevo_paciente(paciente)
        return medico
    
    
    def mostrar_diccionario(self):
        '''
        Imprime el diccionario de médicos con sus respectivos pacientes.
        '''
        nombres_medico = self.diccionario_medicos.keys()
        for medico in nombres_medico:
            print "El Dr." + str(medico) + " tiene estos pacientes en cola: "
            for paciente in self.diccionario_medicos[medico].lista:
                if paciente:
                    print paciente.get_nombre()
                    
                    
    def medico_cura_paciente(self):
        
        medico = self.medico_aleatorio()
        paciente_curado = self.diccionario_medicos[medico].proximo_paciente()
        if paciente_curado:
            return paciente_curado
        else:
            pass
        