from manimlib.imports import *
import numpy as np

class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": "#FFFFFF",
        "axis_color": "#FFFFFF",
        "axis_stroke": 2,
        "labels_scale": 0.5,
        "labels_buff": 0,
        "number_decimals": 2
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = TextMobject(f"{coord_point}").scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes)


def coord(x,y,z=0):
    return np.array([x,y,z])

def Vector3D(x, y, z):
    return np.array([x, y, z])

def getX(mob):
    return mob.get_center()[0]

def getY(mob):
    return mob.get_center()[1]

# Abstract class:
class PathScene(Scene):
    CONFIG = {
        "x_coords":[0,  1, 3,  -2, -3],
        "y_coords":[3, -2, 1, 2.5, -1]
    }
    """
    The setup method it is executed before the construct method, 
    so whatever they write in the setup method will be executed 
    before the construct method
    """
    def setup(self):
        self.screen_grid = ScreenGrid()
        # tuples = [(0,3),(1,-2)...]
        self.tuples = list(zip(self.x_coords,self.y_coords))

        dots,labels,numbers = self.get_all_mobs()
        self.add(self.screen_grid,dots,labels,numbers)

    def get_dots(self,coords):
        # This is called list comprehension, learn to use it here:
        # https://www.youtube.com/watch?v=AhSvKGTh28Q
        dots = VGroup(*[Dot(coord(x,y)) for x,y in coords])
        return dots

    def get_dot_labels(self,dots,direction=RIGHT):
        labels = VGroup(*[
            # This is called f-strings, learn to use it here:
            # https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
            TexMobject(f"({getX(dot)},{getY(dot)})",height=0.3)\
                      .next_to(dot,direction,buff=SMALL_BUFF) 
                      # This is called Multi-line statement, learn how to use it here:
                      # https://www.programiz.com/python-programming/statement-indentation-comments
            for dot in dots
            ])
        return labels

    def get_dot_numbers(self,dots):
        numbers = VGroup(*[
            TextMobject(f"{n}",height=0.2).next_to(dot,DOWN,buff=SMALL_BUFF)
            for n,dot in zip(range(1,len(dots)+1),dots)
            ])
        return numbers

    def get_all_mobs(self):
        dots = self.get_dots(self.tuples)
        labels = self.get_dot_labels(dots)
        numbers = self.get_dot_numbers(dots)
        return dots,labels,numbers

class ShowPoints(PathScene):
    pass

