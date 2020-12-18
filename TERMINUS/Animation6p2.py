from big_ol_pile_of_manim_imports import *

SINE_COLOR = BLUE
X_SQUARED_COLOR = GREEN
SUM_COLOR = YELLOW
PRODUCT_COLOR = YELLOW

class ThreeLines(ReconfigurableScene):
    DR = np.array([3,0,0])
    CONFIG = {
        "start_x" : 3,
        "max_x" : 6000,
        "min_x" : 0,
        "top_x" : 2,
        "example_x" : 1.5,
        "dx" : 0.1,
        "graph_origin" : DR,
        "line_configs" : [
            {
                "func" : lambda x : x,
                "func_label" : "S",
                "triangle_color" : WHITE,
                "center_y" : 3,
                "center_x" : 3,
                "x_min" : 0,
                "x_max" : 6000,
                "numbers_to_show" : [0, 1000, 2000, 3000, 4000, 5000, 6000],
                "numbers_with_elongated_ticks" : [0, 1000, 2000, 3000, 4000, 5000, 6000],
                "tick_frequency" : 250,
            },
        ],
        "line_width" : 8,
        "triangle_height" : 0.25,
    }
    def construct(self):
        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/stars.jpg")
        image.scale(6)
        self.add(image)

        Labela = TextMobject("$x(m)$")
        Labela.move_to(np.array([4.5, 3, 0]))
        self.add(Labela)

        self.line_group = self.get_line_group(self.start_x)
        lines, labels = self.line_group

        for line in lines:
            self.play(Write(line.move_to(np.array([0,2.5,0])), run_time = 0.5))
        self.wait(1)

        last_label = labels[0].copy()
        last_label.move_to(np.array([3,3,0]))
        last_label.set_fill(opacity = 0)
        self.animate_x_change(0, run_time=2)        
        self.animate_x_change(400, run_time=1)
        self.animate_x_change(1100, run_time=2)
        self.animate_x_change(2500, run_time=2)
        self.animate_x_change(2650, run_time=2)        
        self.animate_x_change(2650, run_time=2)
        self.animate_x_change(3500, run_time=2) 
        self.animate_x_change(4600, run_time=2)
        self.animate_x_change(5500, run_time=2)
        self.animate_x_change(5600, run_time=2)
        self.wait(1)
    
    def wiggle_by_dx(self, **kwargs):
        kwargs["run_time"] = kwargs.get("run_time", 1)
        kwargs["rate_func"] = kwargs.get("rate_func", there_and_back)
        target_x = self.line_group.x_val + self.dx
        self.animate_x_change(target_x, **kwargs)

    def animate_x_change(self, target_x, **kwargs):
        #Assume fixed lines, only update labels
        kwargs["run_time"] = kwargs.get("run_time", 2)
        added_anims = kwargs.get("added_anims", [])
        start_x = self.line_group.x_val
        def update(line_group, alpha):
            lines, labels = line_group
            new_x = interpolate(start_x, target_x, alpha)
            for line, label, config in zip(lines, labels, self.line_configs):
                new_label = self.get_line_label(
                    line, new_x, **config
                )
                Transform(label, new_label).update(1)
            line_group.x_val = new_x
        self.play(
            UpdateFromAlphaFunc(self.line_group, update),
            *added_anims,
            **kwargs
        )

    def get_line_group(self, x):
        group = VGroup()
        group.lines, group.labels = VGroup(), VGroup()
        for line_config in self.line_configs:
            number_line = self.get_number_line(**line_config)
            label = self.get_line_label(number_line, x, **line_config)
            group.lines.add(number_line)
            group.labels.add(label)
        group.add(group.lines, group.labels)
        group.x_val = x
        return group

    def get_number_line(
        self, center_y, **number_line_config
        ):
        number_line = NumberLine(color = GREY, **number_line_config)
        number_line.stretch_to_fit_width(self.line_width)
        number_line.add_numbers()
        number_line.shift(center_y*UP)
        number_line.to_edge(LEFT, buff = LARGE_BUFF)

        return number_line

    def get_line_label(
        self, number_line, x, func, func_label, triangle_color, 
        **spillover_kwargs
        ):
        triangle = RegularPolygon(
            n=3, start_angle = -np.pi/2,
            fill_color = triangle_color,
            fill_opacity = 0.75,
            stroke_width = 0,
        )
        triangle.set_height(self.triangle_height)
        triangle.move_to(
            number_line.number_to_point(func(x)), DOWN
        )

        label_mob = TexMobject(func_label)
        label_mob.next_to(triangle, UP, buff = SMALL_BUFF, aligned_edge = LEFT)

        return VGroup(triangle, label_mob)