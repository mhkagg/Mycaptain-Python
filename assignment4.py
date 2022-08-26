def most_function():
    word= input("please enter a string: ")
    dict={}
    for n in word:
        keys=dict.keys()
        if n in keys:
            dict[n] +=1
        else:
            dict[n] = 1
    return dict
print(most_function())
