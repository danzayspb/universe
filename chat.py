from mcpi.minecraft import Minecraft
mc = Minecraft.create()

player_x, player_y, player_z = mc.player.getPos()
arena_x = player_x + 3
arena_y = player_y
arena_z = player_z
column_x = player_x - 2
column_y = player_y
column_z = player_z
arena_block = 42
under_block = 41
column_block = 45
above_block = 57
has_first_struct_event = mc.getBlock(player_x, player_y - 1, player_z) == under_block
has_second_struct_event = mc.getBlock(player_x, player_y + 2, player_z) == above_block

if has_first_struct_event and not(has_second_struct_event):
    mc.postToChat("Появилась арка")
    # Нижний ряд
    mc.setBlock(arena_x, arena_y, arena_z, arena_block)
    mc.setBlock(arena_x, arena_y, arena_z + 1, arena_block)
    mc.setBlock(arena_x, arena_y, arena_z + 2, arena_block)
    mc.setBlock(arena_x, arena_y, arena_z + 3, arena_block)
    # Второй ряд
    mc.setBlock(arena_x, arena_y + 1, arena_z, arena_block)
    mc.setBlock(arena_x, arena_y + 1, arena_z + 3, arena_block)
    # Третий ряд
    mc.setBlock(arena_x, arena_y + 2, arena_z, arena_block)
    mc.setBlock(arena_x, arena_y + 2, arena_z + 3, arena_block)
    # Четвертый ряд
    mc.setBlock(arena_x, arena_y + 3, arena_z, arena_block)
    mc.setBlock(arena_x, arena_y + 3, arena_z + 3, arena_block)
    # Последний ряд
    mc.setBlock(arena_x, arena_y + 4, arena_z, arena_block)
    mc.setBlock(arena_x, arena_y + 4, arena_z + 1, arena_block)
    mc.setBlock(arena_x, arena_y + 4, arena_z + 2, arena_block)
    mc.setBlock(arena_x, arena_y + 4, arena_z + 3, arena_block)
elif has_second_struct_event:
    mc.postToChat("Событие наступило")
    # Нижний блок
    mc.setBlock(column_x, column_y + 1, column_z, column_block)
    # Второй блок
    mc.setBlock(column_x, column_y + 2, column_z, column_block)
    # Третий блок
    mc.setBlock(column_x, column_y + 3, column_z, column_block)
    # Четвертый блок
    mc.setBlock(column_x, column_y + 4, column_z, column_block)
    # Последний блок
    mc.setBlock(column_x, column_y + 5, column_z, column_block)
else:
    mc.postToChat("Ничего не произошло")

