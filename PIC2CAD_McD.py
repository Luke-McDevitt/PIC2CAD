import cv2
from PIL import Image
import os
from zipfile import ZipFile
import urllib.request
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from pdf2image import convert_from_path

documentspath = os.path.expanduser('~/Documents')
directory = "PIC2CAD_McD"
parent_dir = documentspath
folderpath = os.path.join(parent_dir, directory)
if not os.path.exists(folderpath):
    os.mkdir(folderpath)
    print("Directory '% s' created" % directory)

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

filename3, file_extension = os.path.splitext(filename)


if file_extension == r".pdf":
    print("it is a pdf")
    if not os.path.exists(folderpath + r'/Release-22.04.0-0.zip'):
        popzipfile = (folderpath + r'/Release-22.04.0-0.zip')
        urllib.request.urlretrieve(
            "https://github.com/oschwartz10612/poppler-windows/releases/download/v22.04.0-0/Release-22.04.0-0.zip",
            popzipfile)
        print("downloading poppler")
        file_name = (folderpath + '/Release-22.04.0-0.zip')
        with ZipFile(file_name, 'r') as zip:
            # extracting all the files
            print('Extracting all the files now...')
            zip.extractall(folderpath)
            print('Done!')
    poppler_path = (folderpath + r'\poppler-22.04.0\Library\bin')
    images = convert_from_path(filename, poppler_path=poppler_path)
    for image in images:
        image.save(filename3 + '.png')
        newpngfilepath = (filename3 + '.png')
        myfile2 = f"{newpngfilepath}"

if file_extension == r".jpg":
    im1 = Image.open(filename)
    im1.save(filename3 + '.png')
    newjpg2png = (filename3 + '.png')
    myfile2 = f"{newjpg2png}"

if file_extension == r".png":
    myfile2 = f"{filename}"
print("myfile2 is " + myfile2)

# read the image file
img = cv2.imread(myfile2)
ret, bw_img = cv2.threshold(img, 135, 255, cv2.THRESH_BINARY)
# converting to its binary form
bw = cv2.threshold(img, 135, 255, cv2.THRESH_BINARY)
# save image as bitmap
myfile3 = myfile2.replace(".png", ".bmp")
cv2.imwrite(myfile3, bw_img)
print("converted to bitmap")

if not os.path.exists(folderpath + "/potrace-1.16.win64.zip"):
    ...
    print("path to zip: " + folderpath + "\potrace-1.16win64.zip")
    potracezip = (folderpath + "/potrace-1.16.win64.zip")
    urllib.request.urlretrieve("http://potrace.sourceforge.net/download/1.16/potrace-1.16.win64.zip", potracezip)
    file_name = (folderpath + '/potrace-1.16.win64.zip')
    with ZipFile(file_name, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()

        # extracting all the files
        print('Extracting all the files now...')
        zip.extractall(folderpath)
        print('Done!')
    setx = ('setx potrace ' + folderpath + "\potrace-1.16.win64\potrace.exe")
    def mycmd():
        os.system(setx)
    mycmd()

variable = r'potrace "myfile3" -b dxf -t 10 --progress'
variable2 = variable.replace("myfile3", myfile3)

def mycmd():
    os.system(variable2)
mycmd()

print("Converted to DXF")