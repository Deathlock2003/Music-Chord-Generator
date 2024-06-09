pip install aubio
pip install pydub
#### FINAL CODE FOR THE MINI PROJECT

import aubio
from pydub import AudioSegment

def audio_to_notes(audio_file):
    audio = AudioSegment.from_mp3(audio_file)
    audio.export("temp.wav", format="wav")

    audio_source = aubio.source("temp.wav", 0, 512)

    pitch_detection = aubio.pitch("yin", 2048, 512, audio_source.samplerate)

    natural_notes= ['C','C#','D','D#','E', 'F','F#','G','G#','A','A#','B']

    notes = []

    while True:
        samples, read = audio_source()
        pitch = pitch_detection(samples)[0]
        confidence = pitch_detection.get_confidence()

        if confidence > 0.965: #0.991
            midi_pitch = int(pitch) % 128
            note = aubio.midi2note(midi_pitch)

            note_without_octave = note[:-1]

            if note_without_octave in natural_notes:
                if note_without_octave not in notes:
                    notes.append(note_without_octave)

        if read < 512:  # Break the loop when the audio ends
            break

    return notes

audio_file = 'Mini.wav'

musical_notes = audio_to_notes(audio_file)

#print("Extracted Natural and Sharp Musical Notes:")
#print(musical_notes)
natural_notes= ['C','C#','D','D#','E', 'F','F#','G','G#','A','A#','B']
notes1 = []
n=[]
for i in range(0,4):
    note1=musical_notes[i]
    for j in range(0,12):
            if note1==natural_notes[j]:
                n.append(j)
#print(n)
for i in range(0,4):
#    note1=musical_notes[i]
#    print(note1)
#    for j in range(0,12):
#        if note1==natural_notes[j]:
#            n==j
#            print(n)
    if i==0:
        b=n[i]
        a=natural_notes[b-5]
        notes1.append(a)
    elif i==1:
        b=n[i]
        a=natural_notes[b-2]
        notes1.append(a)
    elif i==2:
        b=n[i]
        a=natural_notes[b+2]
        notes1.append(a)
    elif i==3:
        b=n[i]
        a=natural_notes[b+1]
        notes1.append(a)
print(notes1)
#print(natural_notes[])
#Final Output Code
from PIL import Image
from IPython.display import display
#print("Enter the no. of notes (4):", end="")
#n = int(input())

#print("Enter the notes (4):", end="")
#s = input()

note = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
chord = [[1,5,8],
         [1,4,8],
         [2,6,9],
         [2,5,9],
         [3,7,10],
         [3,6,10],
         [4,8,11],
         [4,7,11],
         [5,9,12],
         [5,8,12],
         [6,10,1],
         [6,9,1],
         [7,11,2],
         [7,10,2],
         [8,12,3],
         [8,11,3],
         [9,1,4],
         [9,12,4],
         [10,2,5],
         [10,1,5],
         [11,3,6],
         [11,2,6],
         [12,4,7],
         [12,3,7]]

num = []
for i in range(len(notes1)):
    for j in range(12):
        if notes1[i] == note[j]:
            num.append(j + 1)
            break
#print(num)
#c=0
for j in range(6):
    c = 0
    for k in range(3):
        if chord[j][k] in num:
            c += 1
#    print(c)
    if c >= 2:
        if chord[j] == [1, 5, 8]:
            print("C\n(C E G)")
            #print("C major")
            img = Image.open('Cmajor.jpeg')
            img1 = Image.open('Cmajor1.jpeg')
            img2 = Image.open('Cmajor2.jpeg')
            display(img,img1,img2)
        elif chord[j] == [1, 4, 8]:
            print("Cm\n(C D# G)")
            img = Image.open('Cminor.jpeg')
            img1 = Image.open('Cminor1.jpeg')
            img2 = Image.open('Cminor2.jpeg')
            display(img,img1,img2)
        elif chord[j] == [2, 6, 9]:
            print("C#\n(C# F G#)")
            #print("C# major")
            img = Image.open('C#major.jpeg')
            display(img)
        elif chord[j] == [2, 5, 9]:
            print("C#m\n(C# E G#)")
            img = Image.open('C#minor.jpeg')
            display(img)
        elif chord[j] == [3, 7, 10]:
            print("D\n")
            img = Image.open('Dmajor.jpeg')
            display(img)
        elif chord[j] == [3, 6, 10]:
            print("Dm\n")
            img = Image.open('Dminor.jpeg')
            display(img)
        elif chord[j] == [4, 8, 11]:
            print("D#\n")
            img = Image.open('D#major.jpeg')
            display(img)
        elif chord[j] == [4, 7, 11]:
            print("D#m\n")
            img = Image.open('D#minor.jpeg')
            display(img)
        elif chord[j] == [5, 9, 12]:
            print("E\n")
            img = Image.open('Emajor.jpeg')
            display(img)
        elif chord[j] == [5, 8, 12]:
            print("Em\n")
            img = Image.open('Eminor.jpeg')
            display(img)
        elif chord[j] == [6, 10, 1]:
            print("F\n")
            img = Image.open('Fmajor.jpeg')
            display(img)
        elif chord[j] == [6, 9, 1]:
            print("Fm\n")
            img = Image.open('Fminor.jpeg')
            display(img)
        elif chord[j] == [7, 11, 2]:
            print("F#\n")
            img = Image.open('F#major.jpeg')
            display(img)
        elif chord[j] == [7, 10, 2]:
            print("F#m\n")
            img = Image.open('F#minor.jpeg')
            display(img)
        elif chord[j] == [8, 12, 3]:
            print("G\n")
            img = Image.open('Gmajor.jpeg')
            display(img)
        elif chord[j] == [8, 11, 3]:
            print("Gm\n")
            img = Image.open('Gminor.jpeg')
            display(img)
        elif chord[j] == [9, 1, 4]:
            print("G#\n")
            img = Image.open('G#major.jpeg')
            display(img)
        elif chord[j] == [9, 12, 4]:
            print("G#m\n")
            img = Image.open('G#minor.jpeg')
            display(img)
        elif chord[j] == [10, 2, 5]:
            print("A\n")
            img = Image.open('Amajor.jpeg')
            display(img)
        elif chord[j] == [10, 1, 5]:
            print("Am\n")
            img = Image.open('Aminor.jpeg')
            display(img)
        elif chord[j] == [11, 3, 6]:
            print("A#\n")
            img = Image.open('A#major.jpeg')
            display(img)
        elif chord[j] == [11, 2, 6]:
            print("A#m\n")
            img = Image.open('A#minor.jpeg')
            display(img)
        elif chord[j] == [12, 4, 7]:
            print("B\n(B D# F#)")
            img = Image.open('Bmajor.jpeg')
            display(img)
        elif chord[j] == [12, 3, 7]:
            print("Bm\n")
            img = Image.open('Bminor.jpeg')
            display(img)
        break


