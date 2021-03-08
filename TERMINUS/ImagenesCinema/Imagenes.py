from manimlib.imports import *
from manimCSV import *

class ImagenTwo(GraphScene):
    centro = np.array((-4,-3.5,0))
    CONFIG = {
        "y_max" : 6000,
        "y_min" : 0,
        "x_max" : 9,
        "x_min" : 0,
        "y_tick_frequency" : 1000,
        "axes_color" : WHITE,
        "graph_origin" : centro,
         "x_axis_label" : "$x$",
        "y_axis_label" : "$y$", 
    }

    def construct(self):
        fondo = ImageMobject("/home/jazzzfm/ManimOld/Fondos/dark.jpg")
        fondo.scale(4)
        self.add(fondo)
        
        centro = np.array([-4,-4,0])
        self.setup_axes()
        #self.wait()
        
        A = Vector(np.array([0,4,0]))
        A.set_color(BLUE)
        A.move_to(np.array((-4,-1.5,0)))
        
        B = Vector(np.array([7.416,3,0]))
        B.set_color(GREEN)
        B.move_to(np.array([-0.25, 2.0,0]))
        
        R = Vector(np.array([7.5, 7, 0]))
        R.set_color(RED)
        R.move_to(np.array([-0.3, 0, 0]))
        
        angle_1 = Arc(  radius = 1.5,
                        arc_center = centro,
                        start_angle = (0.33)*PI,
                        angle = (0.17)*PI,
                        color = "RED")
        
        angle_2 = Arc(  radius = 1.5,
                        arc_center = centro + np.array([0, 5, 0]),
                        start_angle = (3/2)*PI,
                        angle = (1/2 + 0.01)*PI,
                        color = "GREEN")
        
        angle_3 = Arc(  radius = 1.0,
                        arc_center = centro + np.array([0, 5, 0]),
                        start_angle = (1/2)*PI,
                        angle = -(1/2 + 0.01)*PI,
                        color = "BLUE")
        
        A_tex = TextMobject("\\textbf{A}")
        A_tex.set_color(BLUE)
        A_tex.scale(1.3)
        A_tex.move_to(A.get_center() + np.array([-0.7, 0.4, 0]))
        
        B_tex = TextMobject("\\textbf{B}")
        B_tex.set_color(GREEN)
        B_tex.scale(1.3)
        B_tex.move_to(B.get_center() + np.array([0.0, 0.7, 0]))
                
        R_tex = TextMobject("\\textbf{R}")
        R_tex.set_color(RED)
        R_tex.scale(1.3)
        R_tex.move_to(R.get_center() + np.array([0.9, 0.0, 0]))
        
        alpha = TexMobject("\\mathbf{\\alpha} = 135^{\\circ}")
        alpha.set_color(RED)
        alpha.scale(1.4)
        alpha.move_to(A.get_end() + np.array([2.8, 0.1, 0.0]))
        
        beta = TexMobject("\\beta = 30.41^{\\circ}")
        beta.set_color(RED)
        beta.scale(1.3)
        beta.move_to(centro + np.array([2.5, 1.0, 0]))
        
        number_1 = TexMobject("135^{\\circ}")
        number_1.set_color(WHITE)
        number_1.scale(1.3)
        number_1.move_to(centro + np.array([1.5, 1.0, 0]))

        number_2 = TexMobject("45^{\\circ}")
        number_2.set_color(WHITE)
        number_2.scale(1.3)
        number_2.move_to(A.get_end() + np.array([1.5, 1.5, 0]))
        
        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/T20a.png")
        image.scale(0.8)
        image.set_color(WHITE)
        image.move_to(np.array([5, -1, 0]))
        self.add(image)
        
        self.add(A,
                  A_tex,
                  B,
                  B_tex,
                  R,
                  R_tex,
                  angle_1,
                  angle_2,
                  angle_3,
                  alpha,
                  beta,
                  number_2
                  )
        
        #self.wait()
        
    def setup_axes(self):
        GraphScene.setup_axes(self)
        # Y parametters
        init_label_y = 0
        end_label_y = 6000
        step_y = 1000
        self.y_axis.label_direction = LEFT
        self.add(self.x_axis, self.y_axis)

