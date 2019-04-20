import re

def searchNum (text):
    textList = list(text)
    num = re.compile('[1-9][0-9]*')
    for i in range(0, len(textList)):
        if num.match(textList[i]):
                if textList[i+1] and num.match(textList[i+1]):
                    twoDig = ''.join(textList[i:i+2])
                    textList.insert(i,stringmatch(textList[0:i], int(twoDig)))
                    textList.pop(i+1)
                    textList.pop(i+1)
                    textList.append("")
                else:
                    textList.insert(i,""+stringmatch(textList[0:i],int(textList[i])))
                    textList.pop(i+1)

        if textList[i] == "0":
            textList.pop(i)
            textList.append("")

    print(''.join(textList))

def stringmatch(text,pos):
    word = re.compile('[a-z]([A-Z]|[a-z])*|[A-Z]([A-Z]|[a-z])*')
    textList = list(text)
    start = 0
    bool = 0
    savedWords = []
    for i in range(0, len(textList)):
        if word.match(textList[i]) and bool == 0:
            start = i
            bool = 1
        if not word.match((textList[i])) and bool == 1:
            if not ''.join(textList[start:i]) in savedWords:
                savedWords.insert(0,''.join(textList[start:i]))
                bool = 0
            else:
                savedWords.remove(''.join(textList[start:i]))
                savedWords.insert(0,''.join(textList[start:i]))
                bool = 0

    return savedWords[pos-1]
file = open("uncomp.txt")

searchNum(file.read())
