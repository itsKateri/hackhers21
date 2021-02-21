import re

def monthToNum(s): # converts months to integer values
    num = 0
    if re.search(r"(?i)Jan", s) is not None:
        num = 1
    elif re.search(r"(?i)Feb", s) is not None:
        num = 2
    elif re.search(r"(?i)Mar", s) is not None:
        num = 3
    elif re.search(r"(?i)Apr", s) is not None:
        num = 4
    elif re.search(r"(?i)May", s) is not None:
        num = 5
    elif re.search(r"(?i)Jun", s) is not None:
        num = 6
    elif re.search(r"(?i)Jul", s) is not None:
        num = 7
    elif re.search(r"(?i)Aug", s) is not None:
        num = 8
    elif re.search(r"(?i)Sep", s) is not None:
        num = 9
    elif re.search(r"(?i)Oct", s) is not None:
        num = 10
    elif re.search(r"(?i)Nov", s) is not None:
        num = 11
    elif re.search(r"(?i)Dec", s) is not None:
        num = 12
    return num

def western(m, d): #calculates zodiac based on Western sign
    if (m == 12 and d >= 22) or (m == 1 and d <= 19):
        sign = "Capricorn"
    elif (m == 1 and d >= 20)or(m == 2 and d <= 18):
        sign = "Aquarius"
    elif (m == 2 and d >= 19)or(m == 3 and d <= 20):
        sign = "Pisces"
    elif (m == 3 and d >= 21)or(m == 4 and d <= 19):
        sign = "Aries"
    elif (m == 4 and d >= 20)or (m == 5 and d <= 20):
        sign = "Taurus"
    elif (m == 5 and d >= 21)or (m == 6 and d <= 21):
        sign = "Gemini"
    elif (m == 6 and d >= 22)or (m == 7 and d <= 22):
        sign = "Cancer"
    elif (m == 7 and d >= 23)or (m == 8 and d <= 22): 
        sign = "Leo"
    elif (m == 8 and d >= 23)or (m == 9 and d<= 22): 
        sign = "Virgo"
    elif (m == 9 and d >= 23)or (m == 10 and d<= 23):
        sign = "Libra"
    elif (m == 10 and d >= 24)or (m == 11 and d<= 21): 
        sign = "Scorpio"
    elif (m == 11 and d >= 22)or (m == 12 and d<= 21):
        sign = "Sagittarius"
    return sign

def western_element(s): #calculates element of Western sign
    if s in ["Aries", "Leo", "Sagittarius"]:
        element = "Fire"
    elif s in ["Taurus", "Virgo", "Capricorn"]:
        element = "Earth"
    elif s in ["Gemini", "Libra", "Aquarius"]:
        element = "Air"
    elif s in ["Cancer", "Scorpio", "Pisces"]:
        element = "Water"
    return element

def chinese(y): #calculates zodiac based on Chinese sign
    #Assumes birth year is 1900 or later.
    x = (y - 1900) % 12
    sign = ""
    if x == 0:
        sign = "Rat"
    elif x == 1:
        sign = "Ox"
    elif x == 2:
        sign = "Tiger"
    elif x == 3:
        sign = "Rabbit"
    elif x == 4:
        sign = "Dragon"
    elif x == 5:
        sign = "Snake"
    elif x == 6:
        sign = "Horse"
    elif x == 7:
        sign = "Goat"
    elif x == 8:
        sign = "Monkey"
    elif x == 9:
        sign = "Rooster"
    elif x == 10:
        sign = "Dog"
    elif x == 11:
        sign = "Pig"

    return sign

def chinese_element(y): #calculates element of Chinese sign
    y = str(y)
    lastDigit = int(y[3])
    if lastDigit == 0 or lastDigit == 1:
        element = "Metal"
    elif lastDigit == 2 or lastDigit == 3:
        element = "Water"
    elif lastDigit == 4 or lastDigit == 5:
        element = "Wood"
    elif lastDigit == 6 or lastDigit == 7:
        element = "Fire"
    elif lastDigit == 8 or lastDigit == 9:
        element = "Earth"
    return element

print("HELLO! I'm HackerNaut, and I can help you figure out your Zodiac Signs!")
print("All I need to know is when you were born. Let's get started:")

info = False

while (info == False): # obtaining birthday
    print("First, what month were you born?")
    month = input()
    if month.isalpha():
        month = monthToNum(month)
    else:
        month = int(month)

    print("Second, what day were you born?")
    day = int(input())

    print("Last, what year were you born?")
    year = int(input())
    
    print("Just to confirm, is this the correct birthdate: %d/%d/%d ?" % (month, day, year))
    
    confirm = input()
    if re.search(r"(?i)y", confirm) is not None:
        print("Alright, awesome!")
        info = True
        break
    elif re.search(r"(?i)n", confirm) is not None:
        print("Oops, sorry! Let me ask again.")

print("Right now, I can figure out your Western Zodiac or your Chinese Zodiac.\nWhich do you want to hear?")
response = input()
while re.search(r"(?i)bye", response) is None:
    if re.search(r"(?i)west", response) is not None:
        w = western(month,day)
        print("According to the Western Horoscope, your sign is: " + w + ".")
        print (w + " is a "+ western_element(w) + " sign.")
    elif re.search(r"(?i)chinese", response) is not None:
        print("According to the Chinese Horoscope, your sign is: " + chinese(year) + ".")
        print ("Your sign is associated with the " + chinese_element(year) + " element.")
    print('You can say "Bye" to leave, or you can tell me which Zodiac you want to hear! (Western or Chinese)')
    response = input()

print("It was nice meeting you, goodbye!")