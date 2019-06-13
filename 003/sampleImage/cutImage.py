import trimImage as ti
import os

svgList, imageList = ti.getList()
iDir = os.getcwd()
for i in range(len(svgList)):
    rect = ti.rectAxis(svgList[i])
    baseName = os.path.basename(svgList[i]).split(".")[0]
    os.mkdir(baseName)
    os.chdir(baseName)
    # saveName = baseName+"{:0=3}_".format(i)
    print("<<{}>>".format(baseName))
    for j in range(len(rect)):
        print(rect[j])
        ti.trimImage(imageList[i],rect[j],baseName+"_{:0=3}".format(j+1)+".jpg")
    os.chdir(iDir)