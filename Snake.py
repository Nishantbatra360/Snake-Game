class Snake:
    def __init__(self, color_rgb=(0, 0, 255), length=3):
        self.__color = color_rgb
        self.__length = length
        self.__score = 0

    def decrease_length(self, amount=1):
        self.__length = self.__length - amount
        if self.__length < 1:
            self.__length = 1

    def increase_length(self, amount=1):
        self.__length = self.__length + amount

    def set_color(self, color_rgb):
        self.__color = color_rgb

    def get_color(self):
        return self.__color

    def get_length(self):
        return self.__length

    def increase_score(self, amount):
        self.__score = self.__score + amount

    def get_score(self):
        return self.__score
