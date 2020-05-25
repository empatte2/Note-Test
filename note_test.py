#modules
import random
import time
import math
import numpy
import pyaudio

## FUNCTIONS ##
#defining sine wave
def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)

def generate_note_data(octaves, noteList,noteFreq):
    octPick = random.randint(octaves[0],octaves[1]) # gen the note's octave
    notePick = random.choice(noteList) # gen the note
    frequency = noteFreq[notePick][octPick] # this is the freq in Hz
    return octPick, notePick, frequency;


def note_options(noteList, notePick):
    #Returns M/C options for the answer
    #print(notePick)
    noteList.remove(notePick) #remove right answer
    options = noteList
    options = random.sample(set(options), 3) # pick 3 remaining wrong answers
    sel = options.insert(3,notePick) #combine those 3 and add back right answer
    random.shuffle(options) #mix those guys up
    print(options)
    return options

def check_ans(noteList, notePick):
    print('Here are your options: (R for replay)')
    options = note_options(noteList, notePick)
    answer = input('Pick an Answer: ').upper()
    loop = 1
    while (loop):
        if answer == notePick:
            print('Nice!')
            global points
            points = points +1
            break
        elif answer == 'R':
            print('Playing again...')
            play_tone(stream, noteList, frequency)
        elif answer != notePick and (answer in options):
            print('wrong')
            loop = 0
        else:
            print('oops you input something incorrectly, try again')
            answer = input('Pick an Answer: ').upper()

def play_tone(stream, noteList, frequency, length=1, rate=44100):
    ## this just plays the sound
    chunks = [] #init this guy
    chunks.append(sine(frequency, length, rate)) # add sine funciton
    chunk = numpy.concatenate(chunks) * 0.25 # add to chunks
    stream.write(chunk.astype(numpy.float32).tostring()) # modify the stream aka play sound
    #reset the stream boy
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1, rate=44100, output=1)

## THE CODEY BIT
# dict of frequencies
noteList = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'] # all the notes
# C = [C0, C1, C2, C3, C4, C5, C6, C7, C8]
#humans cannot really hear the 0th octave and you'll probably have trouble with
#   the 1st as well but the option is fun
noteFreq = {
    'C': [16.35, 32.70, 65.41,  130.81, 261.63, 523.35, 1046.50, 2093.00, 4186.01],
    'C#':[17.32, 34.65, 69.30,  138.59, 277.18, 554.37, 1108.73, 2217.46, 4434.92],
    'D': [18.35, 36.71, 73.42,  146.83, 293.66, 587.33, 1174.66, 2349.32, 4698.63],
    'D#':[19.45, 38.89, 77.78,  155.56, 311.13, 622.25, 1244.51, 2489.02, 4978.03],
    'E': [20.60, 41.20, 81.41,  164.81, 329.63, 659.25, 1318.51, 2637.02, 5274.04],
    'F': [21.83, 43.65, 87.31,  174.61, 349.23, 698.46, 1396.91, 2793.83, 5587.65],
    'F#':[23.12, 46.25, 92.50,  185.00, 369.99, 739.99, 1479.98, 2959.96, 5919.91],
    'G': [24.50, 49.00, 98.00,  196.00, 392.00, 783.99, 1567.98, 3135.96, 6271.93],
    'G#':[25.96, 51.91, 103.83, 207.65, 415.30, 830.61, 1661.22, 3322.44, 6644.88],
    'A': [27.50, 55.00, 110.00, 220.00, 440.00, 880.00, 1760.00, 3520.00, 7040.00],
    'A#':[29.14, 58.27, 116.54, 233.08, 466.16, 932.33, 1864.66, 3729.31, 7458.62],
    'B': [30.87, 61.74, 123.47, 246.94, 493.88, 987.77, 1975.53, 3951.07, 7902.13]
}

#asks if you want more than one octave, makes lowercase
oneOct = input('Would you like more than one octave? (y/n): ').lower()
# initializes empty array, 2 long
octaves = [0]*2

#decide octave choices
if oneOct == 'n':
    # you only want one, so pick it
    octaves[0] = int(input('What Octave do you want? [0-8] (4 is middle): '))
    octaves[1] = octaves[0]
elif oneOct == 'y':
    # you want two, pick them
    octaves[0] = int(input('What is the starting Octave? [0-8]: '))
    octaves[1] = int(input('What is the ending Octave? [0-8]: '))

# init the stream boy
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1, rate=44100, output=1)

numRounds = int(input('How many rounds do you want to play? '))
points = 0

for x in range(numRounds):
    octPick, notePick, frequency = generate_note_data(octaves, noteList, noteFreq)
    play_tone(stream, noteList, frequency)
    check_ans(noteList, notePick)

print('You scored ', points, '/', numRounds)

#close audio stream
stream.close()
p.terminate()
