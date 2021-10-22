import socket
from tkinter import *
from threading import Thread
import random

if True:
    #Theme 1
    ColBackDark = "#05070c"
    ColBack = "#090b13"

    ColButtonSquare = "#f40454"
    ColButtonSquare1 = "#700000"
    ColButtonSquare2 = "#922B21"
    ColButtonSquare3 = "#800080"
    ColButtonSquare4 = "#6C3483"
    ColButtonSquare5 = "#2980B9"
    ColButtonSquare6 = "#F1C40F"
    ColButtonSquare7 = "#00982E"
    ColButtonSquare8 = "#282A35"

    TextColor = "white"









UDP_IP = "192.168.1.148"
UDP_PORT = 5005


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP


try:
    g = open("Theme.txt", "r")

    CouleurDeBase = g.read()
    print("\/")
    print(g.read())
    print("/\ ")

except Exception as e:
    print(e)
    f = open("Theme.txt", "w")
    f.write(ColButtonSquare)
    f.close()
    CouleurDeBase = ColButtonSquare

try:
    f = open("Pseudo.txt", "r")
    Nom = f.read()


except:
    Nom = "n°" + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    f = open("Pseudo.txt", "w")
    f.write(Nom)
    f.close()




SendConnection = f"Nouvelle connection || {Nom}".encode()

sock.sendto(SendConnection, (UDP_IP, UDP_PORT))


MESSAGE = ""



def Sending(e):
    MESSAGE = e.widget.get() +  f" || {Nom}"
    e.widget.delete(0,"end")

    if not MESSAGE.strip() == "":
        sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))




def ChangeTheme(couleur):

    ChatPage.config(highlightbackground = couleur, highlightcolor= couleur)
    Bar_Chat.config(highlightbackground = couleur, highlightcolor= couleur, insertbackground = couleur)
    ButtonParameters.config(bg=couleur)

    f = open("Theme.txt", "w")
    f.write(couleur)
    f.close()




def ChangerDeNom(e):
    global Nom
    Nom = e.widget.get()

    f = open("Pseudo.txt", "w")
    f.write(Nom)
    f.close()



    e.widget.delete(0,"end")



def Parametres(w):
    Params = Toplevel()
    Params.title("Paramètres")
    Params.config(bg=ColBackDark)
    Params.geometry(f"{w.winfo_width()}x{w.winfo_height()}+{w.winfo_x()}+{w.winfo_y()}")



    ColumnRight = Frame(Params, bg=ColBackDark)
    ColumnRight.pack(side=RIGHT, fill=Y)

    ColumnMid = Frame(Params, bg=ColBackDark)
    ColumnMid.pack(side=TOP, fill=BOTH, expand=True)
    if True:

        #Fermer les paramètres
        ButtonBack = Button(ColumnRight, text="x", font=("Consolas", 14), width=3, command=Params.destroy, relief=FLAT, bg="#282A35", fg=TextColor)
        ButtonBack.pack(side=TOP)


        #Titre Nom
        ApparenceLabel = Label(ColumnMid, bg=ColBackDark, fg="white", text="Profil d'utilisateur", font=("comic", 12, "bold", "underline"))
        ApparenceLabel.pack(side=TOP, anchor=N, pady=20)

        #Sous titre nom
        ApparenceLabel = Label(ColumnMid, bg=ColBackDark, fg="white", text="Changer de nom", font=("comic", 10, "bold"))
        ApparenceLabel.pack(side=TOP, anchor=N, pady=40)

        #Entrer le Nom
        Bar_Pseudo_Changer = Entry(ColumnMid, relief=FLAT, bd=10, justify=LEFT, bg=ColBack, fg=TextColor, highlightthickness=2)
        Bar_Pseudo_Changer.config(highlightbackground = "#282A35", highlightcolor= "#282A35", insertbackground = "#282A35")
        Bar_Pseudo_Changer.pack(pady=20, side=TOP)
        Bar_Pseudo_Changer.bind("<Return>", ChangerDeNom)



        Trait = Label(ColumnMid, bg=ColBackDark, fg="#282A35", text="_____________________________________________________________________________", font=("comic", 10, "bold"))
        Trait.pack(side=TOP, anchor=N, pady=40)




        #Titre Apparence
        ApparenceLabel = Label(ColumnMid, bg=ColBackDark, fg="white", text="Apparence", font=("comic", 12, "bold", "underline"))
        ApparenceLabel.pack(side=TOP, anchor=N, pady=20)

        #Sous titre Changer theme
        ApparenceLabel = Label(ColumnMid, bg=ColBackDark, fg="white", text="Changer la couleur du thème", font=("comic", 10, "bold"))
        ApparenceLabel.pack(side=TOP, anchor=N, pady=40)

        #Frame des boutons de couleurs de changement de theme
        FrameButtonsThemeChoser = Frame(ColumnMid, bg=ColBackDark)
        FrameButtonsThemeChoser.pack(side=TOP)

        Bar_Theme_Color = Entry(ColumnMid, relief=FLAT, bd=10, justify=LEFT, bg=ColBack, fg=TextColor, highlightthickness=2)
        Bar_Theme_Color.config(highlightbackground = "#282A35", highlightcolor= "#282A35", insertbackground = "#282A35")
        Bar_Theme_Color.pack(pady=20, side=TOP)

        Bar_Theme_Color.bind("<Return>", lambda x: [ChangeTheme("#" + str(Bar_Theme_Color.get())), Bar_Theme_Color.delete(0, END)])






        ButtonCol = Button(FrameButtonsThemeChoser, bg=ColButtonSquare, width=3, relief=FLAT, command= lambda: ChangeTheme(ColButtonSquare))
        ButtonCol.grid(column=0, row=0, padx=10, pady=10)

        ButtonCol1 = Button(FrameButtonsThemeChoser, bg=ColButtonSquare1, width=3, relief=FLAT, command= lambda: ChangeTheme(ColButtonSquare1))
        ButtonCol1.grid(column=1, row=0, padx=10, pady=10)

        ButtonCol2 = Button(FrameButtonsThemeChoser, bg=ColButtonSquare2, width=3, relief=FLAT, command= lambda: ChangeTheme(ColButtonSquare2))
        ButtonCol2.grid(column=2, row=0, padx=10, pady=10)

        ButtonCol3 = Button(FrameButtonsThemeChoser, bg=ColButtonSquare3, width=3, relief=FLAT, command= lambda: ChangeTheme(ColButtonSquare3))
        ButtonCol3.grid(column=0, row=1, padx=10, pady=10)

        ButtonCol4 = Button(FrameButtonsThemeChoser, bg=ColButtonSquare4, width=3, relief=FLAT, command= lambda: ChangeTheme(ColButtonSquare4))
        ButtonCol4.grid(column=1, row=1, padx=10, pady=10)

        ButtonCol5 = Button(FrameButtonsThemeChoser, bg=ColButtonSquare5, width=3, relief=FLAT, command= lambda: ChangeTheme(ColButtonSquare5))
        ButtonCol5.grid(column=2, row=1, padx=10, pady=10)

        ButtonCol6 = Button(FrameButtonsThemeChoser, bg=ColButtonSquare6, width=3, relief=FLAT, command= lambda: ChangeTheme(ColButtonSquare6))
        ButtonCol6.grid(column=0, row=2, padx=10, pady=10)

        ButtonCol7 = Button(FrameButtonsThemeChoser, bg=ColButtonSquare7, width=3, relief=FLAT, command= lambda: ChangeTheme(ColButtonSquare7))
        ButtonCol7.grid(column=1, row=2, padx=10, pady=10)

        ButtonCol8 = Button(FrameButtonsThemeChoser, bg=ColButtonSquare8, width=3, relief=FLAT, command= lambda: ChangeTheme(ColButtonSquare8))
        ButtonCol8.grid(column=2, row=2, padx=10, pady=10)





        Trait = Label(ColumnMid, bg=ColBackDark, fg="#282A35", text="_____________________________________________________________________________", font=("comic", 10, "bold"))
        Trait.pack(side=TOP, anchor=N, pady=40)






