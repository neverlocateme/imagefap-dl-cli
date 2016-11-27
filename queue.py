import config
import IFUser

queue = []

def CheckUrl(url):
    if (url.find(config.GalleryLink1)!=-1):
        return 1 #IF1
    elif (url.find(config.GalleryLink2)!=-1):
        return 2 #IF2
    elif (url.find(config.GalleryLink3)!=-1):
        return 3 #XH
    elif (url.find(config.GalleryLink4)!=-1):
        return 4 #IF3
    elif (url.find(config.IFFolder1)!=-1):
        return 5 #IFFolder1
    elif (url.find(config.IFFolder2)!=-1):
        return 6 #IFFolder2
    elif (url.find(config.IFUserLink)!=-1):
        return 7 #IFUser
    else:
        return 0

### Place the URL, URL type and destination folder (from config) in to the queue array
def AddToQueue(url,urltype,destination_folder):
    global queue
    queue+=[[url,urltype,destination_folder]]

### Remove when we're done
def RemoveFromQueue():
    global queue
    queue.remove(queue[0])

### If it is a folder then run a loop one-by-one on galleries
def AddFolder(FolderUrl):
    UserName, FolderName, Galleries = IFUser.ListFolderGalleries(FolderUrl)
    for Gal in Galleries:
        AddToQueue(Gal,4,config.MainDirectory+"/"+config.UserDirectory+"/"+UserName+"/"+FolderName)

### Process the URL and decide what to do
def ProcessURL(opturl):
    urltype = CheckUrl(opturl)
    if urltype:
        if urltype < 5:
            if urltype == 3:
                AddToQueue(opturl,urltype,config.MainDirectory+"/xHamster")
            else:
                AddToQueue(opturl,urltype,config.MainDirectory+"/ImageFap")
        elif urltype < 7:
                AddFolder(opturl)
        elif urltype == 7:
            Username, Folders = IFUser.ListUserFolders(opturl)
            for Folder in Folders:
                AddFolder(Folder[1])