class ImagenThree(GraphScene):
    centro = np.array((-4,-2.0,0))
    CONFIG = {
        "y_max" : 6000,
        "y_min" : 0,
        "x_max" : 9,
        "x_min" : 0,
        "y_tick_frequency" : 1000,
        "x_leftmost_tick" : 11,
        "axes_color" : WHITE,
        "graph_origin" : centro,
         "x_axis_label" : "$x$",
        "y_axis_label" : "$y$", 
    }

    def construct(self):
        fondo = ImageMobject("/home/jazzzfm/ManimOld/Fondos/dark.jpg")
        fondo.scale(4)
        self.add(fondo)
        
        centro = np.array([-4,-2.0,0])
        self.setup_axes()
        #self.wait()
        
        A = Vector(np.array([6,3,0]))
        A.set_color(ORANGE)
        A.move_to(np.array((-1,-0.5,0)))
        
        L = Line(start = centro, end = centro + np.array([4, 0, 0]))
        L.set_color(BLUE)
        
        B = Vector(np.array([2.4, -4.47, 0]))
        B.set_color(PURPLE)
        B.move_to(A.get_end() + np.array([1.2,-2.25,0]))
        
        R = Vector(np.array([8.4, -1.5, 0]))
        R.set_color(RED)
        R.move_to(np.array([0.2, -2.8, 0]))
        
        C = Arc(    radius = 1.9,
                    arc_center = centro,
                    start_angle = 0,
                    angle = (1.95)*PI,
                    color = "RED")
        
        angle_2 = Arc(  
                    radius = 4.0,
                    arc_center = centro,
                    start_angle = 0,
                    angle = -(0.055)*PI,
                    color = "BLUE")
        
        A_tex = TextMobject("\\textbf{A}")
        A_tex.set_color(ORANGE)
        A_tex.scale(1.3)
        A_tex.move_to(A.get_center() + np.array([-0.7, 0.4, 0]))
        
        B_tex = TextMobject("\\textbf{B}")
        B_tex.set_color(PURPLE)
        B_tex.scale(1.3)
        B_tex.move_to(B.get_center() + np.array([0.5, 0.7, 0]))
                
        R_tex = TexMobject("\\textbf{R}")
        R_tex.set_color(RED)
        R_tex.scale(1.3)
        R_tex.move_to(R.get_center() + np.array([0.9, -0.5, 0]))
        
        alpha = TexMobject("\\theta '")
        alpha.set_color(BLUE)
        alpha.scale(1.4)
        alpha.move_to(R.get_center() + np.array([0.5, 0.4, 0.0]))
        
        beta = TexMobject("\\theta")
        beta.set_color(RED)
        beta.scale(1.3)
        beta.move_to(centro + np.array([-1.5, 2.0, 0]))
        
        number_1 = TexMobject("135^{\\circ}")
        number_1.set_color(WHITE)
        number_1.scale(1.3)
        number_1.move_to(centro + np.array([1.5, 1.0, 0]))

        number_2 = TexMobject("45^{\\circ}")
        number_2.set_color(WHITE)
        number_2.scale(1.3)
        number_2.move_to(A.get_end() + np.array([1.5, 1.5, 0]))
        
        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/T20a.png")
        image.scale(0.8)
        image.set_color(WHITE)
        image.move_to(np.array([5, 1, 0]))
        self.add(image)
        
        self.add(
                C,
                L,
                angle_2,
                A,
                A_tex,
                B,
                B_tex,
                R,
                R_tex,
                alpha,
                beta,
                  )
        
        #self.wait()
        
    def setup_axes(self):
        GraphScene.setup_axes(self)
        # Y parametters
        init_label_y = 0
        end_label_y = 6000
        step_y = 1000
        self.y_axis.label_direction = LEFT
        self.add(self.x_axis, self.y_axis)

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
# LEARN MORE HERE:
# https://www.youtube.com/watch?v=Xi52tx6phRU


