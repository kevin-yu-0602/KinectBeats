from psonic import *

tick = Message()

speed_mult = 1

drum_preset = 1
bass_preset = 1
synth_preset = 3

key_adjust = -2

@in_thread
def metronom():
	while True:
		tick.cue()
		sleep(2 / speed_mult)

@in_thread
def drum_preset1():
	while drum_preset == 1:
		tick.sync()
		sample(DRUM_HEAVY_KICK)
		sample(DRUM_CYMBAL_CLOSED, amp = 0.5)
		sleep(0.25 / speed_mult)
		sample(DRUM_CYMBAL_CLOSED, amp = 0.5)
		sleep(0.25 / speed_mult)
		sample(DRUM_HEAVY_KICK)
		sample(DRUM_CYMBAL_CLOSED, amp = 0.5)
		sample(DRUM_SNARE_HARD)
		sleep(0.25 / speed_mult)
		sample(DRUM_CYMBAL_CLOSED, amp = 0.5)
		sleep(0.25 / speed_mult)
		sample(DRUM_HEAVY_KICK)
		sample(DRUM_CYMBAL_CLOSED, amp = 0.5)
		sleep(0.25 / speed_mult)
		sample(DRUM_HEAVY_KICK)
		sample(DRUM_CYMBAL_CLOSED, amp = 0.5)
		sleep(0.25 / speed_mult)
		sample(DRUM_HEAVY_KICK)
		sample(DRUM_CYMBAL_CLOSED, amp = 0.5)
		sample(DRUM_SNARE_HARD)
		sleep(0.25 / speed_mult)
		sample(DRUM_CYMBAL_OPEN, amp = 0.5, sustain = 0.25 / speed_mult)

@in_thread
def drum_preset2():
	while drum_preset == 2:
		tick.sync()
		sample(BD_ZUM, amp = 2)
		sleep(0.5 / speed_mult)
		sample(BD_ZUM, amp = 2)
		sample(ELEC_HI_SNARE, amp = 1.25)
		sleep(0.5 / speed_mult)
		sample(BD_ZUM, amp = 2)
		sleep(0.5 / speed_mult)
		sample(BD_ZUM, amp = 2)
		sample(ELEC_HI_SNARE, amp = 1.25)

@in_thread
def drum_preset3():
	while drum_preset == 3:
		tick.sync()
		sample(DRUM_HEAVY_KICK)
		sample(DRUM_TOM_LO_HARD)
		sleep(0.5 / speed_mult)
		sample(DRUM_HEAVY_KICK)
		sample(DRUM_TOM_LO_HARD)
		sleep(0.25 / speed_mult)
		sample(DRUM_TOM_HI_HARD)
		sleep(0.25 / speed_mult)
		sample(DRUM_HEAVY_KICK)
		sample(DRUM_TOM_LO_HARD)
		sleep(0.25 / speed_mult)
		sample(DRUM_TOM_MID_HARD)
		sleep(0.25 / speed_mult)
		sample(DRUM_HEAVY_KICK)
		sample(DRUM_TOM_LO_HARD)

@in_thread
def bass_preset1():
	while bass_preset == 1:
		tick.sync()
		use_synth(SAW)
		play(45 + key_adjust, amp = 2, sustain = 0.25 / speed_mult)
		sleep(0.5 / speed_mult)
		play(45 + key_adjust, amp = 2, sustain = 0.25 / speed_mult)
		sleep(0.5 / speed_mult)
		play(45 + key_adjust, amp = 2, sustain = 0.25 / speed_mult)
		sleep(0.5 / speed_mult)
		play(45 + key_adjust, amp = 2, sustain = 0.25 / speed_mult)

@in_thread
def bass_preset2():
	while bass_preset == 2:
		tick.sync()
		use_synth(ZAWA)
		play(43 + key_adjust, amp = 2, sustain = 0.125 / speed_mult)
		sleep(0.25 / speed_mult)
		play(45 + key_adjust, amp = 2, sustain = 0.125 / speed_mult)
		sleep(0.5 / speed_mult)
		play(45 + key_adjust, amp = 2, sustain = 0.125 / speed_mult)
		sleep(0.5 / speed_mult)
		play(45 + key_adjust, amp = 2, sustain = 0.125 / speed_mult)
		sleep(0.5 / speed_mult)
		play(45 + key_adjust, amp = 2, sustain = 0.125 / speed_mult)

@in_thread
def bass_preset3():
	while bass_preset == 3:
		tick.sync()
		use_synth(DPULSE)
		play(45 + key_adjust, amp = 2, sustain = 0.25 / speed_mult)
		play(44 + key_adjust, amp = 2, sustain = 0.5 / speed_mult)
		play(37 + key_adjust, amp = 2, sustain = 1.25 / speed_mult)


@in_thread
def synth_preset1():
	while synth_preset == 1:
		tick.sync()
		play(69 + key_adjust, amp = 1.5)
		sleep(0.75)
		play(68 + key_adjust, amp = 1.5)
		sleep(0.75)
		play(61 + key_adjust, amp = 1.5)


@in_thread
def synth_preset2():
	while synth_preset == 2:
		tick.sync()
		play(69 + key_adjust, amp = 1.5, sustain = 0.125 / speed_mult)
		sleep(0.25 / speed_mult)
		play(62 + key_adjust, amp = 1.5, sustain = 0.125 / speed_mult)
		sleep(0.25 / speed_mult)
		play(62 + key_adjust, amp = 1.5, sustain = 0.125 / speed_mult)
		sleep(0.25 / speed_mult)
		play(69 + key_adjust, amp = 1.5, sustain = 0.125 / speed_mult)
		sleep(0.25 / speed_mult)
		play(62 + key_adjust, amp = 1.5, sustain = 0.125 / speed_mult)
		sleep(0.25 / speed_mult)
		play(62 + key_adjust, amp = 1.5, sustain = 0.125 / speed_mult)
		sleep(0.25 / speed_mult)
		play(70 + key_adjust, amp = 1.5, sustain = 0.125 / speed_mult)
		sleep(0.25 / speed_mult)
		play(62 + key_adjust, amp = 1.5, sustain = 0.125 / speed_mult)


@in_thread
def synth_preset3():
	while synth_preset == 3:
		tick.sync()
		play(69 + key_adjust, amp = 1.5, sustain = 0.125 / speed_mult)
		sleep(0.5 / speed_mult)
		play(71 + key_adjust, amp = 1.5, sustain = 0.125 / speed_mult)
		sleep(0.5 / speed_mult)
		play(69 + key_adjust, amp = 1.5, sustain = 0.125 / speed_mult)
		sleep(0.5 / speed_mult)
		play(64 + key_adjust, amp = 1.5, sustain = 0.125 / speed_mult)
		sleep(0.25 / speed_mult)
		play(69 + key_adjust, amp = 1.5, sustain = 0.125 / speed_mult)


if __name__ == '__main__':
	speed_mult = float(input())
	metronom()
	synth_preset = int(input())
	drum_preset1()
	drum_preset2()
	drum_preset3()
	bass_preset1()
	bass_preset2()
	bass_preset3()
	synth_preset1()
	synth_preset2()
	synth_preset3()