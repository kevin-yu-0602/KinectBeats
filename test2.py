from psonic import *

tick = Message()
threads = []

@in_thread
def bass1():
    sample(DRUM_HEAVY_KICK)

def snare1():
    sample(DRUM_SNARE_SOFT)

def cymbal1():
    sample(DRUM_CYMBAL_CLOSED)



@in_thread
def metronom():
    while True:
        tick.cue()
        sleep(4)

@in_thread
def instrument1():
    # while True:
    tick.sync()
    sleep(1)

@in_thread
def instrument2():
    tick.sync()
    sample(DRUM_HEAVY_KICK)
    sleep(1.25)
    sample(DRUM_HEAVY_KICK)
    sleep(0.375)
    sample(DRUM_HEAVY_KICK)
    sleep(0.375)
    sample(DRUM_HEAVY_KICK)
    sleep(1.25)
    sample(DRUM_HEAVY_KICK)
    sleep(0.375)
    sample(DRUM_HEAVY_KICK)


@in_thread
def instrument3():
    # while True:
    tick.sync()
    sample(BASS_HARD_C)

@in_thread
def instrument4():
    tick.sync()
    sleep(0.5)
    sample(DRUM_SNARE_SOFT)
    sleep(1)
    sample(DRUM_SNARE_SOFT)
    sleep(1)
    sample(DRUM_SNARE_SOFT)
    sleep(1)
    sample(DRUM_SNARE_SOFT)

@in_thread
def instrument5():
    tick.sync()
    sample(DRUM_CYMBAL_CLOSED, amp = 0.25)
    sleep(0.25)
    sample(DRUM_CYMBAL_CLOSED, amp = 0.25)
    sleep(0.25)
    sample(DRUM_CYMBAL_CLOSED, amp = 0.25)
    sleep(0.25)
    sample(DRUM_CYMBAL_CLOSED, amp = 0.25)
    sleep(0.25)
    sample(DRUM_CYMBAL_CLOSED, amp = 0.25)
    sleep(0.25)
    sample(DRUM_CYMBAL_CLOSED, amp = 0.25)
    sleep(0.25)
    sample(DRUM_CYMBAL_CLOSED, amp = 0.25)
    sleep(0.25)
    sample(DRUM_CYMBAL_CLOSED, amp = 0.25)

@in_thread
def melody1():
    tick.sync()
    play(A4)
    sleep(0.75)
    play(Ab4)
    sleep(0.75)
    play(Db4)



@in_thread
def play_instruments():
    while True:
        tick.sync()
        for thread in threads:
            thread()

metronom()
play_instruments()


while True:
    print(threads)
    gesture = int(input())
    if gesture == 1:
        threads.append(instrument1)
    elif gesture == 2:
        threads.append(instrument2)
    elif gesture == 3:
        threads.append(instrument3)
    elif gesture == 4:
        threads.append(instrument4)
    elif gesture == 5:
        threads.append(instrument5)
    elif gesture == 7:
        threads.append(melody1)
    elif gesture == 8:
        bass1()
    elif gesture == 9:
        snare1()
    elif gesture == 6:
        threads.pop()