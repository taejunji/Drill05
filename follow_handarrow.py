from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')


def make_random_x_y():
    global hand_x, hand_y
    hand_x, hand_y = random.randint(100, 1000), random.randint(100, 800)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
            


frame = 0
now_boy_x, now_boy_y, past_boy_x, past_boy_y = 1280 // 2, 1024 // 2, 1280 // 2, 1024 // 2
hand_x, hand_y = random.randint(100, 1000), random.randint(100, 800)

running = True

while running:
    for i in range(0, 50+1):
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        t = i / 50
        now_boy_x = (1 - t) * past_boy_x + t * hand_x
        now_boy_y = (1 - t) * past_boy_y + t * hand_y
        frame = (frame + 1) % 8
        hand_arrow.draw(hand_x, hand_y)
        if hand_x > now_boy_x:
            character.clip_draw(frame * 100, 100, 100, 100, now_boy_x, now_boy_y)
        else:
            character.clip_draw(frame * 100, 0, 100, 100, now_boy_x, now_boy_y)
        update_canvas()
        handle_events()
        delay(0.03)

    make_random_x_y()
    past_boy_x = now_boy_x
    past_boy_y = now_boy_y

close_canvas()
