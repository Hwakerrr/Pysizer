from PIL import Image
import os,sys
import pathlib


#create new directory for resized images
new_dir = "Resized_Imgdir"

cwd = os.getcwd()
cwd2 = str(cwd)+'/'
#print(cwd2)


path = os.path.join(cwd, new_dir)
path2= str(path) + '/'
#print(path2)

os.mkdir(path)

#list items in cwd
dirs = os.listdir(cwd)
#print(dirs)

#basewidth
basewidth = 1000

#resize function
def resize():
        for item in dirs:
            try:
                if os.path.isfile(cwd2+item):
                    name = os.path.basename(item)
                    #print("image identified")
                    img = Image.open(cwd2 + item)
                    wpercent = (basewidth/float(img.size[0]))
                    hsize = int((float(img.size[1])*float(wpercent)))
                    rimg = img.resize((basewidth, hsize), Image.LANCZOS)
                    rimg.save(path2 + name, 'PNG', quality=90)
            except:
                pass

#function call
resize()


