class Genshin():

    def __init__(link, CharacterName, element, hp):
        link.CharacterName = CharacterName
        link.element = element
        link.hp = hp

    def jump(link):
        print(link.CharacterName , " is jumping")

    def attack(link):
        print(link.CharacterName , " is attacking")
        print(link.CharacterName , " is using charge attack so he've got redeuce hp from his passage")
        print(link.CharacterName, ' hp is now left : ', link.hp / 2)

    def sprint(link):
        print(link.CharacterName , " is sprinting")

    def ElementalSkill(link):
        print(link.CharacterName , " is using elemental skill")

