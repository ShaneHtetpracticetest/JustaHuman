class Genshin():

    def __init__(link, CharacterName, element, hp):
        link.CharacterName = CharacterName
        link.element = element
        link.hp = hp

    def jump(link):
        print(link.CharacterName , " is jumping")

    def attack(link):
        print(link.CharacterName , " is attacking")

    def sprint(link):
        print(link.CharacterName , " is sprinting")

    def ElementalSkill(link):
        print(link.CharacterName , " is using elemental skill")

