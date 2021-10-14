from manimlib.imports import *
from networkx.classes import graph

DISTANCE_COLOR = BLUE
TIME_COLOR = YELLOW
VELOCITY_COLOR = GREEN

#Objetivo: Mostrar con una gráfica tiempo-velocidad, la pendiente en un 
# punto y así introducir la idea de la derivada y su posterior uso para elestudio de la cinemática.

# En la curva que describe la velocidad de un cuerpo, elegir dos puntos A y B y unirlos mediante un segmento. Listo! :D
# Mostrar las longitudes v y t. 
# Aproximar gradualmente el punto B al punto A. 
# Con ello cambiarántambién la longitud del segmento y de las longitudes v y t.
# Cuando los puntos coincidan, remarcar la pendiente al punto.
# Re alizar una gráfica posición-tiempo mostrando el mismo proceso, pero con las unidades correspondientes.
# Para el siguiente diagrama primero mostraremos gráficamente laintegración. El boceto queda pendiente.
# ¿?
# Cambios:
# coloca intercambia el orden de las letras A y B. --Listo! :D
# Esos segmentos verdes, prolongalos  a ambos lados
# Sus prolongaciones ponlas de verde y el segmento que se encuentra entre A y B , ponlo de rojo

class AnimationSevenP1(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 10,
        "x_labeled_nums" : list(range(1, 11)),
        "x_axis_label" : "Tiempo(s)",
        "y_min" : 0,
        "y_max" : 100,
        "y_tick_frequency" : 10,
        "y_axis_label" : "Velocidad(m/s)",
        "graph_origin" : 2.5*DOWN + 5*LEFT,
        "default_graph_colors" : [DISTANCE_COLOR, VELOCITY_COLOR],
        "default_derivative_color" : VELOCITY_COLOR,
        "time_of_journey" : 10,
        "care_movement_rate_func" : smooth,
        "start_time" : 6,
        "end_time" : 2,
        "alt_end_time" : 10,
        "start_dt" : 2,
        "end_dt" : 0.01,
        "secant_line_length" : 10,
    }
    
    def construct(self):
        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/stars2.jpg")
        title = TextMobject("Gráfica velocidad-tiempo")
        image.scale(6)
        self.add(image)
        title.move_to(np.array([0.6,-3.5,0]))
        self.add(title)
        
        self.setup_axes()
        graph = self.graph_sigmoid_trajectory_function()
        origin = self.coords_to_point(0, 0)
        self.introduce_graph(graph, origin)
        
        self.wait()
        
    def graph_sigmoid_trajectory_function(self, **kwargs):
        graph = self.get_graph(
            lambda t : 100*double_smooth(t/10.),
            **kwargs
        )
        self.s_graph = graph
        return graph

    def introduce_graph(self, graph, origin):
        h_line, v_line = [
            Line(origin, origin, color = color, stroke_width = 2)
            for color in (TIME_COLOR, DISTANCE_COLOR)
        ]
        def h_update(h_line, proportion = 1):
            end = graph.point_from_proportion(proportion)
            t_axis_point = end[0]*RIGHT + origin[1]*UP
            h_line.put_start_and_end_on(t_axis_point, end)
            
        def v_update(v_line, proportion = 1):
            end = graph.point_from_proportion(proportion)
            d_axis_point = origin[0]*RIGHT + end[1]*UP
            v_line.put_start_and_end_on(d_axis_point, end)
        
        self.play(
            ShowCreation(
                graph,
                rate_func=linear,
            ),
            UpdateFromFunc(h_line, h_update),
            UpdateFromFunc(v_line, v_update),
            run_time = self.time_of_journey,
        )
        """
        self.wait()
        self.play(*list(map(FadeOut, [h_line, v_line])))
    
        #Show example vertical distance one 
        h_update(h_line, 0.8)
        t1_dot = Dot(h_line.get_start(), color = RED)
        A = Dot(h_line.get_end(), color = h_line.get_color())
        A_tex = TextMobject("B")
        A_tex.move_to(h_line.get_end() + np.array([-0.5, 0.3, 0.0]))
        A_tex.save_state()
        A.save_state()
        t1_dot.save_state()
        t1_dot.move_to(self.x_axis_label_mob)
        t1_dot.set_fill(opacity = 0)

        dashed_h1 = DashedLine(*h_line.get_start_and_end())
        dashed_h1.set_color(h_line.get_color())
        
        #Show example vertical distance two 
        h_update(h_line, 0.4)
        t2_dot = Dot(h_line.get_start(), color = h_line.get_color())
        B = Dot(h_line.get_end(), color = h_line.get_color())
        B_tex = TextMobject("A")
        B_tex.move_to(h_line.get_end() + np.array([-0.5, 0.5, 0.0]))
        B_tex.save_state()
        B.save_state()
        t2_dot.save_state()
        t2_dot.move_to(self.x_axis_label_mob)
        t2_dot.set_fill(opacity = 0)
      
        dashed_h2 = DashedLine(*h_line.get_start_and_end())
        dashed_h2.set_color(h_line.get_color())
        
        brace = Brace(dashed_h1, RIGHT)
        brace_text = brace.get_text("Velocidad obtenida")
        
        self.play(t1_dot.restore)
        self.wait()
        self.play(ShowCreation(dashed_h1))
        self.play(
            Write(brace, run_time=2),
            Write(brace_text, run_time=2)
        )
        self.play(
            FadeOut(brace, run_time=1),
            FadeOut(brace_text, run_time=1)
        )
    
        self.wait()
        self.play(*list(map(FadeIn, [t1_dot, A, A_tex])))
        self.wait()
        self.play(*list(map(FadeIn, [t2_dot, dashed_h2, B, B_tex])))
        self.play()
        
        L_1 = Line(A, B,fill_color=RED, color=RED, stroke_width=6)
        
        Tangent1 = self.get_secant_slope_group(
            4, graph,
            dx = 4,
            secant_line_color = GREEN
        )
        
        self.play(
            Write(Tangent1),
            Write(L_1)
                  )


        #Name graph
        s_of_t = TexMobject("v(t)")
        s_of_t.next_to(
            graph.point_from_proportion(1), 
            DOWN+RIGHT,
            buff = SMALL_BUFF
        )
        s = s_of_t[0]
        d = TexMobject("v")
        d.move_to(s, DOWN)
        d.set_color(DISTANCE_COLOR)

        self.play(Write(s_of_t))
        self.wait()
        s.save_state()
        
        delta_t = 4
        curr_time = 4
        ghost_line_1 = Line(
            origin, 
            self.coords_to_point(delta_t, self.y_max)
        )

        change_lines = self.get_change_lines(curr_time, delta_t)
        self.play(Write(change_lines))
        self.wait()
    
        ################################################################
        # 3 
        
        delta_t = 3
        new_change_lines = self.get_change_lines(curr_time, delta_t)
        
        z = 0.7
        
        h_update(h_line, z)
        t1_3_dot = Dot(h_line.get_start(), color = h_line.get_color())
        
        A_3 = Dot(h_line.get_end(), color = h_line.get_color())
        A_3_tex = TextMobject("B")
        A_3_tex.move_to(h_line.get_end() + np.array([-0.5, 0.5, 0.0]))
     
        
        dashed_h2 = DashedLine(*h_line.get_start_and_end())
        dashed_h2.set_color(h_line.get_color())
        L_2 = Line(A_3, B, fill_color=RED, color=RED, stroke_width=6)
        L_2.set_color(RED)
        
        Tangent2 = self.get_secant_slope_group(
            4, graph,
            dx = 3,
            secant_line_color = GREEN
        )
        self.play(ReplacementTransform(t1_dot, t1_3_dot),
                ReplacementTransform(A, A_3),
                ReplacementTransform(Tangent1, Tangent2),
                ReplacementTransform(L_1, L_2),
                ReplacementTransform(A_tex, A_3_tex),
                ReplacementTransform(dashed_h1, dashed_h2),
                ReplacementTransform(change_lines, new_change_lines))
               
        text_1 = TextMobject("$\\frac{\\text{m}}{{\\text{s}}^2}$")
        text_2 = TextMobject("$\\frac{\\text{metro}}{{\\text{segundo}}^2}$")
        text_1.move_to(np.array([-1.0, 2.0, 0.0]))
        self.play(Write(text_1))
        self.wait()
        text_2.move_to(np.array([-1.0, 2.0, 0.0]))
        self.play(ReplacementTransform(text_1, text_2))
        self.wait()
        self.play(FadeOut(text_2))
    
        self.play(FadeOut(new_change_lines))
        
        change_lines = self.get_change_lines(curr_time, delta_t)

        ##################################################################
        #2 
        
        delta_t = 2
        new_change_lines = self.get_change_lines(curr_time, delta_t)
        
        z = 0.6
        
        h_update(h_line, z)
        t1_4_dot = Dot(h_line.get_start(), color = h_line.get_color())
        
        A_4 = Dot(h_line.get_end(), color = h_line.get_color())
        A_4_tex = TextMobject("B")
        A_4_tex.move_to(h_line.get_end() + np.array([-0.5, 0.5, 0.0]))
     
        
        dashed_h4 = DashedLine(*h_line.get_start_and_end())
        dashed_h4.set_color(h_line.get_color())
        L_4 = Line(A_4, B, fill_color=RED, color=RED, stroke_width=7)
        Tangent3 = self.get_secant_slope_group(
            4, graph,
            dx = 2,
            secant_line_color = GREEN
                                )
        
        self.play(ReplacementTransform(t1_3_dot, t1_4_dot),
                ReplacementTransform(A_3, A_4),
                ReplacementTransform(Tangent2, Tangent3),
                ReplacementTransform(L_2, L_4),
                ReplacementTransform(A_3_tex, A_4_tex),
                ReplacementTransform(dashed_h2, dashed_h4),
                ReplacementTransform(change_lines, new_change_lines))
               
        
        self.play(*list(map(FadeOut, change_lines)))
        self.play(FadeOut(new_change_lines))

        
        change_lines = self.get_change_lines(curr_time, delta_t)

       
        ############################################################################################
        # delta 1
        
        delta_t = 1
        new_change_lines = self.get_change_lines(curr_time, delta_t)
        
        z = 0.5
        
        h_update(h_line, z)
        t1_5_dot = Dot(h_line.get_start(), color = h_line.get_color())
        
        A_5 = Dot(h_line.get_end(), color = h_line.get_color())
        A_5_tex = TextMobject("B")
        A_5_tex.move_to(h_line.get_end() + np.array([-0.5, 0.5, 0.0]))
     
        
        dashed_h5 = DashedLine(*h_line.get_start_and_end())
        dashed_h5.set_color(h_line.get_color())
        L_5 = Line(A_5, B, fill_color=RED, color=RED, stroke_width=7)
        Tangent4 = self.get_secant_slope_group(
            4, graph,
            dx = 1,
            secant_line_color = GREEN
        )
        
        self.play(ReplacementTransform(t1_4_dot, t1_5_dot),
                ReplacementTransform(A_4, A_5),
                ReplacementTransform(Tangent3, Tangent4),
                ReplacementTransform(L_4, L_5),
                ReplacementTransform(A_4_tex, A_5_tex),
                ReplacementTransform(dashed_h4, dashed_h5),
                ReplacementTransform(change_lines, new_change_lines))
               
        self.play(*list(map(FadeOut, change_lines)))       
        self.play(FadeOut(new_change_lines))

        
        change_lines = self.get_change_lines(curr_time, delta_t)
        
        ############################################################################################
        # delta 0
        
        delta_t = 0
        new_change_lines = self.get_change_lines(curr_time, delta_t)
        
        z = 0.4
        
        h_update(h_line, z)
        t1_6_dot = Dot(h_line.get_start(), color = h_line.get_color())

        A_6 = Dot(h_line.get_end(), color = h_line.get_color())
        Tangent5 = self.get_secant_slope_group(
            4, graph,
            dx = 0.0001,
            secant_line_color = GREEN
        )    
        
        dashed_h6 = DashedLine(*h_line.get_start_and_end())
        dashed_h6.set_color(h_line.get_color())
        
        self.play(FadeOut(B_tex))
        self.play(ReplacementTransform(t1_5_dot, t1_6_dot),
                FadeOut(A_5),
                FadeOut(L_5),
                ReplacementTransform(Tangent4, Tangent5),
                FadeOut(A_5_tex),
                ReplacementTransform(dashed_h5, dashed_h6),
                ReplacementTransform(change_lines, new_change_lines))
               
        change_lines = self.get_change_lines(curr_time, delta_t)
        self.wait(3)
        """
        ######################################################################
        
    def get_change_lines(self, curr_time, delta_t=4):
        p1 = self.input_to_graph_point(
            curr_time, self.s_graph
        )
        p2 = self.input_to_graph_point(
            curr_time+delta_t, self.s_graph
        )
        interim_point = p2[0]*RIGHT + p1[1]*UP
        delta_t_line = Line(p1, interim_point, color = TIME_COLOR)
        delta_s_line = Line(interim_point, p2, color = DISTANCE_COLOR)
        brace_1 = Brace(delta_s_line, RIGHT, buff = SMALL_BUFF)
        brace_2 = Brace(delta_t_line, DOWN, buff = SMALL_BUFF)
        
        DeltaV = brace_1.get_text("$\\Delta v$")
        DeltaT = brace_2.get_text("$\\Delta t$")
        Deriv = brace_1.get_text("$\\frac{dv(t=4)}{dt}$")
        
        if delta_t == 3:
            DeltaV.move_to(interim_point + np.array([1.0, 0.6, 0.0]))
            DeltaT.move_to(interim_point + np.array([-1.2, -0.7, 0.0]))
            return VGroup(delta_t_line, delta_s_line, brace_1, brace_2, DeltaT, DeltaV)
        if delta_t == 2:
            DeltaV.move_to(interim_point + np.array([0.6, 0.3, 0.0]))
            DeltaT.move_to(interim_point + np.array([-0.8, -0.7, 0.0]))
            return VGroup(delta_t_line, delta_s_line, brace_1, brace_2, DeltaT, DeltaV)        
        if delta_t == 1:
            DeltaV.move_to(interim_point + np.array([0.4, -0.2, 0.0]))
            DeltaT.move_to(interim_point + np.array([-0.6, -0.7, 0.0]))
            return VGroup(delta_t_line, delta_s_line, brace_1, brace_2, DeltaT, DeltaV)
        if delta_t == 0:
            DeltaV.move_to(interim_point + np.array([1.0, 1.3, 0.0]))
            DeltaT.move_to(interim_point + np.array([-1.5, -0.8, 0.0]))
            Deriv.move_to(interim_point + np.array([1.0,-1.0, 0]))
            return VGroup(delta_t_line, delta_s_line, brace_1, brace_2, Deriv)
        else:
            return VGroup(delta_t_line, delta_s_line, brace_1, brace_2, DeltaT, DeltaV)