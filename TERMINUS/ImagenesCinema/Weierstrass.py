from manimlib.imports import *

maxn = 10


def func(x, b=3):
    y = 0
    for i in range(1, maxn):
        y += np.cos((b ** i) * PI * x) / (3 ** i)
    return y


class Graph(Scene):
    def construct(self):
        t = ValueTracker(0.1)
        f = FunctionGraph(func, color=GOLD).scale(5)
        axes = Axes(
            x_min=-15,
            x_max=15,
            y_min=-15,
            y_max=15,
            number_line_config={
                "color": LIGHT_GREY,
                "include_tip": True,
                "exclude_zero_from_default_numbers": True,
            },
        )
        f.add_updater(lambda x: x.become(
            FunctionGraph(lambda x: func(x, t.get_value()), color=GOLD).scale(5)))

        self.play(Write(f))
        self.play(t.increment_value, 4.9,  run_time=3, rate_func=linear)
        self.wait()


class Secant(MovingCameraScene):
    CONFIG = {
        "x1": -0.4,
        "x2": -2.0,
        "down": 13.5
    }

    def construct(self):
        f = FunctionGraph(lambda x: self.f_s(x, scale=17) - self.down,
                          color=GOLD, stroke_opacity=0.5)

        self.play(Write(f))
        self.wait()
        p1 = Dot(fill_opacity=1, color=YELLOW)
        p1.shift([self.x1, self.f_s(self.x1) - self.down, 0])

        t = ValueTracker(-2)

        p2 = Dot(fill_opacity=1, color=YELLOW)
        p2.shift([t.get_value(), self.f_s(t.get_value()) - self.down, 0])
        p2.add_updater(lambda x: x.become(
            Dot(fill_opacity=1, color=YELLOW).shift(
                [t.get_value(), self.f_s(t.get_value()) - self.down, 0])
        ))

        line = Line([self.x1, self.f_s(self.x1) - self.down, 0],
                    [t.get_value(), self.f_s(t.get_value()) - self.down, 0])
        line.scale(100)

        def line_update(l):
            line = Line([self.x1, self.f_s(self.x1) - self.down, 0],
                        [t.get_value(), self.f_s(t.get_value()) - self.down, 0])
            line.scale(100)
            l.become(line)

        line.add_updater(line_update)

        self.play(Write(line), Write(p1), Write(p2))
        self.wait()

        self.play(t.increment_value, 1.5,  run_time=3, rate_func=linear)
        self.wait()

        grp = VGroup(f, line, p1, p2)
        self.remove(p1, p2)

        width = p1.get_width()*5

        self.play(
            self.camera_frame.set_width, width,
            self.camera_frame.move_to, p1
        )
        p1.scale(0.05)
        d = Dot(radius=0.05 * DEFAULT_DOT_RADIUS,
                color=YELLOW, point=p2.get_center())
        d.add_updater(lambda x: x.become(
            Dot(fill_opacity=1, radius=0.05 * DEFAULT_DOT_RADIUS, color=YELLOW).shift(
                [t.get_value(), self.f_s(t.get_value()) - self.down, 0])
        ))

        self.add(p1, d)
        self.wait()
        self.play(t.increment_value, 0.09, run_time=3, rate_func=linear)
        self.wait()

    def f_s_point(self, x, scale, point):
        def f(x): return self.f_s(x) - self.down
        def g(x): return f(x - point) - f(point)
        def z(x): return scale * g((1 / scale) * x)
        def ans(x): return z(x + point) + f(point)
        return ans(x)

    @staticmethod
    def func(x, b=3):
        x *= 1/10
        y = 0
        for i in range(1, maxn):
            y += np.cos((b ** i) * PI * x) / (2 ** i)
        return y

    def f_s(self, x, scale=17):
        x *= 1/scale
        return scale * self.func(x)


def anti_func(x, b=3):
    y = 0
    for i in range(1, maxn):
        y += (1 / (9 ** i * PI)) * np.sin(3 ** i * PI * x)
        # y += -((b ** i) * PI) * np.sin((b ** i) * PI * x) / 3 ** i
        #y += np.cos((b ** i) * PI * x) / (3 ** i)
    return y


