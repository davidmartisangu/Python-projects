import webbrowser
import random
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from time import strftime

#Creation of the main window to interact with the user
window=tk.Tk()
window.title('Reloj Despertador YouTube')
window.geometry("380x250")
window.config(bg='black')

#Create style for the combobox
style = ttk.Style()
style.theme_create('combostyle', parent='alt',settings = {'TCombobox':
                                    {'configure':
                                    {'selectbackground': 'black',
                                    'fieldbackground': 'grey',
                                    'background': 'white'
                                    }}})
style.theme_use('combostyle')

#Labels for the alarm
label_alarm_hour=tk.Label(window,text="Hora",font=('Helvetica',12),fg='white',bg='black')
label_alarm_hour.grid(row=3,column=0)
label_alarm_minute=tk.Label(window,text="Minutos",font=('Helvetica',12),fg='white',bg='black')
label_alarm_minute.grid(row=3,column=1)
label_alarm_seconds=tk.Label(window,text="Segundos",font=('Helvetica',12),fg='white',bg='black')
label_alarm_seconds.grid(row=3,column=2)

#List of times for hours, minutes and seconds
list_hour=[i for i in range(24)]
list_minute=[i for i in range(60)]
list_seconds=list_minute[:]

#User will set the time for the alarm using a combobox
alarm_hour=ttk.Combobox(window,values=list_hour,style="TCombobox",width=15)
alarm_hour.grid(row=4,column=0,padx=15)
alarm_hour.current(0)
alarm_minute=ttk.Combobox(window,values=list_minute,style="TCombobox",width=15)
alarm_minute.grid(row=4,column=1, pady=0)
alarm_minute.current(0)
alarm_seconds=ttk.Combobox(window,values=list_seconds,style="TCombobox",width=15)
alarm_seconds.grid(row=4,column=2,padx=15)
alarm_seconds.current(0)

def actual_time():
    #Get the current time
    hour=strftime('%H')
    minute=strftime('%M')
    seconds=strftime('%S')
    total_time=f"{hour}:{minute}:{seconds}"
    #Label to display the current time
    label_time=tk.Label(window,text=total_time,font=('Helvetica',50),fg='white',bg='black')
    label_time.grid(row=0,columnspan=3,pady=15)

    #Get the time of the alarm from the combobox
    time_alarm_hour=alarm_hour.get().zfill(2)
    time_alarm_minute=alarm_minute.get().zfill(2)
    time_alarm_seconds=alarm_seconds.get().zfill(2)
    #Label to show the time for the alarm
    alarm_time=f"{time_alarm_hour}:{time_alarm_minute}:{time_alarm_seconds}"
    label_alarm_time=tk.Label(window,text=alarm_time,font=('Helvetica',15),fg='red',bg='black')
    label_alarm_time.grid(row=2,column=1,pady=7)
    label_text_alarm=tk.Label(window,text="Set alarm:",font=('Helvetica',12),fg='white',bg='black')
    label_text_alarm.grid(row=2,column=0,pady=7)

    #Conditional to trigger the alarm. Check if current time same as alarm time
    if int(hour)==int(time_alarm_hour) and int(minute)==int(time_alarm_minute) and int(seconds)==int(time_alarm_seconds):
        #Path to the url for the youtube alarm videos
        ruta_archivo=['8_enlaces.txt']
        #Read the url in the file
        for files in ruta_archivo:
            try:
                with open(files,'r') as lines:
                    content= lines.readlines()
            except FileNotFoundError:
                messagebox.showerror("Archivo no encontrado. Por favor asegurese que existe en el directorio.")
                return
        #Choose one randomly
        url_selectec=random.choice(content)
        #Open the url
        webbrowser.open(url_selectec)
    #Update teh time every second
    label_time.after(1000,actual_time)

actual_time()

window.mainloop()