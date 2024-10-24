#------------------
#
# Código de cambio de DNS ante problemas de red en Windows
# Escrito por: Ramal
#
#-------------------

import os

#Datos del sistema
interface = ""
dns1 = ""

#Este codigo literalmente cambia la DNS a la escogida a
#traves del sistema de windows
def changeDNS(interface:str, dns:str):
    os.system(f"netsh interface ip set dns name={interface} static {dns}")
    pass

#Este codigo deja en el estado de fabrica de windows
#osea el automatico
def changeDefault(interface:str):
    os.system(f"netsh interface ip set dns name={interface} source=dhcp")
    pass


#
#inicio de ejecucion
#

#No hay ninguna interfaz? selecione una
if interface == "":
    while interface == "":
        os.system("netsh interface show interface")

        #Obtener direccion
        print("Copie y pege la interfaz que desea cambiar su dns: ")
        interface = input("->")
        pass

    pass

#Obtener nueva DNS
print("Inserte nueva dns (no pongas nada si quieres ponerla en default)")
dns1 = input("->")

if dns1 == "":
    #Poner en Default
    changeDefault(interface)
    pass
else:
    #Poner la nueva DNS
    changeDNS(interface, dns1)



input("Pulse Enter para cerrar...")


