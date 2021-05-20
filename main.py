from mcpi.minecraft import Minecraft
mc = Minecraft.create
import time

while True:
    player_x, player_y, player_z = mc.getTilePos()
    arena_x = player_x + 10
    arena_y = player_y - 1
    arena_z = player_z
    arena_block = 1
    trigger_block = 41
    gold_struct = mc.getBlock(player_x, player_y - 1, player_z) == trigger_block and \
                  mc.getBlock(player_x, player_y + 2, player_z) == trigger_block
    gold_struct_2 = mc.getBlock(player_x, player_y - 1, player_z) == trigger_block and\
                    mc.getBlock(player_x,player_y + 1,player_z - 1) == trigger_block and\
                    mc.getBlock(player_x,player_y + 1,player_z + 1) == trigger_block
    gold_only_one_struct = gold_struct or gold_struct_2
    gold_double_struct = gold_struct and gold_struct_2

    if gold_only_one_struct:
        mc.setBlock(player_x, player_y - 1, player_z, 86)
        mc.setBlock(player_x, player_y + 2, player_z, 86)
        mc.postToChat("Игра началась!")
    elif gold_double_struct:
        mc.postToChat("Игра окончена!")
        break

for length_bias in range(14):
    for width_bias in range(6):
        if length_bias == 3 or length_bias == 6 or length_bias == 8 or length_bias ==13 or width_bias == 3 or width_bias == 6 or width_bias == 8 or width_bias ==13:
           mc.setBlock(arena_x + length_bias, arena_y, arena_z + width_bias, 49)
           mc.setBlock(arena_x + length_bias, arena_y + 1, arena_z + width_bias, 9)
           mc.setBlock(arena_x + length_bias, arena_y + 2, arena_z + width_bias, 1)
           mc.setBlock(arena_x + length_bias, arena_y + 3, arena_z + width_bias, 4)
           mc.setBlock(arena_x + length_bias, arena_y + 4, arena_z + width_bias, 1)
           mc.setBlock(arena_x + length_bias, arena_y + 5, arena_z + width_bias, 4)
           mc.setBlock(arena_x + length_bias, arena_y + 6, arena_z + width_bias, 1)
           mc.setBlock(arena_x + length_bias, arena_y + 7, arena_z + width_bias, 4)
           mc.setBlock(arena_x + length_bias, arena_y + 8, arena_z + width_bias, 89)
           mc.setBlock(arena_x + length_bias, arena_y + 9, arena_z + width_bias, 4)
           mc.setBlock(arena_x + length_bias, arena_y + 10, arena_z + width_bias, 1)
           mc.setBlock(arena_x + length_bias, arena_y + 11, arena_z + width_bias, 4)
           mc.setBlock(arena_x + length_bias, arena_y + 12, arena_z + width_bias, 1)
           mc.setBlock(arena_x + length_bias, arena_y + 13, arena_z + width_bias, 4)
           mc.setBlock(arena_x + length_bias, arena_y + 14, arena_z + width_bias, 20)
time.sleep(0.1)


