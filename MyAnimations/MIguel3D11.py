from manimlib.imports import *
import numpy as np

pi = 3.1415926535897932384626
twoPi = 2 * pi

def Vector3D(x, y, z):
    return np.array([x, y, z])

def printVector3D(v):
    s = "("
    s += str(v[0]) + ", " + str(v[1]) + ", " + str(v[2]) + ")"   
    return s

def mapVector3D(v, R, r):
    return Vector3D((R - r*np.cos(v[0])) * np.cos(v[1]), (R - r*np.cos(v[0])) * np.sin(v[1]), r * np.sin(v[0]))

def square(v0, v1, v2, v3):
    return [v0, v1, v2, v3]

class TestingClass():

    def __init__(self, n, R, r):
        print("\n\n Hello ------------- \n\n")
        self.n = n
        self.R = R
        self.r = r
        self.domain = [[Vector3D(i, j, 0) for j in range(0, n)] for i in range(0, n)]

    def mapDomain(self):
        self.preDomain = [[Vector3D((twoPi * i)/self.n, (twoPi * j)/self.n, 0) for j in range(0, self.n)] for i in range(0, self.n)]        

    def surface(self):
        self.surface = [[ mapVector3D(self.preDomain[i][j], self.R, self.r) for j in range(0, self.n)] for i in range(0, self.n)]

    def __str__(self):
        s = "\nSurface Info\n\n"
        s += "Partition number: " + str(self.n) + "\n"
        s += "Lattice Struct: \n\n"
        for i in range(len(self.preDomain)):
            for j in range(len(self.preDomain[0])):
                s += printVector3D(self.preDomain[i][j]) + "   "
            s += "\n\n\n"
        return s

    def mesh(self):
        self.mesh = [[square(
                            self.surface[i][j], 
                            self.surface[i+1][j],
                            self.surface[i+1][j+1],
                            self.surface[i][j+1]
                                            ) for j in range(self.n-1)] for i in range(self.n-1)]

    def beginTorus(self):
        self.mapDomain()
        self.surface()
        self.mesh()

test0 = TestingClass(10, 3.2, 2.9)
test0.beginTorus()

print("\n---> Torus memory bank ready for use --->\n\n\n")

class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.5,
        "labels_buff": 0,
        "number_decimals": 2
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = TextMobject(f"{coord_point}").scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)


def coord(x,y,z=0):
    return np.array([x,y,z])

def Vector3D(x, y, z):
    return np.array([x, y, z])

def getX(mob):
    return mob.get_center()[0]

def getY(mob):
    return mob.get_center()[1]

# Abstract class:
class PathScene(Scene):
    CONFIG = {
        "x_coords":[0,  1, 3,  -2, -3],
        "y_coords":[3, -2, 1, 2.5, -1]
    }
    """
    The setup method it is executed before the construct method, 
    so whatever they write in the setup method will be executed 
    before the construct method
    """
    def setup(self):
        self.screen_grid = ScreenGrid()
        # tuples = [(0,3),(1,-2)...]
        self.tuples = list(zip(self.x_coords,self.y_coords))

        dots,labels,numbers = self.get_all_mobs()
        self.add(self.screen_grid,dots,labels,numbers)

    def get_dots(self,coords):
        # This is called list comprehension, learn to use it here:
        # https://www.youtube.com/watch?v=AhSvKGTh28Q
        dots = VGroup(*[Dot(coord(x,y)) for x,y in coords])
        return dots

    def get_dot_labels(self,dots,direction=RIGHT):
        labels = VGroup(*[
            # This is called f-strings, learn to use it here:
            # https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
            TexMobject(f"({getX(dot)},{getY(dot)})",height=0.3)\
                      .next_to(dot,direction,buff=SMALL_BUFF) 
                      # This is called Multi-line statement, learn how to use it here:
                      # https://www.programiz.com/python-programming/statement-indentation-comments
            for dot in dots
            ])
        return labels

    def get_dot_numbers(self,dots):
        numbers = VGroup(*[
            TextMobject(f"{n}",height=0.2).next_to(dot,DOWN,buff=SMALL_BUFF)
            for n,dot in zip(range(1,len(dots)+1),dots)
            ])
        return numbers

    def get_all_mobs(self):
        dots = self.get_dots(self.tuples)
        labels = self.get_dot_labels(dots)
        numbers = self.get_dot_numbers(dots)
        return dots,labels,numbers

class ShowPoints(PathScene):
    pass