#        _         _                  _   
#   __ _| |__  ___| |_ _ __ __ _  ___| |_ 
#  / _` | '_ \/ __| __| '__/ _` |/ __| __|
# | (_| | |_) \__ \ |_| | | (_| | (__| |_ 
#  \__,_|_.__/|___/\__|_|  \__,_|\___|\__|
#   ___  ___ ___ _ __   ___  ___ 
#  / __|/ __/ _ \ '_ \ / _ \/ __|
#  \__ \ (_|  __/ | | |  __/\__ \
#  |___/\___\___|_| |_|\___||___/
# Abstract scenes

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

#       _                         
#   ___| | __ _ ___ ___  ___  ___ 
#  / __| |/ _` / __/ __|/ _ \/ __|
# | (__| | (_| \__ \__ \  __/\__ \
#  \___|_|\__,_|___/___/\___||___/
# This classes returns graphs
class DiscreteGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_as_corners(set_of_points)

class SmoothGraphFromSetPoints(VMobject):
    def __init__(self,set_of_points,**kwargs):
        super().__init__(**kwargs)
        self.set_points_smoothly(set_of_points)

#   ___  ___ ___ _ __   ___  ___ 
#  / __|/ __/ _ \ '_ \ / _ \/ __|
#  \__ \ (_|  __/ | | |  __/\__ \
#  |___/\___\___|_| |_|\___||___/
# Graph with set of points
class CustomGraph1(GraphFromData):
    def construct(self):
        self.setup_axes()
        coords = get_coords_from_csv("custom_graphs/data")
        dots = self.get_dots_from_coords(coords)
        self.add(dots)

# Discrete Graph
class CustomGraph2(GraphFromData):
    def construct(self):
        self.setup_axes()
        # Get coords
        coords = get_coords_from_csv("custom_graphs/data")
        points = self.get_points_from_coords(coords)
        # Set graph
        graph = DiscreteGraphFromSetPoints(points,color=ORANGE)
        # Set dots
        dots = self.get_dots_from_coords(coords)
        self.add(dots)
        self.play(ShowCreation(graph,run_time=4))
        self.wait(3)

# Smooth graph
class ImagenTen(GraphFromData):
    centro = np.array((-4,-3,0))
    CONFIG = {
        "y_max" : 30,
        "y_min" : 0,
        "x_max" : 10,
        "x_min" : 0,
        "y_tick_frequency" : 5,
        "axes_color" : WHITE,
        "graph_origin" : centro,
        "x_axis_label" : "$t(min)$",
        "y_axis_label" : "$x(m)$", 
    }
    def construct(self):
        fondo = ImageMobject("/home/jazzzfm/ManimOld/Fondos/dark.jpg")
        fondo.scale(4)
        self.add(fondo)
        
        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/T20a.png")
        image.scale(0.8)
        image.set_color(WHITE)
        image.move_to(np.array([5, -1, 0]))
        self.add(image)
        
        Table = ImageMobject("/home/jazzzfm/ManimOld/Fondos/Imagen10.png")
        Table.scale(2)
        Table.set_color(WHITE)
        Table.move_to(np.array([5, 1.8  , 0]))
        self.add(Table)
        
        centro = np.array([-4,-3,0])
        self.setup_axes()
        x = [0 , 1, 2, 3,  4,  5,  6]
        y = [0, 13 , 16, 17, 17.5, 18, 20]

        coords = [[px,py] for px,py in zip(x,y)]
        points = self.get_points_from_coords(coords)
        graph = SmoothGraphFromSetPoints(points,color=GREEN)
        dots = self.get_dots_from_coords(coords)
        #T = TexMobject("T (min)"," 0 " ," 1  "," 2 "," 3  "," 4  "," 5  "," 6 ")
        #X = TexMobject("x (m)", " 0 " , " 13 ", " 16 ", " 17 ", " 17.5", " 18  ", " 20  ")
        #T.move_to(centro + np.array([2, 4, 0]))
        # X.move_to(centro + np.array([2, 3.5, 0]))

        self.add(graph,dots)
        
    def setup_axes(self):
        # Add this line
        GraphScene.setup_axes(self) 
        # Parametters of labels
        #   For x
        init_label_x = 2
        end_label_x = 6
        step_x = 2
        #   For y
        init_label_y = 5
        end_label_y = 20
        step_y = 5
        # Position of labels
        #   For x
        self.x_axis.label_direction = DOWN #DOWN is default
        #   For y
        self.y_axis.label_direction = LEFT
        # Add labels to graph
        #   For x
        self.x_axis.add_numbers(*range(
                                        init_label_x,
                                        end_label_x+step_x,
                                        step_x
                                    ))
        #   For y
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        self.add(self.x_axis, self.y_axis)



