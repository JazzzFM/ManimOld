from manimlib.imports import *

class ImagenEjercicio(GraphScene):
    CONFIG = {
        "y_max" : 2,
        "y_min" : -2,
        "x_max" : 50,
        "x_min" : -50,
        "y_tick_frequency" : 1,
        "x_tick_frequency" : 20,
        "axes_color" : WHITE, 
        "graph_origin" : np.array((0,0,0)),
        "x_axis_label" : "$x$",
        "y_axis_label" : "$y$",
        "x_labeled_nums" : range(-50, 51, 10)
    }
    def construct(self):

        self.setup_axes()

        f_1 = self.get_graph(lambda x :(2*x)/(1 + x**2), 
                                    color = BLUE,
                                    x_min = -50, 
                                    x_max = 50
                                    )
        f_1T = ImageMobject("/home/jazzzfm/ManimOld/ESFM/f_1.png").set_color(BLUE)
        f_1T.move_to(np.array([-4, 3, 0]))
        f_1T.scale(0.3)
        
        f_2T = ImageMobject("/home/jazzzfm/ManimOld/ESFM/f_2.png").set_color(GREEN)
        f_2T.move_to(f_1T.get_center() + np.array([0, -0.75, 0]))
        f_2T.scale(0.3)
        
        f_3T = ImageMobject("/home/jazzzfm/ManimOld/ESFM/f_3.png").set_color(ORANGE)
        f_3T.move_to(f_2T.get_center() + np.array([0, -0.75, 0]))
        f_3T.scale(0.3)
        
        f_4T = ImageMobject("/home/jazzzfm/ManimOld/ESFM/f_4.png").set_color(RED)
        f_4T.move_to(f_3T.get_center() + np.array([0, -0.75, 0]))
        f_4T.scale(0.3)
        
        f_2 = self.get_graph(lambda x :(4*x)/(4 + x**2), 
                                    color = GREEN,
                                    x_min = -50, 
                                    x_max = 50
                                    )
        
        f_3 = self.get_graph(lambda x :(6*x)/(9 + x**2), 
                                    color = ORANGE,
                                    x_min = -50, 
                                    x_max = 50
                                    )
        f_4 = self.get_graph(lambda x :(8*x)/(16 + x**2), 
                                    color = RED,
                                    x_min = -50, 
                                    x_max = 50
                                    )
        
        self.add(f_1, f_2, f_3, f_4, f_1T, f_2T, f_3T, f_4T)
    def setup_axes(self):
        GraphScene.setup_axes(self)
        init_label_y = -1
        end_label_y = 1
        step_y = 1
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        self.play(Write(self.x_axis),Write(self.y_axis))