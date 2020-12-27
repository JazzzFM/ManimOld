from manimlib.imports import *

# Objetivo: Mostrar en una gráfica un punto que indique la posición de un cuerpo en movimeinto,  
# al mismo tiempo que se muestra su posición en una línea recta. 
# La tabla (que no se incluye en la animación) describe el movimiento del cuerpo.

####################################################################################

# Mover el punto en la grafica y en la línea recta. 
# La línea en la gráfica debe ir dibujándose a medida que la animación avanza. 
# Cada intervalo debe durar la misma cantidad de segundos. 

class CustomGraph3(GraphFromData):
    CONFIG = {
        "y_max": 25,
    }
    def construct(self):
        
        self.setup_axes()
        x = [0 , 1, 2, 3,  4,  5,  6,  7]
        y = [0 , 1, 4, 9, 16, 25, 20, 10]

        coords = [[px,py] for px,py in zip(x,y)]
        # |
        # V
        points = self.get_points_from_coords(coords)
        
        image = ImageMobject("/home/codexreckoner/manim/media/designs/raster_images/FONDOCOLOR.jpg")
        image.scale(6)
        self.play(FadeIn(image))


        graph = SmoothGraphFromSetPoints(points,color=GREEN)
        dots = self.get_dots_from_coords(coords)

        self.add(graph,dots)

        self.wait(3)