class ImagenTenV2(GraphScene):
    centro = np.array((-4,-3.5,0))
    CONFIG = {
        "y_max" : 30,
        "y_min" : 0,
        "x_max" : 10,
        "x_min" : 0,
        "y_tick_frequency" : 1,
        "axes_color" : WHITE,
        "graph_origin" : centro,
        "x_axis_label" : "$x$",
        "y_axis_label" : "$y$", 
    }

    def construct(self):
        fondo = ImageMobject("/home/jazzzfm/ManimOld/Fondos/dark.jpg")
        fondo.scale(4)
        self.add(fondo)
        

        centro = np.array([-4,-4,0])
        self.setup_axes()
        coords = self.return_coords_from_csv("TERMINUS/ImagenesCinema/data")
        dots = VGroup(*[Dot().move_to(self.coords_to_point(coord[0],coord[1])) for coord in coords])
        path = VMobject()
        #path.set_points_smoothly([[ (1,2)][set_points(2,3)]])
        #self.add(path)
        self.add(dots)

    def return_coords_from_csv(self,file_name):
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


    def setup_axes(self):
        GraphScene.setup_axes(self)
        # Y parametters
        init_label_y = 0
        end_label_y = 30
        step_y = 1
        self.y_axis.label_direction = LEFT
        self.add(self.x_axis, self.y_axis)


class ImagenTreceA(Scene):
    def construct(self):
        def linea(x):
            y = 1.138*(x) + 2.559
            return y 

        fondo = ImageMobject("/home/jazzzfm/ManimOld/Fondos/dark.jpg")
        fondo.scale(4)
        self.add(fondo)
        
        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/T20a.png")
        image.scale(0.8)
        image.set_color(WHITE)
        image.move_to(np.array([-5, 3, 0]))
        
        x_i = np.array([ -5.5, -3.7, 0])
        x_f = np.array([ 1.5, 4.26, 0])
        
        L = Line(x_i, x_f, stroke_width = 3, color = BLUE)
        self.add(L, image) 
        
        dot = []
        for i in range(-5, 1):
            dot.append(Dot())
        
        

        L_1 = Line(np.array([-5, linea(-5),0]),
                   np.array([-3, linea(-3),0]), 
                   stroke_width = 10, color = BLUE)
        

        L_2 = Line(np.array([-1, linea(-1), 0]),
                   np.array([1, linea(1), 0]), 
                   stroke_width = 10, color = GREEN)
        
        self.add(L_1, L_2)
            
        dot[-4].move_to(np.array([-5, linea(-5), 0]))
        self.add(dot[-4])
        
        uno = TexMobject("1")
        uno.move_to([-3.5, linea(-3), 0])
            
        dot[-3].move_to(np.array([-3, linea(-3), 0]))
        self.add(uno, dot[-3])
        
        dot[-1].move_to(np.array([-1, linea(-1), 0]))
        self.add(dot[-1])
        
        dot[-2].move_to(np.array([1, linea(1), 0]))
        self.add(dot[-2])
        
        dot[0].move_to(np.array([0, linea(0), 0]))
        self.add(dot[0])
        
        dos = TexMobject("2")
        dos.move_to(np.array([0.5, linea(0), 0]))

        Text_1 = TextMobject("Pendiente 1 (velocidad promedio)")
        Text_1.move_to(np.array([2.5, 0 , 0]))

        Text_2 = TextMobject("es igual a la pendiente 2")
        Text_2.move_to(np.array([2.5, -0.5, 0]))
        
        Text_3 = TextMobject("(velocidad instantánea)")
        Text_3.move_to(np.array([2.5, -1.0, 0 ]))

        self.add(dos, Text_1, Text_2, Text_3)