class PathAsCorners(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_as_corners([*[coord(x,y) for x,y in self.tuples]])
        self.add(path)

class PathSmoothly(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_smoothly([*[coord(x,y) for x,y in self.tuples]])
        self.add(path)

class PathPoints(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_smoothly([*[coord(x,y) for x,y in self.tuples]])
        bezier_points = VGroup(*[Dot(coord,color=RED) for coord in path.points])
        self.add(path,bezier_points)

class AppendPoints(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_as_corners([*[coord(x,y) for x,y in self.tuples]])
        self.add(path)
        self.wait()
        new_points = np.array([coord(-5,1),coord(-1,1)])
        new_dots = self.get_dots(new_points[:,:2])
        """       Special atention to this: ----
        This is an slice, see: https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
        new_points = 
        [   Columns:
             0   1  2
            [-5  1  0]   <- Row 0
            [-1  1  0]   <- Row 1
                        ]
        So, the first ":" means all rows
        The ":2" means only take the elements from the first column to the second one,
        that is, the columns 0 and 1
        """
        new_labels = self.get_dot_labels(new_dots,UP)
        path.become(
            VMobject().set_points_as_corners([*path.points,*new_points])
        )
        # The most recent version have new methods that can do this more easy.
        VGroup(new_dots,new_labels).set_color(TEAL)
        self.add(new_dots,new_labels)
        self.wait(2)

class TransformPathStyle(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_as_corners([coord(3, 3), coord(-3, 3), coord(-3,-3), coord(3,-3)])
        self.add(path)
        self.play(path.make_smooth)
        self.wait()

Vanilla = "#F3E5AB"

class AnimationTwo(ThreeDScene):
    #Objetivo: Mostrar a partir de un punto en el plano 
    #           cómo se definen las razones trigonométricas 
#    CONFIG={
#        "camera_config":{"background_color" : Vanilla}
#    }
    # En un plano aparecer un punto. Construir el radio vector 
    # y las proyecciones a los ejes x y y. Luego mostrar el 
    # ángulo θ dentro del triángulo rectángulo formado. 
    # Listo :D
    
    def construct(self):
        BLUE2 = "#FFFFFF"
        image = ImageMobject("/home/codexreckoner/manim/media/designs/raster_images/FONDOCOLOR.jpg")
        image.scale(6)
        self.add(image)
        object = ScreenGrid()
        DL2 = np.array([-4,-2,0])
        DL3 = np.array([-2,0,0])
        self.play(FadeIn(object.move_to(DL2), run_time=3))
        self.wait()

        v = np.array([4,4,0])
        vx = np.array([0,-2,0])
        vy = np.array([0,2,0])
        
        hipo = Line(DL2, vy).set_opacity(3)
        hipo.set_color(BLUE2) # Esta linea se va convertir en texto
        punto = Dot(v).move_to(vy)
        punto.set_color(BLUE2)
        self.play(ShowCreation(punto))
        self.play(FadeIn(Vector(v, color=BLUE2).move_to(DL3), run_time=2))
        self.add(hipo)
        self.wait()

        proyx = DashedLine(DL2, vx).set_opacity(3)
        proyx1 = Line(DL2, vx).set_opacity(3) # Esta línea se va a convertir en texto
        proyx.set_color(BLUE2)
        proyx1.set_color(BLUE2)

        proyy = DashedLine(vx,vy).set_opacity(3)
        proyy1= Line(vx, vy).set_opacity(3) # Esta línea se va a convertir en texto
        proyy.set_color(BLUE2)
        proyy1.set_color(BLUE2)

        self.play(ShowCreation(proyx))
        self.play(ShowCreation(proyx1))
        self.play(ShowCreation(proyy))
        self.play(ShowCreation(proyy1))
        self.wait()

        #Primero poner el ángulo theta
        
        poq = np.array([0.8,0.3,0])

        chichi = TexMobject("\\theta")
        chichi.move_to(DL2 + poq)
        chichi.set_color(BLUE2)
        chichi.scale_in_place(1)
        self.play(Write(chichi))
        self.wait()

        ####################################
        
        thipo = TextMobject("hipotenusa")
        catetop = TextMobject("cateto opuesto")
        catetoa = TextMobject("cateto adyacente")

        r = TexMobject("r")
        co = TexMobject("y")
        ca = TexMobject("x")
                
        ###################################
        
        mover = {}
        mover[0] = np.array([-2.5,0,0])
        mover[1] = np.array([-2,-2.5,0])
        mover[2] = np.array([2,-0.5,0])
        mover[3] = np.array([-0.4,-0.8,0])
        mover[4] = np.array([5,1,0])
        
        thipo.shift(mover[0])
        r.shift(mover[0])
        catetoa.shift(mover[1])
        ca.shift(mover[1])
        catetop.shift(mover[2])
        co.shift(mover[2])

        thipo.set_color(BLUE2)
        r.set_color(BLUE2)
        catetop.set_color(BLUE2)
        co.set_color(BLUE2)
        catetoa.set_color(BLUE2)
        ca.set_color(BLUE2)

        thipo.rotate(PI/4) #El centro es el centro de area del texto, en radianes, texto u objeto
        r.rotate(PI/4)
        
        
        self.play(FadeOut(thipo), run_time=2)
        self.play(FadeOut(catetop), run_time=2)
        self.play(FadeOut(catetoa), run_time=2)
        self.wait(1)
        
        title = TexMobject("P(x,y)","=","P(r,\\theta)")
        title.move_to(UP + np.array([1,1.5,0]))
        title.set_color(BLUE2) 
        self.play(Write(title[0]))

        self.play(Transform(hipo,r))
        self.play(Transform(proyx1, ca))
        self.play(Transform(proyy1, co.move_to(np.array([-0.5,0,0]))))
        self.wait(2)

        ####################################################################
        # Mostrar sen θ a la derecha del diagrama.
        # Resaltar la proyección de y, es decir la línea punteada vertical, 
        # que es igual al cateto opuesto al ángulo. 
        # Y llevarla al otro lado de la expresión sen θ
        # Luego resaltar la hipotenusa y llevarla al denominador.
        # Finalmente mostrar a la derecha la razón sen θ=
        # Listo! :D

        seno = TexMobject("sen(\\theta)","=","{y","\\over"," r}")
        seno.shift(mover[4])
        seno.set_color(BLUE2)
        self.play(Write(seno[0]))
        self.play(Write(seno[1]))
        self.play(Write(seno[3]))
        self.wait(1) 
        
        self.play(ReplacementTransform(co.copy(), seno[2]), run_time=2)
        self.play(ReplacementTransform(r.copy(), seno[4]), run_time=2)
        self.wait()
        
        despeje_1 = TexMobject("r sen(\\theta)","=","y")
        despeje_1.set_color(BLUE2)
        despeje_1.move_to(mover[4])
        self.play(ReplacementTransform(seno, despeje_1))
        self.wait(1)
        
        ############################################################
        # Repetir el proceso para las siguientes 2 razones.
        # Listo! :D

        #coseno

        coseno = TexMobject("cos(\\theta)", "=","{x","\\over","r}")
        coseno.shift(mover[4])
        coseno.set_color(BLUE2)
        self.play(ReplacementTransform(despeje_1, coseno[0]))
        self.play(Write(coseno[1]))
        self.play(Write(coseno[3]))
        self.wait(1)
        
        self.play(ReplacementTransform(ca.copy(), coseno[2]), run_time=2)
        self.play(ReplacementTransform(r.copy(), coseno[4]), run_time=2)
        self.wait(1)

        despeje_2 = TexMobject("r cos(\\theta)","=","x")
        despeje_2.set_color(BLUE2)
        despeje_2.move_to(mover[4])
        self.play(ReplacementTransform(coseno, despeje_2))
        self.wait(1)
        
        #tangente

        tang = TexMobject("tan(\\theta)", "=","{y", "\\over", "x}")
        tang.shift(mover[4])
        tang.set_color(BLUE2)
        self.play(ReplacementTransform(despeje_2, tang[0]))
        self.play(Write(tang[1]))
        self.play(Write(tang[3]))
        self.wait(1)
        
        self.play(ReplacementTransform(co.copy(), tang[2]), run_time=2)
        self.play(ReplacementTransform(ca.copy(), tang[4]), run_time=2)
        self.wait(1)

        despeje_3 = TexMobject("x tan(\\theta)","=","y")
        despeje_3.set_color(BLUE2)
        despeje_3.move_to(mover[4])
        self.play(ReplacementTransform(tang,despeje_3))
        self.play(FadeOut(despeje_3))
        self.wait(1)

        ##########################################################################
        # Luego despejar de esas el ángulo y obtener θ=sen-1 yr,  θ=cos-1 xr,  θ=tan-1 yx
        # Listo! :D

        seno = TexMobject("sen(\\theta)","=","{y","\\over"," r}")
        seno.set_color(BLUE2)
        seno.move_to(np.array([3.5, 1,0]))
        igualar_1 = TexMobject("arcsen(sen(\\theta))","=","arcsen({y \\over r})")
        despeje_4 = TexMobject("\\theta")
        despeje_4.set_color(BLUE2)
        igualar_1.set_color(BLUE2)
        despeje_4.shift(np.array([3.5,1,0]))
        igualar_1.shift(np.array([3.5,1,0]))

        self.play(Write(seno))
        self.play(ReplacementTransform(seno, igualar_1), run_time=2)
        self.play(ReplacementTransform(igualar_1[0], despeje_4), run_time=2)
        self.wait(2)
        self.play(FadeOut(igualar_1))
        self.play(FadeOut(despeje_4))

        
        coseno = TexMobject("cos(\\theta)","=","{x","\\over"," r}")
        coseno.set_color(BLUE2)
        coseno.move_to(np.array([3.5, 1,0]))
        igualar_2 = TexMobject("arcos(cos(\\theta))","=","arcos({x \\over r})")
        despeje_5 = TexMobject("\\theta")
        despeje_5.set_color(BLUE2)
        igualar_2.set_color(BLUE2)
        despeje_5.shift(np.array([3.5,1,0]))
        igualar_2.shift(np.array([3.5,1,0]))

        self.play(Write(coseno))
        self.play(ReplacementTransform(coseno, igualar_2), run_time=2)
        self.play(ReplacementTransform(igualar_2[0], despeje_5), run_time=2)
        self.wait(2)
        self.play(FadeOut(igualar_2))
        self.play(FadeOut(despeje_5))

        tan = TexMobject("tan(\\theta)","=","{y","\\over"," x}")
        tan.set_color(BLUE2)
        tan.move_to(np.array([3.5, 1,0]))
        igualar_3 = TexMobject("arctan(tan(\\theta))","=","arctan({y \\over x})")
        despeje_6 = TexMobject("\\theta")
        despeje_6.set_color(BLUE2)
        igualar_3.set_color(BLUE2)
        despeje_6.shift(np.array([3.5,1,0]))
        igualar_3.shift(np.array([3.5,1,0]))

        self.play(Write(tan))
        self.play(ReplacementTransform(tan, igualar_3), run_time=2)
        self.play(ReplacementTransform(igualar_3[0], despeje_6), run_time=2)
        self.wait(2)
        
        ####################################################################################3
        # Para que al final x, y se iguale a  r, θ y así explicar las coordenadas polares del punto en cuestión.
        # Listo! :D

        Teorem = TextMobject("Por el Teorema de Pitágoras")
        R = TexMobject("r^{2} = x^{2} + y^{2}")
        R2 = TexMobject("r = \\sqrt{x^{2} + y^{2}}")   
        
        Teorem.move_to(np.array([3.5, -1, 0]))
        R.shift(np.array([5,-1,0]))
        R2.shift(np.array([5,-1,0]))
        R.set_color(BLUE2)
        R2.set_color(BLUE2)
        Teorem.set_color(BLUE2)
        
        self.play(Write(Teorem))
        self.play(ReplacementTransform(Teorem, R), run_time=2)
        self.play(ReplacementTransform(R, R2), run_time=2)
        self.wait(2)
        
        self.play(Write(title[1]))
        self.play(Write(title[2]))

        self.wait(4)

        # Final c':