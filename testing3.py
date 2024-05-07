import time
class phone():

    def __init__(link, brand, model, battery=100):
        link.brand = brand
        link.model = model
        link.battery = battery
        link.current_battery = 100

    def nonstop_playing(link):
        current_match = 0
        while link.current_battery > 0 :
            print("game playing")
            link.current_battery -= 10
            current_match = current_match + 1
            print(current_match,"matches finished", link.current_battery)
            time.sleep(2)
            if link.current_battery <= 30:
                print("Input Charging")
                break
        print("Battery Down")
