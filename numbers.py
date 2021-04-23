from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x, y, z = mc.player.getPos()
score = "Мой текущий прогресс: 100"
score = score[-3] + score[-2] + score[-1]
name = "Даниил"

mc.postToChat(score)


