import os
import time

# Clear terminal function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Frames of simple running stick figure animation
frames = [
    r"""
     (\_/)  
     ( •_•)  
    / >🏃‍♀️  Hasina running
    """,
    r"""
     (\_/)  
    (•_• )  
    🏃‍♀️< \  
    """,
    r"""
     (\_/)  
    ( •_•)  
     / >🏃‍♀️  
    """,
    r"""
     (\_/)  
    (•_• )  
    🏃‍♀️< \  
    """
]

def animate_running(cycles=10, delay=0.3):
    for _ in range(cycles):
        for frame in frames:
            clear()
            print(frame)
            time.sleep(delay)

if __name__ == "__main__":
    animate_running()