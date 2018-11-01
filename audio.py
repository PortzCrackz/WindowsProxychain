import playsound

def music():
    playsound.playsound('audio.mp3',True)
    music()
music()
