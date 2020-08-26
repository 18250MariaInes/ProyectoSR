"""
Maria Ines Vasquez Figueroa
18250
Gráficas
SR6 Transformations
Main
"""

from gl import Render
from obj import Obj, Texture
from shaders import *

#valores con los que se inicializan la ventana y viewport

width=1000
height=500

#creacion de Window

r = Render(width,height)

#rocketModel Texture
r.active_texture = Texture('./models/planespace.bmp')
r.active_shader = unlit

posModel = ( 0, 0, -5)
r.lookAt(posModel, (0,0,0))

#rocketModel
r.loadModel('./models/space-shuttle-orbiter.obj', (-3,0,-5), (0.002,0.002,0.002),(0,130,0))

#astro texture
r.active_texture = Texture('./models/suit.bmp')
r.active_shader = gouraud #cambiar a gouraud

#Astro
r.loadModel('./models/astronaute.obj', (0,0,-5), (0.5,0.5,0.5),(0,0,0))

#mars
r.active_texture = Texture('./models/metal.bmp')
r.active_shader = unlit #cambiar a gouraud

#Mars robot
r.loadModel('./models/marsRobot.obj',  (2,0,-5), (0.005,0.005,0.005),(0,90,0))

#r.lightx, r.lighty, r.lightz=1,0,0
#( 3, 0, *profundidad y direccion con -*5)


#high angle
#r.lookAt(posModel, (0,2,0))

#low angle
#r.lookAt(posModel, (0,-2,0))

#medium shot
r.lookAt(posModel, (0,0,0))

#Dutch
#r.lookAt(posModel, (-2,-2,-0.25))








r.glFinish('output.bmp')
#r.glZBuffer('zbuffer.bmp')





