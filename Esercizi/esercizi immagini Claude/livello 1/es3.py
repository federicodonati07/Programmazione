import images

def f(img, x, color):
    H = len(img)
    W = len(img[0])
    
    for i in range(H):
        for j in range(W):
            if j == x:
                img[i][j] = color
    
    print(img)
    return img 

   
img = f(images.load("img1.png"), 3, (0, 0, 0))
images.save(img, "img3.png")