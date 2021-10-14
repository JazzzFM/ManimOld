from manimlib.imports import *

class ImagenEjercicio(GraphScene):
    CONFIG = {
        "y_max" : 1,
        "y_min" : 0,
        "x_max" : 50,
        "x_min" : -50,
        "y_tick_frequency" : 1,
        "x_tick_frequency" : 1,
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
        

class ImagenEjercicio2(GraphScene):
    CONFIG = {
        "y_max" : 1,
        "y_min" : 0,
        "x_max" : 1,
        "x_min" : 0,
        "y_tick_frequency" : 1,
        "x_tick_frequency" : 20,
        "axes_color" : WHITE, 
        "graph_origin" : np.array((-6,-3,0)),
        "x_axis_label" : "$x$",
        "y_axis_label" : "$y$",
        "x_labeled_nums" : range(0, 2, 1)
    }
    def construct(self):

        self.setup_axes()

        f_1 = self.get_graph(lambda x :(4)*x*(1-x), 
                                    color = BLUE,
                                    x_min = 0, 
                                    x_max = 1
                                    )
        f_1t = TexMobject("f_{1}(x) = 4^{1}x^{1}(1-x)^{1}").set_color(BLUE)
        f_1t.move_to(np.array([4.5,3,0]))
        f_1t.scale(0.7)
        
        f_2 = self.get_graph(lambda x :(4**2)*(x**2)*(1-x)**2, 
                                    color = GREEN,
                                    x_min = 0, 
                                    x_max = 1
                                    )
        
        f_2t = TexMobject("f_{2}(x) = 4^{2}x^{2}(1-x)^{2}").set_color(GREEN)
        f_2t.move_to(np.array([4.5,2.5,0]))
        f_2t.scale(0.7)
        
        f_3 = self.get_graph(lambda x :(4**4)*(x**4)*(1-x)**4, 
                                    color = YELLOW,
                                    x_min = 0, 
                                    x_max = 1
                                    )
        f_3t = TexMobject("f_{4}(x) = 4^{4}x^{4}(1-x)^{4}").set_color(YELLOW)
        f_3t.move_to(np.array([4.5,2.0,0]))
        f_3t.scale(0.7)
        
        
        f_4 = self.get_graph(lambda x :(4**8)*(x**8)*(1-x)**8, 
                                    color = RED,
                                    x_min = 0, 
                                    x_max = 1
                                    )

        f_4t = TexMobject("f_{8}(x) = 4^{8}x^{8}(1-x)^{8}").set_color(RED)
        f_4t.move_to(np.array([4.5,1.5,0]))
        f_4t.scale(0.7)
        
         
        f_5 = self.get_graph(lambda x :(4**12)*(x**12)*(1-x)**12, 
                                    color = ORANGE,
                                    x_min = 0, 
                                    x_max = 1
                                    )

        f_5t = TexMobject("f_{12}(x) = 4^{12}x^{12}(1-x)^{12}").set_color(ORANGE)
        f_5t.move_to(np.array([4.5,1.0,0]))
        f_5t.scale(0.7)
        
        f_6 = self.get_graph(lambda x :(4**20)*(x**20)*(1-x)**20, 
                                    color = WHITE,
                                    x_min = 0, 
                                    x_max = 1
                                    )

        f_6t = TexMobject("f_{20}(x) = 4^{20}x^{20}(1-x)^{20}").set_color(WHITE)
        f_6t.move_to(np.array([4.5,0.5,0]))
        f_6t.scale(0.7)
        
        f_7 = self.get_graph(lambda x :(4**100)*(x**100)*(1-x)**100, 
                                    color = PURPLE,
                                    x_min = 0, 
                                    x_max = 1
                                    )

        f_7t = TexMobject("f_{100}(x) = 4^{100}x^{100}(1-x)^{100}").set_color(PURPLE)
        f_7t.move_to(np.array([4.5,0.0,0]))
        f_7t.scale(0.7)
        
        
        self.add(f_1, f_1t, f_2, f_2t, f_3, f_3t, f_4, f_4t, f_5, f_5t, f_6, f_6t, f_7, f_7t)
        
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
        
def f(n, x):
    if abs(x) <= n:
        y = 1 - (abs(x)/n)
        y = float(y)
    else:
        y = 0 
    return y
        
class ImagenEjercicio3(GraphScene):
    CONFIG = {
        "y_max" : 1,
        "y_min" : 0,
        "x_max" :  30,
        "x_min" : -30,
        "y_tick_frequency" : 1,
        "x_tick_frequency" : 1,
        "axes_color" : WHITE, 
        "graph_origin" : np.array((0,-3,0)),
        "x_axis_label" : "$x$",
        "y_axis_label" : "$y$",
        "x_labeled_nums" : range(-30, 31, 5)
    }
    def construct(self):

        self.setup_axes()

        f_1 = self.get_graph(lambda x : f(1, x), 
                                    color = BLUE,
                                    x_min = -30, 
                                    x_max =  30
                                    )
        f_1t = TexMobject("f_{1}(x) = \\left( 1-\\frac{|x|}{1} \\right)\\cdot 1_{[-1, 1]}(x)").set_color(BLUE)
        f_1t.move_to(np.array([4.5,3,0]))
        f_1t.scale(0.6)
        
        f_2 = self.get_graph(lambda x : f(2, x), 
                                    color = GREEN,
                                    x_min = -30, 
                                    x_max =  30
                                    )
        
        f_2t = TexMobject("f_{2}(x) = \\left( 1-\\frac{|x|}{2} \\right)\\cdot 1_{[-2, 2]}(x)").set_color(GREEN)
        f_2t.move_to(np.array([4.5,2,0]))
        f_2t.scale(0.6)
        
        f_3 = self.get_graph(lambda x : f(4, x), 
                                    color = YELLOW,
                                    x_min = -30, 
                                    x_max =  30
                                    )
        f_3t = TexMobject("f_{4}(x) = \\left( 1-\\frac{|x|}{4} \\right)\\cdot 1_{[-4, 4]}(x)").set_color(YELLOW)
        f_3t.move_to(np.array([4.5,1,0]))
        f_3t.scale(0.6)
        
        
        f_4 = self.get_graph(lambda x : f(8, x), 
                                    color = RED,
                                    x_min = -30, 
                                    x_max = 30
                                    )

        f_4t = TexMobject("f_{8}(x) = \\left( 1-\\frac{|x|}{8} \\right)\\cdot 1_{[-8, 8]}(x)").set_color(RED)
        f_4t.move_to(np.array([-4.5,3,0]))
        f_4t.scale(0.6)
        
         
        f_5 = self.get_graph(lambda x : f(12, x), 
                                    color = ORANGE,
                                    x_min = -30, 
                                    x_max = 30
                                    )

        f_5t = TexMobject("f_{12}(x) = \\left( 1-\\frac{|x|}{12} \\right)\\cdot 1_{[-12, 12]}(x)").set_color(ORANGE)
        f_5t.move_to(np.array([-4.5, 2,0]))
        f_5t.scale(0.6)
        
        f_7 = self.get_graph(lambda x : f(20, x), 
                                    color = PURPLE,
                                    x_min = -30, 
                                    x_max = 30
                                    )

        f_7t = TexMobject("f_{20}(x) = \\left( 1-\\frac{|x|}{20} \\right)\\cdot 1_{[-20, 20]}(x)").set_color(PURPLE)
        f_7t.move_to(np.array([-4.5,1,0]))
        f_7t.scale(0.6)
        
        
        self.add(f_1, f_1t, f_2, f_2t, f_3, f_3t, f_4, f_4t, f_5, f_5t, f_7, f_7t)
        
        
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





class Ejercicio_1(GraphScene):
    CONFIG = {
        "y_max" : 100,
        "y_min" : 0,
        "x_max" : 100,
        "x_min" : -100,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 10,
        "axes_color" : WHITE,
        "graph_origin" : np.array((0,-3.5,0)),
        "x_axis_label" : "$x$",
        "y_axis_label" : "$y$",
        "x_labeled_nums" : range(-100, 100, 10)
    }
    def construct(self):

        self.setup_axes()

        f = self.get_graph(lambda x : x*x + 7,
                                    color = BLUE,
                                    x_min = -100,
                                    x_max = 100
                                    )
        f_t = TexMobject("f(x) = x^2 + 7").set_color(BLUE)
        f_t.move_to(np.array([4.5,3,0]))
        f_t.scale(0.7)
        self.play(Write(f), Write(f_t))
        self.wait(2)


