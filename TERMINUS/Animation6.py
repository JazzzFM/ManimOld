from manimlib.imports import *

# Objetivo: Mostrar en una gráfica un punto que indique la posición de un cuerpo en movimeinto,  
# al mismo tiempo que se muestra su posición en una línea recta. 
# La tabla (que no se incluye en la animación) describe el movimiento del cuerpo.
####################################################################################
# Mover el punto en la grafica y en la línea recta. 
# La línea en la gráfica debe ir dibujándose a medida que la animación avanza. 
# Cada intervalo debe durar la misma cantidad de segundos. 

class AnimationSix(GraphScene):
    centro = np.array((-6,-3,0))
    CONFIG = {
        "y_max" : 6000,
        "y_min" : 0,
        "x_max" : 9,
        "x_min" : 0,
        "y_tick_frequency" : 1000,
        "axes_color" : BLUE,
        "graph_origin" : centro,
         "x_axis_label" : "$t(s)$",
        "y_axis_label" : "$X(m)$",
    }
    
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()
        
    def setup_axes(self):
        GraphScene.setup_axes(self)
        # Custom parametters
        
        self.x_axis.add_numbers(*[0,1,2,3,5,4,5,6,7,8,9])
        # Y parametters
        init_label_y = 0
        end_label_y = 6000
        step_y = 1000
        self.y_axis.label_direction = LEFT
        self.y_axis.add_numbers(*range(
                                        init_label_y,
                                        end_label_y+step_y,
                                        step_y
                                    ))
        self.play(Write(self.x_axis),Write(self.y_axis))