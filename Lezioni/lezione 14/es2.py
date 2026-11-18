import images

def f(img):
    img = images.load(img)
    black = (0, 0, 0)
    W = len(img)
    H = len(img[0])
    spessore = 20
    
    for i in range(H):
        for j in range(W):
            if i < spessore or  i >= H-spessore or j < spessore or j >= W-spessore:
                img[i][j] = black
                
    return img
            
immagine = f("test.png")
images.save(immagine, "test.png")