'''crear un programa que evalúe cuan rápido puedes escribir una oración de manera precisa'''

import tkinter as tk
import timeit
import frases_prueba3

#Function to start the time of the test
def init_time():
    return timeit.default_timer()

#Function to end the time of the test
def end_time():
    time=timeit.default_timer()-start_time
    formatted_time='{:.2f}'.format(time)
    return formatted_time

input_text=" "
#Function to work with the button
def start_test():
    global input_text
    global sentence
    sentence=frases_prueba3.test_sentence()
    welcome_msg.config(text=sentence) #Modified the text in welcome_msg
    boton.pack_forget() #hide the button
    boton_finish.pack()
    #Create a box to write the text
    box=tk.Entry(ventana, width=90)
    box.pack()
    input_text = box #Variable where it´s saved the text

#Function to save the text written by the user, stop the time & show the result
def finish():
    global input_text
    user=input_text.get()
    input_text.config(state='disabled')
    boton_finish.pack_forget()
    #Test score
    score=input_check(sentence,user)
    formatted_time=end_time()
    if score is not None:
        score_msg.config(text='Score: '+str(score)+'%'+'   '+'Time: '+str(formatted_time))
        boton_end.pack()
    else:
        score_msg.config(text='Tienes que escribir el mismo número de caracteres. Reinicia el programa para hacer la prueba de nuevo')
        boton_end.pack()


#Function to calculate the accuracy of the text written
def input_check(text_1,text_2):
    match=0
    try:
        for i in range(len(text_1)):
            if text_1[i]==text_2[i]:
                match+=1
        accuracy=(match/len(text_1))*100
        return accuracy
    except IndexError:
        return None

#Function to close the window
def close_window():
    ventana.destroy()

#Create the main window interface
ventana=tk.Tk()
ventana.title('WRITING TEST')
ventana.geometry('650x300')

#Create a label with a welcome message
welcome_msg=tk.Label(ventana, text='Bienvenido a la prueba de escritura. Te vamos a mostrar un texto aletario para escribir en un tiempo limitado')
welcome_msg.pack()  #show the message

#Label with the test performance
score_msg=tk.Label(ventana, text='')
score_msg.pack()  #show the message

#Create a button to start the test
start_time=init_time()
boton=tk.Button(ventana,text='Press to Start', command=lambda:[init_time(), start_test()])
boton.pack()

#Create a button to finish the test
boton_finish=tk.Button(ventana,text='Press to finish', command=lambda:[end_time(), finish()])
boton_finish.pack_forget()

#Create a button to close the window
boton_end=tk.Button(ventana,text='Close',command=close_window)

ventana.mainloop()