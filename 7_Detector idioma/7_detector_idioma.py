import tkinter as tk
from langdetect import detect, LangDetectException

class LanguageDetector():
    def __init__(self, width=600, height=250):
        #Initialization of the class with default width and height
        self.width=width
        self.height=height

        #Creation of the main window to interact with the user
        self.window=tk.Tk()
        self.window.title('Lenguage detector')
        self.window.geometry(f"{self.width}x{self.height}")

        #Create a frame to display the messages in the window
        self.frame=tk.Frame()
        self.frame.pack()

        #Initial label message
        init_message=tk.Label(self.frame,text='Introduce el texto para poder identificar el idioma:')
        init_message.grid(row=0,column=0, padx=5, pady=5)

        #Text entry box
        self.box=tk.Entry(self.frame, width=90)
        self.box.grid(row=2,column=0, padx=5, pady=5)

        #Button to detect the language
        button_lang=tk.Button(self.frame,text="Detect",command=self.get_language)
        button_lang.grid(row=4,column=0, padx=5, pady=5)

        #Label to display the detected language
        self.label_language=tk.Label(self.frame,text="")
        self.label_language.grid(row=6,column=0, padx=5, pady=5)

    def get_language(self):
        #Function to get the text from the box and return the detected language
        try:
            code_lang=detect(self.box.get())
            #Using a dictionary to get the full name of the language
            language=idiomas[code_lang]
            self.label_language.config(text=f'Idioma detectado: {language.title()}')
        except LangDetectException as e:
            #Error handling in case there is no text in the box
            self.label_language.config(text=f'Detección de idioma falló debido a la falta de caracteres en el texto')

# Dictionary of language codes and their full names
idiomas = {
    'af': 'afrikáans', 'ar': 'árabe', 'bg': 'búlgaro','bn': 'bengalí', 'ca': 'catalán', 'cs': 'checo',
    'cy': 'galés', 'da': 'danés', 'de': 'alemán','el': 'griego', 'en': 'inglés', 'es': 'español',
    'et': 'estonio', 'fa': 'persa', 'fi': 'finlandés','fr': 'francés', 'gu': 'guyaratí', 'he': 'hebreo',
    'hi': 'hindi', 'hr': 'croata', 'hu': 'húngaro','id': 'indonesio', 'it': 'italiano', 'ja': 'japonés',
    'kn': 'kannada', 'ko': 'coreano', 'lt': 'lituano','lv': 'letón', 'mk': 'macedonio', 'ml': 'malabar',
    'mr': 'maratí', 'ne': 'nepalí', 'nl': 'neerlandés','no': 'noruego', 'pa': 'punjabí', 'pl': 'polaco',
    'pt': 'portugués', 'ro': 'rumano', 'ru': 'ruso','sk': 'eslovaco', 'sl': 'esloveno', 'so': 'somalí',
    'sq': 'albanés', 'sv': 'sueco', 'sw': 'suajili','ta': 'tamil', 'te': 'telugu', 'th': 'tailandés',
    'tl': 'filipino', 'tr': 'turco', 'uk': 'ucraniano','ur': 'urdu', 'vi': 'vietnamita', 'zh-cn': 'chino (simplificado)',
    'zh-tw': 'chino (tradicional)'
}

#Create an object of the LanguageDetector class
detection=LanguageDetector()

#Start the main loop for the graphical interface
detection.window.mainloop()