"""
Суть задачи - показать понимание ООП
Ваш проект - что-то похожее на шахматы, ваша задача написать класс/иерархию классов для фигуры в вашей игре.
 Важно понимать, реализация никакая не требуется, необходимо написать только их интерфейсы для примера вот:
Class User:
	def call(phone: str):
		pass
Никакая реализация не требуется!

*	Написать иерархию классов для работы карты с дорожными знаками. Также, никакой внутренней реализации, только интерфейс.
Как понимаете, так и напишите. Важно понять логику, которой вы придерживались, можете добавить собственные пояснения,
 если посчитаете нужным.

"""


class Figure:
    """
    Usual chess piece
    """
    def __init__(self, color, status, pos_x, pos_y):
        self.color = color
        self.status = status
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self):
        pass

    def attack(self):
        pass


class Board:
    """
    Board description
    """

    def __init__(self, width, length):
        self.width = width
        self.length = length


class King(Figure):
    """
    King description
    """

    def __init__(self, color, status, pos_x, pos_y):
        super().__init__(color, status, pos_x, pos_y)

    def move(self, new_x, new_y):
        if True:
            pass
        pos_x = new_x
        pos_y = new_y
        return pos_x, pos_y

    def сastling(self):
        """King and the rook move"""
        pass


#################################################################################

class UsualSign:
    def __init__(self, sign_material, size, figure):
        self.sign_material = sign_material
        self.size = size
        self.figure = figure


class Stand:
    def __init__(self, height, st_material, permanently):
        self.st_material = st_material
        self.height = height
        self.permanently = permanently

    def st_move(self):
        pass

    def st_broke(self):
        pass


class Picture:
    def __init__(self, pic, colors):
        self.pic = pic
        self.colors = colors

    def pic_repaint(self):
        pass

    def pic_dirty(self):
        pass

    def pic_clean(self):
        pass


class ProhibitionSign(UsualSign, Stand, Picture):
    def __init__(self, pic, colors, height, st_material, permanently, sign_material, size, figure, location):
        super().__init__(pic, colors, height, st_material, permanently, sign_material, size, figure)
        self.location = location
