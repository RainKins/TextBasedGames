#Rain Lawson
import random
class Card:
    def __init__(self):
        self.__value = 0

    def deal(self):
        self.__value = random.randint(1,13)
    
    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def get_face_value(self):
  
        face_value = {1:"Ace",
        								2:"Two",
        								3:"Three",
												4:"Four",
        								5:"Five",
        								6:"Six",
        								7:"Seven",
        								8:"Eight",
        								9:"Nine",
        								10:"Ten",
        								11:"Jack",
        								12:"Queen",
        								13:"King"}

        return face_value[self.__value]
        
        def __str__(self):
            return "All Face Value Card are " + str(self.__value) + "\n"