class ImagenTreceB(GraphScene):
    centro = np.array((-4,-3,0))
    CONFIG = {
        "y_max" : 6,
        "y_min" : 0,
        "x_max" : 6,
        "x_min" : 0,
        "x_tick_frequency" : 1,
        "y_tick_frequency" : 1,
        "axes_color" : WHITE,
        "graph_origin" : centro,
        "x_axis_label" : "$t$",
        "y_axis_label" : "$x$"
        }
    def construct(self):
        def parabola(x):
            y = -(0.7*x-2)**2 + 5
            return y 
        
        def linea(x):
            y = 5
            return y
        
        fondo = ImageMobject("/home/jazzzfm/ManimOld/Fondos/dark.jpg")
        fondo.scale(4)

        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/T20a.png")
        image.scale(0.8)
        image.set_color(WHITE)
        image.move_to(np.array([-5, 3, 0]))
        
        self.add(fondo, image)
        centro = np.array([-4,-3,0])
        self.setup_axes()
        
        graph = self.get_graph(lambda x : parabola(x), color = BLUE)
        lineaG = self.get_graph(lambda x : linea(x), color = GREEN)
        Dots = []
        
        for i in range(0, 8):
            Dots.append(Dot())

        Dots[0].move_to(centro + np.array([0, 1.0, 0.0]))
        Dots[1].move_to(centro + np.array([1, 2.65, 0.0]))
        Dots[2].move_to(centro + np.array([2, 3.85, 0.0]))
        Dots[3].move_to(centro + np.array([3, 4.65, 0.0]))
        Dots[4].move_to(centro + np.array([4, 5.0, 0.0])) 
        Dots[5].move_to(centro + np.array([5.1, 4.85, 0.0]))
        Dots[6].move_to(centro + np.array([6.4, 4.0, 0.0]))
        Dots[7].move_to(centro + np.array([7.3, 3.0, 0.0]))
        

        self.add(graph,
                 lineaG,
                 Dots[0],
                 Dots[1],
                 Dots[2],
                 Dots[3],
                 Dots[4],
                 Dots[5],
                 Dots[6],
                 Dots[7])
        
    def setup_axes(self):
        GraphScene.setup_axes(self)
        init_label_y = 0
        end_label_y = 6
        step_x = 1
        step_y = 1
        self.y_axis.label_direction = LEFT
        self.add(self.x_axis, self.y_axis)

