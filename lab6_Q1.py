#program to calculate count of vowels,consonants and words
string=input("enter the sentence:")


#initiliazing
vowel_count=0
consonants_count=0
word_count=1
#looping
for char in string:
    if(char=='A'or char=='E' or char=='O'or char=='U' or char=='I' or char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
        vowel_count=vowel_count+1
    elif char!=" " and char!="\n" and char!="\t":
        consonants_count=consonants_count+1
    elif char==" ":
        word_count=word_count+1
#printing the output
print(f'The vowel count is:{vowel_count}') 
print(f'Consonant count is:{consonants_count}') 
print(f'Word count is:{word_count}')      
        
    


    
