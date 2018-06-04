#-*- coding: latin-1 -*-

'''
Created on Jun 3, 2018

@author: Jesús Molina
'''

class ColaPacientes(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.lista = []
        
    
    def nuevo_paciente(self,paciente):
        
        self.lista.append(paciente)    
        
        
    def proximo_paciente(self):
        
        if not self.lista_vacia():
            paciente_saliente  = self.lista.pop(0)
            return paciente_saliente
    
    
    def lista_vacia(self):
        
        if len(self.lista) == 0:
            return True
    