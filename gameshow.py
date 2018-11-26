#imports
import random

#opponents
o1 = 'Daisy'
o2 = 'Conrad'

#questions
#level 1
q1a = 'What is the capital of France?'
q1b = 'What color is the average apple?'
q1c = 'What character did Harrison Ford play in Star Wars?'
q1d = 'What is 50 divided by 10?'
q1e = 'What color is the Incredible Hulk?'
q1f = 'What is the main language spoken in Japan?'
q1g = 'What is the name of Harry Potter`s owl?'
q1h = 'How do you say `hello` in German?'
q1i = 'How many legs does a spider have?'
#level 2
q2a = 'What is the driest desert in the world?'
q2b = 'What is the most popular type of apple in the US?'
q2c = 'What is the last name of the protagonist in `The Hunger Games?'
q2d = 'Which country has the largest spanish-speaking population?'
q2e = 'What is Captain America`s real first name?'
q2f = 'What is the common name for the animal `Canis Lupus Familiaris`?'
q2g = 'How many bones does the human body contain?'
q2h = 'In which fictional city could you find the Wizard of Oz?'
q2i = 'In which country did coffee originate?'
#level 3
q3a = 'What is the middle name of the actor Rami Malek?'
q3b = 'How many licks does it take, on average, does it take to reach the center of a Tootsie Pop?'
q3c = 'How many millions of kilometers away from Earth is Jupiter?'
q3d = 'Who is credited as the inventor of basketball?'
q3e = 'What is the second most populated city in the world?'
q3f = 'What is the most popular word in the King James Bible?'
q3g = 'Who is the author of `Bridge to Terabithia`?'
q3h = 'How do you say `hello` in Czech?'
q3i = 'Where was the highest recorded temperature of 134°F occur?'

#options
option1 = (q1a, q1b, q1c, q1d, q1e, q1f, q1g, q1h, q1i)
option2 = (q2a, q2b, q2c, q2d, q2e, q2f, q2g, q2h, q2i)
option3 = (q3a, q3b, q3c, q3d, q3e, q3f, q3g, q3h, q3i)
optiono = (o1, o2)

#randomized definitions
prizeMoney = random.randint(1,1000000)
nameComp = random.choice(optiono)

point = 0

print('******WELCOME TO GEOPARTY******')
print('I`m your host, Alec Rezek.')
print('Today`s prize is a grand total of $' +  str(prizeMoney) + '!')
print('Would you like to play?')
while True:
    play = input()
    if play in ['yes', 'y', 'yeah', 'yep', 'Yes', 'Yep', 'Yeah', 'Y']:
        break
    elif play in ['no', 'n', 'No', 'N', 'nah', 'Nah', 'nope', 'Nope']:
        print('Please?')
    else:
        print('Is that a yes?')
print('Great! Your enthusiasm is overwhelming!')
print('Today you`ll be competing against ' + str(nameComp) + '. Say `hello` to your competition!')
while True:
    greeting = input()
    if greeting in ['hello', 'Hello', 'hi', 'Hi', 'hey', 'Hey'] :
        print('What wonderful sportsmanship you have!')
        break
    else:
        print('I SAID, SAY HELLO!!!!!')
print('Now let`s get started!')
print('Round one will be easy questions, round two medium, and round three hard.')
print('Round one will begin now. Please type `ok`.')
while True:
    ok = input()
    if ok != 'ok':
        print('(type `ok`)')
    else:
        break
i = 0
while i < 3:
    question1 = random.choice(option1)
    print(question1)
    i += 1
    if question1 == q1a:
        answer = input()
        if answer in ['Paris', 'paris']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question1 == q1b:
        answer = input()
        if answer in ['red', 'Red']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question1 == q1c:
        answer = input()
        if answer in ['han solo', 'Han solo', 'han Solo', 'Han Solo']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question1 == q1d:
        answer = input()
        if answer == '5':
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question1 == q1e:
        answer = input()
        if answer in ['green', 'Green']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question1 == q1f:
        answer = input()
        if answer in ['Japanese', 'japanese']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question1 == q1g:
        answer = input()
        if answer in ['Hedwig', 'hedwig']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question1 == q1h:
        answer = input()
        if answer in ['Hallo', 'hallo']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question1 == q1i:
        answer = input()
        if answer == '8':
            print('correct')
            point += 1
        else:
            print('incorrect')
print('Good job! You passed the first round with ' + str(point) + ' point(s)!')
if point == 3:
    print('You and ' + str(nameComp) + ' are currently tied.')
else:
    print(str(nameComp) + ' is currently ' + str(3 - int(point)) + ' point(s) ahead. Try to catch up!')
print('Time for round two. Are you ready?')
while True:
    ready = input()
    if ready != 'yes':
        print('(please type `yes`)')
    else:
        break
