import images

def f(img, y, color):
    H = len(img)
    W = len(img[0])
    
    for i in range(H):
        for j in range(W):
            if i == y:
                img[i][j] = color
                
              
    print(img)  
    return img


img = f(images.load("img1.png"), 2, (0, 0, 0))
images.save(img, "img2.png")