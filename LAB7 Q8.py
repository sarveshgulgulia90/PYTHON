#program to count the number of times a word occurs in a sentence
#without inbuilt function
#taking input from user
sen=str(input("enter a sentence:"))
word=str(input("enter a word:"))
#initializing counter
c=0
#loop to check for word
for i in sen.split():
    if i==word:
        c=c+1
#displaying results
print(f'Number of times {word} occurs in {sen} is {c}')

#with inbuilt function
#taking input from user
sen=str(input("enter a sentence:"))
word=str(input("enter a word:"))
#displaying results
print(f'Number of times {word} occurs in {sen} is {sen.count(word)}')
