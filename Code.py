from adafruit_circuitplayground.express import cpx
import time
#A dictionary of every note from octave 4 to octave 5 along with the frequencies associated with that note name
notes = dict({"C": 262, "C# / Db": 277, "D": 294, "D# / Eb": 311, "E": 330, "F": 349, "F# / Gb": 370, "G": 392,
             "G# / Ab": 415, "A":440, "A# / Bb": 467, "B": 494, "C5": 523, "C#5 / Db5": 554, "D5": 587, "D#5 / Eb5": 622,
             "E5":659, "F5": 698, "F#5 / Gb5": 740, "G5": 785, "G#5 / Ab5": 831, "A5":880, "A#5 / Bb5":932, "B5":988})
#Array of strings with every note name from octave 4 to octave 5
keys = ["C", "C# / Db", "D", "D# / Eb", "E", "F", "F# / Gb", "G", "G# / Ab", "A", "A# / Bb", "B", "C5", "C#5 / Db5",
         "D5", "D#5 / Eb5", "E5", "F5", "F#5 / Gb5", "G5", "G#5 / Ab5", "A5", "A#5 / Bb5", "B5"]

#Original index of notes - standard with this device will be C major, so "do" will be at the index 0 in the keys array - or "C"
d = 0
r = 2
m = 4
f = 5
s = 7
l = 9
t = 11
dd = 12

while True:
    if cpx.switch: #This prevents the device from constantly being "on" and getting annoying
        print("Slide switch off!")
        cpx.pixels.fill((0, 0, 0))
        cpx.stop_tone()
        continue
    if cpx.button_a and d<11: #If do is in octave 4 and button a is pressed, every note is moved up one halfstep to change keys
        d = d+1
        r = r+1
        m = m +1
        f = f+1
        s = s+1
        l = l +1
        t = t + 1
        dd = dd +1
        print("You are in the key of " + keys[d] + "!")
        time.sleep(0.5)
    if cpx.button_a and d>=11: #If this button is pressed, but do will no longer be in 4th octave, the key goes back to C
        d = 0
        r = 2
        m = 4
        f = 5
        s = 7
        l = 9
        t = 11
        dd = 12
        print("You are in C major!")
        time.sleep(0.5)
    if cpx.button_b and m - d == 4:
        #If the interval between mi and do is four, the key is major, and from here we will decrease the index of the 3rd 6th
        #and 7th to be in natural minor
        m = m-1
        l = l-1
        t = t-1
        print("You are in " + keys[d] + " Natural Minor")
        time.sleep(0.5)
    if cpx.button_b and m - d == 3 and l-s ==1 and dd-t==2: #if the interval between the 1st and 3rd is 3, you have a minor 3rd
    #index between la and so is one, you have flat 6 if the index between the 7th and 8th is 2, you have a flat 7th
    #This is natural minor and from here you will raise the 7th to be harmonic minor
        t = t+1
        print("You are in " + keys[d] + " Harmonic Minor")
        time.sleep(0.5)
    if cpx.button_b and m - d == 3 and l-s == 1 and dd-t==1: #If interval between 1st and 3rd is three: minor 3rd
    #if interval between 6th and 7th is one: flat 6, if interval between 8th and 7th is one, raised 7th
    #This makes it harmonic minor, and from here you raise the 6th to be in melodic minor
        l = l + 1
        print("You are in " + keys[d] + " Melodic Minor")
        time.sleep(0.5)
    if cpx.button_b and m-d == 3 and l-s == 2 and dd-t ==1: #interval of 3 = minor 3rd 6th-5th being 2 semitones = raised 6th
    #8th to 7th being one semitone = raised 7th - melodic minor.  Raise the 3rd to be in major again
        m = m+1
        print("You are in " + keys[d] + " Major")
        time.sleep(0.5)
    if cpx.touch_A4: #A4 is always the 1st scale degree of the key so you play do - whatever index in the keys array that is
        print('Touched ' + keys[d])
        cpx.pixels.fill((15, 0, 0))
        cpx.start_tone(notes[keys[d]])
    elif cpx.touch_A5: #A5 is always the 2nd scale degree of the key so you play re - whatever index in the keys array that is
        print('Touched ' + keys[r])
        cpx.pixels.fill((15, 5, 0))
        cpx.start_tone(notes[keys[r]])
    elif cpx.touch_A6: #A6 is always the 3rd scale degree of the key so you play mi - whatever index in the keys array that is
        print('Touched ' + keys[m])
        cpx.pixels.fill((15, 15, 0))
        cpx.start_tone(notes[keys[m]])
    elif cpx.touch_A7: #A7 is always the 4th scale degree of the key so you play fa - whatever index in the keys array that is
        print('Touched ' + keys[f])
        cpx.pixels.fill((0, 15, 0))
        cpx.start_tone(notes[keys[f]])
    elif cpx.touch_A1: #A1 is always the 5th scale degree of the key so you play so - whatever index in the keys array that is
        print('Touched ' + keys[s])
        cpx.pixels.fill((0, 15, 15))
        cpx.start_tone(notes[keys[s]])
    elif cpx.touch_A2 and not cpx.touch_A3: #A2 is always the 6th
   # scale degree of the key so you play la - whatever index in the keys array that is
        print('Touched ' + keys[l])
        cpx.pixels.fill((0, 0, 15))
        cpx.start_tone(notes[keys[l]])
    elif cpx.touch_A3 and not cpx.touch_A2: #A3 is always the 7th scale degree
   # of the key so you play ti - whatever index in the keys array that is
        print('Touched ' + keys[t])
        cpx.pixels.fill((5, 0, 15))
        cpx.start_tone(notes[keys[t]])
    elif cpx.touch_A2 and cpx.touch_A3:
        #As there are 8 notes and 7 sensors, 2 and 3 together makes up the octave, playing high do
        #- whatever index of the array
        print('Touched ' + keys[dd])
        cpx.pixels.fill((15, 0, 15))
        cpx.start_tone(notes[keys[dd]])
    else:
        cpx.pixels.fill((0, 0, 0))
        cpx.stop_tone()
    time.sleep(0.05)

