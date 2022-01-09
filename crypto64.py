# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 06:12:38 2022

@author: javier
"""
import base64

def codificar(mensaje):
    mensaje_bytes = mensaje.encode('ascii')
    mensaje_base64 = base64.b64encode(mensaje_bytes)
    mensaje_codificado = mensaje_base64.decode('ascii')
    return mensaje_codificado

def decodificar(mensaje_codificado):
    mensaje_bytes = mensaje_codificado.encode('ascii')
    mensaje_base64 = base64.b64decode(mensaje_bytes)
    mensaje = mensaje_base64.decode('ascii')
    return mensaje