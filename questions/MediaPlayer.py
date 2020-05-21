# Windows Media Player

from pygame import mixer

mixer.init()
mixer.music.load('../song.mp3')
mixer.music.set_volume(1)
mixer.music.play()
while 1:
    print('Press p to pause')
    print('Press r to resume')
    print('Press e to exit')
    choice = input()

    if choice == 'p':
        mixer.music.pause()
    elif choice == 'r':
        mixer.music.unpause()
    elif choice == 'e':
        mixer.music.stop()
        break
    else:
        print('Invalid choice')