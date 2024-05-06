class Phone():
    def __init__(link, brand, model, battery=100):
        link.brand = brand
        link.model = model
        link.battery = battery

    def camera(link):
        print(link.brand, "is filming. Cha Luck Cha Luck")

    def call(link):
        print(link.brand, "is calling. tu tu tu")