#Creer la fenetre
window = Tk()
window.config(bg=ColBackDark)
window.title("Chat Local")
window.geometry("800x800")

#Creer la frame dans lequel on voit la discution
ChatFrame = Frame(window, bg=ColBackDark)
ChatFrame.pack(side=RIGHT, fill=BOTH, expand=True)

#Creer une frame pour voir différentes personnes
HumanFrame = Frame(window, bg=ColBackDark)
HumanFrame.pack(side=LEFT, fill=BOTH, expand=False)

#Frame pour l'espace d'écriture
EntryFrame = Frame(ChatFrame, bg=ColBackDark)
EntryFrame.pack(side=BOTTOM, fill=X)

#A fficher la discution
ChatPage = Text(ChatFrame, relief=FLAT, bg=ColBack, fg=TextColor, highlightthickness=2)
ChatPage.config(highlightbackground = CouleurDeBase, highlightcolor= CouleurDeBase)
ChatPage.pack(pady = 20, fill=BOTH, expand=True)
ChatPage.config(state = DISABLED)


#Entry pour envoyer les messages
Bar_Chat = Entry(EntryFrame, relief=FLAT, bd=10, justify=LEFT, bg=ColBack, fg=TextColor, highlightthickness=2)
Bar_Chat.config(highlightbackground = CouleurDeBase, highlightcolor= CouleurDeBase, insertbackground = CouleurDeBase)
Bar_Chat.pack(pady=20, side=BOTTOM, fill=X)
Bar_Chat.bind("<Return>", Sending)

#Bouton paramètres
ButtonParameters = Button(HumanFrame, text="Paramètres", relief=FLAT, width=25, bg=CouleurDeBase, fg=TextColor, command=lambda: Parametres(window))
ButtonParameters.pack(pady = 20, side=BOTTOM, expand=False)












#Recevoir les messages et les afficher
def Receiving():
    global ChatPage
    global window
    while True:
        data, addr = sock.recvfrom(1024)
        data = data.decode('utf-8')
        print(data)

        ChatPage.config(state = NORMAL)
        ChatPage.insert(END, "\n\n" + str(data))
        ChatPage.config(state = DISABLED)
        ChatPage.see("end")



Thread(target=Receiving).start()




window.mainloop()
