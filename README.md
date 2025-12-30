# SSSolution - Screenshot Clipboard Saver

A lightweight Python script that automatically saves images from your clipboard to a custom Screenshots folder. Built to work around Windows' annoying habit of not recreating the Screenshots folder when it gets deleted.

## What It Does

- Monitors your clipboard for images
- Automatically saves any new image to your custom Screenshots folder
- Creates timestamped filenames so nothing gets overwritten
- Runs continuously in the background

## Why I Made This

Windows sometimes refuses to recreate the Screenshots folder in `Pictures` no matter what you do. Instead of fighting with Windows, this script just handles it for you.

## How To Use

### Option 1: Run the Python Script

1. Make sure you have Python installed with Pillow:
```bash
   pip install pillow
```

2. Edit the `save_folder` path in the script to your preferred location

3. Run it:
```bash
   python SSSolution.py
```

4. Keep the window open and use Windows+V to paste images from clipboard history

### Option 2: Use the Compiled .exe

1. Download the `.exe` from [Releases](https://github.com/YourUsername/SSSolution/releases)
2. Double-click to run
3. Keep it running in the background

## Configuration

Change the save location by editing this line in the script:
```python
save_folder = r"C:\Users\YourUsername\Pictures\Screenshots"
```

## Requirements

- Python 3.x
- Pillow (PIL)

Happy Screenshotting <3
- KatsCeationsAI
