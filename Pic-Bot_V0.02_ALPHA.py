import cv2
import configparser
import pyautogui
import numpy as np
import keyboard
import time

def load_config(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config

def find_and_perform_actions(config):
    while True:
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)
        screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
        found_images = []

        for image_name in config.sections():
            image_path = config[image_name]['Path']
            template = cv2.imread(image_path)

            result = cv2.matchTemplate(screenshot_bgr, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            locations = np.where(result >= threshold)

            for pt in zip(*locations[::-1]):
                bottom_right = (pt[0] + template.shape[1], pt[1] + template.shape[0])

                action = config[image_name].get('Action', 'none')
                if action.lower() == 'click_location':
                    click_location = ((pt[0] + bottom_right[0]) // 2, (pt[1] + bottom_right[1]) // 2)
                    pyautogui.click(click_location)
                elif action.lower() == 'button_press':
                    key_to_press = config[image_name].get('Key', 'enter')
                    keyboard.press_and_release(key_to_press)

                found_images.append(image_name)

        if found_images:
            print(f"Found images: {', '.join(found_images)}")
            time.sleep(5)  # Sperrzeit von 5 Sekunden nach der Aktion

if __name__ == "__main__":
    config_path = "config.ini"
    config = load_config(config_path)
    find_and_perform_actions(config)
