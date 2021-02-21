## Motivation
This year’s theme being space inspired me to create something related to astrology! As someone with a side interest in horoscopes, I found that most apps focus on the Western Zodiac. However, there are countless other horoscopes around the world that deserve just as much attention! Thus, my project is focused on creating a single program that can figure out various Zodiac signs based on a single birth date. 💫

## What HackerNaut Does
HackerNaut is a chat-bot styled program in which it asks the user for their birthday and calculates their Zodiac signs based on the entered date. Currently, HackerNaut can calculate the user’s Western and Chinese Zodiac signs.

## How I Built It
Created solely in Python, I imported the regular expression (or RE) library in order to create a chat-bot experience. By using regular expressions, HackerNaut is able to disregard case sensitivity and understand phrases with similar meaning. For instance, if asking a “Yes” or “No” question, HackerNaut is able to distinguish between answers such as “Yep”, “Yeah”, “Nope”, and “Nah” appropriately. As a result, interacting with HackerNaut feels like a natural conversation while learning about horoscopes.

## Challenges I Ran Into
The main challenge I came across was type errors. Although many of the horoscopes dealt with numerical values, HackerNaut would need to converse in English to interact naturally with the user. Thus, I had to pay attention to the type of values that were being passed between functions and also be careful with typecasting between strings and integers.

## Accomplishments That I'm Proud Of
This is my first Hackathon ever, and thus, this is the first Hackathon project I’ve ever done. Despite only having a day to work on it, I was able to get HackerNaut running as intended and successfully submit it.
Python is the most recent coding language I’ve learned, and I’ve only spent less than a month learning how to code with it. Thus, at about 150 lines of code, HackerNaut is the longest program that I’ve written in Python so far!

## What I Learned
I learned how to translate horoscope “rules” into code and algorithms. Each horoscope has its own system and set of rules. For example, Western horoscopes are based on birth month and day, while Chinese horoscopes are based on a cycle of birth years. Thus, I had to figure out how to best express the horoscopes in code so that HackerNaut can figure out the sign for all birthdays given to it.

## What's Next for HackerNaut
The next steps in improving HackerNaut would be:
- Adding a user interface so that HackerNaut can run outside the unix shell,
- Adding more information, such as personality traits and predictions, associated with the resulting horoscope,
- Accounting for irrelevant responses that don’t answer HackerNaut’s questions,
- And of course, adding more horoscopes!
