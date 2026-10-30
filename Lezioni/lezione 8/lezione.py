#%%
x = {1, 2, 3, 4, 5}
y = {2, 3, 7}

unione = x|y
intersezione = x&y
print("x: ", x)
print("y: ", y)
print(f"\nUnione: {unione}")
print(f"Intersezione: {intersezione}\n\n")


#%%

charList = ["P", "A", "P", "E", "R", "I", "N", "O"]
vocali = "aeiouAEIOU"

for i in range(len(charList)):
    if charList[i] in vocali:
        charList[i] = ""
        
nlist = []

for char in charList:
    if char != "":
        nlist.append(char)
        
print(nlist)
# %%
