# Первое задание
# Author: Dan Zaytsev

import mcpi.minecraft as minecraft
import mcpi.block as blocks


def fill_pot(pot_x, pot_y, pot_z, height, block_id):
    """
    Постройка ямы
    :param pot_x:  точка начала ямы по оси х
    :param pot_y: точка начала ямы по оси y
    :param pot_z: точка начала ямы по оси z
    :param height: глубина ямы
    :param block_id: ID блока ямы
    :return:
    """
    for current_height in range(height):
        mc.setBlock(pot_x, pot_y - current_height, pot_z, block_id)


def restore_terrain(start_x, start_y, start_z, block_id,
                    first_pot_height, second_pot_height, third_pot_height, fourth_pot_height, fifth_pot_height,
                    sixth_pot_height, seventh_pot_height):
    """
    Заполнение ямы
    """

    fill_pot(start_x + 1, start_y, start_z, first_pot_height, block_id)
    fill_pot(start_x + 2, start_y, start_z, second_pot_height, block_id)
    fill_pot(start_x + 3, start_y, start_z, third_pot_height, block_id)
    fill_pot(start_x + 4, start_y, start_z, fourth_pot_height, block_id)
    fill_pot(start_x + 5, start_y, start_z, fifth_pot_height, block_id)
    fill_pot(start_x + 6, start_y, start_z, sixth_pot_height, block_id)
    fill_pot(start_x + 7, start_y, start_z, seventh_pot_height, block_id)


if __name__ == '__main__':
    mc = minecraft.Minecraft.create()
    # Получение текущих координат игрока
    player_x, player_y, player_z = mc.player.getPos()
    # Точка размещения блока
    block_x, block_y, block_z = player_x + 3, player_y - 1, player_z
    # Установка блока возле игрока
    mc.setBlock(block_x, block_y, block_z, blocks.DIAMOND_BLOCK)

    text_message = "Глубина этой ямы - 14 блоков"
    my_float_value = 8.65

    # Выведем текущие координаты для отладки
    x, y, z = mc.player.getPos()
    mc.postToChat("Мои координаты: X - " + str(x) + ", Y - " + str(y) + ", Z - " + str(z))

    # Здесь должен быть ваш код
    # my_block_id: Числовой ID блока, которым будет заполнена яма.
    # Здесь ID 57 - алмазный блок
    my_block_id = 57
    # first_pot_height: в эту переменную нужно присвоить значение 6
    first_pot_height = 6
    # second_pot_height: в этой переменной должна быть сумма
    # переменной first_pot_height и заранее объявленной my_float_value
    second_pot_height = int(first_pot_height + my_float_value)
    # third_pot_height: в этой переменной должна быть разность переменной
    third_pot_height = first_pot_height - 3
    # fourth_pot_height: в этой переменной должно быть произведение
    # переменной first_pot_height и числа 4
    fourth_pot_height = first_pot_height * 4
    # fifth_pot_height: в этой переменной должно быть произведение
    # переменной first_pot_height и числа 3
    fifth_pot_height = first_pot_height * 3
    # sixth_pot_height: в этой переменной должно быть число извлеченное из строки text_message
    sixth_pot_height = int(text_message[19] + text_message[20])
    # sixth_pot_height: в этой переменной должно быть число извлеченное из строки text_message
    seventh_pot_height = first_pot_height + sixth_pot_height




    # Выкапывание ямы
    restore_terrain(block_x, block_y, block_z, my_block_id,
                    first_pot_height, second_pot_height, third_pot_height, fourth_pot_height, fifth_pot_height,
                    sixth_pot_height, seventh_pot_height)


