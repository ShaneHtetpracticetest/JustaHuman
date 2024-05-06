
class Genshin():

    def __init__(link, CharacterName, element, hp, max_stamina):
        link.CharacterName = CharacterName
        link.element = element
        link.hp = hp
        link.max_stamina = max_stamina
        link.stamina = max_stamina

    def jump(link):
        print(link.CharacterName , " is jumping")

    def attack(link):
        print(link.CharacterName , " is attacking")
        print(link.CharacterName , " is using charge attack so he've got redeuce hp from his passage")
        print(link.CharacterName, ' hp is now left : ', link.hp / 2)

    def sprint(link):
        print(link.CharacterName , " is sprinting")
        
    def decrease_stamina(link):
        while True:
            time.sleep(1)
            if link.stamina > 0:
                link.stamina -= 30
            else :
                link.stamina = 0

    def sprinting(link):
        if link.stamina >= sprint_cost: 
            link.stamina -= sprint_cost
        print(f"{link.name} is sprinting! Stamina: {link.stamina}")
        else:
            print(f"{link.name} doesn't have enough stamina to sprint! Stopping sprint...")
sprint_cost = 30

import threading
thread = threading.Thread(target=Cha2.decrease_stamina)
thread.daemon = True
thread.start()
    
while True:
    Cha2.sprint()
    if Cha2.stamina == 0:
        break  
    time.sleep(2)  

      

    def ElementalSkill(link):
        print(link.CharacterName , " is using elemental skill")


