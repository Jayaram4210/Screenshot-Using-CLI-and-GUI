import pyautogui
import datetime
import os

folder = "../screenshots"
os.makedirs(folder, exist_ok=True)

timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = os.path.join(folder, f"screenshot_{timestamp}.png")

screenshot = pyautogui.screenshot()
screenshot.save(filename)

print(f"✅ Screenshot saved at: {filename}")
