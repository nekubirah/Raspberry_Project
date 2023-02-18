import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
#             0   1   2   3   4   5   6
#             A   B   C   D   E   F   G
abschnitte = [15, 32, 33, 35, 37, 38, 40]
buchstaben = {
        "0": [0, 1, 2, 3, 4, 5],
        "1": [2, 1],
        "2": [0, 1, 6, 4, 3],
        "3": [0, 1, 2, 3, 6],
        "4": [5, 6, 1, 2],
        "5": [0, 5, 6, 2, 3],
        "6": [0, 5, 6, 4, 3, 2],
        "7": [0, 1, 2],
        "8": [0, 1, 2, 3, 4, 5, 6],
        "9": [0, 1, 2, 3, 5, 6],
        "10": [3, 6, 1, 5, 0],
        "A": [0, 1, 2, 4, 5, 6],
        "B": [0, 1, 2, 3, 4, 5, 6],
        "C": [0, 5, 4, 3],
        "D": [0, 1, 2, 3, 4, 5],
        "E": [0, 3, 4, 5, 6],
        "F": [0, 6, 5, 4],
        "U": [5, 4, 3, 2, 1],
        "V": [5, 4, 3, 2, 1]
        }

for abschnitt in abschnitte:
    GPIO.setup(abschnitt, GPIO.OUT)

def testAll():
    for abschnitt in abschnitte:
        GPIO.output(abschnitt, GPIO.HIGH)

def cleanAbschnitte():
    for abschnitt in abschnitte:
        GPIO.output(abschnitt, GPIO.LOW)


def defineChars(tollerChar):
    cleanAbschnitte()
    aktAbschnitte = buchstaben[str(tollerChar)]
    for abschnitt in aktAbschnitte:
        GPIO.output(abschnitte[abschnitt], GPIO.HIGH)


