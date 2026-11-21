import images

def f(img, color):
    H = len(img)
    W = len(img[0])
    
    counter = 0
    for i in range(H):
        for j in range(W):
            if img[i][j] == color:
                counter += 1
    
    return counter
    
    

img = f(images.load("img3.png"), (0, 0, 0))
print(img)