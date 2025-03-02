from tkinter import *
from tkinter import ttk
import subprocess
import requests
import psutil
import shutil
import math
import os

#Create start menu
def start_menu():
    #Create Create window
    def clicked_create():
    #Create back
        def create_back():
            Create.destroy()
            start_menu()
        #Create server file
        def create_file():
            #Clicker create error
            def clicked_create_error():
                #
                #CLICKED_CREATE_ERROR()
                #
                #Close error and create Create window
                Error.destroy()
                clicked_create()
            #
            #CREATE_FILE()
            #    
            #check if everything is filled
            if CreateFileName.get() != "" and Eula.get() == 1:
                #Create Servers folder if it dont exist
                try:
                    os.mkdir("Servers")
                except:
                    print()
                
                #test if the file already exist
                try:    
                    #Create server folder
                    Folder = "Servers/"+CreateFileName.get()
                    os.mkdir(Folder)
                    
                    #Create file that start server
                    StartDirectory  = "Servers/"+CreateFileName.get()+"/start.bat"
                    Start = open(StartDirectory, "x")
                    FileCommand = "java -Xms1G -Xmx"+CreateRamAmount.get()+" -jar server.jar"
                    Start = open(StartDirectory, "w")
                    Start.write(FileCommand)
                    Start.close()
                    
                    #Create eula file
                    EulaDirectory = "Servers/"+CreateFileName.get()+"/eula.txt"
                    Eulafile = open(EulaDirectory, "x")
                    EulaContent = "eula=true"
                    Eulafile = open(EulaDirectory, "w")
                    Eulafile.write(EulaContent)
                    Eulafile.close()
                    
                    #Download server jar file
                    if CreateVersion.get() == "1.20.2":
                        url = "https://api.papermc.io/v2/projects/paper/versions/1.20.2/builds/217/downloads/paper-1.20.2-217.jar"
                    if CreateVersion.get() == "1.16.5":
                        url = "https://papermc.io/api/v2/projects/paper/versions/1.16.5/builds/790/downloads/paper-1.16.5-790.jar"
                    if CreateVersion.get() == "1.12.2":
                        url = "https://papermc.io/api/v2/projects/paper/versions/1.12.2/builds/1618/downloads/paper-1.12.2-1618.jar"
                    if CreateVersion.get() == "1.8.8":
                        url = "https://papermc.io/api/v2/projects/paper/versions/1.8.8/builds/443/downloads/paper-1.8.8-443.jar"
                    r = requests.get(url, allow_redirects=True)
                    open('server.jar','wb').write(r.content)
                    
                    #Copy server.jar to server folder
                    shutil.copyfile("server.jar", "Servers/"+CreateFileName.get()+"/server.jar")
                    os.remove("server.jar")
                    Create.destroy()
                    start_menu()
                #if file already exist
                except:
                    #Close Create window
                    Create.destroy()
                    #Create window
                    Error = Tk()
                    Error.title("ERROR")
                    Error.geometry("175x85")
                    #Create text and button
                    ErrorText = Label(Error, text="That folder name\n already exist")
                    ErrorText.grid(column=0, row=0, padx=(35, 0), pady=(10, 0))
                    ErrorButton = Button(Error, text="OK", command=clicked_create_error)
                    ErrorButton.grid(column=0, row=1, pady=(5, 0), padx=(45, 0))
            #if not everything is filled show error
            else:
                #Create error window
                Error = Tk()
                Error.title("ERROR")
                Error.geometry("175x85")
                #Show error ver. if file name is empty
                if CreateFileName.get() == "":
                    Create.destroy()
                    ErrorText = Label(Error, text="File name can't be empty", font=("Arial Bold", 10))
                    ErrorText.grid(column=0, row=0, padx=(12, 0), pady=(10, 0))
                    ErrorButton = Button(Error, text="OK", command=clicked_create_error)
                    ErrorButton.grid(column=0, row=1, pady=(10, 0), padx=(10, 0))
                #Show error ver. if eula is not accepted
                elif Eula.get() == 0:
                    Create.destroy()
                    ErrorFile = Label(Error, text="Eula must be accepted")
                    ErrorFile.grid(column=0, row=0, pady=(10, 0), padx=(25, 0))
                    ErrorButton = Button(Error, text="OK", command=clicked_create_error)
                    ErrorButton.grid(column=0, row=1, pady=(10, 0), padx=(20, 0))
        
        #
        #CLICKED_CREATE()
        #
        #Destroy menu window if it exist
        try:    
            Menu.destroy()
        except:
            print()
            
        #Create Create window
        Create = Tk()
        Create.title("Create Server")
        Create.geometry("450x250")
        
        #Create Create all buttons and texts
        #Create Creating Server Menu texts
        CreateText = Label(Create, text="Creating Server Menu: ", font=("Arial Bold", 15))
        CreateText.grid(column=0, row=0, pady=(10,10))
        #Create Create back button
        CreateBack = Button(Create, text="<- Back", command=create_back)
        CreateBack.grid(column=1, row=0, padx=(130, 0))
        #Create version choose
        CreateVersionText = Label(Create, text="Select version:")
        CreateVersion = ttk.Combobox(Create, state="readonly")
        CreateVersion['values'] = ("1.8.x", "1.12.2", "1.16.5")
        CreateVersion.current(2)
        CreateVersionText.grid(column=0, row=1)
        CreateVersion.grid(column=1, row=1, pady=(0,10))
        #Create choose RAM amount Combobox
        CreateRamAmountText = Label(Create, text="Choose max RAM usage:")
        CreateRamAmount = ttk.Combobox(Create, state="readonly")
        RAMamount = []
        for i in range (math.ceil(psutil.virtual_memory().total / (1024 ** 3)/2)):
            RAMamount.append(f"{i+1}GB")
        CreateRamAmount['values'] = (RAMamount)
        CreateRamAmount.current(0)
        CreateRamAmountText.grid(column=0, row=2)
        CreateRamAmount.grid(column=1, row=2, pady=(0,10))
        #Create server file input name
        CreateFileNameText = Label(Create, text="Enter server file name")
        CreateFileName = Entry(Create, width=30)
        CreateFileNameText.grid(column=0, row=3)
        CreateFileName.grid(column=1, row=3, pady=(0,10))
        #Create accept eula button
        Eula = IntVar()
        CreateEulaText = Label(Create, text="Accept eula:")
        CreateEula = Checkbutton(Create, variable=Eula)
        CreateEulaText.grid(column=0, row=4)
        CreateEula.grid(column=1, row=4, pady=(0,10))
        #Create create server file button
        CreateBtn = Button(Create, text="Create file", command=create_file)
        CreateBtn.grid(column=0, row=5, padx=(190,0), pady=(25,0))   
    def clicked_menageServers():
        def menage_back():
            Menage.destroy()
            start_menu()
        def start_server():
            if MenageChooseFile.get() != "":
                folder_name = f'Servers/{MenageChooseFile.get()}'
                file_name = 'start.bat'

                # Utwórz pełną ścieżkę do pliku batcha
                batch_file_path = os.path.join(folder_name, file_name)

                # Przejdź do folderu przed uruchomieniem pliku batcha
                os.chdir(folder_name)

                # Uruchom plik batcha w nowym oknie, bez zamykania okna cmd
                subprocess.Popen(f'start cmd /k "{file_name}"', shell=True)
        def delete_server():
            if MenageChooseFile.get() != "":
                FilePath = "Servers/"+MenageChooseFile.get()
                shutil.rmtree(FilePath)
                Menage.destroy()
                clicked_menageServers()
        def show_IP():
            def IP_back():
                IP.destroy()
                clicked_menageServers()
            Menage.destroy()
            IP = Tk()
            IP.title("IP")
            IP.geometry("200x100")
            
            IPButtonBack = Button(IP, text="<- back", command=IP_back)
            IPButtonBack.grid(column=0, row=0, padx=(10,100), pady=(10,0))
            
            PrivateIP = "localhost:25565"
            IPprivate = Label(IP, text=f"Private IP: {PrivateIP}")
            IPprivate.grid(column=0, row=1, pady=(5,0))
            
            PublicIP = requests.get('https://api.ipify.org').text
            IPPublic = Label(IP, text=f"Public IP: {PublicIP}")
            IPPublic.grid(column=0, row=2, padx=(0,10))
            
        #Create Menage window
        try:
            Menu.destroy()
        except:
            print()
        Menage = Tk()
        Menage.title("Menage Servers")
        Menage.geometry("300x175")
        
        #Create Menage all buttons and texts
        #Create choose file text
        MenageTextChoose = Label(Menage, text="Choose Server file:", font=("Arial Bold", 13))
        MenageTextChoose.grid(column=0, row=0, padx=(0, 20))
        #Create Menage back button
        MenageBack = Button(Menage, text="<- Back", command=menage_back)
        MenageBack.grid(column=1, row=0, padx=(70, 0), pady=(10, 0))
        #Create choose file
        MenageChooseFile = ttk.Combobox(Menage, state="readonly")
        MenageChooseFile['values'] = [name for name in os.listdir('./Servers') if os.path.isdir(os.path.join('./Servers', name))]
        MenageChooseFile.grid(column=0, row=1, padx=(20, 0), pady=(2, 0))
        
        #Create Actions text
        MenageTextAction = Label(Menage, text="Actions:", font=("Arial Bold", 13))
        MenageTextAction.grid(column=0, row=2, padx=(0, 100))
        #Create start server button
        MenangeButtonStartServer = Button(Menage, text="Start Server", command=start_server)
        MenangeButtonStartServer.grid(column=0, row=3, pady=(3, 0))
        #Create show IP button
        MenageButtonShowIP = Button(Menage, text="Show IP", command=show_IP)
        MenageButtonShowIP.grid(column=1, row=3, pady=(3, 0))
        #Create Del server button
        MenageButtonDeleteServer = Button(Menage, text="Delete Server" ,command=delete_server)
        MenageButtonDeleteServer.grid(column=0, row=4, pady=(10, 0))

    #Create main window
    Menu = Tk()
    Menu.title("MyServMC")
    Menu.geometry("250x150")
    
    #Create Menu all buttons and texts
    #Create Server Menu text
    lbl = Label(Menu, text="Server Menu:", font=("Arial Bold", 15))
    lbl.grid(column=0 , row=0, pady=(15,10), padx=60)
    #Create button to start Create window
    ButtonCreate = Button(Menu, text="Create", command=clicked_create)
    ButtonCreate.grid(column=0, row=1, pady=(0,10))
    #create button to start Menage window
    ButtonMenage = Button(Menu, text ="Menage Servers", command=clicked_menageServers)
    ButtonMenage.grid(column=0, row=2)
    Menu.mainloop()
    
start_menu()

#███████╗░█████╗░░██╗░░░░░░░██╗░█████╗░░█████╗░██████╗░██╗░░██╗██╗
#██╔════╝██╔══██╗░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██║
#█████╗░░███████║░╚██╗████╗██╔╝██║░░██║██║░░██║██████╔╝█████═╝░██║
#██╔══╝░░██╔══██║░░████╔═████║░██║░░██║██║░░██║██╔══██╗██╔═██╗░██║
#██║░░░░░██║░░██║░░╚██╔╝░╚██╔╝░╚█████╔╝╚█████╔╝██║░░██║██║░╚██╗██║
#╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