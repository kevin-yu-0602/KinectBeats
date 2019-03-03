from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
from psonic import *
from pygame.locals import *

from Instructions import *
import ctypes
import _ctypes
import pygame
import sys
import math

if sys.hexversion >= 0x03000000:
    import _thread as thread
else:
    import thread

WAVE_ACCENTUATION = 100
WAVE_SEGMENTS_REQUIRED = 4
POST_WAVE_DELAY = 150   
MAX_WAVE_FRAME_WAIT = 60
MVT_THRESHOLD = 18
POST_NOTE_DELAY = 10
PITCH_ADJ_DELAY = 15
CONFIRM_DELAY = 10

# Set pitch bounds here, feel free to add more bounds
# Lower number means higher by Kinect coordinate plane
HIGHEST = -25
MID_HIGH = -15
MEDIUM = 0
MID_LOW = 15
LOW = 25

# Thresholds for preset selection
FIRST_PRESET = -15
SECOND_PRESET = 15

MODE = {"baseline":0, "drum":1, "synth":2}

# Options for presets for each mode
LOOP_PRESETS = [["LO-FI", "ZAWA", "SCI-FI"],["UPBEAT", "GROOVY", "HEAVY"],["DREAMY", "SPOOKY", "UPLIFTING"]]
PRESET_COLORS = [[pygame.Color(249, 215, 59, 150), pygame.Color(242, 144, 46, 150), pygame.Color(242, 80, 62, 150)],
[pygame.Color(25, 214, 204, 150), pygame.Color(20, 173, 86, 150), pygame.Color(20, 173, 30, 150)],
[pygame.Color(156, 19, 165, 150), pygame.Color(165, 18, 111, 150), pygame.Color(165, 17, 76, 150)]]


# colors for drawing different bodies 
SKELETON_COLORS = [pygame.color.THECOLORS["red"], 
                  pygame.color.THECOLORS["blue"], 
                  pygame.color.THECOLORS["green"], 
                  pygame.color.THECOLORS["orange"], 
                  pygame.color.THECOLORS["purple"], 
                  pygame.color.THECOLORS["yellow"], 
                  pygame.color.THECOLORS["violet"]]

tick = Message()

speed_mult = 1

drum_preset = 0
bass_preset = 0
synth_preset = 0

key_adjust = 0

@in_thread
def metronom():
    while True:
        tick.cue()
        sleep(2 / speed_mult)

@in_thread
def drum_preset1():
    print("drum preset 1")
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
    print("drum preset 2")
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
    print("drum preset 3")
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
    print("bass preset 1")
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
    print("bass preset 2")
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
    print("bass preset 3")
    while bass_preset == 3:
        tick.sync()
        use_synth(DPULSE)
        play(45 + key_adjust, amp = 2, sustain = 0.25 / speed_mult)
        play(44 + key_adjust, amp = 2, sustain = 0.5 / speed_mult)
        play(37 + key_adjust, amp = 2, sustain = 1.25 / speed_mult)


@in_thread
def synth_preset1():
    print("synth preset 1")
    while synth_preset == 1:
        tick.sync()
        play(69 + key_adjust, amp = 1.5)
        sleep(0.75)
        play(68 + key_adjust, amp = 1.5)
        sleep(0.75)
        play(61 + key_adjust, amp = 1.5)


@in_thread
def synth_preset2():
    print("synth preset 2")
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
    print("synth preset 3")
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

# metronom()

