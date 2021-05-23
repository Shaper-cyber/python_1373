class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight_road(self):
        return f"При длине: {self._length} м. и ширине: {self._width} м." \
               f" асфальта надо {(self._length * self._width * 0.025 * 5)} т"


b = Road(5000, 20)
print(b.weight_road())
