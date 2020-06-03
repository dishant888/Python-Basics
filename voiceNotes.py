from AssistantModule import Recognize, Speak, Greet

Greet()

Speak('Welcome! Add note, Show note or exit.')
choice = Recognize().lower()

while choice != 'exit':

    if choice == 'add':
        file = open('files/voiceNotes.txt', 'w')
        Speak('What should I add ?')
        note = Recognize()
        print(f'Input: {note}')
        file.write(note)
        Speak('Successfully added!')

    if choice == 'show':
        note = file = open('files/voiceNotes.txt', 'r')
        Speak(file.read())

    Speak('Add note, Show note or exit')
    choice = Recognize().lower()
else:
    Speak('Thank you ! have a good day.')
