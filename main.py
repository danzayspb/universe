# Homework 2
# Author: Dan Zaytsev

import mcpi.minecraft as minecraft
import mcpi.block as blocks


def build_score(start_x, start_y, start_z, *positions):
    """
    Заполнение ямы
    """

    mc.setBlock(start_x, start_y, start_z + positions[0], blocks.DIAMOND_BLOCK)
    mc.setBlock(start_x, start_y, start_z + positions[1], blocks.DIAMOND_BLOCK)
    mc.setBlock(start_x, start_y, start_z + positions[2], blocks.DIAMOND_BLOCK)
    mc.setBlock(start_x, start_y + 1, start_z + positions[3], blocks.DIAMOND_BLOCK)
    mc.setBlock(start_x, start_y + 2, start_z + positions[4], blocks.DIAMOND_BLOCK)
    mc.setBlock(start_x, start_y + 2, start_z + positions[5], blocks.DIAMOND_BLOCK)
    mc.setBlock(start_x, start_y + 3, start_z + positions[6], blocks.DIAMOND_BLOCK)
    mc.setBlock(start_x, start_y + 4, start_z + positions[7], blocks.DIAMOND_BLOCK)
    mc.setBlock(start_x, start_y + 4, start_z + positions[8], blocks.DIAMOND_BLOCK)
    mc.setBlock(start_x, start_y + 4, start_z + positions[9], blocks.DIAMOND_BLOCK)


if __name__ == '__main__':
    mc = minecraft.Minecraft.create()
    # Получение текущих координат игрока
    player_x, player_y, player_z = mc.player.getPos()
    # Точка размещения блока
    block_x, block_y, block_z = player_x + 3, player_y, player_z

    who_am_i = "Я студент Слёрм!"
    """ В переменную position_1 нужно присвоить количество вопросительных знаков в уже заготовленной строке 
    who_am_i. Подсчитать количество символов в строке позволяет функция строк count. 
    В качестве аргумента она принимает строку, количество вхождений которой нужно подсчитать."""
    position_1 = who_am_i.count("?")
    """В переменную position_2 нужно присвоить длину результата выражения who_am_i[1]"""
    position_2 = len(who_am_i[1])
    '''В переменная position_3 формируется следующим образом: из строки who_am_i при помощи среза нужно 
    извлечь слово "студент"; затем нужной строковой функцией заменить букву т на пустую строку; 
    после подсчитать длину полученной строки и в переменную position_3 присвоить остаток от деления этой 
    строки на 3 (Остаток от деления можно получить при помощи оператора %)
    '''
    position_3 = len(who_am_i[2:9].replace("т", ""))%3
    '''Переменная position_4 формируется так: строковым методом нужно сделать все буквы в строке who_am_i 
    заглавными и подсчитать количество букв Т строковым методом'''
    position_4 = who_am_i.upper().count("Т")
    '''В переменной position_5 должен находиться результат следующих действий: при помощи среза извлечь 
    из строки who_am_i строку Слёрм. Подсчитать её длину и поделить нацело на 2. Поделить нацело (взять целую часть без остатка) можно оператором //'''
    position_5 = len(who_am_i[-6:-1])//2
    '''В переменную position_6 нужно присвоить нужно присвоить количество восклицательных знаков в строке who_am_i'''
    position_6 = who_am_i.count("!")
    '''В переменную position_7 нужно присвоить разность переменной position_5 и константы 2'''
    position_7 = position_5 - 2
    '''В переменную position_8 нужно присвоить приведенный к числу результат строкового метода 
    islower(), примененного к строке who_am_i. Этот строковый метод проверяет все ли буквы в строке 
    прописные (маленькие) и возвращает логический (булев) тип.'''
    position_8 = int(who_am_i.islower())
    '''В переменную position_9 нужно присвоить количество букв л в строке who_am_i'''
    position_9 = who_am_i.count("л")
    '''В переменную position_10 нужно присвоить длину полного среза строки who_am_i с шагом 3, деленную на 3'''
    position_10 = len(who_am_i[::3])//3

    build_score(block_x, block_y, block_z,
                position_1, position_2, position_3, position_4, position_5,
                position_6, position_7, position_8, position_9, position_10)

