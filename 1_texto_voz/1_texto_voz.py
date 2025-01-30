import os
from langdetect import detect
from newspaper import Article
from gtts import gTTS

'''webs in differente languages to import the article'''
# https://www.tendencias.kpmg.es/2018/06/blockchain-aun-no-sabes-que-es-articulo/
# https://www.ibm.com/topics/blockchain#:~:text=first%20blockchain%20application-,Blockchain%20overview,patents%2C%20copyrights%2C%20branding).
# https://www.lesechos.fr/monde/europe/laffaire-rubiales-une-masterclass-acceleree-contre-le-machisme-en-espagne-1973060

def article_info():
    #Function to introduce the url and to get text from it
    url=input('Write the url to convert text on audio:\n')
    #Create an Article object
    article=Article(url)
    #Download an analyze the article
    article.download()
    article.parse()
    return article.text

def language_detect(article):
    #Function to detect the languaje of the url given
    language=detect(article)
    return language

def text_voice(article_content, idiom,audio_name):
    #Function to transform text to audio
    # Create a gTTS object (Google Text-to-Speech)
    tts=gTTS(article_content,lang=idiom)
    # Save the audio in a file
    tts.save(audio_name)

def main():
    # Main function tah manages the entire process of converting an article into audio
    text_to_transform=article_info()
    language=language_detect(text_to_transform)
    audio_name='audio_article.mp3'
    #Verified if there is a file with the samen name. If there is it will ask to remove the name or rename the new file
    if os.path.exists(audio_name):
        choice=input('An audio with the same name already exists. Do you want to delete it? (y/n): ')
        if choice.lower()=='y':
            os.remove(audio_name)
        else:
            new_name=input('Enter a new name for the audio file (including the .mp3 extension)')
            audio_name=new_name

    print('Processing...')
    text_voice(text_to_transform,language,audio_name)
    print('MP3 file is created under the name: audio_article.mp3')

if __name__=="__main__":
    main()