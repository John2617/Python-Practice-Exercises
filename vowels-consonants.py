n=input("enter the word:").lower()
vowels="aeiou"
vow=0
consonant=0
other=0
for i in n:
    if i==" ":
        continue
    elif i.isalpha():
        if i in vowels:
            vow+=1
        else:
            consonant+=1
    else:
        other+=1
print(vow,"-",consonant,"-",other)
