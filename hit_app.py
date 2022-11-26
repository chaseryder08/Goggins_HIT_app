
# TODO add docstring
# https://realpython.com/documenting-python-code/

import pygame as pg
import time
from pathlib import Path


SKILL_LEVEL = ['1', '2', '3']
TRACK_PATH = Path(r"C:\Users\User\Desktop\workspaces\local\python_projects\HIT_time_app\sound_files\inspirational_music.wav")
GOGGINS_PATH = Path(r"C:\Users\User\Desktop\workspaces\local\python_projects\HIT_time_app\sound_files\goggins.wav")
EXERCISES = ["Jumping Jacks", "Burpees", "Mountain Climbers", "Push ups", "Lunges", "Squats", "Plank", "Bicycle kicks", "Leg Thrusts", "High knees"]
music_track = ""
goggins_track = ""

pg.mixer.init()
pg.init()
pg.mixer.set_num_channels(50)

def ready_go(start):
    # TODO add docstring, typing
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

def workout_timer(set_time):
    # TODO add docstring, typing

    while set_time:

        mins, secs = divmod(set_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        set_time -= 1

    print("REST! -- Time until next set: ")

def rest_timer(rest_time):
    # TODO add docstring, typing

    while rest_time:

        mins, secs = divmod(rest_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        rest_time -= 1

def check_goggins_resp(msg: str) -> str:
    # TODO add docstring

    while True:
        user_goggins_resp = input(f"{msg}: ").lower()
        if user_goggins_resp == "yes":
            return user_goggins_resp
        elif user_goggins_resp == "no":
            break
        print("Please enter yes or no")

# Prompt user for skill level.
user_input = None
while user_input not in SKILL_LEVEL:
    user_input = input("Please enter your HIT skill level. (1 = beginner | 2 = intermediate | 3 = advanced)")

# Prompt user for music option.
user_music_resp = None
while user_music_resp not in ("yes", "no"):
    user_music_resp = input("Would you like motivational music to pump you up? (yes or no)")

if user_input == '1':

    level = "Beginner"
    set_time = 20
    rest_time = 10
    set_num = 8
    
elif user_input == '2':

    level = "Intermediate"
    set_time = 30
    rest_time = 10
    set_num = 10

elif user_input == '3':

    level = "Advanced"
    set_time = 45
    rest_time = 15
    set_num = 12

print("You selected " + level + " : ")
print("Your workout will have " + str(set_num ) + " sets total")
print("Each set will last " + str(set_time) + " seconds")
print("You will have " + str(rest_time) + " seconds of rest time in between sets")

goggins_user_resp = check_goggins_resp("Would you like David Goggins to provide you motivational support?")
start = input("Hit enter when you are ready to start your workout : ")
ready_go(start)

if user_music_resp == "yes":
    pg.mixer.init()
    pg.init()
    pg.mixer.set_num_channels(50)
    music_track = pg.mixer.Sound(TRACK_PATH)
    music_track.play()

if goggins_user_resp == "yes":
    pg.mixer.init()
    pg.init()
    pg.mixer.set_num_channels(50)
    goggins_track = pg.mixer.Sound(GOGGINS_PATH)
    goggins_track.play()

counter = 1

for i in range(set_num):
    print("Go!")
    time.sleep(1)
    print("Exercise " + str(counter) + ":")
    counter = int(counter)
    counter += 1
    print(EXERCISES[i])
    workout_timer(int(set_time))
    rest_timer(int(rest_time))
    print("NEXT EXERCISE: " + EXERCISES[i+1])
    time.sleep(1)


print("GREAT JOB!")
