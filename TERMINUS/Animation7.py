from big_ol_pile_of_manim_imports import *

DISTANCE_COLOR = BLUE
TIME_COLOR = YELLOW
VELOCITY_COLOR = GREEN

#Objetivo: Mostrar con una gráfica tiempo-velocidad, la pendiente en un 
# punto y así introducir la idea de la derivada y su posterior uso para elestudio de la cinemática.

# En la curva que describe la velocidad de un cuerpo, elegir dos puntos A y B y unirlos mediante un segmento.
#   Coding in process ... 
# Mostrar las longitudes v y t. 
# Aproximar gradualmente el punto B al punto A. 
# Con ello cambiarántambién la longitud del segmento y de las longitudes v y t.
# Cuando los puntos coincidan, remarcar la pendiente al punto.
# Realizar una gráfica posición-tiempo mostrando el mismo proceso, pero con las unidades correspondientes.
# Para el siguiente diagrama primero mostraremos gráficamente laintegración. El boceto queda pendiente.
# ¿?

def graph_sigmoid_trajectory_function(self, **kwargs):
    graph = self.get_graph(
    lambda t : 100*smooth(t/10.), **kwargs)
    self.s_graph = graph
    return graph

    def show_velocity_graph(self):
        velocity_graph = self.get_derivative_graph(self.s_graph)

        self.play(ShowCreation(velocity_graph))
        def get_velocity_label(v_graph):
            result = self.get_graph_label(
                v_graph,
                label = "v(t)",
                direction = UP+RIGHT,
                x_val = 5,
                buff = SMALL_BUFF,
            )
            self.remove(result)
            return result
        label = get_velocity_label(velocity_graph)
        self.play(Write(label))
        self.wait()
        self.rect.move_to(self.coords_to_point(0, 0), DOWN+LEFT)
        self.play(FadeIn(self.rect))
        self.wait()
        for time, show_slope in (4.5, True), (9, False):
            self.play(
                self.rect.move_to, self.coords_to_point(time, 0), DOWN+LEFT
            )
            if show_slope:
                change_lines = self.get_change_lines(time)
                self.play(FadeIn(change_lines))
                self.wait()
                self.play(FadeOut(change_lines))
            else:
                self.wait()
        self.play(FadeOut(self.rect))

        #Change distance and velocity graphs
        self.s_graph.save_state()
        velocity_graph.save_state()
        label.save_state()
        def shallow_slope(t):
            return 100*smooth(t/10., inflection = 4)
        def steep_slope(t):
            return 100*smooth(t/10., inflection = 25)
        def double_smooth_graph_function(t):
            if t < 5:
                return 50*smooth(t/5.)
            else:
                return 50*(1+smooth((t-5)/5.))
        graph_funcs = [
            shallow_slope,
            steep_slope,
            double_smooth_graph_function,
        ]
        for graph_func in graph_funcs:
            new_graph = self.get_graph(
                graph_func,
                color = DISTANCE_COLOR,
            )
            self.remove(new_graph)
            new_velocity_graph = self.get_derivative_graph(
                graph = new_graph,
            )
            new_velocity_label = get_velocity_label(new_velocity_graph)

            self.play(Transform(self.s_graph, new_graph))
            self.play(
                Transform(velocity_graph, new_velocity_graph),
                Transform(label, new_velocity_label),
            )
            self.wait(2)
        self.play(self.s_graph.restore)
        self.play(
            velocity_graph.restore,
            label.restore,
        )
        self.wait(2)

class AnimationSeven(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 10,
        "x_labeled_nums" : list(range(1, 11)),
        "x_axis_label" : "Tiempo (segundos)",
        "y_min" : 0,
        "y_max" : 110,
        "y_tick_frequency" : 10,
        "y_labeled_nums" : list(range(10, 110, 10)),
        "y_axis_label" : "Distancia Recorrida \\\\ (metros)",
        "graph_origin" : 2.5*DOWN + 5*LEFT,
        "default_graph_colors" : [DISTANCE_COLOR, VELOCITY_COLOR],
        "default_derivative_color" : VELOCITY_COLOR,
        "time_of_journey" : 10,
        "care_movement_rate_func" : smooth,
    }
    def construct(self):
        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/stars.jpg")
        Title = TexMobject("Gráfica velocidad-tiempo")
        image.scale(6)
        self.add(image)

        self.setup_axes(animate = False)
        graph = self.graph_sigmoid_trajectory_function()
        origin = self.coords_to_point(0, 0)

        self.introduce_graph(graph, origin)
        #self.comment_on_slope(graph, origin)
        #self.show_velocity_graph()




   