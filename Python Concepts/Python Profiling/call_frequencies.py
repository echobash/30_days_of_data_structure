'''
Given these strings, find the all the VOWEL word 
and print them out. Each vowel word are vowel char that are right next to each other. 

* Please use the same formatting as show. Do not leave unnecessary 
line and space. Preserved the char order and cases as shown in the same output 

** There is no need for you to read the input as a file. Just show how you go about process the 2 strings and show the required output will do. 


Example 
str1: bcdaeightiout 

Output: 
aei 
iou 

str2: 12456#!a#e33aeiouut345.uUuio 
Output: 
a 
e 
aeiouu 
uUuio
'''

# str1 = '12456#!a#e33aeiouut345.uUuio'

def finaVowelWords(str1):
    n = len(str1)
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    result = []

    temp_char = ''
    for char in str1:
        if char not in vowels:
            continue
        else:
            temp_char += char
            if






str1 = 'bcdaxeightiout'
print(finaVowelWords(str1))

str1 = '12456#!a#e33aeiouut345.uUuio'
print(finaVowelWords(str1))













