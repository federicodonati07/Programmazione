import images

def f(img):
    img = images.load(img)
    red = (255, 0, 0)
    
    W = len(img)
    H = len(img[0])
    
    for i in range(W):
        for j in range(H):
            if img[i][j] == (255, 255, 255):
                img[i][j] = red
                
    return img
                
immagine = f("test.png")
images.save(immagine, "test.png")