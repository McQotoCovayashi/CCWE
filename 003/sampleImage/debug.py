import trimImage as ti
# svg = ti.getSVGs()
# image = ti.getImages()
# rect = ti.rectAxis(svg[0])
# ti.trimImage(image[0],rect[0],"test.jpg")

# dirPath = ti.getDir()
# print(dirPath)

svgList,imageList = ti.getList()
for i in range(len(svgList)):
    print("svg  :{0}\nimage:{1}".format(svgList[i], imageList[i]))
print("svg  :{0} \nimage:{1}".format(len(svgList),len(imageList)))
