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
        "grid_color": BLUE,
        "axis_color": RED,
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

Vanilla = "#F3E5AB"

class AnimationThree(ThreeDScene):
    
    #Objetivo: Mostrar en una sola animación, la igualdad,
    # suma, resta y multiplicación de vectores.

#    CONFIG={
 #       "camera_config":{"background_color" : Vanilla}
  #  }

    def construct(self):
        # Comenzando con la igualdad de vectores.
        # Muestra de inicio 4 vectores donde 2 de ellos son iguales. 
        # Éstos con su debida etiqueta. 


        image = ImageMobject("/home/codexreckoner/manim/media/designs/raster_images/FONDOCOLOR.jpg")
        image.scale(6)
        self.play(FadeIn(image))

        Prop = TextMobject("Propiedades de los vectores")
        Achul = "#FFFFFF"
        Prop.set_color(Achul)
        self.play(Write(Prop, run_time=2))
        self.play(FadeOut(Prop))
    
        v_1 = np.array([2, 3, 0])
        v_2 = np.array([2*0.5, 3*0.5, 0])
        v_3 = np.array([3, 4, 0])

        mover = {}
        mover[-1] = np.array([-4, 3, 0])
        mover[0] = np.array([-3, 0 , 0])
        mover[1] = np.array([-1, 0, 0])
        mover[2] = np.array([2, -1, 0])
        mover[3] = np.array([5, 1, 0 ])

        u = TexMobject("\\overrightarrow{u}")
        u.set_color(Achul)
        u.shift(v_1)

        v = TexMobject("\\overrightarrow{v}")
        v.set_color(Achul)
        v.shift(v_2)

        y = TexMobject("\\overrightarrow{y}")
        y.set_color(Achul)
        y.shift(v_3)

        w = TexMobject("\\overrightarrow{w}")
        w.set_color(Achul)
        w.shift(v_1)

        title_1 = TextMobject("Igualdad vectorial")
        title_1.move_to(mover[-1])
        title_1.set_color(Achul)
        self.play(Write(title_1, run_time = 2))
        
        vectors = {}
        vectors[0] = Vector(v_1, color = Achul).move_to(mover[0])
        vectors[1] = Vector(v_2, color = Achul).move_to(mover[1])
        vectors[2] = Vector(v_3, color = Achul).move_to(mover[2])   

        self.play(Write(vectors[0]))
        self.play(Write(u.move_to(mover[0] + np.array([0.5, 2, 0]))))

        self.play(Write(vectors[1]))
        self.play(Write(v.move_to(mover[1] + np.array([0.3, 1.3, 0]))))

        self.play(Write(vectors[2]))
        self.play(Write(y.move_to(mover[2] + np.array([1.2, 2.4, 0]))))
        
        igualito = Vector(v_1, color = Achul).move_to(mover[3])
        self.play(Write(igualito))
        self.play(Write(w.move_to(mover[3] + np.array([1.2, 2.4, 0]))))

        self.wait(1.5)

        # Traslapar los dos vectores iguales para hacer notar que miden lo mismo. 
        # Lo que se va a hacer es tratar de "Traslapar" a cada uno de los vectores:w



        translade_1 = Vector(v_1, color = Achul).move_to(mover[2] + np.array([-0.1, 0, 0]))
        translade_2 = Vector(v_1, color = Achul).move_to(mover[1] + np.array([-0.1, 0, 0]))
        translade_3 = Vector(v_1, color = Achul).move_to(mover[0] + np.array([-0.1, 0, 0]))
        
        self.play(ReplacementTransform(igualito.copy(), translade_1), run_time=2)
        not_iqual_1 = TexMobject("\\overrightarrow{y} \\neq \\overrightarrow{w}")
        not_iqual_1.set_color(Achul)
        not_iqual_1.move_to(mover[2] + np.array([1.2, 2.4, 0]))
        self.play(ReplacementTransform(y, not_iqual_1))
        self.play(FadeOut(not_iqual_1))
        y = TexMobject("\\overrightarrow{y}")
        y.set_color(Achul)
        y.shift(v_3)
        self.play(Write(y.move_to(mover[2] + np.array([1.2, 2.4, 0]))))
        self.play(FadeOut(translade_1))

        self.play(ReplacementTransform(igualito.copy(), translade_2), run_time=2)
        not_iqual_2 = TexMobject("\\overrightarrow{v} \\neq \\overrightarrow{w}")
        not_iqual_2.set_color(Achul)
        not_iqual_2.move_to(mover[1] + np.array([0.3, 2.4, 0]))
        self.play(ReplacementTransform(v, not_iqual_2))
        self.play(FadeOut(not_iqual_2))
        v = TexMobject("\\overrightarrow{v}")
        v.set_color(Achul)
        v.shift(v_2)
        self.play(Write(v.move_to(mover[1] + np.array([0.3, 1.3, 0]))))
        self.play(FadeOut(translade_2))

        self.play(ReplacementTransform(igualito.copy(), translade_3), run_time=2)
        iqual = TexMobject("\\overrightarrow{u} = \\overrightarrow{w}")
        iqual.set_color(Achul)
        iqual.move_to(mover[0] + np.array([0.5, 2, 0]))
        self.play(ReplacementTransform(translade_3.copy(), vectors[0]), run_time=2)
        self.play(ReplacementTransform(u, iqual))

        self.play(FadeOut(y))
        self.play(FadeOut(vectors[2]))
        self.play(FadeOut(v))
        self.play(FadeOut(vectors[1]))
        self.play(FadeOut(w))
        self.play(FadeOut(igualito))
        self.play(FadeOut(translade_3))

        # Finalmente mostrar la igualdad en la parte de arriba de la pantalla.
        # Desaparece totalmente de la pantalla la animación anterior y
        
        self.play(FadeOut(iqual))
        self.play(FadeOut(vectors[0]))
        self.play(FadeOut(title_1))

        # comenzamos con la siguiente.
        # Realizar las siguientes operaciones apareciendo siempre el vector U y luego el V.
        # y al final el vector resultante.

        # SUMA

        title_2 = TextMobject("Suma vectorial")
        title_2.move_to(mover[-1])
        title_2.set_color(Achul)
        self.play(Write(title_2, run_time = 2))
        
        u_1 = TexMobject("\\overrightarrow{u}")
        u_1.set_color(Achul)
        u_1.shift(np.array([-4, -1, 0]))

        v_1 = TexMobject("\\overrightarrow{v}")
        v_1.set_color(Achul)
        v_1.shift(np.array([4.3, 0.5, 0]))

        U_1 = Vector(np.array([-2.3, 2, 0])).move_to(np.array([-2, -1.5, 0]))
        V_1 = Vector(np.array([3, 3, 0])).move_to(np.array([2, -1.5, 0]))
        
        VSu = Vector(np.array([-2.3, 2, 0])).move_to(np.array([2.3, 1, 0]))
        USu = Vector(np.array([3, 3, 0])).move_to(np.array([-0.3, 0.5, 0]))


        U_1.set_color(Achul)
        V_1.set_color(Achul)
        VSu.set_color(Achul)
        USu.set_color(Achul)

        self.play(Write(u_1))
        self.play(FadeIn(U_1))

        self.play(Write(v_1))
        self.play(FadeIn(V_1))
        
        U_11 = Vector(np.array([-2.3, 2, 0])).move_to(np.array([-0.65, -2, 0]))
        V_11 = Vector(np.array([3, 3, 0])).move_to(np.array([0, 0, 0]))
        
        U_11.set_color(Achul)
        V_11.set_color(Achul)

        self.play(ReplacementTransform(U_1.copy(), U_11)) 
        self.play(ReplacementTransform(u_1.copy(), u_1.move_to(np.array([-2.5, -1 ,0]))))
        self.play(FadeOut(U_1))
        self.play(ReplacementTransform(U_11.copy(), VSu))
        self.play(ReplacementTransform(V_1.copy(), USu))
        self.wait()

        suma = Vector(np.array([0.7, 5, 0])).move_to(np.array([0.9, -0.5, 0]))
        suma.set_color("#FFFFFF")
        self.play(GrowArrow(suma))
        sumt = TexMobject("\\overrightarrow{u}+\\overrightarrow{v}")
        sumt.set_color("#FFFFFF")
        sumt.move_to(np.array([1.65, -0.8, 0]))
        self.play(Write(sumt))
        self.play(FadeOut(VSu))
        self.play(FadeOut(USu))
        self.wait(2)

        self.play(FadeOut(U_11))
        self.play(FadeOut(u_1))
        self.play(FadeOut(V_1))
        self.play(FadeOut(v_1))
        self.play(FadeOut(sumt))
        self.play(FadeOut(suma))
        self.play(FadeOut(title_2))
        self.wait(2)

        # En la resta, aparecer primero un vector V.
        # Luego el vector U y a continuación el vector negativo de V.

        title_3 = TextMobject("Resta vectorial")
        title_3.set_color(Achul)
        title_3.move_to(mover[-1])
        self.play(Write(title_3))

        U_2 = Vector(np.array([-3, 0, 0])).set_color(Achul)
        U_2.move_to(np.array([-2, 0, 0]))
        mu2 = TexMobject("\\overrightarrow{u}")
        mu2.set_color(Achul)
        mu2.move_to(np.array([-2, 1 , 0]))
        self.play(Write(mu2))
        self.play(GrowArrow(U_2))

        V_2 = Vector(np.array([2, 3, 0])).set_color(Achul)
        V_2.move_to(np.array([1, 0, 0]))
        mv2 = TexMobject("\\overrightarrow{v}")
        mv2.set_color(Achul)
        mv2.move_to([1, 1, 0])
        self.play(Write(mv2))
        self.play(GrowArrow(V_2))
        
        U_22 = Vector(np.array([-3, 0, 0])).set_color(Achul)
        U_22.move_to(np.array([-1.5, -1.5, 0]))
        
        self.play(ReplacementTransform(U_2, U_22))
        self.play(ReplacementTransform(mu2.copy(), mu2.move_to(np.array([-2, -1, 0]))))
        menu2 = TexMobject("-\\overrightarrow{u}").set_color("#FFFFFF")
        menu2.move_to(np.array([2, -1, 0]))
        self.play(Write(menu2))
        
        _U_2 = Vector(np.array([3, 0, 0])).set_color("#FFFFFF")
        _U_2.move_to(np.array([1.5, -1.5, 0]))
        self.play(GrowArrow(_U_2))
       
        VSu2 = Vector(np.array([2, 3, 0])).move_to(np.array([4, 0, 0]))
        VSu2.set_color(Achul)

        USu2 = Vector(np.array([3, 0, 0])).set_color("#FFFFFF")
        USu2.move_to(np.array([3.5, 1.5, 0]))

        self.play(ReplacementTransform(V_2.copy(), VSu2))
        self.play(ReplacementTransform(_U_2.copy(), USu2))
        
        rest = Vector(np.array([5, 3, 0])).move_to(np.array([2.5, 0, 0]))
        rest.set_color("#FFFFFF")
        self.play(GrowArrow(rest))

        self.play(FadeOut(VSu2))
        self.play(FadeOut(USu2))
        self.play(FadeOut(menu2))
        self.play(FadeOut(_U_2))
        
        restt = TexMobject("\\overrightarrow{v}-\\overrightarrow{u}").set_color("#FFFFFF")
        restt.move_to(np.array([3, -1, 0]))
        self.play(Write(restt))
        self.wait(3)

        self.play(FadeOut(U_2))
        self.play(FadeOut(mu2))
        self.play(FadeOut(U_22))
        self.play(FadeOut(V_2))
        self.play(FadeOut(mv2))
        self.play(FadeOut(rest))
        self.play(FadeOut(restt))
        self.play(FadeOut(title_3))
        self.wait(3)

        # En la multiplicación mostrar primero un vector A. 
        # luego hacer una copia de si mismo que se expanda en longitud 
        # hasta obtener el vector 2A

        title_4 = TextMobject("Multiplicación vectorial por escalar ") 
        title_4.set_color(Achul)
        title_4.move_to(mover[-1] + np.array([1, 0, 0]))
        self.play(Write(title_4))
        self.wait(2)

        A = Vector(np.array([3, 2, 0])).move_to(np.array([-1, -1, 0]))
        A.set_color(Achul)
        self.play(GrowArrow(A))
        self.wait(1)

        Ate = TexMobject("\\overrightarrow{A}").set_color(Achul)
        Ate2 = TexMobject("2\\overrightarrow{A}").set_color(Achul)
        Ate.move_to(np.array([1.5, 0, 0]))
        Ate2.move_to(np.array([4, 2.5, 0]))
        self.play(Write(Ate))

        A2 = Vector(np.array([6, 4, 0])).move_to(np.array([0.5, 0, 0]))
        A2.set_color(Achul)
        self.play(GrowArrow(A2))
        self.play(Write(Ate2))
        self.play(FadeOut(A))
        self.play(FadeOut(Ate))

        self.wait(3)

