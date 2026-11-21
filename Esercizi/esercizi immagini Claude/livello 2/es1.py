import images

def f(img):
    H = len(img)
    W = len(img[0])
    
    for i in range(H):
        for j in range(W):
            for _ in range(len(img[i][j])):
                inverted = (255-img[i][j][0], 255-img[i][j][1], 255-img[i][j][2])
                
            img[i][j] = inverted
    
    return img
    
    
img = f(images.load("img.png"))
images.save(img, "inverted.png")