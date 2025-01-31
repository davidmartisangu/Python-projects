import tkinter as tk
import urllib.request

def get_code():
    #Function to verified the status of the URL with urllib
    #Get the URL from the box
    web=input_text.get()
    try:
        response=urllib.request.urlopen(web)
        status_url=response.getcode()
        status_message.config(text=str(status_url))
    except Exception as e:
        #Show the message error in case there is one, so the user can check what is wrong
        status_message.config(text=str(e))

#Main window to interact with the user
window=tk.Tk()
window.title('Web conectivity')
window.geometry('650x300')

#Initial label message
init_message=tk.Label(window,text='Se va a comprobar la conectividad del sitio web. Un resultado mayor a 200 mostrará un correcto desempeño')
init_message.pack()

tk.Label(window).configure()
tk.Label(window).pack()

init_message_2=tk.Label(window,text='Escribe la URL a verificar:')
init_message_2.pack()

#Create a box to write the text
box=tk.Entry(window, width=70)
box.pack()
input_text = box #Variable where it´s saved the URL

#Create a button to check and show the URL status
status_button=tk.Button(window,text="Check",command=get_code)
status_button.pack()

status_message=tk.Label(window)
status_message.pack()

window.mainloop()