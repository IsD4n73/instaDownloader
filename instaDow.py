from ast import Pass
from instaloader import *
from getpass import getpass
import shutil
import os
from colorama import init, Fore, Back, Style
from numpy import true_divide
init()


fr  =   Fore.RED                                                                                     
fw  =   Fore.WHITE                                          
fg  =   Fore.GREEN
#############################################################################################

def ripeti_programma():
    scelta = None
    while scelta not in ("si", "SI", "yes", "YES", "s", "S", "y", "n", "no", "NO", "N"): 
        scelta = input("\n\n[#] Vuoi ripetere il programma? (s/n) ")
        if scelta in ('y', 'yes', 's', 'si', 'Y', 'S', 'SI', 'YES'):
            os.system('cls')
            banner()
        elif scelta in ('n', 'no', 'NO', 'N'): 
            input("\nClicca un tasto per chiudere il programma...")
            break

#############################################################################################

def remove_file(user):
    dir = f"./{user}/"
    test = os.listdir(dir)

    for item in test:
        if item.endswith(".xz"):
            os.remove(os.path.join(dir, item))
        if item.endswith(".txt"):
            os.remove(os.path.join(dir, item))
        if item.endswith("id"):
            os.remove(os.path.join(dir, item))

#############################################################################################

def crea_zip(user):
    print("{}\n\n\n============= Inizio Crazione Archivio =============\n\n\n".format(fw))
    shutil.make_archive(f"{user}", 'zip', f"./{user}/")
    
    if os.path.exists("./{user}.zip"):
        print("{}\n\n\n============= Archivio creato =============\n\n\n".format(fw)) 
    else:
        print("{}\n\n\n============= Errore nel creare l'archivio =============\n\n\n".format(fr) + "{}".format(fw))
    ripeti_programma()

#############################################################################################

def insta_post():
    USERNAME = input("[#] Inserisci l'username dell'account => ")
    il = instaloader.Instaloader()

    try:
        for post in Profile.from_username(il.context, USERNAME).get_posts():
            il.download_post(post,USERNAME)
    except:
        print("{}[#] C'è stato un errore nello scaricare i post. Riprova".format(fr) + "{}".format(fw))
    remove_file(USERNAME)
    ripeti_programma()

#############################################################################################

def insta_propic():
    il = instaloader.Instaloader()
    USERNAME = input("[#] Inserisci l'username dell'account => ")
    try:
        il.download_profile(USERNAME,profile_pic_only=True)
    except:
        print("{}Non è stato possibile scaricare la foto profilo, riprova...".format(fr) + "{}".format(fw))
    remove_file(USERNAME)
    ripeti_programma()

#############################################################################################

def profile_infos():
    il = instaloader.Instaloader()
    USERNAME = input("[#] Inserisci l'username dell'account => ")
    profile = Profile.from_username(il.context, USERNAME)
    print("\n{}           Informazioni ".format(fw) + "{}".format(fg) +f"{USERNAME}\n" + "{}".format(fw))

    print("{}\nUser ID: ".format(fw) + "{}".format(fr) + f"{profile.userid}" + "{}".format(fw))
    print("{}\nUser Post: ".format(fw) + "{}".format(fr) + f"{profile.mediacount}" + "{}".format(fw))
    print("{}\nUser IGTV Post: ".format(fw) + "{}".format(fr) + f"{profile.igtvcount}" + "{}".format(fw))
    print("{}\nUser Followers: ".format(fw) + "{}".format(fr) + f"{profile.followers}" + "{}".format(fw))
    print("{}\nAccount Seguiti: ".format(fw) + "{}".format(fr) + f"{profile.followees}" + "{}".format(fw))
    print("{}\nUser ID: ".format(fw) + "{}".format(fr) + f"{profile.userid}" + "{}\n".format(fw))

    print("{}\nNome User: ".format(fw) + "{}".format(fr) + f"{profile.full_name}" + "{}".format(fw))
    if profile.is_verified == True:
        print("{}\nUser Verificato: ".format(fw) + "{}".format(fg) + "SI" + "{}".format(fw))
    else:
        print("{}\nUser Verificato: ".format(fw) + "{}".format(fr) + "NO" + "{}".format(fw))
    print("{}\nBIO User: ".format(fw) + "{}".format(fr) + f"{profile.biography}" + "{}".format(fw))

    ripeti_programma()

#############################################################################################

def e_privato():
    il = instaloader.Instaloader()
    USERNAME = input("[#] Inserisci l'username dell'account => ")

    profilo = Profile.from_username(il.context, USERNAME).is_private
    if profilo == True:
        print(f"{USERNAME}" + " {}ha un profilo ".format(fw) + "{}privato".format(fr) + "{}".format(fw))
    else:
        print(f"{USERNAME}" + " {}ha un profilo ".format(fw) + "{}pubblico".format(fg) + "{}".format(fw))
    ripeti_programma()

#############################################################################################

def insta_login():
    il = instaloader.Instaloader()
    print("{}".format(fw))
    USER = input("Inserisci il tuo username: ")
    print("[#] Inserisci la tua password: ")
    PASSWORD = getpass()

    USERNAME = input("\n[#] Inserisci l'username dell'account => ")
    try:
        il.login(USER, PASSWORD)
    except:
        print("{}[#] Non siamo riusciti a connetterci al tuo account, prova a verificare che le credenziali sono corrette e ripova.".format(fr) + "{}".format(fw))
    
    print("""{}
             [#] 1. Instagram Post Downloader (Profili privati)
             [#] 2. Instagram Stories Downloader
    """.format(fw))
    choose = input("\nSeleziona Opzione => ")
    if choose == '1':
        try:
            for post in Profile.from_username(il.context, USERNAME).get_posts():
                il.download_post(post,USERNAME)
        except:
            print("{}[#] C'è stato un errore nello scaricare i post. Riprova".format(fr) + "{}".format(fw))
        remove_file(USERNAME)
        input("Clicca un tasto per chiudere il programma...")
    elif choose == '2':
        try:
            il.download_stories(userids=[il.check_profile_id(USERNAME)])
        except:
            print("{}Non è stato possibile scaricare le storie, se il profilo è privato effettua il login".format(fr) + "{}".format(fw))
        input("Clicca un tasto per chiudere il programma...")
    else:
        print("{}\n[#] Opzione non disponibile".format(fr) + "{} ".format(fw))    
        ripeti_programma()

#############################################################################################

def banner():

    print("""{}
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
""".format(fr))

    print("""{}
             [#] 1. Instagram Post Downloader
             [#] 2. Instagram Profile Picture Downloader
             [#] 3. Effettua il login (Scarica post/storie da profili privati)
             [#] 4. Crea file ZIP
             [#] 5. Controlla se un account è privato
             [#] 6. Vedi le informazioni di un profilo
    """.format(fw))

    choose = input("\nSeleziona Opzione => ")
    if choose == '1':
        insta_post()
    elif choose == '2':
        insta_propic()
    elif choose == '3':
        insta_login()
    elif choose == '4':
        print("{}".format(fw))
        u = input("Inserisci l' username (nome Cartella): ")
        crea_zip(u)
    elif choose == '5':
        e_privato()
    elif choose == '6':
        profile_infos()
    else:
        print("{}\n[#] Opzione non disponibile".format(fr) + "{} ".format(fw))
        input("Clicca un tasto per continuare...")
        os.system("cls")
        banner()

#############################################################################################

if __name__ == "__main__":
    banner()