class ImagenCatorce(GraphScene):
    CONFIG = {
        "y_max" : 14,
        "y_min" : 0,
        "x_max" : 10,
        "x_min" : 0,
        "y_tick_frequency" : 2,
        "x_tick_frequency" : 2,
        "axes_color" : WHITE, 
        "graph_origin" : np.array((-4,-3,0)),
        "x_axis_label" : "$t(s)$",
        "y_axis_label" : "$v(m/s)$",

    }

    def construct(self):
        fondo = ImageMobject("/home/jazzzfm/ManimOld/Fondos/dark.jpg")
        fondo.scale(4)

        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/T20a.png")
        image.scale(0.8)
        image.set_color(WHITE)
        image.move_to(np.array([-5.5, 2, 0]))

        self.add(fondo, image)
        self.setup_axes()

        graph = self.get_graph(lambda x :(4.0) + (x**2)/5.0, 
                                    color = BLUE,
                                    x_min = 0, 
                                    x_max = 7
                                    )

        dGraph = self.get_graph(lambda x :(1/5)*(8.0*x + 4.0), color = GREEN, x_min = -1, x_max = 8)
        
        A = Dot(np.array([-4.0, -1.3, 0.0]))
        B = Dot(np.array([-0.5,  0.0, 0.0]))
        A.set_color("#0000FF")
        B.set_color("#0000FF")
        
        A_tex = TextMobject("\\textbf{A}")
        B_tex = TextMobject("\\textbf{B}")
        A_tex.move_to(np.array([ -3.7, -1.6, 0.0]))
        B_tex.move_to(np.array([ -0.6, 0.5, 0.0]))
        
        L = Line(np.array([-4.0, -1.3, 0.0]), np.array([-0.5,  0.0, 0.0]))
        L.set_color(RED)
        self.add(graph, dGraph, L, A, A_tex, B, B_tex)

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.add_numbers(*[0,2,4,6,8])
        init_label_y = 2
        end_label_y = 12
        step_y = 2
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        self.play(Write(self.x_axis),Write(self.y_axis))

class Imagen16(GraphScene):
    def construct(self):
        fondo = ImageMobject("/home/jazzzfm/ManimOld/Fondos/dark.jpg")
        fondo.scale(4)

        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/T20a.png")
        image.scale(0.8)
        image.set_color(WHITE)
        image.move_to(np.array([-5.5, 3.0, 0]))
        
        self.add(fondo, image)
        
        x_i = np.array([-5.5, 0.0, 0.0])
        x_f = np.array([ 5.5, 0.0, 0.0])

        X_i = Dot(x_i).set_color(BLUE)
        X_f = Dot(x_f).set_color(BLUE)
        
        B = Dot(x_f + np.array([-1.3, 0.0, 0.0])).set_color(BLUE)
        B_tex = TextMobject("\\textbf{B}").move_to(B.get_center() + np.array([0.0, 0.5, 0.0]))
        B_tex.scale(0.8)

        A = Dot(x_f + np.array([-3.5, 0.0, 0.0])).set_color(BLUE)
        A_tex = TextMobject("\\textbf{A}").move_to(A.get_center() + np.array([0.0, 0.5, 0.0]))
        A_tex.scale(0.8)
        
        line2 = Line(B.get_center(), X_f.get_center()).set_color(RED)

        xi_tex = TexMobject("x_{i}").move_to(x_i + np.array([-0.5, 0.0, 0.0]))
        xf_tex = TexMobject("x_{f}").move_to(x_f + np.array([0.5, 0.0, 0.0]))

        line = Line(X_i.get_center(), X_f.get_center()).set_color(BLUE)
        b1 = Brace(line, direction=line.copy().rotate(PI/2).get_unit_vector()).set_color(WHITE)
        b1.move_to(np.array([0.0, 1.0, 0.0]))

        b1text = TextMobject("2000 m recorridos por la moto").move_to(np.array([0.0, 1.5, 0.0]))
        b1text.scale(0.8)
        
        line3 = Line(X_i.get_center(), A.get_center())
        b2 = Brace(line3).set_color(WHITE)
        texto1 = b2.get_text("1500 m recorridos por el auto")
        texto1.scale(0.8)

        line4 = Line(A.get_center(), X_f.get_center())
        b3 = Brace(line4).set_color(WHITE)
        texto2 = b3.get_text("últimos 500 m")
        texto2.scale(0.8)
    
        self.add(X_i, xi_tex, xf_tex, line, b1,
                 b1text, line2, B, A, A_tex, B_tex,
                 b2, b3, texto1, texto2, X_f)

