from manimlib.imports import *
 
class ImagenTwo(GraphScene):
    centro = np.array((-6,-3,0))
    CONFIG = {
        "y_max" : 6000,
        "y_min" : 0,
        "x_max" : 9,
        "x_min" : 0,
        "y_tick_frequency" : 1000,
        "axes_color" : BLUE,
        "graph_origin" : centro,
         "x_axis_label" : "$y$",
        "y_axis_label" : "$y$", 
    }

    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(ShowCreation(graph), run_time = 2)
        self.wait()
        
    def setup_axes(self):
        GraphScene.setup_axes(self)
        # Y parametters
        init_label_y = 0
        end_label_y = 6000
        step_y = 1000
        self.y_axis.label_direction = LEFT
        self.play(Write(self.x_axis),Write(self.y_axis))