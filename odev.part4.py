liste1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in liste1:
    for j in liste2:
        a = i * j
        print(f"{i}x{j} = {a}", end="\t")
    
    print()