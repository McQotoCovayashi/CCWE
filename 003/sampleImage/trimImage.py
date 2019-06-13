import tkinter
import tkinter.filedialog as fdlg
import os
import cv2
import matplotlib.pyplot as plt

def getNames(fType, iDir = os.getcwd()):
    root = tkinter.Tk()
    root.withdraw()
    files = fdlg.askopenfilenames(filetypes = fType, initialdir = iDir)
    return files

def getDir(iDir = os.getcwd()):
    root = tkinter.Tk()
    root.withdraw()
    Dir = fdlg.askdirectory(initialdir = iDir)
    return Dir

def getImages():
    images = getNames(fType = [('jpeg file','*.jpg'),('jpeg file','*.jpeg'),('png file','*.png')])
    return images

def getSVGs():
    SVGs = getNames(fType=[('svg file','*.svg')])
    return SVGs

def getList():
    dirPath = getDir()
    fileList = os.listdir(dirPath)
    svgList = []
    imageList = []
    for name in fileList:
        if len(name.split(".")) == 1:
            continue
        elif name.split(".")[1] == "svg":
            svgList.append(os.path.join(dirPath, name))
        else:
            continue
    for name in svgList:
        imageName = name.split(".")[0]
        if os.path.exists(imageName+".jpg") == True:
            imageList.append(os.path.join(dirPath, imageName+".jpg"))
        elif os.path.exists(imageName+".png") == True:
            imageList.append(os.path.join(dirPath, imageName+".png"))
        elif os.path.exists(imageName+".jpeg") == True:
            imageList.append(os.path.join(dirPath, imageName+".jpeg"))
        else:
            continue
    return svgList,imageList
    

def rectAxis(path):
    #path is a SVG file's path.
    rectAxis = []
    with open(path, 'r', encoding='utf8') as f:
        dFlag = 0
        count = 0
        a = []
        b = []
        lines = f.readlines()
        for line in lines:                           
            #if line == "</svg>":
            #    break
            line = line.strip()
            if line[:2] != "d=" and dFlag == 0:
                continue
            elif line[:2] == "d=" and dFlag == 0:
                dFlag = 1
                continue
            else:
                if line[:2] == "M ":
                    continue
                elif line == "</svg>":
                    dFlag = 0
                    count = 0
                    continue
                elif line[:2] == "C ":
                    a = line.split()[1].split(",")
                    count += 1
                    continue
                elif count == 1 :
                    count += 1
                    continue
                elif count == 2:
                    count += 1
                    b = line.split()[0].split(",")
                    c = tuple(a), tuple(b)
                    rectAxis.append(c)
                    a = []
                    b = []
                    continue
                else:
                    count = 0
                    if line[:-2] == "/>":
                        dFlag = 0
    return rectAxis                

def trimImage(image,rectAxis,saveName,showImage = False):
    # image is a image file path.
    img = cv2.imread(image)
    x_0 = int(float(rectAxis[0][0]))
    x_1 = int(float(rectAxis[1][0]))
    y_0 = int(float(rectAxis[0][1]))
    y_1 = int(float(rectAxis[1][1]))
    cutImg = img[y_0:y_1, x_1:x_0]
    if showImage == True:
        plt.subplot(1,2,1)
        plt.imshow(img)
        plt.subplot(1,2,2)
        plt.imshow(cutImg)
        plt.show()
    cv2.imwrite(saveName, cutImg)
