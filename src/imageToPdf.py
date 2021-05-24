from PIL import Image

def combineToPdf(pathList, outputPath):
    images = []
    img0 = Image.open(r'{}'.format(pathList[0])).convert('RGB')
    for ipath in pathList[1:]:
        images.append((Image.open(r'{}'.format(ipath)).convert('RGB')))
    img0.save(r'{}'.format(outputPath), save_all=True, append_images=images)

def test():
    from os import listdir
    pathList=[]
    for path in listdir("test/images"):
        pathList.append("test/images/"+path)
    outputPath = "paper.pdf"
    combineToPdf(pathList, outputPath)
    print("Done!")