#from big_ol_pile_of_manim_imports import *
from manimlib.imports import *

#Me gusta mucho lo que me mandaste. Mis observaciones:
#
#1. De la primer parte porfa coloca la etiqueta de longitud en minúscula (x) Listo! :D
#
#2. Imagino que más adelante vas a centrar toda la gráfica verdad. listo! :D
#
#3. Me encanta la segunda parte ! Se ve mucho mejor con esa flechita. Pero no uses la etiqueta (t).
#  Con eso me doy cuenta que es mejor usar una para esa partícula , elige la letra mayúscula que quieras 
#  y ponla en lugar de esa (t) . De igual manera pon esa etiqueta en la gráfica, y que esa letra vaya 
#  desplazándose conforme avanzan los puntos . 
#
#4. Olvidé colocar las unidades en esa recta. Ponlas a la derecha de la recta porfa. Fue mi error. Simplemente es x(m)
# Ya están listos los tiempos Maybe
# Ya solo falta ponerle fondo y renderizar en HD

def get_coords_from_csv(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            x,y = row
            coord = [float(x),float(y)]
            coords.append(coord)
    csvFile.close()
    return coords


class GraphFromData(GraphScene):
    # Covert the data coords to the graph points
    def get_points_from_coords(self,coords):
        return [
            # Convert COORDS -> POINTS
            self.coords_to_point(px,py)
            # See manimlib/scene/graph_scene.py
            for px,py in coords
        ]

    # Return the dots of a set of points
    def get_dots_from_coords(self,coords,radius=0.1):
        points = self.get_points_from_coords(coords)
        dots = VGroup(*[
            Dot(radius=radius).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots

class DiscreteGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners(set_of_points)

class SmoothGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_smoothly(set_of_points)

class AnimationSix(GraphFromData): 
    centro = np.array((-5,-3,0))
    CONFIG = {
        "y_max" : 6000,
        "y_min" : 0,
        "x_max" : 9,
        "x_min" : 0,
        "y_tick_frequency" : 1000,
        "axes_color" : BLUE,
        "graph_origin" : centro,
         "x_axis_label" : "$t(s)$",
        "y_axis_label" : "$x(m)$",
    }
    def construct(self):
        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/stars.jpg")
        image.scale(6)
        self.add(image)
        self.setup_axes()
        coords = get_coords_from_csv("custom_graphs/data")

        points2 = self.get_points_from_coords(coords[0:2])
        points3 = self.get_points_from_coords(coords[1:3])
        points4 = self.get_points_from_coords(coords[2:4])
        points5 = self.get_points_from_coords(coords[3:5])
        points6 = self.get_points_from_coords(coords[4:6])
        points7 = self.get_points_from_coords(coords[5:7])
        points8 = self.get_points_from_coords(coords[6:8])
        points9 = self.get_points_from_coords(coords[7:9])

        graph2 = DiscreteGraphFromSetPoints(points2,color=ORANGE)
        graph3 = DiscreteGraphFromSetPoints(points3,color=ORANGE)
        graph4 = DiscreteGraphFromSetPoints(points4,color=ORANGE)
        graph5 = DiscreteGraphFromSetPoints(points5,color=ORANGE)
        graph6 = DiscreteGraphFromSetPoints(points6,color=ORANGE)
        graph7 = DiscreteGraphFromSetPoints(points7,color=ORANGE)
        graph8 = DiscreteGraphFromSetPoints(points8,color=ORANGE)
        graph9 = DiscreteGraphFromSetPoints(points9,color=ORANGE)

        dots1 = self.get_dots_from_coords(coords[0:1])
        dots2 = self.get_dots_from_coords(coords[0:2])
        dots3 = self.get_dots_from_coords(coords[1:3])
        dots4 = self.get_dots_from_coords(coords[2:4])
        dots5 = self.get_dots_from_coords(coords[3:5])
        dots6 = self.get_dots_from_coords(coords[4:6])
        dots7 = self.get_dots_from_coords(coords[5:7])
        dots8 = self.get_dots_from_coords(coords[6:8])
        dots9 = self.get_dots_from_coords(coords[7:9])
        

        self.play(FadeIn(dots1, run_time=1))

        self.play(ShowCreation(graph2,run_time=1))
        self.play(FadeIn(dots2, run_time=1))
        
        self.play(ShowCreation(graph3,run_time=1))
        self.play(FadeIn(dots3, run_time=1))
        
        self.play(ShowCreation(graph4,run_time=1))
        self.play(FadeIn(dots4, run_time=1))
        
        self.play(ShowCreation(graph5,run_time=1))
        self.play(FadeIn(dots5, run_time=1))

        self.play(ShowCreation(graph6,run_time=1))
        self.play(FadeIn(dots6, run_time=1))

        self.play(ShowCreation(graph7,run_time=1))
        self.play(FadeIn(dots7, run_time=1))
        
        self.play(ShowCreation(graph8,run_time=1))
        self.play(FadeIn(dots8, run_time=1))
        
        self.play(ShowCreation(graph9,run_time=1))
        self.play(FadeIn(dots9, run_time=1))
            
    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.add_numbers(*[0,1,2,3,4,5,6,7,8,9])
        init_label_y = 0
        end_label_y = 6000
        step_y = 1000
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        self.play(Write(self.x_axis),Write(self.y_axis))
