#Programa principal
import random
from shaders import *
from gl import *
from obj import *
from texture import *
width = 100  #alto de la pantalla
height = 100 #ancho de la pantalla
rende = Renderer(height,width)

rende.active_shader = thermal
rende.active_texture = Texture("models/camptex.bmp")



rende.glLoadModel("models/campfire.obj",translate=V3(width/2,height/2,0),rotate=V3(0,0,0),scale=V3(1,1,1))


rende.glFinish("./salida.bmp")