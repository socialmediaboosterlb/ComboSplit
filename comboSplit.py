import os

emails = open('emailsExtracted.txt','a+')
passwords = open('passExtracted.txt','a+')
print('''
   _____                _              _____       _ _ _   _            
  / ____|              | |            / ____|     | (_) | | |           
 | |     ___  _ __ ___ | |__   ___   | (___  _ __ | |_| |_| |_ ___ _ __ 
 | |    / _ \| '_ ` _ \| '_ \ / _ \   \___ \| '_ \| | | __| __/ _ \ '__|
 | |____ (_) | | | | | | |_) | (_) |  ____) | |_) | | | |_| |_  __/ |   
  \_____\___/|_| |_| |_|_.__/ \___/  |_____/| .__/|_|_|\__|\__\___|_|   
                                            | |                         
                                            |_|                     
   CREDITS INSTAGRAM: socialmediaboosterlb TELEGRAM: socialmediaboosterlb
''')
lol= input("Press enter to start splitting your combo list")

with open('combos.txt', 'r') as f:
    combos = [line.strip() for line in f]

for combo in combos:
    b= combo.split(':')
    emails.write(str(b[0])+'\n')
    passwords.write(str(b[1])+'\n')

lol= input("Splitting is done press ENTER to exit")

