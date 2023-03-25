import tkinter as tk
import requests
########################################################################################
#obtener la imagen
def on_button_click():
    rblxid = texto_entry.get()
    response = requests.get('https://www.roblox.com/avatar-thumbnails?params=[{userId:'+rblxid+'}]')
    json_data = response.json()
    rblxname= json_data[0]['name']
    rblximgurl = json_data[0]['thumbnailUrl']
    rblximgurlescala = rblximgurl.replace("60/60/", "420/420/")
    img = requests.get(rblximgurlescala)

    if img.status_code == 200:
        #puedes cambiar 'img/{rblxname}.png' por la ruta en donde quieres que se guarde y el nombre
        
        with open(f'img/{rblxname}.png', 'wb') as f:
            f.write(img.content)
        print(f'Guardado como: {rblxname}.png')
#ventana de tkinter
ventana = tk.Tk()
ventana.title("ObtenerImagen")
ventana.geometry("300x150")
texto_entry = tk.Entry(ventana)
texto_entry.pack()
texto= tk.Label(ventana, text="introduce tu id de roblox")
texto.pack()
boton = tk.Button(ventana, text="Aceptar", command=on_button_click)
boton.pack()
ventana.mainloop()