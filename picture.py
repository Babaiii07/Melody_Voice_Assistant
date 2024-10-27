from datetime import datetime
import pyautogui
import os
from systemOperations import speak
import cv2

def generate_image():
    pass

def take_selfie():
    cap = cv2.VideoCapture(0)
    
    ret, frame = cap.read()
    if ret:
        save_dir = 'pictures'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        filename = os.path.join(save_dir, f'image_{datetime.now().strftime("%Y%m%d_%H%M%S")}.jpg')
        cv2.imwrite(filename, frame)
    cap.release()
    cv2.destroyAllWindows()

    speak("captured image")

def take_screenshot():
    try:
        screenshots_dir = "screenshots"
        
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_filename = f"{screenshots_dir}/screenshot_{timestamp}.png"
        
        screenshot = pyautogui.screenshot()
        
        screenshot.save(screenshot_filename)
        
        speak("Screenshot taken and saved as screenshots_file")
    except Exception as e:
        speak(f"Sorry, I couldn't take the screenshot. Error: {str(e)}")