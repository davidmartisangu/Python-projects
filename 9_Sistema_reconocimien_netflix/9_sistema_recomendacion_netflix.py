import pandas as pd
import tkinter as tk
import re
from unidecode import unidecode

def search_id_film():
    #Function that get the name and return the id
    film_name=film_box.get()
    #Remove the accents and transform to lowercase
    uni_film_name=unidecode(film_name).lower()
    #Remove the accents and transform to lowercase Title column 
    df['Title'] = df['Title'].apply(unidecode).str.lower()
    #Get id film
    id_film = df.loc[df['Title'].str.lower() == uni_film_name, 'Show_Id']
    if not id_film.empty:
        return id_film.values[0]
    else:
        label_data_film2=tk.Label(text=f"No se encontró {uni_film_name}",font=('Helvetica',9),fg='white',bg='black')
        label_data_film2.grid(row=5,column=0)

def director_films():
    #Function to get the director´s name using film´s ID and show other films/series the director participate
    identification_film=search_id_film()
    director_film=df.loc[df['Show_Id']==identification_film,'Director']
    #Conditional to verified if the directos info is empty or not
    if not pd.isna(director_film.iloc[0]):
        director_name = director_film.iloc[0]
        director_name_label=tk.Label(window,text=f"Más películas/series del director {director_name}:",font=('Helvetica',9),fg='white',bg='black')
        director_name_label.grid(row=5,column=0,sticky="w",padx=10)
        #Search for more films/series from the director
        director_productions=df.loc[df["Director"]==director_name,"Title"].tolist()
        # Remove current film from the list:
        director_productions=[title for title in director_productions if title != df.loc[df["Show_Id"]==identification_film,"Title"].values[0]]
        #Formatting the text into string
        director_productions_text = ", ".join(director_productions).title()
        if len(director_productions) <=1:
            director_productions_label=tk.Label(window,text=f"No se encontraron más películas/series de {director_name}",font=('Helvetica',9),fg='white',bg='black')
            director_productions_label.grid(row=6,column=0,padx=10)
        else:
            director_productions_label=tk.Label(window,text=director_productions_text,font=('Helvetica',9),fg='white',bg='black')
            director_productions_label.grid(row=6,column=0,padx=10)
    else:
        director_productions_label=tk.Label(window,text="Director no disponible",font=('Helvetica',9),fg='white',bg='black')
        director_productions_label.grid(row=5,column=0,padx=10)

def production_country():
    #Function to get the country from the film using film´s ID and show other films/series from the same country
    identification_film=search_id_film()
    country_film=df.loc[df['Show_Id']==identification_film,'Production_Country']
    #Conditional to verified if the directos info is empty or not
    if not pd.isna(country_film.iloc[0]):
        country = country_film.iloc[0]
        country_label=tk.Label(window,text=f"Más películas/series del país {country}:",font=('Helvetica',9),fg='white',bg='black')
        country_label.grid(row=7,column=0,sticky="w",padx=10,pady=(15,0))
        #Search for more films/series from the director
        country_works=df[df["Production_Country"]==country].head(5)
        country_prods=country_works["Title"].tolist()
        # Remove current film from the list:
        country_prods=[title for title in country_prods if title != df.loc[df["Show_Id"]==identification_film,"Title"].values[0]]
        #Formatting the text into string
        country_prods_text=",".join(country_prods).title()
        country_productions_label=tk.Label(window,text=country_prods_text,font=('Helvetica',9),fg='white',bg='black')
        country_productions_label.grid(row=8,column=0,padx=10)
    else:
        country_label=tk.Label(window,text="Lugar no disponible",font=('Helvetica',9),fg='white',bg='black')
        country_label.grid(row=7,column=0,padx=10,pady=(15,0))

