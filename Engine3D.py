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

width=1920
height=1080

#creacion de Window

r = Render(width,height)

posModel = ( 0, 0, -5)
r.lookAt(posModel, (0,0,0))

"""
#rocketModel Texture
r.active_texture = Texture('./models/planespace.bmp')
r.active_shader = unlit

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
"""

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
r.loadModel('./models/earth.obj', (3,0,-5), (0.004,0.004,0.004),(0,130,0))

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





