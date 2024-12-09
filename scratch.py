import os

MAIN_FILE_PATH = os.path.dirname(__file__)
IMAGES_FOLDER = os.path.join(MAIN_FILE_PATH, "images")
#ICON_FOLDER = os.path.join(MAIN_FILE_PATH, "icon")
CARDS_FOLDER = os.path.join(IMAGES_FOLDER, "cards")
files= [f for f in os.listdir(CARDS_FOLDER)]

for i in files:
    print(f"'{i[:-4]}': '{i}',")