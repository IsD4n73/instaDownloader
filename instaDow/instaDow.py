from instaloader import *
from getpass import getpass
import shutil
import os


#############################################################################################

def remove_file(user):
    dir = f"./{user}/"
    test = os.listdir(dir)

    for item in test:
        if item.endswith(".xz"):
            os.remove(os.path.join(dir, item))
        if item.endswith(".txt"):
            os.remove(os.path.join(dir, item))

#############################################################################################

def crea_zip(user):
    print("\n\n\n============= Inizio Crazione Archivio =============\n\n\n")
    shutil.make_archive(f"{user}", 'zip', f"./{user}/")
    
    if os.path.exists("./{user}.zip"):
        print("\n\n\n============= Archivio creato =============\n\n\n") 
    else:
        print("\n\n\n============= Errore nel creare l'archivio =============\n\n\n")
    input("\nClicca un tasto per chiudere il programma...")  

#############################################################################################

def insta_post():
    USERNAME = input("[#] Inserisci l'username dell'account: ")
    il = instaloader.Instaloader()

    try:
        for post in Profile.from_username(il.context, USERNAME).get_posts():
            il.download_post(post,USERNAME)
    except:
        print("[#] C'è stato un errore nello scaricare i post. Riprova")
    remove_file(USERNAME)
    input("\nClicca un tasto per chiudere il programma...") 

#############################################################################################

def insta_propic():
    il = instaloader.Instaloader()
    USERNAME = input("[#] Inserisci l'username dell'account: ")
    try:
        il.download_profile(USERNAME,profile_pic_only=True)
    except:
        print("Non è stato possibile scaricare la foto profilo, riprova...")
    remove_file(USERNAME)
    input("\nClicca un tasto per chiudere il programma...")

#############################################################################################

def insta_login():
    il = instaloader.Instaloader()
    USER = input("Inserisci il tuo username: ")
    print("[#] Inserisci la tua password: ")
    PASSWORD = getpass()
    USERNAME = input("\n[#] Inserisci l'username dell'account: ")
    try:
        il.login()
    except:
        print("[#] Non siamo riusciti a connetterci al tuo account, prova a verificare che le credenziali sono corrette e ripova.")
    try:
        for post in Profile.from_username(il.context, USERNAME).get_posts():
            il.download_post(post,USERNAME)
    except:
        print("[#] C'è stato un errore nello scaricare i post. Riprova")
    remove_file(USERNAME)
    input("\nClicca un tasto per chiudere il programma...") 

#############################################################################################

def banner():

    print("""
                        ██████╗ ██╗  ██╗███╗   ██╗███████╗██████╗   
                        ██╔══██╗██║  ██║████╗  ██║╚════██║╚════██╗  
                        ██║  ██║███████║██╔██╗ ██║    ██╔╝ █████╔╝  
                        ██║  ██║╚════██║██║╚██╗██║   ██╔╝  ╚═══██╗  
                        ██████╔╝     ██║██║ ╚████║   ██║  ██████╔╝  
                        ╚═════╝      ╚═╝╚═╝  ╚═══╝   ╚═╝  ╚═════╝   
                                          

██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝
██║░░██║██║░░██║░░████╔═████║░██║╚████║██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║
╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
""")

    print("[#] 1. Instagram Post Downloader\n[#] 2. Instagram Profile Picture Downloader\n[#] 3. Effettua il login (Scarica post da profili privati)\n[#] 4. Crea file ZIP")

    choose = input("\nSeleziona Opzione => ")
    if choose == '1':
        insta_post()
    elif choose == '2':
        insta_propic()
    elif choose == '3':
        insta_login()
    elif choose == '4':
        u = input("Inserisci l' username (nome Cartella): ")
        crea_zip(u)
    else:
        print("\n[#] Opzione non disponibile")
        input("Premi un tasto per chiudere il programma...\n")

#############################################################################################

if __name__ == "__main__":
    banner()