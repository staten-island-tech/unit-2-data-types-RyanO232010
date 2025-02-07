""" x = 3
y = float(3)
print(x,y) """
#TIPCALCULATOR
""" def add (x,y):
    print(x+y)


bill = float(input("How much was the bill?"))
print(type(bill))

tip = int(bill * .15)
print(add(tip,bill))
 """

#WORD COUNTER
""" def count (text) :
    words = text.split() #split the text into a list of words
    return len(words) #return the number of words
response = input("Please enter a sentence or paragraph: ")

word_count= count(response)

print(f"The word count is: {word_count}") """


#MADLIBS

""" a = input("Please input a Verb: ")
b = input("Please input a Second Verb: ")
c = input("Please input a Noun: ")
d = input("Please input a Number: ")
e = input("Please input a Celebrity: ")

print("Mohamed had to",a,",even though the quickest way to class is when you",b,". Mohamed being stupid got chased by a",c,", turns out he was actually being chased by",d,c,". While running like a idiot, he somehow met",e) """

#Odd or Even
""" odd_or_even = float(input("Please input a number: "))
if odd_or_even %  2 == 0 :
    print("This number is Even")
else:
    print("This number is Odd")

 """

#TIPBASEDONSERVICE

""" def add (x,y):
    return x + y


bill = float(input("How much was the bill?"))
print(type(bill))

x=0

service = input("How was your service? Bad, Okay, Good , or Great?")

if service.lower() == "bad":
    x = 0
elif service.lower() == "okay":
    x = 0.15
elif service.lower() == "good":
    x=0.2
elif service.lower() == "great":
    x=0.25
else:
    print("Please restart the program and try again.")
while service not in ["bad", "okay", "good", "great"]:
    service = input("Invalid input. Please enter 'Bad', 'Okay', 'Good', or 'Great': ").lower()
tip = bill * x
total = add(bill, tip)

print(f"The total bill, including the tip, is: ${total:.2f}") """

#FACTORIZER OF NUMBERS