class Imagen17A(GraphScene):
    CONFIG = {
        "y_max" : 5,
        "y_min" : 0,
        "x_max" : 5,
        "x_min" : 0,
        "y_tick_frequency" : 1,
        "x_tick_frequency" : 1,
        "axes_color" : WHITE,
        "graph_origin" : np.array((-4,-3,0)),
        "x_axis_label" : "$t(s)$",
        "y_axis_label" : "$a(m/s^2)$"
    }
    def construct(self):
        fondo = ImageMobject("/home/jazzzfm/ManimOld/Fondos/dark.jpg")
        fondo.scale(4)

        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/T20a.png")
        image.scale(0.8)
        image.set_color(WHITE)
        image.move_to(np.array([-5.5, 3.0, 0]))

        self.add(fondo, image)

        self.setup_axes()
        graph = self.get_graph(lambda x : 1.0, color = BLUE, x_min = 0, x_max = 5)
        dots = []
        
        for i in range(1, 7):
            dots.append(Dot())
        for i in range(1, 6):
            dots[i].move_to(np.array((-4,-3,0)) + np.array((i*1.8,1.2,0)))    
        self.add(graph)
        for i in  range(1, 6):
            self.add(dots[i])

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.add_numbers(*[0,1,2,3,4,5])
        init_label_y = 1
        end_label_y = 5
        step_y = 1
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        self.play(Write(self.x_axis),Write(self.y_axis))

class Imagen17A(GraphScene):
    CONFIG = {
        "y_max" : 25,
        "y_min" : 0,
        "x_max" : 5,
        "x_min" : 0,
        "y_tick_frequency" : 5,
        "x_tick_frequency" : 1,
        "axes_color" : WHITE,
        "graph_origin" : np.array((-4,-3,0)),
        "x_axis_label" : "$t(s)$",
        "y_axis_label" : "$x(m)$"
    }
    def construct(self):
        fondo = ImageMobject("/home/jazzzfm/ManimOld/Fondos/dark.jpg")
        fondo.scale(4)

        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/T20a.png")
        image.scale(0.8)
        image.set_color(WHITE)
        image.move_to(np.array([-5.5, 3.0, 0]))

        self.add(fondo, image)

        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = BLUE, x_min = 0, x_max = 5)
        dots = []

        for i in range(1, 7):
            dots.append(Dot())
        for i in range(1, 6):
            dots[i].move_to(np.array((-4,-3,0)) + np.array((1.8*i,0.24*(i*i),0)))
        self.add(graph)
        for i in  range(1, 6):
            self.add(dots[i])

    def setup_axes(self):
        GraphScene.setup_axes(self)
        init_label_y = 0
        end_label_y = 25
        step_y = 5
        self.y_axis.label_direction = LEFT
        self.play(Write(self.x_axis),Write(self.y_axis))

class Imagen17B(GraphScene):
    CONFIG = {
        "y_max" : 5,
        "y_min" : 0,
        "x_max" : 5,
        "x_min" : 0,
        "y_tick_frequency" : 1,
        "x_tick_frequency" : 1,
        "axes_color" : WHITE,
        "graph_origin" : np.array((-4,-3,0)),
        "x_axis_label" : "$t(s)$",
        "y_axis_label" : "$v(m/s)$"
    }
    def construct(self):
        fondo = ImageMobject("/home/jazzzfm/ManimOld/Fondos/dark.jpg")
        fondo.scale(4)

        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/T20a.png")
        image.scale(0.8)
        image.set_color(WHITE)
        image.move_to(np.array([-5.5, 3.0, 0]))

        self.add(fondo, image)

        self.setup_axes()
        graph = self.get_graph(lambda x : (0.7*x) + 1.5, color = BLUE, x_min = 0, x_max = 5)
        dots = []

        for i in range(-1, 7):
            dots.append(Dot())
        for i in range(-1, 6):
            dots[i].move_to(np.array((-4,-3,0)) + np.array((1.8*i,0.84*i + 1.8 ,0)))
        self.add(graph)
        for i in  range(0, 6):
            self.add(dots[i])

    def setup_axes(self):
        GraphScene.setup_axes(self)
        init_label_y = 0
        end_label_y = 5
        step_y = 1
        self.y_axis.label_direction = LEFT
        self.play(Write(self.x_axis),Write(self.y_axis))

