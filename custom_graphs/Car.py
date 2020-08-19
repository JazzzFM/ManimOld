from big_ol_pile_of_manim_imports import *

class IntroduceCar(Scene):
    CONFIG = {
        "should_transition_to_graph" : True,
        "show_distance" : True,
        "point_A" : DOWN+4*LEFT,
        "point_B" : DOWN+5*RIGHT,
    }
    def construct(self):
        point_A, point_B = self.point_A, self.point_B
        A = Dot(point_A)
        B = Dot(point_B)
        line = Line(point_A, point_B)

        VGroup(A, B, line).set_color(WHITE)        
        for dot, tex in (A, "A"), (B, "B"):
            label = TexMobject(tex).next_to(dot, DOWN)
            dot.add(label)

        car = Dot()
        car.set_color(BLUE)
        self.car = car #For introduce_added_mobjects use in subclasses
        car.move_to(point_A)
#        front_line = car.get_front_line()

        time_label = TextMobject("Time (in seconds):", "0")
        time_label.shift(2*UP)

        distance_brace = Brace(line, UP)
        # distance_brace.set_fill(opacity = 0.5)
        distance = distance_brace.get_text("100m")

        self.add(A, B, line, car, time_label)
        #self.play(ShowCreation(front_line))
        #self.play(FadeOut(front_line))
        self.introduce_added_mobjects()
        self.play(
            MoveCar(car, point_B, run_time = 10),
            IncrementNumber(time_label[1], run_time = 11),
            *self.get_added_movement_anims()
        )
        #front_line = car.get_front_line()
        #self.play(ShowCreation(front_line))
        #self.play(FadeOut(front_line))

        if self.show_distance:
            self.play(
                GrowFromCenter(distance_brace),
                Write(distance)
            )
            self.wait()

        if self.should_transition_to_graph:
            self.play(
                car.move_to, point_A,
                FadeOut(time_label),
                FadeOut(distance_brace),
                FadeOut(distance),
            )
            graph_scene = GraphCarTrajectory(skip_animations = True)
            origin = graph_scene.graph_origin
            top = graph_scene.coords_to_point(0, 100)
            new_length = get_norm(top-origin)
            new_point_B = point_A + new_length*RIGHT
            
            car_line_group = VGroup(car, A, B, line)
            for mob in car_line_group:
                mob.generate_target()
            car_line_group.target = VGroup(*[
                m.target for m in car_line_group
            ])
            B = car_line_group[2]
            B.target.shift(new_point_B - point_B)
            line.target.put_start_and_end_on(
                point_A, new_point_B
            )

            car_line_group.target.rotate(np.pi/2, about_point = point_A)
            car_line_group.target.shift(graph_scene.graph_origin - point_A)
            self.play(MoveToTarget(car_line_group, path_arc = np.pi/2))
            self.wait()