class AntiDerivative(Scene):
    def construct(self):
        r_axes = axes = Axes(
            x_min=0,
            x_max=6,
            y_min=-1,
            y_max=1,
            axis_config={"include_tip": False}
        )
        r_axes.shift(3 * LEFT)
        # r_axes.set_opacity(0.5)

        c2 = ParametricFunction(
            self.w_func,
            t_min=0,
            t_max=6,
            color=RED,
        ).shift(3 * LEFT)

        fgrp = VGroup(r_axes, c2)
        fgrp.shift(1.5 * DOWN)

        t = ValueTracker(0)

        grp = VGroup()

        def updater(x):
            rect = self.get_rect(t.get_value())
            x.add_to_back(rect)
            self.bring_to_back(x)
        grp.add_updater(updater)

        axes = Axes(
            x_min=0,
            x_max=6,
            y_min=-1,
            y_max=1,
            axis_config={"include_tip": False}
        )

        def updater2(x):
            f = FunctionGraph(self.anti, x_min=-0.01, x_max=t.get_value())
            f.shift(3 * LEFT + 1.5 * UP)
            x.become(f)

        f2 = FunctionGraph(self.anti, x_min=0, x_max=6)
        f2.add_updater(updater2)

        grp2 = VGroup(axes, f2)
        grp2.shift(3 * LEFT + 1.5 * UP)

        self.play(Write(fgrp), Write(grp))
        self.play(Write(axes), Write(f2))
        self.bring_to_back(grp)
        self.wait()
        self.play(t.increment_value, 6,  run_time=6, rate_func=linear)
        self.wait()

    def anti(self, x, dx=0.1):
        return 20 * anti_func(x / 5)

    @staticmethod
    def w_func(t):
        return [t, 2.5 * func(t / 5), 0]

    def get_rect(self, t, dx=0.025):
        y = self.w_func(t)[1]
        pairity = -1 if y < 0 else (0 if y  == 0 else 1)

        return Line(
            ORIGIN,
            pairity * (abs(y) - dx) * UP,
            stroke_width=8,
            stroke_opacity=0.75,
            color=BLUE_E
        ).set_opacity(0.75).shift(3 * LEFT + 1.5 * DOWN + (t * RIGHT))


class TestScene(Scene):
    def construct(self):
        l = Line(ORIGIN, 2 * RIGHT)

class LebesgueIntegral(Scene):
    CONFIG = {
        "func": lambda x: -0.9 * (x - 2.5) ** 2 + 2.5,
    }

    def construct(self):
        axes = Axes(
            x_min=0,
            x_max=5,
            y_min=0,
            y_max=3,
            axis_config={
                "include_tip": False
            }
        )
        f = FunctionGraph(self.func, x_min=0.833, x_max=4.167,
                          color=WHITE, stroke_width=2)
        rects = VGroup(
            *[self.get_lebesgue_rectangles(dx=dx) for dx in np.arange(0.5, 0.1, -0.1)]
        )
        grp = VGroup(axes, f, rects)
        grp.center()
        grp.scale(2)

        self.play(Write(axes), Write(f))
        self.play(Write(rects[0]))
        self.wait(1)

        for rect in rects[1:]:
            self.play(Transform(rects[0], rect))
            self.wait(1)

    def get_lebesgue_rectangles(self, dx=0.2, y=(0, 2.4)):
        rects = VGroup()
        y_range = np.arange(y[0], y[1], dx)
        colors = color_gradient([BLUE, GREEN], len(y_range))
        for color, y in zip(colors, y_range):
            x = abs(2.5 - ((((y + dx) - 2.5)/(-0.9))**(1/2) + 2.5))
            rect = Rectangle(height=dx, width=2*x, stroke_color=BLACK,  fill_color=color,
                             stroke_opacity=1, fill_opacity=1, stroke_width=2*dx)
            rect.shift([2.5, y+dx/2, 0])
            rects.add(rect)

        return rects
    
