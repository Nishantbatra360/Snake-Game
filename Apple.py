class Apple:
    def __init__(self, color_rgb=(255, 0, 0), score=10):
        self.__color = color_rgb
        self.__score = score

    def set_color(self, color_rgb):
        self.__color = color_rgb

    def get_color(self):
        return self.__color

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score
