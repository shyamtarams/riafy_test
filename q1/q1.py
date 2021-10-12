with open('input.txt') as f:
    contents = f.read()
    word=contents.split()
    print(len(word))
    for i in range(len(word)):
        print(i)

   
