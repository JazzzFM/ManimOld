from manimlib.imports import *
from networkx.classes import graph

DISTANCE_COLOR = BLUE
TIME_COLOR = YELLOW
VELOCITY_COLOR = GREEN

class Uno(GraphScene):
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
        
        self.wait(5)