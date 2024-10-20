words=0
with open("text.txt", "r",encoding= "utf-8") as file:
    for line in file:
        w=line.split()
        words+=len(w)
print("количество слов в файле ", words)