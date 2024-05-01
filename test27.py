class Character():
    
    def __init__(link, name, spell, hp):
        link.name = name
        link.spell= spell
        link.hp = hp

    def jump(link):
        print(link.name , " is jumping")

    def prone(link):
        print(link.name , " is proning")

    def shoot(link):
        print(link.name , " is shooting")

    def using_emote(link):
        print(link.name , " is using emote")

    def run(link):
        print(link.name , " is running")

    def using_spell(link):
        print(link.name , " is using spell")