__author__ = 'dogukansonmez'
from PIL import Image

import os
from django.contrib.auth import get_user
import time

APP_ROOT = os.path.dirname(globals()['__file__'])


def generate_file_name(i):
    return str(int(time.time())) + str(i) + "." + "jpg"


def create_folder_for_current_user(user_path):
    user_path = "static" + user_path
    folder_path = os.path.join(APP_ROOT, user_path)
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)
    return folder_path


def get_user_folder(current_user_name):
    return "/pictures/" + current_user_name


def handle_uploaded_file(path_to_write, f):
    with open(path_to_write, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def save_image_files(request):
    images = []
    i = 0
    max_size = 5000000
    if request.FILES is not None:
        for fileName, image_file in request.FILES.iteritems():
            if max_size > image_file.size:
                #TODO give message about upload image_file
                name = generate_file_name(i)

                i += 1
                #TODO error check
                user_folder = get_user_folder(get_user(request).username)

                img_folder = create_folder_for_current_user(user_folder)

                image_file_path = img_folder + "/" + name
                images.append(user_folder + "/" + name)

                handle_uploaded_file(image_file_path, image_file)

                try:
                    # Open the image file.
                    img = Image.open(image_file_path)
                    # Resize it.
                    w = img.size[0]
                    h = img.size[1]
                    w_box = 750
                    h_box = 650
                    f1 = 1.0 * w_box / w # 1.0 forces float division in Python2
                    f2 = 1.0 * h_box / h
                    factor = min([f1, f2])
                    #print(f1, f2, factor) # test
                    # use best down-sizing filter
                    width = int(w * factor)
                    height = int(h * factor)
                    img = img.resize((width, height), Image.ANTIALIAS)
                    # Save it back to disk.
                    img.save(os.path.join(img_folder, name))
                except IOError:
                    images.pop()
    return images