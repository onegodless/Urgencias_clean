#-*- coding: latin-1 -*-
'''
Created on Jun 3, 2018

@author: Jesús Molina
'''

import random

from faker import Faker


class Pacientes(object):
    '''
    classdocs
    '''


    def __init__(self,nss=0,nombre="",edad=0,id_historial=0):
        '''
        Constructor
        '''
        self.__nss = nss
        self.__nombre = nombre
        self.__edad = edad
        self.__id_historial = id_historial
        self.generador = Faker('en_GB')
    
    
    def __str__(self):
        
        cadena = "Numero de afiliación: " + str(self.__nss) +  " Nombre: " + str(self.__nombre) + " Edad: " + str(self.__edad) + " Id historial: " + str(self.__id_historial)
        return cadena
    
    def get_nss(self):
        return self.__nss
    def set_nss(self,nss):
        self.__nss = nss
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def get_edad(self):
        return self.__edad
    def set_edad(self,edad):
        self.__edad = edad
    def get_id_historial(self):
        return self.__id_historial
    def set_id_historial(self,id_historial):
        self.__id_historial = id_historial
    
    def generar_paciente(self):
        
        self.__nss = self.generador.ssn()
        self.__nombre = self.generador.name()
        self.edad = random.randint(14,99)
        self.__id_historial = random.randint(9999,999999)