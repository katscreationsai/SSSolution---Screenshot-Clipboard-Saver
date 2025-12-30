import time
import os
from datetime import datetime
from PIL import ImageGrab, Image

def start_rescue_mission():
    # --- CONFIGURATION ---
    # We use r"..." to tell Python to ignore the backslashes in Windows paths
    save_folder = r"C:\Users\ilove\Pictures\Screenshots"
    # ---------------------

    # 1. Create the folder if it doesn't exist
    if not os.path.exists(save_folder):
        try:
            os.makedirs(save_folder)
            print(f"📁 Folder was missing, so I created it: {save_folder}")
        except OSError as e:
            print(f"❌ Error creating folder: {e}")
            return
    else:
        print(f"✅ Found existing folder: {save_folder}")

    print("---------------------------------------------------------")
    print("👀 CLIPBOARD WATCHER ACTIVE")
    print("---------------------------------------------------------")
    print("1. Keep this window open.")
    print("2. Press 'Windows Key + V'.")
    print("3. Click your images one by one.")
    print(f"   (Saving directly to: {save_folder})")
    print("---------------------------------------------------------")

    last_image_bytes = None
    count = 1

    try:
        while True:
            # Grab content from clipboard
            img = ImageGrab.grabclipboard()

            if isinstance(img, Image.Image):
                current_image_bytes = img.tobytes()

                # Check if this is a new image (different from the last one we saw)
                if current_image_bytes != last_image_bytes:
                    
                    # Create a filename with a precise timestamp
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    filename = f"Screenshot ({timestamp}).png"
                    filepath = os.path.join(save_folder, filename)
                    
                    try:
                        img.save(filepath, "PNG")
                        print(f"✅ Saved #{count}: {filename}")
                        count += 1
                        last_image_bytes = current_image_bytes
                    except Exception as e:
                        print(f"❌ Error saving file: {e}")
            
            # Check every 0.2 seconds for faster response
            time.sleep(0.2)

    except KeyboardInterrupt:
        print("\n🛑 Stopped.")

if __name__ == "__main__":
    start_rescue_mission()