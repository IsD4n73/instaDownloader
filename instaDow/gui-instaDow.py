import tkinter as tk
import shutil, os, sys
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo
from instaloader import *
from time import sleep

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



# root window
root = tk.Tk()
root.geometry("300x450")
root.resizable(False, False)
root.title('D4n73 Downloader')
root.iconbitmap(resource_path('./asset/icon.ico'))

# store thing
email = tk.StringVar()
password = tk.StringVar()
username = tk.StringVar()

# instaloader
il = instaloader.Instaloader()

##############################################################################
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




# login 
def login_clicked():
    USER = email.get()
    PASSWORD = password.get()
    
    try:
        try:
            il.load_session_from_file(USER)
        except FileNotFoundError:
            il.login(USER, PASSWORD)
            il.save_session_to_file()
        

        logged = tk.Toplevel(root)
        logged.geometry("300x450")
        logged.resizable(False, False)
        logged.title('D4n73 Downloader - Logged')
        logged.iconbitmap(resource_path('./asset/icon.ico'))

        # Sign in frame
        login = ttk.Frame(logged)
        login.pack(padx=10, pady=10, fill='x', expand=True)

        # user
        user_labe = ttk.Label(login, text="Username Account:")
        user_labe.pack(fill='x', expand=True)

        user_entri = ttk.Entry(login, textvariable=username)
        user_entri.pack(fill='x', expand=True)
        user_entri.focus()

        # post download
        post_btn = ttk.Button(login, text="Download Post", command=insta_post_prv)
        post_btn.pack(fill='x', expand=True, pady=10)

        # profile pic
        stories_button = ttk.Button(login, text="Download Profile Stories", command=stories)
        stories_button.pack(fill='x', expand=True, pady=10)

        # saved posts
        saved_button = ttk.Button(login, text="Download Saved Post", command=saved_post)
        saved_button.pack(fill='x', expand=True, pady=10)
    except:
        showinfo(
            title='Login Error',
            message="Login non riuscito, riprova"
        )


# saved post
def saved_post():
    try:
        il.download_saved_posts(max_count=None, fast_update=False, post_filter=None)
    except LoginRequiredException:
        showinfo(
            title='Errore',
            message="Non è stato possibile scaricare i post salvati..."
        )

# profile post
def insta_post_prv():
    USERNAME = username.get()
    msg = "I post sono stati scaricati correttamente!"
    try:
        for post in Profile.from_username(il.context, USERNAME).get_posts():
            il.download_post(post,USERNAME)
    except:
        msg = "C'è stato un errore nello scaricare i post. Riprova"
    remove_file(USERNAME)
    showinfo(
        title='Private Profile - Post',
        message=msg
    )


# stories
def stories():
    USERNAME = username.get()
    msg = "Le storie sono state scaricate correttamente!"
    try:
        il.download_stories(userids=[il.check_profile_id(USERNAME)])
    except:
        msg = "Non è stato possibile scaricare le storie, riprova"
    remove_file(USERNAME)
    showinfo(
        title='Private Profile - Stories',
        message=msg
    )

# info function
def get_info():
    USERNAME = username.get()
    try:
        profile = Profile.from_username(il.context, USERNAME)
        msg = f"\n           Informazioni {USERNAME}\n" + f"\nUser ID: {profile.userid}"
        msg += f"\n\nUser Post: {profile.mediacount}" + f"\nUser IGTV Post: {profile.igtvcount}"
        msg += f"\n\nUser Followers: {profile.followers}" + f"\nAccount Seguiti: {profile.followees}"
        msg += f"\n\nUser ID: {profile.userid}" +f"\nNome User: {profile.full_name}"
        if profile.is_verified == True:
            msg += f"\n\nUser Verificato: SI"
        else:
            msg += f"\n\nUser Verificato: NO"
        msg += f"\n\nBIO User: {profile.biography}"
        showinfo(
            title='Profile Info',
            message=msg
        )
    except ProfileNotExistsException:
        showinfo(
            title='Profile Info ERROR',
            message="L'username non corrisponde a nessun utente...\n\nControlla l'username e riprova."
        )

# private
def get_priv():
    USERNAME = username.get()
    try:
        profilo = Profile.from_username(il.context, USERNAME).is_private
        if profilo == True:
            msg = f"{USERNAME}" + " ha un profilo privato"
        else:
            msg = f"{USERNAME}" + " ha un profilo pubblico"
    except ProfileNotExistsException:
        msg = "L'username non corrisponde a nessun utente...\n\nControlla l'username e riprova.\n\n"
    showinfo(
        title='Private Profile ',
        message=msg
    ) 
    

# create zip
def get_zip():
    user = username.get()
    shutil.make_archive(f"{user}", 'zip', f"./{user}/")
    
    sleep(0.8)
    
    if os.path.exists("./{user}.zip"):
        msg = "L'archivio è stato creato correttamente"
    else:
        msg = "C'è stato un errore nel creare l'archivio...\n\nRiprova"
    showinfo(
        title='ZIP',
        message=msg
    )
    


# post 
def insta_post():
    USERNAME = username.get()
    try:
        for post in Profile.from_username(il.context, USERNAME).get_posts():
            il.download_post(post,USERNAME)
        msg = "I post sono stati scaricati correttamente!"
    except:
        msg = "C'è stato un errore nello scaricare i post. Riprova"
    remove_file(USERNAME)
    showinfo(
        title='Post Download',
        message=msg
    )

def propic():
    USERNAME = username.get()
    msg = "La foto profilo è stata scaricata correttamente!"
    try:
        il.download_profile(USERNAME,profile_pic_only=True)
    except:
        msg = "Non è stato possibile scaricare la foto profilo, riprova..."
    remove_file(USERNAME)
    showinfo(
        title='Profile Picture Download',
        message=msg
    )
##############################################################################

# Sign in frame
signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)

# user
user_label = ttk.Label(signin, text="Username Account:")
user_label.pack(fill='x', expand=True)

user_entry = ttk.Entry(signin, textvariable=username)
user_entry.pack(fill='x', expand=True)
user_entry.focus()

# post download
post_button = ttk.Button(signin, text="Download Post", command=insta_post)
post_button.pack(fill='x', expand=True, pady=10)

# profile pic
propic_button = ttk.Button(signin, text="Download Profile Picture", command=propic)
propic_button.pack(fill='x', expand=True, pady=10)

# create zip
zip_button = ttk.Button(signin, text="Create ZIP", command=get_zip)
zip_button.pack(fill='x', expand=True, pady=10)

# private account
priv_button = ttk.Button(signin, text="Private Account", command=get_priv)
priv_button.pack(fill='x', expand=True, pady=10)

# account info
info_button = ttk.Button(signin, text="Get Account Info", command=get_info)
info_button.pack(fill='x', expand=True, pady=10)



# username
email_label = ttk.Label(signin, text="Email:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)


# password
password_label = ttk.Label(signin, text="Password:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)

# login button
login_button = ttk.Button(signin, text="Login", command=login_clicked)
login_button.pack(fill='x', expand=True, pady=10)





root.mainloop()