class PathAsCorners(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_as_corners([*[coord(x,y) for x,y in self.tuples]])
        self.add(path)

class PathSmoothly(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_smoothly([*[coord(x,y) for x,y in self.tuples]])
        self.add(path)

class PathPoints(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_smoothly([*[coord(x,y) for x,y in self.tuples]])
        bezier_points = VGroup(*[Dot(coord,color=RED) for coord in path.points])
        self.add(path,bezier_points)

class AppendPoints(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_as_corners([*[coord(x,y) for x,y in self.tuples]])
        self.add(path)
        self.wait()
        new_points = np.array([coord(-5,1),coord(-1,1)])
        new_dots = self.get_dots(new_points[:,:2])
        """       Special atention to this: ----
        This is an slice, see: https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/
        new_points = 
        [   Columns:
             0   1  2
            [-5  1  0]   <- Row 0
            [-1  1  0]   <- Row 1
                        ]
        So, the first ":" means all rows
        The ":2" means only take the elements from the first column to the second one,
        that is, the columns 0 and 1
        """
        new_labels = self.get_dot_labels(new_dots,UP)
        path.become(
            VMobject().set_points_as_corners([*path.points,*new_points])
        )
        # The most recent version have new methods that can do this more easy.
        VGroup(new_dots,new_labels).set_color(TEAL)
        self.add(new_dots,new_labels)
        self.wait(2)

class TransformPathStyle(PathScene):
    def construct(self):
        path = VMobject()
        path.set_points_as_corners([coord(3, 3), coord(-3, 3), coord(-3,-3), coord(3,-3)])
        self.add(path)
        self.play(path.make_smooth)
        self.wait()

Vanilla = "#F3E5AB"

class Testing(ThreeDScene):
    CONFIG={
        "camera_config":{"background_color" : Vanilla}
    }

    def construct(self):
        axes = ThreeDAxes()
        axes.set_color(BLACK)
        self.add(axes)
        #grid = ScreenGrid()
        #self.add(grid)
        self.set_camera_orientation(phi = 0 * DEGREES, theta = -90 * DEGREES)
        self.wait(1)
        #self.move_camera(np.array[1, 0, 0])
        #self.wait(1)


        text = TexMobject("(x, y)")
        text.move_to(np.array([3.7, 3, 0]))
        text.set_color(BLACK)
        self.play(FadeIn(text))
        self.wait(1.5)

#        vecDir = Vector(np.array([3, 3, 0]))
#        vecDir.set_color(RED)
#        self.play(ShowCreation(vecDir))
#        self.wait(2)
#
#        text = TexMobject("A")
#        text.move_to(np.array([1.5, 2.3, 0]))
#        text.set_color(BLACK)
#        self.play(FadeIn(text))
#        self.wait(1)
#
#        vecDir0 = Vector(np.array([3, 0, 0]))
#        vecDir0.set_color(BLUE)
#        self.play(ShowCreation(vecDir0))
#        self.wait(1)
#
#        text0 = TexMobject("A_{x}")
#        text0.move_to(np.array([1.5, -0.7, 0]))
#        text0.set_color(BLACK)
#        self.play(FadeIn(text0))
#        self.wait(1)
#
#        vecDir1 = Vector(np.array([0, 3, 0]))
#        vecDir1.set_color(GREEN)
#        vecDir1.move_to(np.array([3, 1.5, 0]))
#        self.play(ShowCreation(vecDir1))
#        self.wait(1)
#
#        text1 = TexMobject("A_{y}")
#        text1.move_to(np.array([3.7, 1.5, 0]))
#        text1.set_color(BLACK)
#        self.play(FadeIn(text1))
#        self.wait(1)
#
#        text2 = TexMobject("A = A_{x} + A_{y}")
#        text2.move_to(np.array([-4, 2.5, 0]))
#        text2.set_color(BLACK)
#        text2.scale(1)
#        self.play(Write(text2))
#        self.wait(2)
#
#        text3 = TexMobject("\\norm{A} = \sqrt{A_{x}^2 + A_{y}^2}")
#        text3.move_to(np.array([-4, 1, 0]))
#        text3.set_color(BLACK)
#        text3.scale(1)
#        self.play(Write(text3))
#        self.wait(2)
#
#        self.play(FadeOut(text2))
#        self.play(FadeOut(text3))
#        self.play(FadeOut(text0))
#        self.play(FadeOut(text1))
#
#        vecDir2 = Vector(np.array([2, 0, 0]))
#        vecDir2.set_color(BLUE)
#        self.play(ShowCreation(vecDir2))
#        self.wait(1.6)
#
#        text4 = TexMobject("\\hat{i}")
#        text4.move_to(np.array([1,-0.7, 0]))
#        text4.set_color(BLACK)
#        self.play(FadeIn(text4))
#        self.wait(1)
#
#        vecDir3 = Vector(np.array([0, 2, 0]))
#        vecDir3.set_color(GREEN)
#        self.play(ShowCreation(vecDir3))
#        self.wait(1)
#
#        text5 = TexMobject("\\hat{j}")
#        text5.move_to(np.array([-0.7, 1, 0]))
#        text5.set_color(BLACK)
#        self.play(FadeIn(text5))
#        self.wait(1)
#
#
#
#        aux0 = TexMobject("\\norm{A_{x}}")
#        aux0.move_to(np.array([3, -0.7, 0]))
#        aux0.set_color(BLACK)
#        #self.play(FadeIn(aux0))
#        #self.wait(1)
#
#        aux1 = TexMobject("\\norm{A_{y}}")
#        aux1.move_to(np.array([-0.7, 3, 0]))
#        aux1.set_color(BLACK)
#        #self.play(FadeIn(aux1))
#        #self.wait(1)
#
#
#
#        text6 = TexMobject("\\norm{A_{x}} \\hat{i}")
#        text6.move_to(np.array([3, -0.7, 0]))
#        text6.set_color(BLACK)
#        #self.play(FadeIn(text6))
#        #self.wait(1)
#
#        text7 = TexMobject("\\norm{A_{y}} \\hat{j}")
#        text7.move_to(np.array([-0.7, 3, 0]))
#        text7.set_color(BLACK)
#        #self.play(FadeIn(text7))
#        #self.wait(1)
#
#        text8 = TexMobject("\\norm{A_{x}} \\hat{i}", " = A_{x}")
#        text8.move_to(np.array([-4, 2.5, 0]))
#        text8.set_color(BLACK)
#        text8.scale(1)
#
#        text9 = TexMobject("\\norm{A_{y}} \\hat{j}", " = A_{y}")
#        text9.move_to(np.array([-4, 1.9, 0]))
#        text9.set_color(BLACK)
#        text9.scale(1)
#
#        self.play(
#            ReplacementTransform(text4, text6))
#        self.wait(1)
#
#        self.play(
#            ReplacementTransform(text5, text7))
#        self.wait(1)
#
#        self.play(
#            ReplacementTransform(text6, text8[0]),
#            Write(text8[1]))
#        self.wait(1)
#
#        self.play(
#            ReplacementTransform(text7, text9[0]),
#            Write(text9[1]))
#        self.wait(1)
#
#        self.play(FadeOut(text8[1]))
#        self.play(FadeOut(text9[1]))
#
#        text10 = TexMobject(
#                                 "A",   #0
#                                " =",   #1 
#             "\\norm{A_{x}}\\hat{i}",   #2
#                               " + ",   #3
#             "\\norm{A_{y}}\\hat{j}"    #4
#             )
#        text10.move_to(np.array([-4, 1, 0]))
#        text10.set_color(BLACK)
#        text10.scale(1)
#
#        self.play(
#            Write(text10[0]),
#            Write(text10[1]),
#            ReplacementTransform(text8[0], text10[2]),
#            Write(text10[3]),
#            ReplacementTransform(text9[0], text10[4]))
#
#        self.wait(2)

        self.move_camera(phi = 45 * DEGREES, theta = -90 * DEGREES, run_time = 3)
        self.wait(0.1)
        self.move_camera(phi = 45 * DEGREES, theta = -45 * DEGREES, run_time = 3)
        self.wait(2)

        I = Vector(np.array([2, 0, 0]))
        I.set_color(BLACK)
        self.play(ShowCreation(I))
        self.wait(0.2)

        J = Vector(np.array([0, 2, 0]))
        J.set_color(BLACK)
        self.play(ShowCreation(J))
        self.wait(0.2)

        K = Vector(np.array([0, 0, 2]))
        K.set_color(BLACK)

        K.tip.rotate(PI, axis = LEFT)
        #K.tip.rotate(PI, axis = UP)

        self.play(ShowCreation(K))
        self.wait(0.5)

        base = TexMobject("\\hat{i}", "\\hat{j}", "\\hat{k}")
        base[0].move_to(np.array([1, 0, 0.5]))
        base[0].set_color(BLACK)
        base[0].scale(1)
        base[0].rotate(PI/2, axis = UP)

        base[1].move_to(np.array([0, 1, 0.5]))
        base[1].set_color(BLACK)
        base[1].scale(1)
        base[1].rotate(PI/2, axis = UP)

        base[2].move_to(np.array([0.5, 0, 1]))
        base[2].set_color(BLACK)
        base[2].scale(1)
        base[2].rotate(PI/2, axis = UP)

        base[0].rotate(PI/2, axis = RIGHT)
        base[1].rotate(PI/2, axis = RIGHT)
        base[2].rotate(PI/2, axis = RIGHT)

        self.play(Write(base))
        self.wait(1)
        #self.play(FadeOut(text10))
        self.move_camera(phi = 45 * DEGREES, theta = 45 * DEGREES, run_time = 3)

        self.wait(3)