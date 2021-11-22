from manimlib.imports import *

DISTANCE_COLOR = BLUE
TIME_COLOR = YELLOW
VELOCITY_COLOR = GREEN

class Posicion(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 40,
        "x_labeled_nums" : list(range(0, 41, 10)),
        "y_labeled_nums" : list(range(0, 51, 10)),
        "x_axis_label" : "$t(s)$",
        "y_min" : 0,
        "y_max" : 50,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 10,
        "y_axis_label" : "$x(m)$",
        "graph_origin" : 3*DOWN + 6.5*LEFT,
        "default_graph_colors" : [DISTANCE_COLOR, VELOCITY_COLOR],
        "default_derivative_color" : VELOCITY_COLOR,
        "time_of_journey" : 10,
        "care_movement_rate_func" : smooth
    }
    
    def construct(self):
        def x_t(t):
            #return t**2/5
            if t < 10:
                return (t**2)/5
            elif 10 <= t and t < 15:
                return 4*(t-5)
            elif 15 <= t and t < 25:
                return (-(2/5)*((t-20)**2)) + 50
            elif 25 <= t and t < 30:
                return -4*(t-35)
            elif 30 <= t < 40:
                return ((t-40)**2)/5
            else:
                return 0
       
        title = TextMobject("Gráfica posición-tiempo")
        self.setup_axes()
        origin = self.coords_to_point(0, 0)
        
        ecuacion_pos = TexMobject("x = ").move_to(np.array([3.0, 1.0, 0]))
        L = Line(np.array([4, 3, 0]), np.array([4, -1, 0]), stroke_width = 3, color = BLUE)
        b1 = Brace(L, direction = L.copy().rotate(-PI/2).get_unit_vector()).set_color(WHITE)
        posicion = self.get_graph(lambda t : x_t(t), 
                                    color = WHITE,
                                    x_min = 0, 
                                    x_max = 40
                                    )

        self.play(
            ShowCreation(posicion),
            Write(ecuacion_pos),
            Write(b1),
            run_time = 4
        )
        self.wait(2)