i = 0
while i < 3:
    question2 = random.choice(option2)
    print(question2)
    i += 1
    if question2 == q2a:
        answer = input()
        if answer in ['Atacama', 'atacama']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question2 == q2b:
        answer = input()
        if answer in ['Gala apple', 'Gala Apple', 'Gala', 'gala apple', 'gala']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question2 == q2c:
        answer = input()
        if answer in ['Everdeen', 'everdeen']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question2 == q2d:
        answer = input()
        if answer in ['Mexico', 'mexico']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question2 == q2e:
        answer = input()
        if answer in ['Steve', 'steve']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question2 == q2f:
        answer = input()
        if answer in ['Dog', 'dog']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question2 == q2g:
        answer = input()
        if answer == '206':
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question2 == q2h:
        answer = input()
        if answer in ['Emerald City', 'The Emerald City', 'the emerald city', 'emerald city', 'The emerald city']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question2 == q2i:
        answer = input()
        if answer in ['Ethiopia', 'ethiopia']:
            print('correct')
            point += 1
        else:
            print('incorrect')
print('Good job! You passed the second round with a new total of ' + str(point) + ' point(s)!')
if point == 6:
    print('Wow! You`re beating ' + str(nameComp) + ' by one point! I didn`t exactly see this coming....')
elif point == 5:
    print('You and ' + str(nameComp) + ' are tied with 5 points each.')
else:
    print('You`re losing to ' + str(nameComp) + '. ' + str(nameComp) + ' is ' + str(5 - int(point)) + ' point(s) ahead of you.')
print('Finally we have arrived at the final round.')
if point == 6:
    print('If you keep your lead, you could win the prize of $' + str(prizeMoney) + '!')
if point <= 5:
    print('Try and pull ahead for that prize of $' + str(prizeMoney) + '!')
if point <= 2:
    print('You have no chance of winning :-) Say goodbye to those $' + str(prizeMoney) + '!')
print('Are you prepared for the final, hardest round?')
while True:
    prepared = input()
    if prepared != 'yes':
        print('(please type `yes`)')
    else:
        break
i = 0
while i < 3:
    question3 = random.choice(option3)
    print(question3)
    i += 1
    if question3 == q3a:
        answer = input()
        if answer in ['Said', 'said']:
            print('correct')
            point +=  1
        else:
            print('incorrect')
    if question3 == q3b:
        answer = input()
        if answer == '364':
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question3 == q3c:
        answer = input()
        if answer == '588':
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question3 == q3d:
        answer = input()
        if answer in ['James Naismith', 'James naismith', 'james Naismith', 'james naismith', 'naismith', 'Naismith']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question3 == q3e:
        answer = input()
        if answer in ['Beijing', 'beijing']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question3 == q3f:
        answer = input()
        if answer in ['And', 'and']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question3 == q3g:
        answer = input()
        if answer in ['Katherine Paterson', 'Katherine paterson', 'katherine Paterson', 'katherine paterson', 'paterson', 'Paterson']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question3 == q3h:
        answer = input()
        if answer in ['Ahoj', 'ahoj']:
            print('correct')
            point += 1
        else:
            print('incorrect')
    if question3 == q3i:
        answer = input()
        if answer in ['death valley', 'Death Valley', 'Death valley', 'death Valley', 'deathvalley']:
            print('correct')
            point += 1
        else:
            print('incorrect')
print('Congratulations, you have finished the final round with a total of ' + str(point) + '!')
if point < 6:
    print('Unfortunately, you`ve lost to ' + str(nameComp) + ' by ' + str(6 - int(point)) + ' point(s). ' + str(nameComp) + ' wins the $' + str(prizeMoney) + '!')
    if point == 0:
        print('Are you an idiot?????????')
    elif point in [1, 2, 3, 4]:
        print('That was pretty rough... Your future doesn`t lie with trivia game shows.')
    else:
        print('You weren`t too far off! Maybe try again?')
elif point == 6:
    print('Wow! You somehow managed to tie with ' + str(nameComp) + '..! Well done...')
    print('I guess you can split the money between yourselves. You each get $' + str(int(prizeMoney)/2) + '!')
elif point in [7, 8]:
    print('WHAT????? You won???!!! That wasn`t supposed to... I mean... Congratulations...!')
    print('I guess you win the money then... here, $' + str(prizeMoney) + '... Spend it wisely...')
if point == 9:
    print('Yeah, right. There`s no way you could have actually known all of those, cheater. No prize money for you.')
    print('Here, ' + str(nameComp) + '.  You win $' + str(prizeMoney) + ' for playing fairly.')
print('We`ve reached the end of Geoparty!')
print('Did you enjoy the game?')
enjoy = input()
if enjoy in ['yes', 'y', 'Yes', 'Y', 'Yeah', 'Yep', 'yeah', 'yep']:
    print('Thanks! Please play again soon!')
elif enjoy in ['no', 'n', 'No', 'N', 'nah', 'Nah', 'nope', 'Nope']:
    print('Don`t be rude. This is the best game ever!')
else:
    print(':-)')
print('END.')