class IRLebesgue(Scene):
    def construct(self):
        eq1 = TexMobject("f(x), x \in [0, 1]")
        eq1.scale(1.5)
        eq1.shift(3.25 * UP)

        arr1 = Arrow(2.75 * UP, 2 * UP + 4 * LEFT, color=YELLOW)
        arr2 = Arrow(2.75 * UP, 2 * UP + 4 * RIGHT, color=YELLOW)

        a0 = TexMobject("A_0", color=BLUE)
        a0.scale(1.5)
        a0.shift(1.25 * UP + 4 * LEFT)

        a1 = TexMobject("A_1", color=BLUE)
        a1.scale(1.5)
        a1.shift(1.25 * UP + 4 * RIGHT)

        eq2 = TextMobject(r"\(f(x) = 0 \) \\ \(x\) is rational",
                          tex_to_color_map={"rational": GREEN})
        eq2.shift(0 * UP + 4 * LEFT)

        eq3 = TextMobject(r"\( f(x) = 1 \) \\ \(x\) is irrational",
                          tex_to_color_map={"irrational": GREEN})
        eq3.shift(0 * UP + 4 * RIGHT)

        integ = TexMobject(r"\int_0^1 f(x) \mathrm{d}\mu = 0 \cdot \mu (A_0) + 1 \cdot \mu (A_1)",
                           tex_to_color_map={r"A_0": BLUE, r"A_1": BLUE, r"\mu": GOLD})
        integ.shift(2 * DOWN)
        integ.scale(1.5)

        self.play(Write(eq1))
        self.play(Write(arr1), Write(arr2))
        self.play(Write(a0), Write(eq2))
        self.play(Write(a1), Write(eq3))
        self.wait()

        self.play(Write(integ))
        self.wait()

        self.play(Uncreate(VGroup(eq1, arr1, arr2, a0, eq2, a1, eq3)))
        self.play(integ.shift, 3 * UP)
        self.wait()

        soln = TexMobject(r"= 0 \cdot 0 + 1 \cdot 1 = ", r"1")
        soln.scale(1.5)
        soln.shift(1 * DOWN + 1 * RIGHT)

        brect = BackgroundRectangle(
            soln[-1],
            color=YELLOW,
            fill_opacity=0,
            stroke_width=4,
            stroke_opacity=1,
            buff=0.25
        )

        self.play(Write(soln))
        self.play(Write(brect))
        self.wait()


class LebesgueEq(Scene):
    def construct(self):
        title = TextMobject("Lebesgue Integral", color=PURPLE)
        title.scale(1.5)
        title.shift(3 * UP)

        self.play(FadeInFromDown(title))
        self.wait()

        eq1 = TexMobject(r"\int_{a}^{b} f(x) \mathrm{d} \mu =\sum_{i=1}^{n} y_{i} \cdot \mu \left(A_{y_{i}}\right)",
                         tex_to_color_map={r"A_{y_{i}}": BLUE, r"\mu": GOLD})
        eq1.scale(1.5)
        eq1.shift(1 * UP)

        self.play(Write(eq1))
        self.wait()

        eq2 = TexMobject(r"\int_{a}^{b} f(x) d \mu =\lim _{n \rightarrow \infty} \int_{a}^{b} f_{n}(x) d \mu",
                         tex_to_color_map={r"f_{n}": BLUE, r"\mu": GOLD})
        eq2.scale(1.5)
        eq2.shift(2 * DOWN)

        self.play(Write(eq2))
        self.wait()
        
class HigherDim(ThreeDScene):
    def construct(self):
        axis_config = {
            "x_min": -5,
            "x_max": 5,
            "y_min": -5,
            "y_max": 5,
            "z_min": -3.5,
            "z_max": 3.5,
        }
        axes = ThreeDAxes(**axis_config)
        cubes = VGroup()

        for x in np.arange(-5, 5.1, 0.5):
            for y in np.arange(-5, 5.1, 0.5):
                z = np.sin(x) + np.cos(y)
                p = Prism(dimensions=[0.5, 0.5, z])
                p.shift([x, y, z/2])
                cubes.add(p)

        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.play(Write(axes))
        self.play(Write(cubes))
        self.begin_ambient_camera_rotation(rate=0.08)
        self.wait(35)