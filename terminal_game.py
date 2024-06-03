#Title
print('[Eldoria - Outskirts of the Ruins]')

#Background Info
print('You stand at the edge of the ancient ruins, the sun casting long shadows across the crumbling stone structures. The air is thick with the scent of earth and decay, mingling with the faint hum of forgotten machinery. Your name is Alex, a scavenger by trade, always on the lookout for anything valuable that might be hidden in these desolate remains.') 
print('The village of Eldoria is not far from here, a small haven of life in an otherwise desolate landscape. But life in Eldoria is hard, and you need to find something worthwhile to bring back to the village elder, someone who might exchange it for a few coins or some much-needed supplies.')
print('You adjust your pack and step forward into the ruins, the weight of your decision heavy on your shoulders. As you move deeper, the light dims, and an eerie silence envelops you.')

#Choice 1
print('What will you do?)')

print('     1) Move forward')
print('     2) Hesitate')

answerOne = int(input('Enter your answer (1-2): '))

while answerOne != 1 and answerOne != 2:
    answerOne = int(input('Wrong input, please try again (1-2)'))
if answerOne == 1:
    print('You walk cautiously forward, the ground crunching beneath your boots. The ruins seem to stretch endlessly, each turn revealing more of the same decayed architecture. You keep your eyes peeled for anything that might stand out.')
if answerOne == 2:
    print('You stand there in fear...however the wind pushes you forward. This leads you to looking around your surroundings cautiously.')

#Choice 2
print('As you look around, what do you decide to do?')

print('      1) Inspect surroundings')
print('      2) Yell "Who is there!"')

answerTwo = int(input('Enter your answer(1-2): '))

while answerTwo != 1 and answerTwo != 2:
    answerTwo = int(input('Wrong input, please try again (1-2)'))
if answerTwo == 1:
    print('You take a moment to closely examine the area around you. Broken pillars, shattered tiles, and remnants of ancient machines are scattered everywhere. Among the rubble, something glints in the dim light, partially buried under a layer of dust and debris.')
if answerTwo == 2:
    print('You scream at the top of your lungs. Then, suddenly, you see an object glint in the dim light, partially buried under a layer of dust and debris.')

#Choice 3
print('Staring at the bright object, you make a choice to...')

print('      1) Pick up the object')
print('      2) Wait for the object to do something')

answerThree = int(input('Enter your answer(1-2): '))

while answerThree != 1 and answerThree != 2:
    answerThree = int(input('Wrong input, please try again (1-2)'))
if answerThree == 1:
    print('You reach down and brush away the dirt, revealing a small, intricately designed artifact. It hums softly at your touch, a faint blue light emanating from its core. As you hold it up, the artifact suddenly activates, projecting a holographic image into the air.')
if answerThree == 2:
    print('As you stare at the object, the object gets brighter. You try to resiste the urge to pick it up, but it makes you pick up the object instead. This reveals a small, intricately designed artifact. It hums softly at your touch, a faint blue light emanating from its core. As you hold it up, the artifact suddenly activates, projecting a holographic image into the air.')

#The Holographic Message
print('[Holographic Message]')
print('"Greetings, seeker. If you have found this message, then you hold a fragment of the Ancients legacy. Our world faces a great danger, and only by unlocking the power within this artifact can salvation be found. Seek out the five ancient temples, for within them lies the key to our survival. Beware, for others will seek this power for themselves. The fate of the world rests in your hands.')
print("The hologram fades, leaving you in stunned silence. The artifact's glow dims but continues to pulse gently in your hand. Your heart races as the weight of the message sinks in.")

#Return to Eldoria
print('Return to Eldoria?')
print('       1) Yes')
Eldoria = int(input('Enter your answer(1): '))
while Eldoria != 1:
    Eldoria = int(input('Wrong input, please try again (1)'))
if Eldoria == 1:
    print('With the artifact safely tucked into your pack, you make your way back to Eldoria. Your mind is a whirlwind of thoughts and questions. What is this danger? Who were the Ancients? And why were you the one to find this artifact?')
    print('As the village comes into view, you know one thing for certain: your life has just changed forever, and a journey of great significance lies ahead.')

#End of Prologue

print('You have returned to Eldoria with the mysterious artifact. Seek out the village elder to learn more about your next steps.')