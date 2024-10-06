
import pyautogui
import webbrowser
from time import sleep

# Define a dictionary of brothers and their phone numbers
bro = {
    //ingrese los numeros de sus bros con sus nombres
    // 'nombre', numero
}

# Function to generate the WhatsApp URL for a given phone number
def generar_url_whatsapp(numero):
    base_url = 'https://web.whatsapp.com/send?phone='
    full_url = f'{base_url}+{numero}'
    return full_url

# Print the available brothers
print("bros disponibles:")
for nombre in bro:
    print(nombre)

# Ask the user to choose a brother to send a message to
bro_elegido = input("eliga a tu bro para mandarle un msg:  ")

# If the chosen brother is in the list, open the WhatsApp URL and send a message
if bro_elegido in bro:
    numero_bro = bro[bro_elegido]
    webbrowser.open(generar_url_whatsapp(numero_bro))
    sleep(10)
    for _ in range(10):
        pyautogui.typewrite('funciono jeje')
        pyautogui.press('enter')
else:
    print("tu bro no esta en la lista.")
#
#This code defines a dictionary of brothers and their phone numbers. It then prints the available brothers and asks the user to choose one to send a message to. If the chosen brother is in the list, the code opens the WhatsApp URL for that brother and sends a message..</s>
