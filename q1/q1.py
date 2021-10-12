# open test file
with open('input.txt') as f:
    contents = f.read()
    # split each words after space
    sentence=contents.split()
    # initialize empty dict to store values
    counts = {}
    for i in sentence:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    print(counts)



