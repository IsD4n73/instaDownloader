import os, sys
from tkinter.messagebox import showinfo
from instaloader import *
from urllib.parse import urlparse

##############################################################################

def remove_file(user):
    '''Remove unused file after download'''
    dir = f"./{user}/"
    test = os.listdir(dir)

    for item in test:
        if item.endswith(".xz"):
            os.remove(os.path.join(dir, item))
        if item.endswith(".txt"):
            os.remove(os.path.join(dir, item))
        if item.endswith("id"):
            os.remove(os.path.join(dir, item))
    
    dir = f"./：stories/"
    test = os.listdir(dir)

    for item in test:
        if item.endswith(".xz"):
            os.remove(os.path.join(dir, item))
        if item.endswith(".txt"):
            os.remove(os.path.join(dir, item))
        if item.endswith("id"):
            os.remove(os.path.join(dir, item))
        if item.endswith(".webp"):
            os.remove(os.path.join(dir, item))

##############################################################################

def url_to_user(url):
    '''Transform instagrm.com url to instagram username'''
    path = url
    if "instagram.com" in url:
        path = urlparse(url).path 
        path = path[1:] 
        path = path.replace("/", "")
        path = path.split("?", 1)[0]
        print("Username: " + path + "\n\n")
    return path   

##############################################################################

def help_clicked():
    '''Get message with help'''
    showinfo(
        title='Spiegazione App',
        message="""
Username Account -- Username dell account instagram su cui vuoi eseguire l'operazione

Download Post -- Scarica tutti i post da profili pubblici

Downoad Profile Picture -- Scarica la foto profilo di un account

Create ZIP -- Crea un archivio zip della cartella contentente i media

Private Account -- Controlla se l'username ha un profilo pubblico/privato

Get Account Info -- Controlla tutte le informazioni di un account

Email & Password -- Credenziali per effettuare il login ed eseguire operazioni extra

Login -- Da l'accesso ad operazioni come:
        > Download Post -- Scarica post da un account privato

        > Download Single Post -- Scarica post singolo da un account

        > Download Profile Stories -- Scarica le storie di un account

        > Download Saved Post -- Scarica i post salvati dell'account che ha effettuato il login

        > Download Liked Post -- Scarica i post a cui hai messo mi piace

        > Download Highlight -- Scarica le storie in evidenza di un utente
        """
    )


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
