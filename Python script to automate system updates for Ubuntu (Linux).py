import os

def update_system():
    os.system('sudo apt update && sudo apt upgrade -y')

if __name__ == "__main__":
    update_system()