class Imagen22(GraphScene):
    CONFIG = {
        "y_max" : 6,
        "y_min" : -2,
        "x_max" : 3,
        "x_min" : -2,
        "y_tick_frequency" : 1,
        "x_tick_frequency" : 1,
        "axes_color" : WHITE,
        "graph_origin" : np.array((-2,-1,0)),
        "x_axis_label" : "$t(s)$",
        "y_axis_label" : "$v(m/s)$"
    }
    def construct(self):
        fondo = ImageMobject("/home/jazzzfm/ManimOld/Fondos/dark.jpg")
        fondo.scale(4)

        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/T20a.png")
        image.scale(0.8)
        image.set_color(WHITE)
        image.move_to(np.array([-5.5, 3.0, 0]))

        self.add(fondo, image)

        self.setup_axes()
        graph = self.get_graph(lambda x : -5*x*(x-2), color = BLUE, x_min = -0.3, x_max = 2.3)
        dots = []

        self.add(graph)

    def setup_axes(self):
        GraphScene.setup_axes(self)
        init_label_y = 0
        end_label_y = 25
        step_y = 5
        self.y_axis.label_direction = LEFT
        self.play(Write(self.x_axis),Write(self.y_axis))


class Imagen23(GraphScene):
    CONFIG = {
        "y_max" :  6,
        "y_min" : -2,
        "x_max" :  3,
        "x_min" : -2,
        "y_tick_frequency" : 1,
        "x_tick_frequency" : 1,
        "axes_color" : WHITE,
        "graph_origin" : np.array((-2,-1,0)),
        "x_axis_label" : "$t(s)$",
        "y_axis_label" : "$a(m/s^2)$"
        }
    def construct(self):
        fondo = ImageMobject("/home/jazzzfm/ManimOld/Fondos/dark.jpg")
        fondo.scale(4)

        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/T20a.png")
        image.scale(0.8)
        image.set_color(WHITE)
        image.move_to(np.array([-5.5, 3.0, 0]))

        self.add(fondo, image)

        self.setup_axes()
        graph = self.get_graph(lambda x : -10*x + 10, color = BLUE, x_min = 0.5, x_max = 1.3)
        dots = []
        self.add(graph)

    def setup_axes(self):
        GraphScene.setup_axes(self)
        init_label_y = 0
        end_label_y = 5
        step_y = 1
        self.y_axis.label_direction = LEFT
        self.play(Write(self.x_axis),Write(self.y_axis))

class Imagen24(GraphScene):
    CONFIG = {
        "y_max" :  10,
        "y_min" : -1,
        "x_max" :  5,
        "x_min" : -5,
        "y_tick_frecuency" : 1,
        "axes_color" : WHITE,
        "graph_orgin" : np.array([4, -1, 0]),
        "x_axis_label" : "t(s)",
        "y_axis_label" : "x(m)"
        }
    def construct(self):
        fondo = ImageMobject("/home/jazzzfm/ManimOld/Fondos/dark.jpg")
        fondo.scale(4)
        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/T20a.png")
        image.scale(0.8)
        image.set_color(WHITE)
        image.move_to(np.array([-5.5, 3.0, 0]))

        self.add(fondo, image)
        self.setup_axes()
        graph = self.get_graph(lambda x : ((-5/3)*x*x*x) + 5*(x*x), color = BLUE, x_min = -10, x_max = 10)
        self.add(graph)

    def setup_axes(self):
        GraphScene.setup_axes(self)
        init_label_y = -1
        end_label_y = 10
        step_y = 1
        self.y_axis.label_direction = LEFT
        self.play(Write(self.x_axis),Write(self.y_axis))
