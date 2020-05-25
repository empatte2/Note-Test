#modules
import random
import time
import math
import numpy
import pyaudio

#database
Octave = {
    "Cl":["Cl", 261.63],
    "C#/d": ["C#/d", 277.18],
    "D": ["D", 293.66],
    "D#/e": ["D#/e", 311.13],
    "E": ["E", 329.63],
    "F": ["F", 349.23],
    "F#/g": ["F#/g", 269.99],
    "G": ["G", 392.00],
    "G#/a": ["G#/a", 415.30],
    "A": ["A", 440.00],
    "A#/b": ["A#/b", 466.16],
    "B": ["B", 493.88],
    "Ch": ["Ch", 523.25],
    }

#defining sine wave
def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)




#names of notes
options = ["Cl","C#/d","D","D#/e","E","F","F#/g","G","G#/a","A","A#/b","B","Ch"]


score = 0

#responses
gj = "Good Job!"
s = "sorry"


print ("ready")
time.sleep(1)
print ("set")
time.sleep(1)
print("begin")
time.sleep(1)

y = 'y'

while y == 'y':
    try:
        a = None
        while a is None:
            try:
                a = int(input("How many rounds would you like to play?: "))
            except ValueError:
                print("Not an integer value...")
        for x in range(a) :
            print ("round", x)
            print("Here is your note:")
            time.sleep(2)
            i = random.random()
            play_again = 'y'
            if i<= (1/13):
                options = ["Cl","C#/d","D","D#/e","E","F","F#/g","G","G#/a","A","A#/b","B","Ch"]
                options.remove(Octave["Cl"][0])
                options = random.sample(set(options), 3)
                sel = options.insert(3,Octave["Cl"][0])
                random.shuffle(options)
                print (options)
                while play_again == 'y':
                    #play Octave["Cl"][1]
                    def play_tone(stream, frequency=Octave["Cl"][1], length=1, rate=44100):
                        chunks = []
                        chunks.append(sine(frequency, length, rate))

                        chunk = numpy.concatenate(chunks) * 0.25

                        stream.write(chunk.astype(numpy.float32).tostring())

                    p = pyaudio.PyAudio()
                    stream = p.open(format=pyaudio.paFloat32,
                                    channels=1, rate=44100, output=1)

                    play_tone(stream)

                    stream.close()
                    p.terminate()
                    play_again = input('Play note again? (y/n)')

                ans = input('Pick the right note!: ')
                ans = ans.lower()
                time.sleep(1)
                if ans == "cl":
                    score = score + 1
                    print (gj)
                else:
                    print (s)
                print ('it was Cl')
                play_again = "y"
                time.sleep(1)
                print ("Score: ", score)
                time.sleep(1)

            elif i>= (1/13) and i<= (2/13):
                options = ["Cl","C#/d","D","D#/e","E","F","F#/g","G","G#/a","A","A#/b","B","Ch"]
                options.remove(Octave["C#/d"][0])
                options = random.sample(set(options), 3)
                sel = options.insert(3,Octave["C#/d"][0])
                random.shuffle(options)
                print (options)
                while play_again == 'y':
                    #play Octave["C#/d"][1]
                    def play_tone(stream, frequency=Octave["C#/d"][1], length=1, rate=44100):
                        chunks = []
                        chunks.append(sine(frequency, length, rate))

                        chunk = numpy.concatenate(chunks) * 0.25

                        stream.write(chunk.astype(numpy.float32).tostring())

                    p = pyaudio.PyAudio()
                    stream = p.open(format=pyaudio.paFloat32,
                                    channels=1, rate=44100, output=1)

                    play_tone(stream)

                    stream.close()
                    p.terminate()
                    play_again = input('Play note again? (y/n)')

                ans = input('Pick the right note!: ')
                ans = ans.lower()
                time.sleep(1)
                if ans == "c#/d":
                    score = score + 1
                    print (gj)
                else:
                    print (s)

                print ('it was C#/d')
                time.sleep(1)
                print ("Score: ", score)
                time.sleep(1)

            elif i>= (2/13) and i<= (3/13):
                options = ["Cl","C#/d","D","D#/e","E","F","F#/g","G","G#/a","A","A#/b","B","Ch"]
                options.remove(Octave["D"][0])
                options = random.sample(set(options), 3)
                sel = options.insert(3,Octave["D"][0])
                random.shuffle(options)
                print (options)
                while play_again == 'y':
                    #play Octave["D"][1]
                    def play_tone(stream, frequency=Octave["D"][1], length=1, rate=44100):
                        chunks = []
                        chunks.append(sine(frequency, length, rate))

                        chunk = numpy.concatenate(chunks) * 0.25

                        stream.write(chunk.astype(numpy.float32).tostring())

                    p = pyaudio.PyAudio()
                    stream = p.open(format=pyaudio.paFloat32,
                                    channels=1, rate=44100, output=1)

                    play_tone(stream)

                    stream.close()
                    p.terminate()
                    play_again = input('Play note again? (y/n)')

                ans = input('Pick the right note!: ')
                ans = ans.lower()
                time.sleep(1)
                if ans == "d":
                    score = score + 1
                    print (gj)
                else:
                    print (s)

                print ('it was D')
                time.sleep(1)
                print ("Score: ", score)
                time.sleep(1)

            elif i>= (3/13) and i<= (4/13):
                options = ["Cl","C#/d","D","D#/e","E","F","F#/g","G","G#/a","A","A#/b","B","Ch"]
                options.remove(Octave["D#/e"][0])
                options = random.sample(set(options), 3)
                sel = options.insert(3,Octave["D#/e"][0])
                random.shuffle(options)
                print (options)
                while play_again == 'y':
                    #play Octave["D#/e"][1]
                    def play_tone(stream, frequency=Octave["D#/e"][1], length=1, rate=44100):
                        chunks = []
                        chunks.append(sine(frequency, length, rate))

                        chunk = numpy.concatenate(chunks) * 0.25

                        stream.write(chunk.astype(numpy.float32).tostring())

                    p = pyaudio.PyAudio()
                    stream = p.open(format=pyaudio.paFloat32,
                                    channels=1, rate=44100, output=1)

                    play_tone(stream)

                    stream.close()
                    p.terminate()
                    play_again = input('Play note again? (y/n)')

                ans = input('Pick the right note!: ')
                ans = ans.lower()
                time.sleep(1)
                if ans == "d#/e":
                    score = score + 1
                    print (gj)
                else:
                    print (s)

                print ('it was D#/e')
                time.sleep(1)
                print ("Score: ", score)
                time.sleep(1)

            elif i>= (4/13) and i<= (5/13):
                options = ["Cl","C#/d","D","D#/e","E","F","F#/g","G","G#/a","A","A#/b","B","Ch"]
                options.remove(Octave["E"][0])
                options = random.sample(set(options), 3)
                sel = options.insert(3,Octave["E"][0])
                random.shuffle(options)
                print (options)
                while play_again == 'y':
                    #play Octave["E"][1]
                    def play_tone(stream, frequency=Octave["E"][1], length=1, rate=44100):
                        chunks = []
                        chunks.append(sine(frequency, length, rate))

                        chunk = numpy.concatenate(chunks) * 0.25

                        stream.write(chunk.astype(numpy.float32).tostring())

                    p = pyaudio.PyAudio()
                    stream = p.open(format=pyaudio.paFloat32,
                                    channels=1, rate=44100, output=1)

                    play_tone(stream)

                    stream.close()
                    p.terminate()
                    play_again = input('Play note again? (y/n)')

                ans = input('Pick the right note!: ')
                ans = ans.lower()
                time.sleep(1)
                if ans == "e":
                    score = score + 1
                    print (gj)
                else:
                    print (s)

                print ('it was E')
                time.sleep(1)
                print ("Score: ", score)
                time.sleep(1)

            elif i>= (5/13) and i<= (6/13):
                options = ["Cl","C#/d","D","D#/e","E","F","F#/g","G","G#/a","A","A#/b","B","Ch"]
                options.remove(Octave["F"][0])
                options = random.sample(set(options), 3)
                sel = options.insert(3,Octave["F"][0])
                random.shuffle(options)
                print (options)
                while play_again == 'y':
                    #play Octave["F"][1]
                    def play_tone(stream, frequency=Octave["F"][1], length=1, rate=44100):
                        chunks = []
                        chunks.append(sine(frequency, length, rate))

                        chunk = numpy.concatenate(chunks) * 0.25

                        stream.write(chunk.astype(numpy.float32).tostring())

                    p = pyaudio.PyAudio()
                    stream = p.open(format=pyaudio.paFloat32,
                                    channels=1, rate=44100, output=1)

                    play_tone(stream)

                    stream.close()
                    p.terminate()
                    play_again = input('Play note again? (y/n)')

                ans = input('Pick the right note!: ')
                ans = ans.lower()
                time.sleep(1)
                if ans == "f":
                    score = score + 1
                    print (gj)
                else:
                    print (s)

                print ('it was F')
                time.sleep(1)
                print ("Score: ", score)
                time.sleep(1)

            elif i>= (6/13) and i<= (7/13):
                options = ["Cl","C#/d","D","D#/e","E","F","F#/g","G","G#/a","A","A#/b","B","Ch"]
                options.remove(Octave["F#/g"][0])
                options = random.sample(set(options), 3)
                sel = options.insert(3,Octave["F#/g"][0])
                random.shuffle(options)
                print (options)
                while play_again == 'y':
                    #play Octave["F#/g"][1]
                    def play_tone(stream, frequency=Octave["F#/g"][1], length=1, rate=44100):
                        chunks = []
                        chunks.append(sine(frequency, length, rate))

                        chunk = numpy.concatenate(chunks) * 0.25

                        stream.write(chunk.astype(numpy.float32).tostring())

                    p = pyaudio.PyAudio()
                    stream = p.open(format=pyaudio.paFloat32,
                                    channels=1, rate=44100, output=1)

                    play_tone(stream)

                    stream.close()
                    p.terminate()
                    play_again = input('Play note again? (y/n)')

                ans = input('Pick the right note!: ')
                ans = ans.lower()
                time.sleep(1)
                if ans == "f#/g":
                    score = score + 1
                    print (gj)
                else:
                    print (s)

                print ('it was F#/g')
                time.sleep(1)
                print ("Score: ", score)
                time.sleep(1)

            elif i>= (7/13) and i<= (8/13):
                options = ["Cl","C#/d","D","D#/e","E","F","F#/g","G","G#/a","A","A#/b","B","Ch"]
                options.remove(Octave["G"][0])
                options = random.sample(set(options), 3)
                sel = options.insert(3,Octave["G"][0])
                random.shuffle(options)
                print (options)
                while play_again == 'y':
                    #play Octave["G"][1]
                    def play_tone(stream, frequency=Octave["G"][1], length=1, rate=44100):
                        chunks = []
                        chunks.append(sine(frequency, length, rate))

                        chunk = numpy.concatenate(chunks) * 0.25

                        stream.write(chunk.astype(numpy.float32).tostring())

                    p = pyaudio.PyAudio()
                    stream = p.open(format=pyaudio.paFloat32,
                                    channels=1, rate=44100, output=1)

                    play_tone(stream)

                    stream.close()
                    p.terminate()
                    play_again = input('Play note again? (y/n)')

                ans = input('Pick the right note!: ')
                ans = ans.lower()
                time.sleep(1)
                if ans == "g":
                    score = score + 1
                    print (gj)
                else:
                    print (s)

                print ('it was G')
                time.sleep(1)
                print ("Score: ", score)
                time.sleep(1)

            elif i>= (8/13) and i<= (9/13):
                options = ["Cl","C#/d","D","D#/e","E","F","F#/g","G","G#/a","A","A#/b","B","Ch"]
                options.remove(Octave["G#/a"][0])
                options = random.sample(set(options), 3)
                sel = options.insert(3,Octave["G#/a"][0])
                random.shuffle(options)
                print (options)
                while play_again == 'y':
                    #play Octave["G#/a"][1]
                    def play_tone(stream, frequency=Octave["G#/a"][1], length=1, rate=44100):
                        chunks = []
                        chunks.append(sine(frequency, length, rate))

                        chunk = numpy.concatenate(chunks) * 0.25

                        stream.write(chunk.astype(numpy.float32).tostring())

                    p = pyaudio.PyAudio()
                    stream = p.open(format=pyaudio.paFloat32,
                                    channels=1, rate=44100, output=1)

                    play_tone(stream)

                    stream.close()
                    p.terminate()
                    play_again = input('Play note again? (y/n)')

                ans = input('Pick the right note!: ')
                ans = ans.lower()
                time.sleep(1)
                if ans == "g#/a":
                    score = score + 1
                    print (gj)
                else:
                    print (s)

                print ('it was G#/a')
                time.sleep(1)
                print ("Score: ", score)
                time.sleep(1)

            elif i>= (9/13) and i<= (10/13):
                options = ["Cl","C#/d","D","D#/e","E","F","F#/g","G","G#/a","A","A#/b","B","Ch"]
                options.remove(Octave["A"][0])
                options = random.sample(set(options), 3)
                sel = options.insert(3,Octave["A"][0])
                random.shuffle(options)
                print (options)
                while play_again == 'y':
                    #play Octave["A"][1]
                    def play_tone(stream, frequency=Octave["A"][1], length=1, rate=44100):
                        chunks = []
                        chunks.append(sine(frequency, length, rate))

                        chunk = numpy.concatenate(chunks) * 0.25

                        stream.write(chunk.astype(numpy.float32).tostring())

                    p = pyaudio.PyAudio()
                    stream = p.open(format=pyaudio.paFloat32,
                                    channels=1, rate=44100, output=1)

                    play_tone(stream)

                    stream.close()
                    p.terminate()
                    play_again = input('Play note again? (y/n)')

                ans = input('Pick the right note!: ')
                ans = ans.lower()
                time.sleep(1)
                if ans == "a":
                    score = score + 1
                    print (gj)
                else:
                    print (s)

                print ('it was A')
                time.sleep(1)
                print ("Score: ", score)
                time.sleep(1)

            elif i>= (10/13) and i<= (11/13):
                options = ["Cl","C#/d","D","D#/e","E","F","F#/g","G","G#/a","A","A#/b","B","Ch"]
                options.remove(Octave["A#/b"][0])
                options = random.sample(set(options), 3)
                sel = options.insert(3,Octave["A#/b"][0])
                random.shuffle(options)
                print (options)
                while play_again == 'y':
                    #play Octave["A#/b"][1]
                    def play_tone(stream, frequency=Octave["A#/b"][1], length=1, rate=44100):
                        chunks = []
                        chunks.append(sine(frequency, length, rate))

                        chunk = numpy.concatenate(chunks) * 0.25

                        stream.write(chunk.astype(numpy.float32).tostring())

                    p = pyaudio.PyAudio()
                    stream = p.open(format=pyaudio.paFloat32,
                                    channels=1, rate=44100, output=1)

                    play_tone(stream)

                    stream.close()
                    p.terminate()
                    play_again = input('Play note again? (y/n)')

                ans = input('Pick the right note!: ')
                ans = ans.lower()
                time.sleep(1)
                if ans == "a#/b":
                    score = score + 1
                    print (gj)
                else:
                    print (s)

                print ('it was A#/b')
                time.sleep(1)
                print ("Score: ", score)
                time.sleep(1)

            elif i>= (11/13) and i<= (12/13):
                options = ["Cl","C#/d","D","D#/e","E","F","F#/g","G","G#/a","A","A#/b","B","Ch"]
                options.remove(Octave["B"][0])
                options = random.sample(set(options), 3)
                sel = options.insert(3,Octave["B"][0])
                random.shuffle(options)
                print (options)
                while play_again == 'y':
                    #play Octave["B"][1]
                    def play_tone(stream, frequency=Octave["B"][1], length=1, rate=44100):
                        chunks = []
                        chunks.append(sine(frequency, length, rate))

                        chunk = numpy.concatenate(chunks) * 0.25

                        stream.write(chunk.astype(numpy.float32).tostring())

                    p = pyaudio.PyAudio()
                    stream = p.open(format=pyaudio.paFloat32,
                                    channels=1, rate=44100, output=1)

                    play_tone(stream)

                    stream.close()
                    p.terminate()
                    play_again = input('Play note again? (y/n)')

                ans = input('Pick the right note!: ')
                ans = ans.lower()
                time.sleep(1)
                if ans == "b":
                    score = score + 1
                    print (gj)
                else:
                    print (s)

                print ('it was B')
                time.sleep(1)
                print ("Score: ", score)
                time.sleep(1)

            elif i>= (12/13) and i<= (13/13):
                options = ["Cl","C#/d","D","D#/e","E","F","F#/g","G","G#/a","A","A#/b","B","Ch"]
                options.remove(Octave["Ch"][0])
                options = random.sample(set(options), 3)
                sel = options.insert(3,Octave["Ch"][0])
                random.shuffle(options)
                print (options)
                while play_again == 'y':
                    #play Octave["Ch"][1]
                    def play_tone(stream, frequency=Octave["Ch"][1], length=1, rate=44100):
                        chunks = []
                        chunks.append(sine(frequency, length, rate))

                        chunk = numpy.concatenate(chunks) * 0.25

                        stream.write(chunk.astype(numpy.float32).tostring())

                    p = pyaudio.PyAudio()
                    stream = p.open(format=pyaudio.paFloat32,
                                    channels=1, rate=44100, output=1)

                    play_tone(stream)

                    stream.close()
                    p.terminate()
                    play_again = input('Play note again? (y/n)')

                ans = input('Pick the right note!: ')
                ans = ans.lower()
                time.sleep(1)
                if ans == "ch":
                    score = score + 1
                    print (gj)
                else:
                    print (s)

                print ('it was Ch')
                time.sleep(1)
                print ("Score: ", score)
                time.sleep(1)
        score = 0
        y = str(input("would you like to play again [y/n]: "))
    except ValueError:
        print("bye")
