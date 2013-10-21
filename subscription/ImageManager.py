__author__ = 'dogukansonmez'
from PIL import Image

import os
from django.contrib.auth import get_user
import time

APP_ROOT = os.path.dirname(globals()['__file__'])
max_with=1200
max_height =800

def generateFileName(extension,i):
    return str(int(time.time())) + str(i) + "." + "jpg"

def createFolderForCurrentUser(userPath):
    userPath = "static" + userPath
    folderPath = os.path.join(APP_ROOT,userPath)
    if not os.path.isdir(folderPath):
        os.makedirs(folderPath)
    return folderPath


def getUserFolder(currentUserName):
    folderPath = "/pictures/" + currentUserName
    return folderPath


def save_image_files(request):
    images = []
    i = 0
    if request.FILES is not None:
        for fileName,file in request.FILES.iteritems():
            name = generateFileName(file.name.split(".")[-1],i)
            i= i+1
            #TODO error check
            userFolder = getUserFolder(get_user(request).username)

            imgFolder = createFolderForCurrentUser(userFolder)

            images.append(userFolder + "/" + name)
            # Open the image file.
            img = Image.open(file)
            # Resize it.
            width = img.size[0]
            height = img.size[1]

            if width > max_with:
                width = max_with

            if height > max_height:
                height = max_height

            img = img.resize((width,height), Image.ANTIALIAS)
            # Save it back to disk.
            img.save(os.path.join(imgFolder, name))

    return images