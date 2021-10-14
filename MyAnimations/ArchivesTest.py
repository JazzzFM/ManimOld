from manimlib.imports import *

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
        image.scale(5)
        self.play(FadeIn(image))
        self.wait(3)
        
        Text = TextMobject("Prueba para fondos de animacion")
        self.play(Write(Text))
        self.wait(3)