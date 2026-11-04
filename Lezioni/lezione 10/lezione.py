'''
with open("new_file.txt", "w") as f:
    f.write("Hello\nPippo")
    f.close()
    
    
with open("new_file.txt", "r") as f:
    print(f.readline())
    f.close()
'''

with open("testo.txt", "r") as f:
    print(f.read())
    
    
