from psonic import *

tick = Message()
threads = []
params = []
idx = 0

@in_thread
def metronom():
    while True:
        tick.cue()
        sleep(1)

@in_thread
def instrument1():
    while True:
        tick.sync()
        sleep(1)

@in_thread
def instrument2():
    tick.sync()
    sample(DRUM_HEAVY_KICK)

@in_thread
def instrument3():
    while True:
        tick.sync()
        sample(BASS_HARD_C)

@in_thread
def instrument4():
    tick.sync()
    sleep(0.5)
    sample(DRUM_SNARE_HARD)

@in_thread
def instrument5():
    tick.sync()
    sample(DRUM_CYMBAL_CLOSED)
    sleep(0.25)
    sample(DRUM_CYMBAL_CLOSED)
    sleep(0.25)
    sample(DRUM_CYMBAL_CLOSED)
    sleep(0.25)
    sample(DRUM_CYMBAL_CLOSED)

@in_thread
def playLoop():
    tick.sync()
    instrument, n, start = params[idx]
    print(params[idx])
    sleep(start)
    sample(instrument)
    for i in range(n-1):
        sleep(1/n)
        sample(instrument)
            

@in_thread
def play_instruments():
    global idx
    while True:
        tick.sync()
        for i in range(len(threads)):
            idx = i
            print(idx)
            threads[i]()

metronom()
play_instruments()


while True:
    # print(threads)
    # print(params)
    gesture = int(input()), float(input())
    threads.append(playLoop)
    params.append((DRUM_HEAVY_KICK, gesture[0], gesture[1]))
    # print("threads", threads)
    # print("params", params)
    # if gesture == 1:
    #     threads.append(instrument1)
    # elif gesture == 2:
    #     threads.append(instrument2)
    # elif gesture == 3:
    #     threads.append(instrument3)
    # elif gesture == 4:
    #     threads.append(instrument4)
    # elif gesture == 5:
    #     threads.append(instrument5)
    # elif gesture == 6:
    #     threads.pop()