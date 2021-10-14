from big_ol_pile_of_manim_imports import *
from networkx.classes import graph

DISTANCE_COLOR = BLUE
TIME_COLOR = YELLOW
VELOCITY_COLOR = GREEN

# Construccion de gráficas - Derivación e integración
# Objetivo: 
#   Construir   gradualmente   tres   graficas   al   mismo   tiempo:posición-tiempo, velocidad tiempo y aceleracion tiempo.
#   De esa manerase visualiza que las dos ultimas surgen de la derivada de la anterior.
#    Mostrar   las   tres   gráficas   al   mismo   tiempo. Comenzamosremarcando el punto en el origen. 
#    Construir la curva de cada una con diferente color. 
#    Indicar   con   línea   punteada   los   puntos   donde   los   movimientos cambian.

class AnimationEight1(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 40,
        "x_labeled_nums" : list(range(1, 40)),
        "x_axis_label" : "t(s)",
        "y_min" : 0,
        "y_max" : 50,
        "x_labeled_nums" : list(range(1, 50)),
        "y_tick_frequency" : 10,
        "y_axis_label" : "$a(\\frac{m}{s^2})$",
        "graph_origin" : 2*DOWN + 5*LEFT,
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
        #image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/stars.jpg")
        title = TextMobject("Gráfica aceleración-tiempo")
        #image.scale(6)
        #self.add(image)
        title.move_to(np.array([0.3, 2.0,0]))
        self.add(title)
        self.setup_axes()
       
        graph = self.graph_sigmoid_trajectory_function()
        velocity = self.velocity()
        aceleration = self.aceleration()
        origin = self.coords_to_point(0, 1.5)

        #self.introduce_graph(graph, origin)
        #self.show_velocity_graph(velocity, origin)
        self.show_aceleration_graph(aceleration, origin)

    def graph_sigmoid_trajectory_function(self, **kwargs):
        graph = self.get_graph( lambda t : animmeig(t),
                    **kwargs
                    )
        self.s_graph = graph
        return graph
    
    def velocity(self, **kwargs):
        position = self.graph_sigmoid_trajectory_function()
        velocity = self.get_derivative_graph(self.s_graph)
        self.v_graph = velocity
        return velocity
    
    def aceleration(self, **kwargs):
        position = self.graph_sigmoid_trajectory_function()
        velocity = self.get_derivative_graph(self.s_graph)
        aceleration = self.get_derivative_graph(self.v_graph)
        self.a_graph = velocity
        return aceleration

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
        self.wait()
        self.play(*list(map(FadeOut, [h_line, v_line])))

        #Show example vertical distance
        h_update(h_line, 0.2)
        t_1_dot = Dot(h_line.get_start(), color = h_line.get_color())
        t_1_dot.save_state()
        t_1_dot.move_to(self.x_axis_label_mob)
        t_1_dot.set_fill(opacity = 0)
        dashed_h1 = DashedLine(*h_line.get_start_and_end())
        dashed_h1.set_color(h_line.get_color())
        
        ########################################
        h_update(h_line, 0.3)
        t_2_dot = Dot(h_line.get_start(), color = h_line.get_color())
        t_2_dot.save_state()
        t_2_dot.move_to(self.x_axis_label_mob)
        t_2_dot.set_fill(opacity = 0)
        dashed_h2 = DashedLine(*h_line.get_start_and_end())
        dashed_h2.set_color(h_line.get_color())
        
        #######################################
        h_update(h_line, 0.5)
        t_3_dot = Dot(h_line.get_start(), color = h_line.get_color())
        t_3_dot.save_state()
        t_3_dot.move_to(self.x_axis_label_mob)
        t_3_dot.set_fill(opacity = 0)
        dashed_h3 = DashedLine(*h_line.get_start_and_end())
        dashed_h3.set_color(h_line.get_color())
        
        #######################################
        h_update(h_line, 0.6)
        t_4_dot = Dot(h_line.get_start(), color = h_line.get_color())
        t_4_dot.save_state()
        t_4_dot.move_to(self.x_axis_label_mob)
        t_4_dot.set_fill(opacity = 0)
        dashed_h4 = DashedLine(*h_line.get_start_and_end())
        dashed_h4.set_color(h_line.get_color())
        
        self.play(t_1_dot.restore)
        self.play(t_2_dot.restore)
        self.play(t_3_dot.restore)
        self.play(t_4_dot.restore)
        self.wait()
        self.play(ShowCreation(dashed_h1), 
                  ShowCreation(dashed_h2),
                  ShowCreation(dashed_h3),
                  ShowCreation(dashed_h4)
                  )
        
        self.wait(2)

        #Name graph
        s_of_t = TexMobject("s(t)")
        s_of_t.next_to(
            graph.point_from_proportion(1), 
            8*UP+RIGHT,
            buff = SMALL_BUFF
        )
        s = s_of_t[0]
        d = TexMobject("d")
        d.move_to(s, DOWN)
        d.set_color(DISTANCE_COLOR)

        self.play(Write(s_of_t))
        self.wait()
        s.save_state()
        self.play(Transform(s, d))
        self.wait()
        self.play(s.restore)

    def get_change_lines(self, curr_time, delta_t = 1):
        p1 = self.input_to_graph_point(
            curr_time, self.s_graph
        )
        p2 = self.input_to_graph_point(
            curr_time+delta_t, self.s_graph
        )
        interim_point = p2[0]*RIGHT + p1[1]*UP
        delta_t_line = Line(p1, interim_point, color = TIME_COLOR)
        delta_s_line = Line(interim_point, p2, color = DISTANCE_COLOR)
        brace = Brace(delta_s_line, RIGHT, buff = SMALL_BUFF)
        return VGroup(delta_t_line, delta_s_line, brace)

    def show_velocity_graph(self, velocity, origin):
        h_line, v_line = [
            Line(origin, origin, color = color, stroke_width = 2)
            for color in (TIME_COLOR, DISTANCE_COLOR)
        ]
        def h_update(h_line, proportion = 1):
            end = velocity.point_from_proportion(proportion)
            t_axis_point = end[0]*RIGHT + origin[1]*UP
            h_line.put_start_and_end_on(t_axis_point, end)
        def v_update(v_line, proportion = 1):
            end = velocity.point_from_proportion(proportion)
            d_axis_point = origin[0]*RIGHT + end[1]*UP
            v_line.put_start_and_end_on(d_axis_point, end)
        
        self.play(
            ShowCreation(
                velocity,
                rate_func=linear,
            ),
            run_time = self.time_of_journey,
        )
        self.wait()
        self.play(*list(map(FadeOut, [h_line, v_line])))
        
        #Show example vertical distance
        h_update(h_line, 0.2)
        t_1_dot = Dot(h_line.get_start(), color = h_line.get_color())
        t_1_dot.save_state()
        t_1_dot.move_to(self.x_axis_label_mob)
        t_1_dot.set_fill(opacity = 0)
        dashed_h1 = DashedLine(*h_line.get_start_and_end())
        dashed_h1.set_color(h_line.get_color())
        
        ########################################
        h_update(h_line, 0.3)
        t_2_dot = Dot(h_line.get_start(), color = h_line.get_color())
        t_2_dot.save_state()
        t_2_dot.move_to(self.x_axis_label_mob)
        t_2_dot.set_fill(opacity = 0)
        dashed_h2 = DashedLine(*h_line.get_start_and_end())
        dashed_h2.set_color(h_line.get_color())
        
        #######################################
        h_update(h_line, 0.5)
        t_3_dot = Dot(h_line.get_start(), color = h_line.get_color())
        t_3_dot.save_state()
        t_3_dot.move_to(self.x_axis_label_mob)
        t_3_dot.set_fill(opacity = 0)
        dashed_h3 = DashedLine(*h_line.get_start_and_end())
        dashed_h3.set_color(h_line.get_color())
        
        #######################################
        h_update(h_line, 0.6)
        t_4_dot = Dot(h_line.get_start(), color = h_line.get_color())
        t_4_dot.save_state()
        t_4_dot.move_to(self.x_axis_label_mob)
        t_4_dot.set_fill(opacity = 0)
        dashed_h4 = DashedLine(*h_line.get_start_and_end())
        dashed_h4.set_color(h_line.get_color())
        
        self.play(t_1_dot.restore)
        self.play(t_2_dot.restore)
        self.play(t_3_dot.restore)
        self.play(t_4_dot.restore)
        self.wait()
        self.play(ShowCreation(dashed_h1), 
                  ShowCreation(dashed_h2),
                  ShowCreation(dashed_h3),
                  ShowCreation(dashed_h4)
                  )
        
        self.wait(2)

        #Name graph
        s_of_t = TexMobject("v(t)")
        s_of_t.next_to(
            velocity.point_from_proportion(1), 
            12*UP+RIGHT,
            buff = SMALL_BUFF
        )
        s = s_of_t[0]
        d = TexMobject("v")
        d.move_to(s, DOWN)
        d.set_color(GREEN)

        self.play(Write(s_of_t))
        self.wait()
        s.save_state()
        self.play(Transform(s, d))
        self.wait()
        self.play(s.restore)        
    
    def show_aceleration_graph(self, aceleration, origin):
        h_line, v_line = [
            Line(origin, origin, color = color, stroke_width = 2)
            for color in (TIME_COLOR, DISTANCE_COLOR)
        ]
        def h_update(h_line, proportion = 1):
            end = aceleration.point_from_proportion(proportion)
            t_axis_point = end[0]*RIGHT + origin[1]*UP
            h_line.put_start_and_end_on(t_axis_point, end)
        def v_update(v_line, proportion = 1):
            end = aceleration.point_from_proportion(proportion)
            d_axis_point = origin[0]*RIGHT + end[1]*UP
            v_line.put_start_and_end_on(d_axis_point, end)
        
        aceleration.set_color(RED)
        self.play(
            ShowCreation(
                aceleration,
                rate_func=linear,
            ),
            run_time = self.time_of_journey,
        )
        self.wait()
        
        #Show example vertical distance
        h_update(h_line, 0.2)
        t_1_dot = Dot(h_line.get_start(), color = h_line.get_color())
        t_1_dot.save_state()
        t_1_dot.move_to(self.x_axis_label_mob)
        t_1_dot.set_fill(opacity = 0)
        dashed_h1 = DashedLine(*h_line.get_start_and_end())
        dashed_h1.set_color(h_line.get_color())
        
        ########################################
        h_update(h_line, 0.3)
        t_2_dot = Dot(h_line.get_start(), color = h_line.get_color())
        t_2_dot.save_state()
        t_2_dot.move_to(self.x_axis_label_mob)
        t_2_dot.set_fill(opacity = 0)
        dashed_h2 = DashedLine(*h_line.get_start_and_end())
        dashed_h2.set_color(h_line.get_color())
        
        #######################################
        h_update(h_line, 0.5)
        t_3_dot = Dot(h_line.get_start(), color = h_line.get_color())
        t_3_dot.save_state()
        t_3_dot.move_to(self.x_axis_label_mob)
        t_3_dot.set_fill(opacity = 0)
        dashed_h3 = DashedLine(*h_line.get_start_and_end())
        dashed_h3.set_color(h_line.get_color())
        
        #######################################
        h_update(h_line, 0.6)
        t_4_dot = Dot(h_line.get_start(), color = h_line.get_color())
        t_4_dot.save_state()
        t_4_dot.move_to(self.x_axis_label_mob)
        t_4_dot.set_fill(opacity = 0)
        dashed_h4 = DashedLine(*h_line.get_start_and_end())
        dashed_h4.set_color(h_line.get_color())
        
        self.play(t_1_dot.restore)
        self.play(t_2_dot.restore)
        self.play(t_3_dot.restore)
        self.play(t_4_dot.restore)
        self.wait()
        self.play(ShowCreation(dashed_h1), 
                  ShowCreation(dashed_h2),
                  ShowCreation(dashed_h3),
                  ShowCreation(dashed_h4)
                  )
        
        self.wait(2)

        #Name graph
        s_of_t = TexMobject("a(t)")
        s_of_t.next_to(
            aceleration.point_from_proportion(1), 
            12*UP+RIGHT,
            buff = SMALL_BUFF
        )
        s = s_of_t[0]
        d = TexMobject("a")
        d.move_to(s, DOWN)
        d.set_color(RED)

        self.play(Write(s_of_t))
        self.wait()
        s.save_state()
        self.play(Transform(s, d))
        self.wait()
        self.play(s.restore)            
        self.wait(1)
