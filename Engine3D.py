"""
Maria Ines Vasquez Figueroa
18250
Gráficas
Proyecto Software Rendering
Main
"""

from gl import Render
from obj import Obj, Texture
from shaders import *
import random

#valores con los que se inicializan la ventana y viewport

width=1920
height=1080

#creacion de Window

r = Render(width,height)

for x in range (2,width-2):
    for y in range (2, height-2):
        
        size=random.randint(1,2400)
        if size==1:
            r.glVertex_coord(x,y)
        elif size==2:
            r.glVertex_coord(x,y)
            r.glVertex_coord(x+1,y)
            r.glVertex_coord(x,y+1)
            r.glVertex_coord(x+1,y+1)
        elif size==3:
            r.glVertex_coord(x,y)
            r.glVertex_coord(x+1,y)
            r.glVertex_coord(x,y+1)
            r.glVertex_coord(x-1,y)

#r.glColor(1,1,1)

#r.glVertex_coord(960,540)

posModel = ( 0, 0, -5)
r.lookAt(posModel, (0,0,0))


#rocketModel Texture
r.active_texture = Texture('./models/planespace.bmp')
r.active_shader = toon

#rocketModel
r.loadModel('./models/space-shuttle-orbiter.obj', (3,-1,-4), (0.002,0.002,0.002),(0,130,0))

#astro texture
r.active_texture = Texture('./models/suit.bmp')
r.active_normalMap = Texture('./models/normal_suit.bmp')
r.active_shader = normalMap

#Astro
r.loadModel('./models/astronaute.obj', (-1,1,-5), (0.5,0.5,0.5),(0,0,0))

#mars
r.active_texture = Texture('./models/metal.bmp')
r.active_shader = unlit #si no es pura sombra

#Mars robot
r.loadModel('./models/marsRobot.obj',  (-4,0.75,-5), (0.0025,0.0025,0.0025),(0,90,0))


#r.lightx, r.lighty, r.lightz=1,0,0
#( 3, 0, *profundidad y direccion con -*5)

#Mars Texture
r.active_texture = Texture('./models/2k_mars.bmp')
r.active_shader = thermal

#Mars Model
r.loadModel('./models/earth.obj', (-4,0,-5), (0.002,0.002,0.002),(0,130,0))

#neptune Texture
r.active_texture = Texture('./models/2k_neptune.bmp')
r.active_shader = stripes_neptune

#neptune Model
r.loadModel('./models/earth.obj', (-1,0,-5), (0.003,0.003,0.003),(0,130,0))

#jupiter Texture
r.active_texture = Texture('./models/2k_jupiter.bmp')
r.active_shader = static_jupiter

#jupiter Model
r.loadModel('./models/earth.obj', (3,0,-6), (0.004,0.004,0.004),(0,130,0))

"""#astro texture
r.active_texture = Texture('./models/suit.bmp')
r.active_normalMap = Texture('./models/normal_suit.bmp')
r.active_shader = normalMap#cambiar a gouraud


#Astro
r.loadModel('./models/astronaute.obj', (-1,-2,-5), (2,2,2),(0,0,0))"""

#high angle
#r.lookAt(posModel, (0,2,0))

#low angle
#r.lookAt(posModel, (0,-2,0))

#medium shot
#r.lookAt(posModel, (0,0,0))

#Dutch
#r.lookAt(posModel, (-2,-2,-0.25))


r.glFinish('output.bmp')
#r.glZBuffer('zbuffer.bmp')





