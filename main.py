import time
import keyboard
import pyautogui as pyag

def run(wait_time, modifier):
    try:
        while True:
            if keyboard.is_pressed('q') and keyboard.is_pressed('ctrl'):
                break
            start_pos = pyag.position()
            print(start_pos)
            time.sleep(float(wait_time))
            end_pos = pyag.position()
            print(end_pos)

            dist = ((end_pos[0] - start_pos[0]), (end_pos[1] - start_pos[1]))

            print(dist)
            pyag.move(((dist[0] * abs(modifier - 1)), (dist[1] * abs(modifier - 1))), duration=wait_time)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    wait_time = float(input("Wait Time: "))
    modifier = float(input("Modifier: "))
    run(wait_time, modifier)