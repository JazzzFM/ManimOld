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

class AnimationOne(ThreeDScene):
#    CONFIG={
#        "camera_config":{"background_color" : Vanilla}
#    }
    def construct(self):
        image = ImageMobject("/home/codexreckoner/manim/media/designs/raster_images/FONDOCOLOR.jpg")
        image.scale(6)
        self.play(FadeIn(image))
        axes = ThreeDAxes()
        axes.set_color("#FFFFFF")
        self.add(axes)
        self.set_camera_orientation(phi = 5 * DEGREES, theta = -90 * DEGREES)
        self.wait(1)
        path  = VMobject()
        path0 = VMobject()

        text = TextMobject("M")
        text.move_to(np.array([-2.5,-2.5, 0]))
        text.set_color(RED)
        self.play(FadeIn(text))
        self.wait(1)

        point = Dot()
        point.move_to(np.array([-2,-2, 0]))
        point.set_color("#FFFFFF")
        self.add(point)
        self.wait(1)

        text = TextMobject("N")
        text.move_to(np.array([2.5, 2.5, 0]))
        text.set_color(GREEN)
        self.play(FadeIn(text))
        self.wait(1)

        point1 = Dot()
        point1.move_to(np.array([2, 2, 0]))
        point1.set_color("#FFFFFF")
        self.add(point1)
        self.wait(2)

        path.set_points_smoothly(
            [   Vector3D(-2,-2, 0),
                Vector3D(-1,-2, 1),
                Vector3D( 1,-1, 2),
                Vector3D( 1, 2, 1),
                Vector3D( 2, 2, 0)])

        path.set_color("#FFFFFF")
        self.play(FadeIn(path))
        self.wait(1)

        path0.set_points_smoothly(
            [   Vector3D(-2,-2, 0),
                Vector3D(-3,-1, 1),
                Vector3D(-2, 1, 2),
                Vector3D( 3, 3, 1),
                Vector3D( 2, 2, 0)])
        path0.set_color(GREEN)
        self.play(FadeIn(path0))
        self.wait(3)
        self.move_camera(phi = 45 * DEGREES, theta =-110 * DEGREES, run_time = 4)
        self.wait(2)

        vecDir = Vector(np.array([2, 2, 0]))
        vecDir.set_color(RED)
        vecDir.scale(2)
        vecDir.move_to(np.array([0, 0, 0]))
        self.play(ShowCreation(vecDir))
        self.wait(3)
