import socket
import server
from mcpi import block
from mcpi import minecraft
import shapes
from woolcolors import WoolColors


class SimpleMine:
    COLORS = {
        'y': WoolColors.yellow,
        'x': WoolColors.black,
        'g': WoolColors.green,
        'G': WoolColors.dark_green,
        'b': WoolColors.blue,
        'p': WoolColors.purple,
        'r': WoolColors.red,
        'P': WoolColors.pink,
        'o': WoolColors.orange,
        'B': WoolColors.brown,
        'e': WoolColors.light_gray
    }

    def __init__(self, name):
        self.name = name
        self.mc = minecraft.Minecraft.create(server.address)
        self.ip = socket.getfqdn()

    def reset_world(self):
        self.mc.player.setPos(0, 0, 0)
        self.mc.setBlocks(-50, 0, -50, 50, 50, 50, block.AIR)
        self.mc.setBlocks(-50, -1, -50, 50, -2, 50, block.SAND)
        self.chat('World reset by ' + self.ip)

    def clear_space(self):
        pos = self.mc.player.getPos()
        pos = minecraft.Vec3(int(pos.x), int(pos.y), int(pos.z))
        self.mc.setBlocks(pos.x-50, pos.y+0, pos.z-50, pos.x+50, pos.y+60, pos.z+42, block.AIR)
        self.mc.setBlocks(pos.x-50, pos.y-1, pos.z-50, pos.x+50, pos.y-2, pos.z+50, block.SAND)
        self.chat('Space cleared by ' + self.ip)

    def make_thing(self, thing, depth=1):
        pos = self.mc.player.getPos()
        pos = minecraft.Vec3(int(pos.x), int(pos.y), int(pos.z))
        for x_delta in range(depth):
            height = len(thing)
            for row in thing:
                idx = 0
                for b in row:
                    if b != ' ':
                        color = WoolColors.gray.value
                        try:
                            color = SimpleMine.COLORS[b].value
                        except:
                            color = WoolColors.gray.value
                        self.mc.setBlock(pos.x + x_delta + 1, pos.y + height, pos.z + idx, block.WOOL.id,
                                         color)
                    idx += 1
                height -= 1
        self.chat('Thing made by ' + self.name)

    def chat(self, message):
        self.mc.postToChat(message)

    def get_pos(self):
        return self.mc.player.getPos()

if __name__ == '__main__':
    pass
    # create object from class SimpleMine()
    steve = SimpleMine('Steve')


    # steve.clear_space()

    steve.chat('Hi from steve')
    steve.make_thing(shapes.batman,5)

    # clear a space to make things

    # practice making things from shapes.py

    # practice setting the depth of the thing by setting optional parameter in make_thing()

    # create your own thing in shapes and draw it here

    # print your position
