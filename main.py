def pip(wee):
    doubl = False
    word = wee.split()
    for i in range(len(word)):
        subword = []
        for j in word[i]:
            if j in subword:
                doubl = True
            subword.append(j)
    return doubl
print(pip("Gooby goob goblin dell I maybe"))


def function(exist):
    doing = exist[0]
    for i in range(len(exist)):
        if i != 0:
            if doing < exist[i]:
                doing = exist[i]
    return doing
print(function([10000000000000000,8,4632,4,7,9,11]))
coollist = []
for j in range(10):
    print("input a number")
    inpoo = input()
    coollist.append(inpoo)
print(function(coollist))