def same_genre():
    #Function to get the genre from the film using film´s ID and show other films/series from the genre
    identification_film=search_id_film()
    genre_film=df.loc[df['Show_Id']==identification_film,'Genres']
    #Conditional to verified if the genre info is empty or not
    if not pd.isna(genre_film.iloc[0]):
        genre = genre_film.iloc[0]
        genre_label=tk.Label(window,text=f"Más películas/series del genero {genre}:",font=('Helvetica',9),fg='white',bg='black')
        genre_label.grid(row=9,column=0,sticky="w",padx=10,pady=(15,0))
        #Search for more films/series with the same genre
        genre_works=df[df["Genres"]==genre].head(5)
        genre_prods=genre_works["Title"].tolist()
        # Remove current film from the list:
        genre_prods=[title for title in genre_prods if title != df.loc[df["Show_Id"]==identification_film,"Title"].values[0]]
        #Formatting the text into string
        genre_productions=",".join(genre_prods).title()
        genre_productions_label=tk.Label(window,text=genre_productions,font=('Helvetica',9),fg='white',bg='black')
        genre_productions_label.grid(row=10,column=0,padx=10)
    else:
        genre_label=tk.Label(window,text="Genero no disponible",font=('Helvetica',9),fg='white',bg='black')
        genre_label.grid(row=9,column=0,padx=10,pady=(15,0))

def same_cast():
    #Function that get the cast from the film using film´s ID and show other films/series where the actors perform
    identification_film=search_id_film()
    cast_film=df.loc[df['Show_Id']==identification_film,'Cast']
    #Conditional to verified if the cast info is empty or not
    if not pd.isna(cast_film.iloc[0]):
        cast = cast_film.iloc[0].split(",")
        cast=cast[:2] #only the first two actors
        cast_str=",".join(cast)
        cast_label=tk.Label(window,text=f"Más películas/series de los actores {cast_str}:",font=('Helvetica',9),fg='white',bg='black')
        cast_label.grid(row=11,column=0,sticky="w",padx=10,pady=(15,0))
        #Search more films/series with the same actors
        for i in range (2):
            actor=cast[i].strip() #Remove spaces
            cast_works=df[df["Cast"].str.contains(actor,case=False,na=False)]
            cast_prods=cast_works["Title"].tolist()
            # Remove current film from the list:
            cast_prods=[title for title in cast_prods if title != df.loc[df['Show_Id'] == identification_film,'Title'].values[0]]
            cast_prods=','.join(cast_prods).title()
            if cast_prods:
                cast_productions_label=tk.Label(window,text=f"{actor}:\n{cast_prods}",font=('Helvetica',9),fg='white',bg='black')
                cast_productions_label.grid(row=12+i,column=0,padx=10,pady=(0,5))
    else:
        cast_label=tk.Label(window,text="No se encontraron los actores",font=('Helvetica',9),fg='white',bg='black')
        cast_label.grid(row=11,column=0,padx=10,pady=(15,0))

#Import netflix data frame from the csv file
df = pd.read_csv('netflixData.csv')

#Create graphical usur interface with tkinter
window=tk.Tk()
window.title('Netflix System Recomendation')
window.minsize(400,250)
window.config(bg='black')

#Initial message
init_label=tk.Label(window,text="Película / Serie que le gustaría tener recomendaciones:"
                    ,font=('Helvetica',12),fg='white',bg='black',justify='center')
init_label.grid(column=0,row=1,padx=10,pady=(0,10))

init_label2=tk.Label(window,text="Netflix"
                    ,font=('Helvetica',30),fg='red',bg='black')
init_label2.grid(column=0,row=0,padx=10,pady=(20,15))

#Entry box for the name of the film
film_box=tk.Entry(width=50)
film_box.grid(column=0,row=2,pady=10)

#Button to get the info from the box and show the film´s info
film_button=tk.Button(window,text='Recomendaciones',command=lambda:(search_id_film(),director_films(),production_country(),same_genre(),same_cast()))
film_button.grid(row=3,column=0,pady=(0,15))

#Initialze mainloop
window.mainloop()