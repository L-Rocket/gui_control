import pyautogui


import keyboard
table = []
print("Press any key (ESC to exit):")

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == 'esc':
            print("Exiting the program.")
            break
        else:
            print(f"You pressed the key: {event.name}")
            table.append(event.name)


print(table)