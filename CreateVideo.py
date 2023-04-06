import cv2
import os

path = "Images"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file = path +"/" + file

        #print(file)
               
        images.append(file)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])

height,width,channels = frame.shape
size = (width,height)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DVIX'),0.8,size)

for i in range(count - 1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("done")
