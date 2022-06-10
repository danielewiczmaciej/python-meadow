import os

from animals.antylope import Antylope
from animals.cybersheep import CyberSheep
from animals.fox import Fox
from animals.sheep import Sheep
from animals.turtle import Turtle
from animals.wolf import Wolf
from window import Window
from ground import Ground
from human import Human
from plants.guarana import Guarana
from plants.Borscht import Borscht
from tkinter import *
from random import random, randrange

from plants.dandelion import Dandelion
from plants.wolfberries import WolfBerries


class World:
    sinceLastSuperAbility = 0
    width = None
    height = None
    organisms = []
    toAdd = []
    toRem = []
    log = ""
    humanAlive = False
    board = None
    window = Window()

    def __init__(self, _width, _height):
        self.width = _width
        self.height = _height
        self.board = [[Ground(self, i, j) for i in range(self.height)] for j in range(self.width)]
        self.log = ""
        print("H: " + str(self.height))
        print("W: " + str(self.width))

    def printAmounts(self):
        antylopes = 0
        cs = 0
        f = 0
        hum = 0
        s = 0
        t = 0
        w = 0
        guar = 0
        B = 0
        D = 0
        wB = 0
        gr = 0
        print(str(len(self.organisms)))
        for it in self.organisms:
            if it.GetSign() == 'a':
                antylopes += 1
            elif it.GetSign() == 'c':
                cs += 1
            elif it.GetSign() == 'h':
                hum += 1
            elif it.GetSign() == 's':
                s += 1
            elif it.GetSign() == 't':
                t += 1
            elif it.GetSign() == 'f':
                f += 1
            elif it.GetSign() == 'w':
                w += 1
            elif it.GetSign() == '*':
                wB += 1
            elif it.GetSign() == '$':
                B += 1
            elif it.GetSign() == '.':
                gr += 1
            elif it.GetSign() == '#':
                guar += 1
            elif it.GetSign() == '@':
                D += 1
        print("Antylopes: " + str(antylopes))
        print("CyberSheeps: " + str(cs))
        print("Humans: " + str(hum))
        print("Sheeps: " + str(s))
        print("Turtles: " + str(t))
        print("Foxes: " + str(f))
        print("Wolves: " + str(w))
        print("Wolf Berries: " + str(wB))
        print("Borschts: " + str(B))
        print("Grass: " + str(gr))
        print("Guaranas: " + str(guar))
        print("Dandelions: " + str(D))

    def PrintWorld(self):
        out = ""
        for i in range(self.height):
            for j in range(self.width):
                out += self.board[j][i].GetSign()
            out += '\n'
        print(out)
        self.window.addWorld(self)

    def StartHumanAbility(self):
        if self.sinceLastSuperAbility == 0:
            for it in self.organisms:
                if isinstance(it, Human):
                    it.UseAbility()
                    self.sinceLastSuperAbility = 10
                    print("Superability used!")

    def AddRandomOrganisms(self):
        amount = 100
        for i in range(amount):
            x = randrange(self.width)
            y = randrange(self.height)

            if isinstance(self.board[y][x], Ground):
                org = randrange(10)
                if org == 0:
                    self.add(Antylope(self, x, y))
                elif org == 1:
                    self.add(Fox(self, x, y))
                elif org == 2:
                    self.add(Guarana(self, x, y))
                elif org == 3:
                    self.add(Sheep(self, x, y))
                elif org == 4:
                    self.add(Borscht(self, x, y))
                elif org == 5:
                    self.add(Dandelion(self, x, y))
                elif org == 6:
                    self.add(Turtle(self, x, y))
                elif org == 7:
                    self.add(Wolf(self, x, y))
                elif org == 8:
                    self.add(WolfBerries(self, x, y))
                elif org == 9:
                    self.add(CyberSheep(self, x, y))
        x = randrange(self.width)
        y = randrange(self.height)
        while not isinstance(self.board[y][x], Ground):
            x = randrange(self.width)
            y = randrange(self.height)
        self.add(Human(self, x, y, 0))


    def add(self, _newO):
        print("Adding new organism!")
        self.board[_newO.y][_newO.x] = _newO
        if len(self.organisms) == 0:
            self.organisms.insert(len(self.organisms), _newO)
        else:
            added = False
            for it in self.organisms:
                if _newO.initiative > it.initiative:
                    self.organisms.insert(self.organisms.index(it), _newO)
                    return
            if not added:
                self.organisms.insert(len(self.organisms), _newO)

    def ToAdd(self, _newO):
        self.board[_newO.y][_newO.x] = _newO
        self.toAdd.insert(len(self.toAdd), _newO)

    def NextTurn(self, _dir=None):
        for it in self.organisms:
            if it.age > 0:
                if self.board[it.y][it.x].GetSign() == it.GetSign():
                    if isinstance(it, Human):
                        it.Action(_dir)
                    else:
                        it.Action()
        for it in self.toAdd:
            if not isinstance(it, Ground):
                self.add(it)
        self.toAdd.clear()
        for it in self.organisms:
            if isinstance(it, Borscht):
                it.Burn()
        for it in self.organisms:
            if isinstance(self.board[it.y][it.x], Ground):
                self.toRem.insert(len(self.toRem), it)
        for it in self.toRem:
            self.organisms.remove(it)
        self.toRem.clear()
        for it in self.organisms:
            it.age += 1
        if self.sinceLastSuperAbility > 0:
            self.sinceLastSuperAbility -= 1
        out = ""
        for i in range(self.height):
            for j in range(self.width):
                out += self.board[j][i].GetSign()
            out += '\n'
        print(out)

    def Log(self, _log):
        self.log += _log
        self.log += '\n'

    def PrintLog(self):
        output = Tk()
        t = Text(output, height=100, width=100)
        t.pack()
        t.insert(END, self.log)
        print("Log:")
        print(self.log)

    def Save(self):
        input = Tk()
        e = Entry(input)
        e.pack()

        def callback():
            name = e.get()
            self.SaveToFile(name)
            input.destroy()

        b = Button(input, text="Confirm", command=callback)
        b.pack()

    def SaveToFile(self, name):
        file = open("saves/" + name, "w")
        file.write(str(self.width) + ":" + str(self.height) + ":" + str(len(self.organisms)) + ":" +
                   str(self.sinceLastSuperAbility) + '\n')
        for it in self.organisms:
            file.write(it.Print() + '\n')
        file.close()

    def Load(self):
        input = Tk()
        e = Entry(input)
        e.pack()

        def callback():
            name = e.get()
            self.LoadFromFile(name)
            input.destroy()

        b = Button(input, text="Confirm", command=callback)
        b.pack()

    def LoadFromFile(self, name):
        if os.path.isfile("saves/" + name):
            file = open("saves/" + name, "r")
            self.log = ""
            self.board = []
            self.organisms.clear()
            data = file.readline()
            print(data)
            data = data.split(':')
            print(data)
            print(data[0] + " " + str(int(data[0])))
            self.width = int(data[0])
            self.height = int(data[1])
            self.sinceLastSuperAbility = int(data[3])
            self.board = [[Ground(self, i, j) for i in range(self.height)] for j in range(self.width)]
            out = ""
            for i in range(self.height):
                for j in range(self.width):
                    out += self.board[j][i].GetSign()
                out += '\n'
            print(out)
            for i in range(int(data[2])):
                data = file.readline()
                data = data.split(':')
                _org = data[0]
                _x = int(data[1])
                _y = int(data[2])
                _age = int(data[3])
                _power = int(data[4])
                _init = int(data[5])
                if _org == 'a':
                    self.add(Antylope(self, _x, _y, _age, _power, _init))
                elif _org == 'c':
                    self.add(CyberSheep(self, _x, _y, _age, _power, _init))
                elif _org == 'f':
                    self.add(Fox(self, _x, _y, _age, _power, _init))
                elif _org == 'h':
                    self.add(Human(self, _x, _y, _age, _power, _init, int(data[6])))
                elif _org == 's':
                    self.add(Sheep(self, _x, _y, _age, _power, _init))
                elif _org == 't':
                    self.add(Turtle(self, _x, _y, _age, _power, _init))
                elif _org == 'w':
                    self.add(Wolf(self, _x, _y, _age, _power, _init))
                elif _org == '#':
                    self.add(Guarana(self, _x, _y, _age, _power, _init))
                elif _org == '$':
                    self.add(Borscht(self, _x, _y, _age, _power, _init))
                elif _org == '*':
                    self.add(WolfBerries(self, _x, _y, _age, _power, _init))
                elif _org == '@':
                    self.add(Dandelion(self, _x, _y, _age, _power, _init))
            self.window.printBoard()
            file.close()
        else:
            print("File doesnt exist!")
