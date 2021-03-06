import tkinter as tk
import shutil, os
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import showinfo
from instaloader import *
from time import sleep
from urllib.parse import urlparse
from functions import *




# root window
root = tk.Tk()
root.geometry("300x500")
#root.resizable(False, False)
root.title('D4n73 Downloader')
root.iconbitmap(resource_path('./asset/icon.ico'))

# store thing
email = tk.StringVar()
password = tk.StringVar()
username = tk.StringVar()
username_single = tk.StringVar()
link_single = tk.StringVar()
post_count = tk.IntVar()

# instaloader
il = instaloader.Instaloader()



# get shortcode from url 
def ig_shortcode(url):
    path = urlparse(url).path 
    path = path[1:] 
    path = path.replace("p/", "")
    path = path.replace("/", "")
    return path

 

# saved post
def saved_post():
    try:
        il.load_session_from_file(email.get())
        il.download_saved_posts(fast_update=False)
    except:
        showinfo(
            title='Errore',
            message="Non è stato possibile scaricare i post salvati..."
        )


# profile post
def insta_post_prv():
    USERNAME = url_to_user(username.get())
    msg = "I post sono stati scaricati correttamente!"
    il.load_session_from_file(email.get())
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
    USERNAME = url_to_user(username.get())
    il.load_session_from_file(email.get())
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

# scarica evidenza highlight
def scarica_highlight():
    USERNAME = url_to_user(username.get())
    try: 
        profile = Profile.from_username(il.context, USERNAME)
        for highlight in il.get_highlights(profile):
            for item in highlight.get_items():
                il.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))
            remove_file(highlight.owner_username + "∕" + highlight.title)
    except:
        showinfo(
            title='Highlight - Storie in evidenza',
            message="Non è stato possibile scaricare le storie in evidenza."
        )


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
        #logged.resizable(False, False)
        logged.title('D4n73 Downloader - Logged')
        logged.iconbitmap(resource_path('./asset/icon.ico'))

        # Sign in frame
        login = ttk.Frame(logged)
        login.pack(padx=10, pady=10, fill='x', expand=True)

        # window title
        ltitle_label = ttk.Label(login, text="Logged In", style= 'Title.TLabel')
        ltitle_label.pack(anchor="center", expand=True)

        # user
        user_labe = ttk.Label(login, text="Username Account:")
        user_labe.pack(fill='x', expand=True)

        user_entri = ttk.Entry(login, textvariable=username)
        user_entri.pack(fill='x', expand=True)
        user_entri.focus()

        # post download
        post_btn = ttk.Button(login, text="Download Post", command=insta_post_prv)
        post_btn.pack(fill='x', expand=True, pady=10)
        
        # post download
        spost_btn = ttk.Button(login, text="Download Single Post", command=single_post)
        spost_btn.pack(fill='x', expand=True, pady=10)

        # profile pic
        stories_button = ttk.Button(login, text="Download Profile Stories", command=stories)
        stories_button.pack(fill='x', expand=True, pady=10)

        # saved posts
        saved_button = ttk.Button(login, text="Download Saved Post", command=saved_post)
        saved_button.pack(fill='x', expand=True, pady=10)

        # liked posts
        liked_button = ttk.Button(login, text="Download Liked Post", command=liked_post)
        liked_button.pack(fill='x', expand=True, pady=10)

        # highlight downloader
        highlight_button = ttk.Button(login, text="Download Highlight", command=scarica_highlight)
        highlight_button.pack(fill='x', expand=True, pady=10)
    except:
        showinfo(
            title='Login Error',
            message="Login non riuscito, riprova"
        )


#single post 
def single_post():
    
    #scarica post singolo
    def dow_singel_post():
        SHORTCODE = ig_shortcode(link_single)
        user = username_single
        try:
            post = Post.from_shortcode(il.context, SHORTCODE)
            profilo = Profile.from_username(il.context, user)
            
            il.download_post(post, target=profilo.username)
            remove_file(user)
        except:
            showinfo(
                title='Post Error',
                message="Non è stato possibile scaricare il post.\n\nRiprova..."
            )

    post = tk.Toplevel(root)
    post.geometry("290x250")
    post.resizable(False, False)
    post.title('D4n73 Downloader - Post')
    post.iconbitmap(resource_path('./asset/icon.ico'))

    # Post frame
    spost = ttk.Frame(post)
    spost.pack(padx=10, pady=10, fill='x', expand=True)

    # window title
    stitle_label = ttk.Label(spost, text="Single Post Downloader", style= 'Title.TLabel')
    stitle_label.pack(anchor="center", expand=True)

    # username single post label
    spostuser_labe = ttk.Label(spost, text="Username dell'account:")
    spostuser_labe.pack(fill='x', expand=True)

    # username single post input
    spost_user_entri = ttk.Entry(spost, textvariable=username_single)
    spost_user_entri.pack(fill='x', expand=True)
    spost_user_entri.focus()

    # link single post label
    spostlink_labe = ttk.Label(spost, text="Link del post:")
    spostlink_labe.pack(fill='x', expand=True)

    # link single post input
    spost_link_entri = ttk.Entry(spost, textvariable=link_single)
    spost_link_entri.pack(fill='x', expand=True)

    # download liked button
    spost_button = ttk.Button(spost, text="Download", command=dow_singel_post)
    spost_button.pack(fill='x', expand=True, pady=5)

   


# liked post download
def liked_post():

    # download x liked post
    def dow_post():
        il.load_session_from_file(email.get())
        try:
            il.download_feed_posts(max_count=post_count.get(), fast_update=True,
                            post_filter=lambda post: post.viewer_has_liked)
        except:
            showinfo(
                title='Liked Error',
                message="Non è stato possibile scaricare i post salvati..."
            )

    liked = tk.Toplevel(root)
    liked.geometry("290x250")
    liked.resizable(False, False)
    liked.title('D4n73 Downloader - Liked')
    liked.iconbitmap(resource_path('./asset/icon.ico'))

    # Liked frame
    like = ttk.Frame(liked)
    like.pack(padx=10, pady=10, fill='x', expand=True)
    
    liktitle_label = ttk.Label(like, text="Liked Post", style= 'Title.TLabel')
    liktitle_label.pack(anchor="center", expand=True)
    
    # download liked label
    post_labe = ttk.Label(like, text="Max Post Da Scaricare:")
    post_labe.pack(fill='x', expand=True)

    # download liked input
    post_entri = ttk.Entry(like, textvariable=post_count)
    post_entri.pack(fill='x', expand=True)
    post_entri.focus()
    
    # download liked button
    like_button = ttk.Button(like, text="Download", command=dow_post)
    like_button.pack(fill='x', expand=True, pady=5)
    
    
    


# info function
def get_info():
    USERNAME = url_to_user(username.get())
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
    USERNAME = url_to_user(username.get())
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
    user = url_to_user(username.get())
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
    USERNAME = url_to_user(username.get())
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

# profile pic
def propic():
    USERNAME = url_to_user(username.get())
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

#style
style = ttk.Style(root)
#style.theme_use('xpnative')
print(style.theme_names())
style.configure('Title.TLabel', font=("Monospace", 15))


title_label = ttk.Label(signin, text="D4n73 Downloader", style= 'Title.TLabel')
title_label.pack(anchor="center", expand=True)

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




# login label
login_label = ttk.Label(signin, text="Login", style= 'Title.TLabel')
login_label.pack(anchor="center", expand=True)

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

# help button
help_button = ttk.Button(signin, text="Aiuto", command=help_clicked)
help_button.pack(fill='x', expand=True, pady=5)


root.mainloop()