def AAfilledRoundedRect(surface,rect,color,radius=0.4):

    """
    AAfilledRoundedRect(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect         = pygame.Rect(rect)
    color        = pygame.Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = pygame.Surface(rect.size,pygame.SRCALPHA)

    circle       = pygame.Surface([min(rect.size)*3]*2,pygame.SRCALPHA)
    pygame.draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = pygame.transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle,(0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright     = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags=pygame.BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=pygame.BLEND_RGBA_MIN)

    return surface.blit(rectangle,pos)

class StateController(object):
    def __init__(self):
        # Keep track of which mode you are in
        self.mode = MODE['baseline']
        # Boolean to check if user in freeplay mode
        self.freeplay = False
        # 0 is in the middle, below this middle frequency is negative
        self.frequency = 0
        self.style = 0

    def change_mode(self, forward):
        if forward:
            # If at last mode, wrap around
            if self.mode == MODE["synth"]:
                self.mode = MODE["baseline"]
            # Otherwise, increment mode
            else:
                self.mode += 1
        else:
            # Wrap around
            if self.mode == MODE["baseline"]:
                self.mode = MODE["synth"]
            # Decrement mode
            else:
                self.mode -= 1
        print_msg = "Now in mode " + str(self.mode)
        print(print_msg)    

        self.freeplay = False
        return self.mode
    def print_instructions(self, screen):
        
        if self.freeplay:
            screen.blit(freeplay_lh, (30, 370))
            screen.blit(freeplay_rh, (700, 370))
        else:
            screen.blit(loop_lh, (30, 370))
            screen.blit(loop_rh, (700, 370))
            screen.blit(loop_select, (200, 300))
        screen.blit(mode_change, (600, 400))

class ArmPositionRuntime(object):
    def __init__(self):
        pygame.init()
   
        # Initiate a game controller
        self.controller = StateController()

        # Initiate the font
        pygame.font.init()

        # Used to manage how fast the screen updates
        self._clock = pygame.time.Clock()

        # Set the width and height of the screen [width, height]
        self._infoObject = pygame.display.Info()
        self._screen = pygame.display.set_mode((self._infoObject.current_w >> 1, self._infoObject.current_h >> 1), 
                                               pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE, 32)

        pygame.display.set_caption("Kinect for Windows v2 Body Game")

        # Loop until the user clicks the close button.
        self._done = False

        # Used to manage how fast the screen updates
        self._clock = pygame.time.Clock()

        # Kinect runtime object, we want only color and body frames 
        self._kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Body)

        # back buffer surface for getting Kinect color frames, 32bit color, width and height equal to the Kinect color frame size
        self._frame_surface = pygame.Surface((self._kinect.color_frame_desc.Width, self._kinect.color_frame_desc.Height), 0, 32)

        # here we will store skeleton data 
        self._bodies = None

        # Note to play for freeplay
        self.note = 0

        self.first_preset = True

    def dragSegment1(self, joints, jointPoints, right):
        """
        Check if hand is RIGHT of elbow
        """
        if right:
            # Get the tracking states for right hand and right elbow
            hand = (jointPoints[PyKinectV2.JointType_HandRight].x, jointPoints[PyKinectV2.JointType_HandRight].y)
            elbow = (jointPoints[PyKinectV2.JointType_ElbowRight].x, jointPoints[PyKinectV2.JointType_ElbowRight].y)
        else:
            hand = (jointPoints[PyKinectV2.JointType_HandLeft].x, jointPoints[PyKinectV2.JointType_HandLeft].y)
            elbow = (jointPoints[PyKinectV2.JointType_ElbowLeft].x, jointPoints[PyKinectV2.JointType_ElbowLeft].y)           

        if hand[0] > elbow[0]:
                return True
        return False
    def dragSegment2(self, joints, jointPoints, right):
        """
        Check if hand is LEFT of elbow
        """
        if right:
            # Get the tracking states for right hand and right elbow
            hand = (jointPoints[PyKinectV2.JointType_HandRight].x, jointPoints[PyKinectV2.JointType_HandRight].y)
            elbow = (jointPoints[PyKinectV2.JointType_ElbowRight].x, jointPoints[PyKinectV2.JointType_ElbowRight].y)
        else:
            hand = (jointPoints[PyKinectV2.JointType_HandLeft].x, jointPoints[PyKinectV2.JointType_HandLeft].y)
            elbow = (jointPoints[PyKinectV2.JointType_ElbowLeft].x, jointPoints[PyKinectV2.JointType_ElbowLeft].y)           

        if hand[0] < elbow[0]:
                return True
        return False
    def waveSegment1(self, joints, jointPoints, right):
        """
        If either hand is to the right and above the elbow
        """
        if right:
            # Get the tracking states for right hand and right elbow
            hand = (jointPoints[PyKinectV2.JointType_HandRight].x, jointPoints[PyKinectV2.JointType_HandRight].y)
            elbow = (jointPoints[PyKinectV2.JointType_ElbowRight].x, jointPoints[PyKinectV2.JointType_ElbowRight].y)
        else:
            hand = (jointPoints[PyKinectV2.JointType_HandLeft].x, jointPoints[PyKinectV2.JointType_HandLeft].y)
            elbow = (jointPoints[PyKinectV2.JointType_ElbowLeft].x, jointPoints[PyKinectV2.JointType_ElbowLeft].y)           

        if hand[1] < elbow[1]:
            if hand[0] > elbow[0] + WAVE_ACCENTUATION:
                return True
        return False

    def waveSegment2(self, joints, jointPoints, right):
        """
        If either hand is to the left and above the elbow
        """
        if right:
            # Get the tracking states for right hand and right elbow
            hand = (jointPoints[PyKinectV2.JointType_HandRight].x, jointPoints[PyKinectV2.JointType_HandRight].y)
            elbow = (jointPoints[PyKinectV2.JointType_ElbowRight].x, jointPoints[PyKinectV2.JointType_ElbowRight].y)
        else:
            hand = (jointPoints[PyKinectV2.JointType_HandLeft].x, jointPoints[PyKinectV2.JointType_HandLeft].y)
            elbow = (jointPoints[PyKinectV2.JointType_ElbowLeft].x, jointPoints[PyKinectV2.JointType_ElbowLeft].y)           

        if hand[1] + WAVE_ACCENTUATION < elbow[1]:
            if hand[0] < elbow[0]:
                return True
        return False
    
    def fistPumpSegment(self, joints, jointPoints, right):
        """If hand is below the head"""
        head = (jointPoints[PyKinectV2.JointType_Head].x, jointPoints[PyKinectV2.JointType_Head].y)
        if right:
            hand = (jointPoints[PyKinectV2.JointType_HandRight].x, jointPoints[PyKinectV2.JointType_HandRight].y)
        else:
            hand = (jointPoints[PyKinectV2.JointType_HandLeft].x, jointPoints[PyKinectV2.JointType_HandLeft].y)
        
        return hand[1] > head[1]

    def handElbowValid(self, joints, jointPoints, right):
        if right:
            handState = joints[PyKinectV2.JointType_HandRight].TrackingState
            elbowState = joints[PyKinectV2.JointType_ElbowRight].TrackingState
        else:
            handState = joints[PyKinectV2.JointType_HandLeft].TrackingState
            elbowState = joints[PyKinectV2.JointType_ElbowLeft].TrackingState

        # both joints are not tracked
        if (handState == PyKinectV2.TrackingState_NotTracked) or (elbowState == PyKinectV2.TrackingState_NotTracked): 
            return False

        # Don't do it if input is SUS
        if (handState == PyKinectV2.TrackingState_Inferred) and (elbowState == PyKinectV2.TrackingState_Inferred):
            return False
        return True

    def headValid(self, joints, jointPoints):
        headState = joints[PyKinectV2.JointType_Head].TrackingState
        return headState == PyKinectV2.TrackingState_Tracked

    def draw_body_bone(self, joints, jointPoints, color, joint0, joint1):
        joint0State = joints[joint0].TrackingState
        joint1State = joints[joint1].TrackingState

        # both joints are not tracked
        if (joint0State == PyKinectV2.TrackingState_NotTracked) or (joint1State == PyKinectV2.TrackingState_NotTracked): 
            return

        # both joints are not *really* tracked
        if (joint0State == PyKinectV2.TrackingState_Inferred) and (joint1State == PyKinectV2.TrackingState_Inferred):
            return

        # ok, at least one is good 
        start = (jointPoints[joint0].x, jointPoints[joint0].y)
        end = (jointPoints[joint1].x, jointPoints[joint1].y)

        try:
            pygame.draw.line(self._frame_surface, color, start, end, 8)
        except: # need to catch it due to possible invalid positions (with inf)
            pass

    def number_to_mode(self, mode):
        if mode == 0:
            return "BASS"
        elif mode == 1:
            return "DRUMS"
        elif mode == 2:
            return "SYNTH"



    def check_closed(self, handState, right):
        if handState == PyKinectV2.HandState_Closed:
            return True
        return False

    def get_coords(self, joints, jointPoints, joint0, jointName = "Unidentified"):
        joint0State = joints[joint0].TrackingState;

        # both joints are not tracked
        if (joint0State == PyKinectV2.TrackingState_NotTracked): 
            return

        # both joints are not *really* tracked
        if (joint0State == PyKinectV2.TrackingState_Inferred):
            return

        # ok, at least one is good 
        start = (jointPoints[joint0].x, jointPoints[joint0].y)
        print(jointName, "x:", start[0], jointName,"y:", start[1])
    
    def print_presets(self, mode, highlight_preset, choosing_style):
        # Get the list of presets for this mode
        presets = LOOP_PRESETS[mode]
        # y coords of the first box
        y_offset = 50

        # Loop through each preset in this mode
        for i in range(len(presets)):
            # Highlight box if box is highlighted, otherwise draw as normal
            if highlight_preset == i:
                rect = pygame.Rect(20, y_offset-50, 200, 150)
                AAfilledRoundedRect(self._screen, rect, PRESET_COLORS[self.controller.mode][i])
            else:
                rect = pygame.Rect(20, y_offset-20, 200, 80)
                AAfilledRoundedRect(self._screen, rect, PRESET_COLORS[self.controller.mode][i])
            # Generate the text
            myfont = pygame.font.SysFont('impact', 45)
            # If we are grabbing and matches this text
            if not choosing_style and highlight_preset == i:
                # Draw as black
                textsurface = myfont.render(presets[i], True, (0,0,0,150))
            # Draw as normal
            else:
                textsurface = myfont.render(presets[i], True, (255, 255, 255))
            self._screen.blit(textsurface,(53, y_offset-5))
            y_offset += 135

    def speed_up_value(self, joints, joint_points):
        spine_mid_y = joint_points[PyKinectV2.JointType_SpineMid].y
        hand_right_y = joint_points[PyKinectV2.JointType_HandRight].y
        y_pos_diff = hand_right_y - spine_mid_y
        return float(y_pos_diff)/10

    def volume_bar_adjust(self, joints, joint_points):
        if self.handElbowValid(joints, joint_points, False) == True:
            spine_mid_y = joint_points[PyKinectV2.JointType_SpineMid].y
            hand_left_y = joint_points[PyKinectV2.JointType_HandLeft].y
            y_pos_diff = hand_left_y - spine_mid_y
            pitch = float(y_pos_diff)/10
            max_rect = pygame.Rect(20, 40, 30, 400)
            black = (0,0,0)
            pygame.draw.rect(self._screen, black, max_rect)

            curr_rect_height = -6.6 * pitch + 200
            curr_rect_height = 400 if curr_rect_height > 400 else curr_rect_height
            curr_rect_height = 0 if curr_rect_height < 0 else curr_rect_height
            curr_rect = pygame.Rect(20, 440 - curr_rect_height, 30, curr_rect_height)
            red = (255,0,0)
            pygame.draw.rect(self._screen, red, curr_rect)


    def draw_body(self, joints, jointPoints, color):
       # Right Arm    
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_HandRight, PyKinectV2.JointType_HandTipRight);
        #self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_WristRight, PyKinectV2.JointType_HandRight);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_ElbowRight, PyKinectV2.JointType_HandRight);

        # Left Arm
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_HandLeft, PyKinectV2.JointType_HandTipLeft);
        #self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_WristLeft, PyKinectV2.JointType_HandLeft);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_ElbowLeft, PyKinectV2.JointType_HandLeft);
        self.draw_body_bone(joints, jointPoints, color, PyKinectV2.JointType_SpineBase, PyKinectV2.JointType_SpineMid);

    def draw_color_frame(self, frame, target_surface):
        target_surface.lock()
        address = self._kinect.surface_as_array(target_surface.get_buffer())
        ctypes.memmove(address, frame.ctypes.data, frame.size)
        del address
        target_surface.unlock()

    def play_preset(self, highlight_preset):

        if self.controller.mode == MODE["baseline"]:
            global bass_preset
            bass_preset = 0
            bass_preset = highlight_preset + 1
            print(bass_preset)
            bass_preset1()
            bass_preset2()
            bass_preset3()
        elif self.controller.mode == MODE["drum"]:
            global drum_preset
            drum_preset = 0
            drum_preset = highlight_preset + 1
            print(drum_preset)
            drum_preset1()
            drum_preset2()
            drum_preset3()
        elif self.controller.mode == MODE["synth"]:
            global synth_preset
            synth_preset = 0
            synth_preset = highlight_preset + 1
            print(synth_preset)
            synth_preset1()
            synth_preset2()
            synth_preset3()


    def run(self):

        # State counters for waving
        rightWaveSegmentsComplete = 0
        rightWaveFrameCount = 0
        leftWaveSegmentsComplete = 0
        leftWaveFrameCount = 0
        delayAfterWave = 0
        justWaved = False

        # State counters for dragging
        rightDragGestureState = 0
        leftDragGestureState = 0
        fistPumpState = 0
        
        # Pitch controls
        pitchGestureState = 0
        state0_Y = -1
        state1_Y = -1
        state1_frame_count = 0
        currentPitch = 0
        currentDifference = 0

        # Loop variable controls
        choosing_style = True
        confirm_frame = 0

        # Keep track of which preset you want to highlight
        highlight_preset = -1

        # State counters for playing notes
        prev_rhy = -1
        note_delay = POST_NOTE_DELAY

        # Printing flag
        print_flag = True
        print_frame_count = 0
        print_to_screen_msg = "msg"
        PRINT_FRAME_COUNT_LIMIT = 120

        # -------- Main Program Loop -----------
        while not self._done:
            # --- Main event loop
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    self._done = True # Flag that we are done so we exit this loop

                elif event.type == pygame.VIDEORESIZE: # window resized
                    self._screen = pygame.display.set_mode(event.dict['size'], 
                                               pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE, 32)
                    
            # --- Game logic should go here

            # --- Getting frames and drawing  
            # --- Woohoo! We've got a color frame! Let's fill out back buffer surface with frame's data 
            if self._kinect.has_new_color_frame():
                frame = self._kinect.get_last_color_frame()
                self.draw_color_frame(frame, self._frame_surface)
                frame = None

            # --- Cool! We have a body frame, so can get skeletons
            if self._kinect.has_new_body_frame(): 
                self._bodies = self._kinect.get_last_body_frame()

            # --- draw skeletons to _frame_surface
            if self._bodies is not None:
                for i in range(0, 6):
                    body = self._bodies.bodies[i]
                    if not body.is_tracked: 
                        continue 

                    joints = body.joints 
                    # convert joint coordinates to color space 
                    joint_points = self._kinect.body_joints_to_color_space(joints)
                    self.draw_body(joints, joint_points, SKELETON_COLORS[i])
                    #self.get_coords(joints, joint_points, PyKinectV2.JointType_HandLeft, "Left Hand")
                    #self.get_coords(joints, joint_points, PyKinectV2.JointType_ElbowLeft, "Left Elbow")

                    # Code for detecting RIGHT HAND WAVE
                    if justWaved == False:
                        if self.handElbowValid(joints, joint_points, True):
                            # Code for checking whether a wave has been performed
                            if rightWaveSegmentsComplete % 2 == 0:
                                # Check for waveSeg1
                                if self.waveSegment1(joints, joint_points, True):
                                    rightWaveSegmentsComplete += 1
                                    rightWaveFrameCount = 0
                                else:
                                    rightWaveFrameCount += 1
                            else:
                                # Check for waveSeg2
                                if self.waveSegment2(joints, joint_points, True):
                                    rightWaveSegmentsComplete += 1
                                    rightWaveFrameCount = 0
                                else:
                                    rightWaveFrameCount += 1
                        
                            # Check if you have been waiting for too many frames
                            if rightWaveFrameCount > MAX_WAVE_FRAME_WAIT:
                                rightWaveSegmentsComplete = 0
                                rightWaveFrameCount = 0
                                # print("you failed to wave right you dumbass")

                            # Check whether we have fully completed a wave
                            if rightWaveSegmentsComplete == WAVE_SEGMENTS_REQUIRED:
                                print("Just completed a right wave")

                                # toggle freeplay/loop
                                self.controller.freeplay = not self.controller.freeplay
                                print("Freeplay mode:", self.controller.freeplay)
                                
                                justWaved = True
                                rightWaveSegmentsComplete = 0
                                rightWaveFrameCount = 0
                        # If input is sus, reset wave detection
                        else:
                            rightWaveSegmentsComplete = 0
                            rightWaveFrameCount = 0

                        # Code for detecting LEFT HAND WAVE
                        if self.handElbowValid(joints, joint_points, False):
                            # Code for checking whether a wave has been performed
                            if leftWaveSegmentsComplete % 2 == 0:
                                # Check for waveSeg1
                                if self.waveSegment1(joints, joint_points, False):
                                    leftWaveSegmentsComplete += 1
                                    leftWaveFrameCount = 0
                                else:
                                    leftWaveFrameCount += 1
                            else:
                                # Check for waveSeg2
                                if self.waveSegment2(joints, joint_points, False):
                                    leftWaveSegmentsComplete += 1
                                    leftWaveFrameCount = 0
                                else:
                                    leftWaveFrameCount += 1
                        
                            # Check if you have been waiting for too many frames
                            if leftWaveFrameCount > MAX_WAVE_FRAME_WAIT:
                                leftWaveSegmentsComplete = 0
                                leftWaveFrameCount = 0
                                # print("you failed to left wave you dumbass")

                            # Check whether we have fully completed a wave
                            if leftWaveSegmentsComplete == WAVE_SEGMENTS_REQUIRED:
                                print("Just completed a left wave")

                                # toggle freeplay/loop
                                self.controller.freeplay = not self.controller.freeplay
                                print("Freeplay mode:", self.controller.freeplay)
                                
                                justWaved = True
                                leftWaveSegmentsComplete = 0
                                leftWaveFrameCount = 0
                        # If input is sus, reset wave detection
                        else:
                            leftWaveSegmentsComplete = 0
                            leftWaveFrameCount = 0
                    else:
                        delayAfterWave += 1
                        # If you've waited for about 3 seconds, now u can wave again yay
                        if delayAfterWave > POST_WAVE_DELAY:
                            justWaved = False
                            delayAfterWave = 0

                    # Detecting dragging gesture from right to left (right hand)
                    if self.check_closed(body.hand_right_state, True) \
                        and self.dragSegment1(joints, joint_points, True) and rightDragGestureState == 0:
                        rightDragGestureState = 1
                    elif not self.check_closed(body.hand_right_state, True) and rightDragGestureState == 1:
                        if self.dragSegment1(joints, joint_points, True):
                            rightDragGestureState = 0
                        elif self.dragSegment2(joints, joint_points, True):
                            rightDragGestureState = 2
                    elif rightDragGestureState == 2:
                        print("Right Drag gesture complete yay")
                        # Proceed forward in mode
                        self.controller.change_mode(True)
                        print_flag = True
                        # Make sure you don't wave shortly after u drag
                        justWaved = True
                        rightDragGestureState = 0 
                    
                    # Detecting dragging gesture from left to right (right hand)
                    if self.check_closed(body.hand_right_state, True) \
                        and self.dragSegment2(joints, joint_points, True) and leftDragGestureState == 0:
                        leftDragGestureState = 1
                    elif not self.check_closed(body.hand_right_state, True) and leftDragGestureState == 1:
                        if self.dragSegment2(joints, joint_points, True):
                            leftDragGestureState = 0
                        elif self.dragSegment1(joints, joint_points, True):
                            leftDragGestureState = 2
                    elif leftDragGestureState == 2:
                        print("Left Drag gesture complete yay")
                        # Proceed backward in mode
                        self.controller.change_mode(False)
                        # Set printing flag to true
                        print_flag = True
                        
                        justWaved = True
                        leftDragGestureState = 0 

                    # Detecting pitch control using left hand
                    if self.handElbowValid(joints, joint_points, False):
                        # Start capturing the first position to determine pitch
                        if pitchGestureState == 0:
                            pitchGestureState = 1
                            spineMid_Y = joint_points[PyKinectV2.JointType_SpineMid].y
                            state0_Y = spineMid_Y
                        # Give user one second to position their hand to determine pitch
                        elif pitchGestureState == 1 and state1_frame_count < PITCH_ADJ_DELAY:
                            state1_frame_count += 1
                        # Capture second position for a difference in position to determine pitch
                        elif pitchGestureState == 1 and state1_frame_count >= PITCH_ADJ_DELAY:
                            state1_Y = joint_points[PyKinectV2.JointType_HandLeft].y
                            yPosDiff = state1_Y - state0_Y
                            pitch = float(yPosDiff)/10.0
                            
                            if self.controller.mode == MODE["drum"]:
                                if pitch < HIGHEST:
                                    self.note = DRUM_TOM_MID_HARD
                                elif pitch < MID_HIGH:
                                    self.note = DRUM_TOM_LO_HARD
                                elif pitch < MEDIUM:
                                    self.note = DRUM_CYMBAL_CLOSED
                                elif pitch < MID_LOW:
                                    self.note = DRUM_SNARE_HARD
                                elif pitch < LOW:
                                    self.note = DRUM_HEAVY_KICK
                            elif self.controller.mode == MODE["synth"]:
                                self.note = pitch + 60
                                if self.note < 30:
                                    self.note = 30
                            elif self.controller.mode == MODE["baseline"]:
                                self.note = pitch + 70
                                if self.note < 1:
                                    self.note = 0
                            pitchGestureState = 0
                            state1_frame_count = 0
                    
                    # spine_mid_y = joint_points[PyKinectV2.JointType_SpineMid].y
                    # hand_left_y = joint_points[PyKinectV2.JointType_HandLeft].y
                    # y_pos_diff = hand_left_y - spine_mid_y
                    # pitch = float(y_pos_diff)
                    # max_rect = pygame.Rect(20, 40, 30, 300)
                    # black = (0,0,0)
                    # pygame.draw.rect(self._screen, black, max_rect)    
                            
                        # figure out displacement between frame 0 and frame 1
                    
                    # Detecting if we play a note only if it's in freeplay mode
                    if self.controller.freeplay:
                        # If we just played a note
                        if note_delay < POST_NOTE_DELAY:
                            # Don't check for a note 
                            # But incremnet note_delay
                            note_delay += 1
                        
                        # If we surpassed note delay threshold
                        else:
                            rightHandState = joints[PyKinectV2.JointType_HandRight].TrackingState;
                            # both joints are not tracked or not really tracked
                            if (rightHandState == PyKinectV2.TrackingState_NotTracked) or \
                                (rightHandState == PyKinectV2.TrackingState_Inferred): 
                                prev_rhy = -1
                            else:
                                # If prev_rhy is uninitialized, initialize it and don't check for note played
                                if prev_rhy == -1:
                                    prev_rhy = joint_points[PyKinectV2.JointType_HandRight].y
                                # If already initialized, check if note is being played
                                else:
                                    cur_y = joint_points[PyKinectV2.JointType_HandRight].y
                                
                                    if cur_y - prev_rhy > MVT_THRESHOLD:
                                        print("Played a note")
                                        if self.controller.mode == MODE["drum"]:
                                            sample(self.note) # if drums use sample
                                        elif self.controller.mode == MODE["synth"]:
                                            synth(TB303, note = self.note)
                                        elif self.controller.mode == MODE["baseline"]:
                                            synth(SUBPULSE, note = self.note*2//3, amp = 2)
                                        # Reset delay counter to delay between notes played
                                        note_delay = 0
                                        prev_rhy = cur_y
                    # If in LOOP mode
                    else:
                        # If your left hand is available
                        if self.handElbowValid(joints, joint_points, False):
                            # If you are choosing a style, check if you have chosen a style
                            if choosing_style:
                                # Closing your hands for more than 3 seconds means you are SELECTING
                                spine_mid_Y = joint_points[PyKinectV2.JointType_SpineMid].y
                                hand_left_Y = joint_points[PyKinectV2.JointType_HandLeft].y
                                y_pos_diff = hand_left_Y - spine_mid_Y
                                selection = float(y_pos_diff)/10.0
                                if selection < FIRST_PRESET:
                                    # Selecting first preset
                                    highlight_preset = 0
                                    # self.note = DRUM_TOM_MID_HARD
                                elif selection < SECOND_PRESET:
                                    # Selecting second preset
                                    highlight_preset = 1
                                    # self.note = DRUM_TOM_LO_HARD
                                else:
                                    # Selecting third preset
                                    highlight_preset = 2
                                    # self.note = DRUM_BASS_HARD

                                if self.check_closed(body.hand_left_state, False):
                                    confirm_frame += 1

                                    # If you satisfy 10 frames of closing your hand
                                    if confirm_frame > CONFIRM_DELAY:
                                        # You will have successfully picked this 
                                        print("Chose a loop")
                                        # No longer choosing
                                        choosing_style = False
                                        confirm_frame = 0

                                else:
                                    confirm_frame = 0
                                    
                            # If you have already selected a style, watch out for letting go
                            # for 3 seconds
                            else:
                                # If you open your hands for more than 3 seconds
                                if not self.check_closed(body.hand_left_state, False):
                                    confirm_frame += 1

                                    # If you satisfy 10 frames of letting your hand open
                                    if confirm_frame > CONFIRM_DELAY:
                                        # you will have successfully let go
                                        print("Beginning to choose again")
                                        choosing_style = True
                                        confirm_frame = 0

                                        
                                        speed_up = -self.speed_up_value(joints, joint_points)
                                        speed_up /= 23
                                        global speed_mult
                                        speed_mult = math.exp(speed_up)
                                        print(speed_mult)
                                        if self.first_preset:
                                            self.first_preset = False
                                            metronom()
                                        self.play_preset(highlight_preset)
                                        # Check for speed update in another 15 frames
                                        speed_update_frame = 0

                                # If your hands are clenched while holding
                                else:
                                    confirm_frame = 0


                        
                        
                    '''
                    # Detecting fist pump up (right hand)
                    # print("fistPumpState", fistPumpState)
                    if self.check_closed(body.hand_right_state, True):
                        if self.fistPumpSegment(joints, joint_points, True):
                            if fistPumpState == 0:
                                fistPumpState = 1
                            elif fistPumpState == 2:
                                print("Fist pump gesture complete!!!!")
                                fistPumpState = 0
                        else:
                            if fistPumpState == 1:
                                fistPumpState = 2
                    else:
                        # Hand opened, fist pump gesture failed
                        # print("Fist pump gesture failed")
                        fistPumpState = 0
                    '''

            # --- copy back buffer surface pixels to the screen, resize it if needed and keep aspect ratio
            # --- (screen size may be different from Kinect's color frame size) 
            h_to_w = float(self._frame_surface.get_height()) / self._frame_surface.get_width()
            target_height = int(h_to_w * self._screen.get_width())
            surface_to_draw = pygame.transform.scale(self._frame_surface, (self._screen.get_width(), target_height));
            self._screen.blit(surface_to_draw, (0,0))
            surface_to_draw = None

            # Print the instructions for usage
            #self.controller.print_instructions(self._screen)

            # Update loop preset options
            if not self.controller.freeplay:
                self.print_presets(self.controller.mode, highlight_preset, choosing_style)
            else:
                self.volume_bar_adjust(joints, joint_points)

            # Update the text
            if print_flag == True and print_frame_count < PRINT_FRAME_COUNT_LIMIT:
                # Draw a roudned rect behind the text
                titleColor = pygame.Color(143, 214, 216, 200)
                titleRect = pygame.Rect(300, 15, 400, 100)
                AAfilledRoundedRect(self._screen,titleRect,titleColor,1)

                myfont = pygame.font.SysFont('impact', 100)
                textsurface = myfont.render(self.number_to_mode(self.controller.mode), True, (65, 72, 175, 200))
                self._screen.blit(textsurface,(370, 0))

                print_frame_count += 1

            elif print_flag == True and print_frame_count >= PRINT_FRAME_COUNT_LIMIT:
                print_flag = False
                print_frame_count = 0
            pygame.display.update()
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            self._clock.tick(60)

        # Close our Kinect sensor, close the window and quit.
        self._kinect.close()
        bass_preset = 0
        drum_preset = 0
        synth_preset = 0
        pygame.quit()


__main__ = "Kinect v2 Body Game"
game = ArmPositionRuntime()
game.run()

