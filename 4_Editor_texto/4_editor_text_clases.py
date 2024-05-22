'''
Interfaz gráfica de usuario (GUI) que simula un editor de texto.
Incluye funcionalidades como editar el texto en negrita, subrayar, cursiva 
y puede abrir, guardar y cerrar el archivo
'''
import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor():
#Definición de la clase ventana de interfaz gráfica
    def __init__(self,vetana):
        #Definición de las características de la ventana principal
        self.ventana= vetana
        self.ventana.title('Text editor')
        self.ventana.geometry('650x600')

        self.create_frame()
        self.create_menu()
        self.create_buttons()
        self.create_text_entry()
    
    def create_frame(self):
        #Definición del marco donde localizaremos los botones
        self.frame_buttons=tk.Frame(self.ventana)
        self.frame_buttons.pack(side=tk.TOP,fill=tk.X,padx=20)

    def create_menu(self):
        #Definición del menu boton
        menu_bar=tk.Menubutton(self.frame_buttons,text='File',borderwidth=2, relief='raised', font=('Helvetica', 10))
        menu_bar.pack(side=tk.LEFT)
        menu_bar.menu=tk.Menu(menu_bar,tearoff=0)
        menu_bar["menu"]=menu_bar.menu
        #Definición de los submenus
        menu_bar.menu.add_checkbutton(label='New',command=self.new_file)
        menu_bar.menu.add_checkbutton(label='Open',command=self.open_file)
        menu_bar.menu.add_checkbutton(label='Save',command=self.save_file)
        menu_bar.menu.add_separator()
        menu_bar.menu.add_checkbutton(label='Exit',command=self.ventana.destroy)
    
    def create_buttons(self):
        #Definicón de los botones para editar el texto
        bold_button = tk.Button(self.frame_buttons, text='B', font=('Helvetica', 10, 'bold'), command=self.bold_text,width=2)
        bold_button.pack(side=tk.LEFT)
        italic_button = tk.Button(self.frame_buttons, text='K', font=('Helvetica', 10, 'italic'), command=self.italic_text,width=2)
        italic_button.pack(side=tk.LEFT)
        underline_button = tk.Button(self.frame_buttons, text='S', font=('Helvetica', 10, 'underline'), command=self.underline_text,width=2)
        underline_button.pack(side=tk.LEFT)

    def create_text_entry(self):
        self.text_entry = tk.Text(self.ventana)
        self.text_entry.config(font=('Helvetica', 10))
        self.text_entry.pack(expand=tk.YES,fill=tk.BOTH,padx=20,pady=(1,20))

    def new_file(self):
        #Definición de la funcion nuevo archivo
        #comprobamos primero si hay algo escrito para guardarlo primero
        check_content=self.text_entry.get('1.0','end-1c')
        if check_content:
            response=messagebox.askquestion("Abrir",message="¿Deseas guardar el archivo actual?")
            if response=='yes':
                self.save_file()
            else:
                self.text_entry.delete(1.0,tk.END)
        else:
            pass

    def save_file(self):
        #Definición de la funcion guardar archivo
        text_save=filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        file=open(text_save,'w')
        file.write(self.text_entry.get('1.0','end-1c'))
        file.close()
        print('saved')

    def open_file(self):
        #Definición de la funcion abrir archivo
        text_open=filedialog.askopenfilename( filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        file=open(text_open,'r')
        content=file.read()
        self.text_entry.delete(1.0,tk.END)
        self.text_entry.insert(1.0,content)

    def bold_text(self):
        #Definición de la funcion editar en negrita el texto
        text_font=self.text_entry.cget('font')
        if 'bold' not in text_font:
            new_font=f"{text_font} bold"
        else:
            new_font=text_font.replace('bold','')
        self.text_entry.config(font=new_font)

    def italic_text(self):
        #Definición de la funcion editar en cursiva el texto
        text_font=self.text_entry.cget('font')
        if 'italic' not in text_font:
            new_font= f'{text_font} italic'
        else:
            new_font=text_font.replace('italic','')
        self.text_entry.config(font=new_font)

    def underline_text(self):
        #Definición de la funcion subrayar el texto
        text_font=self.text_entry.cget('font')
        if 'underline' not in text_font:
            new_font=f'{text_font} underline'
        else:
            new_font=text_font.replace('underline','')
        self.text_entry.config(font=new_font)

    def run(self):
        self.ventana.mainloop()

if __name__=='__main__':
    ventana=tk.Tk()
    app = TextEditor(ventana)
    app.run()