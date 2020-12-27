#!/usr/bin/env python

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)


class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()


class WriteStuff(Scene):
    def construct(self):
        example_text = TextMobject(
            "This is a some text",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()


class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()

# See old_projects folder for many, many more
class AudioTest(Scene):
    def construct(self):
        group_dots = VGroup(*[Dot()for i in range(3)])
        group_dots.arrange_submobjects(RIGHT)
        
        for dot in group_dots:
            self.add_sound("/home/codexreckoner/manim/media/designs/sounds/click.wav")
            self.play(FadeIn(dot))
        self.wait(3)

class SVGTest(Scene):
    def construct(self):
        svg = SVGMobject("/home/codexreckoner/manim/media/designs/svg_images/finger.svg")
        self.play(Write(svg))
        self.wait()
class ImageTest(Scene):
    def construct(self):
        image = ImageMobject("/home/codexreckoner/manim/media/designs/raster_images/space.jpg")
        image.scale(7)
        self.play(FadeIn(image))
        self.wait(3)
        
        Text = TextMobject("Prueba para fondos de animacion")
        self.play(Write(Text))
        self.wait(3)
        
class TikzMobject(TextMobject):
    CONFIG = {
        "stroke_width": 3,
        "fill_opacity": 0,
        "stroke_opacity": 1,
    }

class ExampleTikz(Scene):
    def construct(self):
        circuit = TikzMobject(r"""
            \begin{circuitikz}[american voltages]
            \draw
              (0,0) to [short, *-] (6,0)
              to [V, l_=$\mathrm{j}{\omega}_m \underline{\psi}^s_R$] (6,2) 
              to [R, l_=$R_R$] (6,4) 
              to [short, i_=$\underline{i}^s_R$] (5,4) 
              (0,0) to [open,v^>=$\underline{u}^s_s$] (0,4) 
              to [short, *- ,i=$\underline{i}^s_s$] (1,4) 
              to [R, l=$R_s$] (3,4)
              to [L, l=$L_{\sigma}$] (5,4) 
              to [short, i_=$\underline{i}^s_M$] (5,3) 
              to [L, l_=$L_M$] (5,0); 
              \end{circuitikz}
            """
            )
        self.play(Write(circuit))
        self.wait()

