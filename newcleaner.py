import os

def createIfNotExist(folder):
    if not os.path.exists(folder):    # os.path.exists(folder) os path is opened folder where vscode and exist all folders
        os.makedirs(folder) # this can creat folder ( folder is varialbe for function you can create your choice perticularily)

def move(folderName, files):
    for file in files:      # file is i and files is variable which is loaded from pc
        os.replace(file, f"{folderName}/{file}") # foldername me file ko put ker do

if __name__ == "__main__":
        
    files = os.listdir()   #files is loaded from here

    createIfNotExist('Images') # function is getting input here by images
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Others')

    imgExts = [".png", ".jpg", ".jpeg"] # which extension do you want to put in images
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]

    docExts = [".txt", ".docx", "doc", ".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]


    mediaExts = [".mp4", ".mp3", ".flv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
            others.append(file)

    move("Images", images)
    move("Docs", docs)
    move("Media", medias)
    move("Others", others)