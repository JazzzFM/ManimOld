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

        I = np.array([1, 0, 0])
        K = np.array([0, 0, 1])
        negK = np.array([0, 0,-1])

        def Polygon3D(listOfPoints, aes_color = BLUE, opacity = 0.7):
            H1 =   listOfPoints
            H2 =   []
            for i in range(len(H1)):
                H2.append([H1[i][0],H1[i][1],H1[i][2]])
        
            S=[]
            for i in range(len(H2)-1):
                s1= [(H2[i][0],H2[i][1],H2[i][2]),
                    (H2[i+1][0],H2[i+1][1],H2[i+1][2]),
                    (H2[i+1][0],H2[i+1][1],H1[i+1][2]),
                    (H2[i][0],H2[i][1],H1[i][2])]
                S.append(Polygon(*s1,fill_color=aes_color, fill_opacity=opacity, color=aes_color,stoke_width=0.1))
        
            b = Polygon(*H1,fill_color=aes_color, fill_opacity=opacity, color=aes_color,stoke_width=0.1)
            h = Polygon(*H2,fill_color=aes_color, fill_opacity=opacity, color=aes_color,stoke_width=0.1)
            s = VGroup(*S)
            poly3D = VGroup(*[b,h,s])
            return poly3D

        def edge(a, b, width, aes_color = BLUE):

            vectorObj = []
            u = [a, b]
            vectorD = np.array([a[0] - b[0], a[1] - b[1], a[2] - b[2]])
            h = [
                np.array([vectorD[0], vectorD[1], 0]),
                np.array([vectorD[0], vectorD[1], vectorD[2]]),
                np.array([0, 0, vectorD[2]]),
                np.array([
                    vectorD[0] + u[1][0],
                    vectorD[1] + u[1][1],
                    vectorD[2] + u[1][2]
                    ])
            ]

            longitud = np.linalg.norm(vectorD)
            if longitud > 0:

                ajuste = 1.0

                #if vectorD[2] < 0:
                #    s = [
                #        np.array([0, 0, longitud*0.05]),                             #0
                #        np.array([ width, width, longitud]),                    #1
                #        np.array([-width, width, longitud]),                    #2
                #        np.array([-width,-width, longitud]),                    #3
                #        np.array([ width,-width, longitud]),                    #4
                #        np.array([ width, width, longitud*0.3]),                #5
                #        np.array([-width, width, longitud*0.3]),                #6
                #        np.array([-width,-width, longitud*0.3]),                #7
                #        np.array([ width,-width, longitud*0.3]),                #8              
                #        np.array([ width*2.97, width*2.97, longitud * 0.3]),      #9
                #        np.array([-width*2.97, width*2.97, longitud * 0.3]),      #10
                #        np.array([-width*2.97,-width*2.97, longitud * 0.3]),      #11
                #        np.array([ width*2.97,-width*2.97, longitud * 0.3])       #12     0 - 13
                #    ]
                #else:
                s = [
                    np.array([0, 0, longitud]),                             #0
                    np.array([ width, width, longitud * 0.7]),              #1
                    np.array([-width, width, longitud * 0.7]),              #2
                    np.array([-width,-width, longitud * 0.7]),              #3
                    np.array([ width,-width, longitud * 0.7]),              #4
                    np.array([ width, width, 0.0]),                         #5
                    np.array([-width, width, 0.0]),                         #6
                    np.array([-width,-width, 0.0]),                         #7
                    np.array([ width,-width, 0.0]),                         #8              
                    np.array([ width*2.97, width*2.97, longitud * 0.7]),      #9
                    np.array([-width*2.97, width*2.97, longitud * 0.7]),      #10
                    np.array([-width*2.97,-width*2.97, longitud * 0.7]),      #11
                    np.array([ width*2.97,-width*2.97, longitud * 0.7])       #12     0 - 13
                ]

                P_pro_p_k = np.dot(h[0], I)
                abs_pro_p = np.linalg.norm(h[0])
                phi = np.arccos(P_pro_p_k / abs_pro_p)

                P_p_k = 1
                if h[1][2] > 0:
                    P_p_k = np.dot(h[1], K)
                else:
                    P_p_k = np.dot(h[1], negK)

                abs_p = np.linalg.norm(h[1])
                teta = np.arccos(P_p_k / abs_p)

                Ry_teta2 = np.array([
                [ np.cos(-teta), 0, np.sin(-teta)], 
                [0, 1, 0],
                [-np.sin(-teta), 0,  np.cos(-teta)]])
    
                #az = 3.1415 * 0.25
                Rz_phi1 = np.array([
                [np.cos(phi),-np.sin(phi), 0],
                [np.sin(phi), np.cos(phi), 0],
                [0, 0, 1]])

                Rz_phi2 = np.array([
                [np.cos(-phi),-np.sin(-phi), 0],
                [np.sin(-phi), np.cos(-phi), 0],
                [0, 0, 1]])

                rotated = []

                if teta == 0.0:
                    for k in range(0, 13):
                        rotated.append(np.array([s[k][0] + h[3][0], s[k][1] + h[3][1], s[k][2] + h[3][2]]))
                else:
                    if vectorD[1] > 0:
                        for k in range(0, 13):
                            rotated.append(np.matmul(Ry_teta2, s[k]))
                            rotated[k] = np.matmul(Rz_phi1, rotated[k])
                    else:
                        for k in range(0, 13):
                            rotated.append(np.matmul(Ry_teta2, s[k]))
                            rotated[k] = np.matmul(Rz_phi2, rotated[k])

                    for k in range(0, 13):
                        rotated[k] = np.add(
                            rotated[k], 
                            h[3])

                square1 = [rotated[1], rotated[4], rotated[8], rotated[5]]
                square2 = [rotated[3], rotated[7], rotated[8], rotated[4]]
                square3 = [rotated[2], rotated[3], rotated[7], rotated[6]]
                square4 = [rotated[1], rotated[2], rotated[6], rotated[5]]

                triangle1 = [rotated[0], rotated[9], rotated[10]]
                triangle2 = [rotated[0], rotated[10], rotated[11]]
                triangle3 = [rotated[0], rotated[11], rotated[12]]
                triangle4 = [rotated[0], rotated[12], rotated[9]]
    
                #squ1 = Polygon(*square1)
                vectorObj.append(Polygon3D(square1, aes_color, 0.7))
                #self.play(FadeIn(vectorObj[0]), run_time = 0.1)
                #self.wait(0.001)

                vectorObj.append(Polygon3D(square2, aes_color, 0.7))
                #self.play(FadeIn(vectorObj[1]), run_time = 0.1)
                #self.wait(0.001)

                vectorObj.append(Polygon3D(square3, aes_color, 0.7))
                #self.play(FadeIn(vectorObj[2]), run_time = 0.1)
                #self.wait(0.001)

                vectorObj.append(Polygon3D(square4, aes_color, 0.7))
                #self.play(FadeIn(vectorObj[3]), run_time = 0.1)
                #self.wait(0.001)

                vectorObj.append(Polygon3D(triangle1, aes_color, 0.7))
                #self.play(FadeIn(vectorObj[4]), run_time = 0.1)
                #self.wait(0.001)

                vectorObj.append(Polygon3D(triangle2, aes_color, 0.7))
                #self.play(FadeIn(tri2), run_time = 0.1)
                #self.wait(0.001)

                vectorObj.append(Polygon3D(triangle3, aes_color, 0.7))
                #self.play(FadeIn(tri3), run_time = 0.1)
                #self.wait(0.001)

                vectorObj.append(Polygon3D(triangle4, aes_color, 0.7))
                #self.play(FadeIn(tri4), run_time = 0.1)
                #self.wait(0.001)

            return vectorObj

        def edgeGo(a, b, width, aes_color = BLUE):

            vectorD = np.subtract(a, b)

            if vectorD[2] < 0:
                return edge(a, b, width, aes_color)
            else:
                return edge(b, a, width, aes_color)

        def playVector(vectorObj):

            self.play(FadeIn(vectorObj[0]), run_time = 0.1)
            self.wait(0.001)
            
            self.play(FadeIn(vectorObj[1]), run_time = 0.1)
            self.wait(0.001)
            
            self.play(FadeIn(vectorObj[2]), run_time = 0.1)
            self.wait(0.001)
            
            self.play(FadeIn(vectorObj[3]), run_time = 0.1)
            self.wait(0.001)
            
            self.play(FadeIn(vectorObj[4]), run_time = 0.1)
            self.wait(0.001)
            
            self.play(FadeIn(vectorObj[5]), run_time = 0.1)
            self.wait(0.001)
            
            self.play(FadeIn(vectorObj[6]), run_time = 0.1)
            self.wait(0.001)
            
            self.play(FadeIn(vectorObj[7]), run_time = 0.1)
            self.wait(0.001)

        def deleteVector(vectorObj):

            self.play(FadeOut(vectorObj[0]), run_time = 0.1)
            self.remove(vectorObj[0])
            
            self.play(FadeOut(vectorObj[1]), run_time = 0.1)
            self.remove(vectorObj[1])
            
            self.play(FadeOut(vectorObj[2]), run_time = 0.1)
            self.remove(vectorObj[2])
            
            self.play(FadeOut(vectorObj[3]), run_time = 0.1)
            self.remove(vectorObj[3])
            
            self.play(FadeOut(vectorObj[4]), run_time = 0.1)
            self.remove(vectorObj[4])
            
            self.play(FadeOut(vectorObj[5]), run_time = 0.1)
            self.remove(vectorObj[5])
            
            self.play(FadeOut(vectorObj[6]), run_time = 0.1)
            self.remove(vectorObj[6])
            
            self.play(FadeOut(vectorObj[7]), run_time = 0.1)
            self.remove(vectorObj[7])


        gold = 1.618033
        g1 = 1.0 / gold
        g2 = g1 * g1

        v = [
        np.array([ g2,  0,  1]), 
        np.array([-g2,  0,  1]),
        np.array([-g1, g1, g1]),
        np.array([  0,  1, g2]),
        np.array([ g1, g1, g1])]

        aa = np.array([1, 1, 1])
        bb = np.array([1.0, 0.0, 0.0])
        print("\n\nVector Test Include:\n\n")
        
        print("\n\n")

        axes = ThreeDAxes()
        axes.set_color(BLACK)
        self.add(axes)
        
        self.set_camera_orientation(phi = 0 * DEGREES, theta = -90 * DEGREES) #0   -90
        self.wait(1)
        
        text0 = TexMobject("(x, y)")
        text0.move_to(np.array([3.7, 3, 0]))
        text0.set_color(BLACK)

        puto = Dot()
        puto.move_to(np.array([3, 3, 0]))
        puto.scale(1.6)
        puto.set_color(BLACK)

        self.play(FadeIn(puto))
        self.play(FadeIn(text0))
        self.wait(1.5)

        center = np.array([0, 0, 0])
        w = 0.05
        
        print("Vector A:")
        vector0 = edgeGo(np.array([3, 3, 0]), center, w, RED)
        playVector(vector0)
        print("end")
        self.wait(2)

        text = TexMobject("\\textbf{A}")
        text.move_to(np.array([1.5, 2.3, 0]))
        text.set_color(BLACK)
        self.play(FadeIn(text))
        self.wait(1)

        print("Vector Ax:")
        vector01 = edgeGo(np.array([3, 0, 0]), center, w, BLUE)
        playVector(vector01)
        print("end")
        self.wait(1)

        text00 = TexMobject("\\textbf{A}_{x}")
        text00.move_to(np.array([1.5, -0.7, 0]))
        text00.set_color(BLACK)
        self.play(FadeIn(text00))
        self.wait(1)

        print("Vector Ay:")
        vector02 = edgeGo(np.array([3, 3, 0]), np.array([3, 0, 0]), w, GREEN)
        playVector(vector02)
        print("end")
        self.wait(1)

        text01 = TexMobject("\\textbf{A}_{y}")
        text01.move_to(np.array([3.7, 1.5, 0]))
        text01.set_color(BLACK)
        self.play(FadeIn(text01))
        self.wait(1)

        text2 = TexMobject("\\textbf{A}", " = ", "\\textbf{A}_{x}", " + ", "\\textbf{A}_{y}")
        text2.move_to(np.array([-4, 2.5, 0]))
        text2.set_color(BLACK)
        text2.scale(1)
        self.play(
            Write(text2[0]),
            Write(text2[1]),
            ReplacementTransform(text00.copy(), text2[2]),
            Write(text2[3]),
            ReplacementTransform(text01.copy(), text2[4]))
        self.wait(2)

        text3 = TexMobject("\\norm{\\textbf{A}} = \sqrt{\\norm{\\textbf{A}_{x}}^2 + \\norm{\\textbf{A}_{y}}^2}")
        text3.move_to(np.array([-4, 1, 0]))
        text3.set_color(BLACK)
        text3.scale(1)
        self.play(Write(text3))
        self.wait(2)

        text31 = TexMobject("\\textit{A} = \sqrt{\\textit{A}_{x}^2 + \\textit{A}_{y}^2}")
        text31.move_to(np.array([-4, 1, 0]))
        text31.set_color(BLACK)
        text31.scale(1)
        self.play(ReplacementTransform(text3, text31))
        self.wait(2)

        self.play(FadeOut(text2))
        self.play(FadeOut(text31))
        self.play(FadeOut(text00))
        self.play(FadeOut(text01))

        print("Vector First_i:")
        vector03 = edgeGo(np.array([2, 0, 0]), center, w, BLACK)
        playVector(vector03)
        print("end")
        self.wait(1.6)

        text4 = TexMobject("\\hat{\\textbf{i}}")
        text4.move_to(np.array([1,-0.7, 0]))
        text4.set_color(BLACK)
        self.play(FadeIn(text4))
        self.wait(1)

        print("Vector First_j:")
        vector04 = edgeGo(np.array([0, 2, 0]), center, w, BLACK)
        playVector(vector04)
        print("end")
        self.wait(1)

        text5 = TexMobject("\\hat{\\textbf{j}}")
        text5.move_to(np.array([-0.7, 1, 0]))
        text5.set_color(BLACK)
        self.play(FadeIn(text5))
        self.wait(1)



        aux0 = TexMobject("\\textit{A}_{x}")
        aux0.move_to(np.array([3, -0.7, 0]))
        aux0.set_color(BLACK)
        #self.play(FadeIn(aux0))
        #self.wait(1)

        aux1 = TexMobject("\\textit{A}_{y}")
        aux1.move_to(np.array([-0.7, 3, 0]))
        aux1.set_color(BLACK)
        #self.play(FadeIn(aux1))
        #self.wait(1)

        text6 = TexMobject("\\textit{A}_{x} \\hat{\\textbf{i}}")
        text6.move_to(np.array([3, -0.7, 0]))
        text6.set_color(BLACK)
        #self.play(FadeIn(text6))
        #self.wait(1)

        text7 = TexMobject("\\textit{A}_{y} \\hat{\\textbf{j}}")
        text7.move_to(np.array([-0.7, 3, 0]))
        text7.set_color(BLACK)
        #self.play(FadeIn(text7))
        #self.wait(1)

        text8 = TexMobject("\\textit{A}_{x} \\hat{\\textbf{i}}", " = \\textbf{A}_{x}")
        text8.move_to(np.array([-4, 2.5, 0]))
        text8.set_color(BLACK)
        text8.scale(1)

        text9 = TexMobject("\\textit{A}_{y} \\hat{\\textbf{j}}", " = \\textbf{A}_{y}")
        text9.move_to(np.array([-4, 1.9, 0]))
        text9.set_color(BLACK)
        text9.scale(1)

        self.play(
            ReplacementTransform(text4, text6))
        self.wait(1)

        self.play(
            ReplacementTransform(text5, text7))
        self.wait(1)

        self.play(
            ReplacementTransform(text6, text8[0]),
            Write(text8[1]))
        self.wait(1)

        self.play(
            ReplacementTransform(text7, text9[0]),
            Write(text9[1]))
        self.wait(1)

        self.play(FadeOut(text8[1]))
        self.play(FadeOut(text9[1]))

        text10 = TexMobject(
                                 "\\textbf{A}",   #0
                                " =",   #1 
             "\\textit{A}_{x}\\hat{\\textbf{i}}",   #2
                               " + ",   #3
             "\\textit{A}_{y}\\hat{\\textbf{j}}"    #4
             )
        text10.move_to(np.array([-4, 1, 0]))
        text10.set_color(BLACK)
        text10.scale(1)

        self.play(
            Write(text10[0]),
            Write(text10[1]),
            ReplacementTransform(text8[0], text10[2]),
            Write(text10[3]),
            ReplacementTransform(text9[0], text10[4]))

        self.wait(2)

        deleteVector(vector02)
        deleteVector(vector01)
        self.play(FadeOut(text10))
        self.play(FadeOut(text))
        self.play(FadeOut(text0))
        deleteVector(vector0)
        self.play(FadeOut(puto))

        self.move_camera(phi = 45 * DEGREES, theta = -90 * DEGREES, run_time = 3)
        self.wait(0.1)
        self.move_camera(phi = 45 * DEGREES, theta = -45 * DEGREES, run_time = 3)
        self.wait(2)

        print("Vector K:")
        vector07 = edgeGo(np.array([0.001, 0.001, 2]), center, w, BLACK)
        playVector(vector07)
        print("end")
        self.wait(0.5)

        base = TexMobject("\\hat{\\textbf{i}}", "\\hat{\\textbf{j}}", "\\hat{\\textbf{k}}")
        base[0].move_to(np.array([1, 0, 0.5]))
        base[0].set_color(BLACK)
        base[0].scale(1)
        base[0].rotate(PI/2, axis = UP)

        base[1].move_to(np.array([0, 1, 0.5]))
        base[1].set_color(BLACK)
        base[1].scale(1)
        base[1].rotate(PI/2, axis = UP)

        base[2].move_to(np.array([0, 0.5, 1]))
        base[2].set_color(BLACK)
        base[2].scale(1)
        base[2].rotate(PI/2, axis = UP)

        base[0].rotate(PI/2, axis = RIGHT)
        base[1].rotate(PI/2, axis = RIGHT)
        base[2].rotate(PI/2, axis = RIGHT)

        self.play(Write(base))
        self.wait(1)
        self.move_camera(phi = 45 * DEGREES, theta = 45 * DEGREES, run_time = 3)

        self.wait(0.4)

        vector3DT0 = edgeGo(np.array([3, 0, 0]), center, w, RED)
        vector3DT1 = edgeGo(np.array([3, 3, 0]), center, w, RED)
        vector3DT2 = edgeGo(np.array([3, 3, 2]), center, w, RED)

        vector3DT3 = edgeGo(np.array([-1, 3, 2]), center, w, RED)
        vector3DT4 = edgeGo(np.array([-1, 4, 2]), center, w, RED)
        vector3DT5 = edgeGo(np.array([-1, 4, 4]), center, w, RED)

        vector3D0 = edgeGo(np.array([3, 0, 0]), center, w, BLUE)
        vector3D1 = edgeGo(np.array([3, 3, 0]), np.array([3, 0, 0]), w, GREEN)
        vector3D2 = edgeGo(np.array([3, 3, 2]), np.array([3, 3, 0]), w, ORANGE)
        
        vector3D3 = edgeGo(np.array([-1, 3, 2]), np.array([3, 3, 2]), w, BLUE)
        vector3D4 = edgeGo(np.array([-1, 4, 2]), np.array([-1, 3, 2]), w, GREEN)
        vector3D5 = edgeGo(np.array([-1, 4, 4]), np.array([-1, 4, 2]), w, ORANGE)

#        self.play(FadeOut(base))

        playVector(vector3D0)
        playVector(vector3D1)
        playVector(vector3D2)
        playVector(vector3DT0)
        self.play(
            ReplacementTransform(vector3DT0[0], vector3DT1[0]),
            ReplacementTransform(vector3DT0[1], vector3DT1[1]),
            ReplacementTransform(vector3DT0[2], vector3DT1[2]),
            ReplacementTransform(vector3DT0[3], vector3DT1[3]),
            ReplacementTransform(vector3DT0[4], vector3DT1[4]),
            ReplacementTransform(vector3DT0[5], vector3DT1[5]),
            ReplacementTransform(vector3DT0[6], vector3DT1[6]),
            ReplacementTransform(vector3DT0[7], vector3DT1[7]))

        text11 = TexMobject(
                       "\\textbf{A}",   #0
                                " =",   #1 
          "\\textit{A}_{x}\\hat{\\textbf{i}}",   #2
                               " + ",   #3
          "\\textit{A}_{y}\\hat{\\textbf{j}}",   #4
                               " + ",   #5
          "\\textit{A}_{z}\\hat{\\textbf{k}}"    #6
             )
        text11.move_to(np.array([3,-2, 2]))
        text11.set_color(BLACK)
        text11.scale(1)
        text11.rotate(PI/2, axis = UP)
        text11.rotate(PI/2, axis = RIGHT)
        self.wait(0.2)
        self.move_camera(phi = 65 * DEGREES, theta = 25 * DEGREES, run_time = 3)
        self.wait(0.5)
        self.play(
            ReplacementTransform(vector3DT1[0], vector3DT2[0]),
            ReplacementTransform(vector3DT1[1], vector3DT2[1]),
            ReplacementTransform(vector3DT1[2], vector3DT2[2]),
            ReplacementTransform(vector3DT1[3], vector3DT2[3]),
            ReplacementTransform(vector3DT1[4], vector3DT2[4]),
            ReplacementTransform(vector3DT1[5], vector3DT2[5]),
            ReplacementTransform(vector3DT1[6], vector3DT2[6]),
            ReplacementTransform(vector3DT1[7], vector3DT2[7]))
        self.wait(0.5)

        text12 = TexMobject(
             "\\textit{A}_{x}\\hat{\\textbf{i}}",   #0
             "\\textit{A}_{y}\\hat{\\textbf{j}}",   #1 
             "\\textit{A}_{z}\\hat{\\textbf{k}}",   #2
             "\\textit{B}_{x}\\hat{\\textbf{i}}",   #3
             "\\textit{B}_{y}\\hat{\\textbf{j}}",   #4
             "\\textit{B}_{z}\\hat{\\textbf{k}}",   #5
             "\\textbf{R}"                        #6
             )

        text12.set_color(BLACK)
        text12.scale(1)
        text12.rotate(PI/2, axis = UP)
        text12.rotate(PI/2, axis = RIGHT)

        text12[0].move_to(np.array([2, 0, 0.7]))
        text12[1].move_to(np.array([3, 2, 0.7]))
        text12[2].move_to(np.array([3, 3.5, 1]))

        #np.array([0, 3, 2]), np.array([3, 3, 2])
        text12[3].move_to(np.array([1.5, 3, 2.5]))

        #np.array([0, 4, 2]), np.array([0, 3, 2])
        text12[4].move_to(np.array([0, 3.5, 2.5]))

        #np.array([0, 4, 4]), np.array([0, 4, 2])
        text12[5].move_to(np.array([0, 4.5, 3]))
        text12[6].move_to(np.array([0, 2, 2.5]))

        self.play(
            Write(text12[0]),
            Write(text12[1]),
            Write(text12[2]))
        self.wait(0.5)

        self.play(Write(text11))
        self.wait(1)

        self.play(FadeOut(text11))
        self.play(FadeOut(base))
        deleteVector(vector07)
        deleteVector(vector04)
        deleteVector(vector03)

        self.wait(1)

        playVector(vector3D3)
        self.play(Write(text12[3]))
        self.wait(0.5)

        self.play(
            ReplacementTransform(vector3DT2[0], vector3DT3[0]),
            ReplacementTransform(vector3DT2[1], vector3DT3[1]),
            ReplacementTransform(vector3DT2[2], vector3DT3[2]),
            ReplacementTransform(vector3DT2[3], vector3DT3[3]),
            ReplacementTransform(vector3DT2[4], vector3DT3[4]),
            ReplacementTransform(vector3DT2[5], vector3DT3[5]),
            ReplacementTransform(vector3DT2[6], vector3DT3[6]),
            ReplacementTransform(vector3DT2[7], vector3DT3[7]))

        self.wait(0.5)

        playVector(vector3D4)
        self.play(Write(text12[4]))

        self.play(
            ReplacementTransform(vector3DT3[0], vector3DT4[0]),
            ReplacementTransform(vector3DT3[1], vector3DT4[1]),
            ReplacementTransform(vector3DT3[2], vector3DT4[2]),
            ReplacementTransform(vector3DT3[3], vector3DT4[3]),
            ReplacementTransform(vector3DT3[4], vector3DT4[4]),
            ReplacementTransform(vector3DT3[5], vector3DT4[5]),
            ReplacementTransform(vector3DT3[6], vector3DT4[6]),
            ReplacementTransform(vector3DT3[7], vector3DT4[7]))

        self.wait(0.5)

        playVector(vector3D5)
        self.play(Write(text12[5]))

        self.play(
            ReplacementTransform(vector3DT4[0], vector3DT5[0]),
            ReplacementTransform(vector3DT4[1], vector3DT5[1]),
            ReplacementTransform(vector3DT4[2], vector3DT5[2]),
            ReplacementTransform(vector3DT4[3], vector3DT5[3]),
            ReplacementTransform(vector3DT4[4], vector3DT5[4]),
            ReplacementTransform(vector3DT4[5], vector3DT5[5]),
            ReplacementTransform(vector3DT4[6], vector3DT5[6]),
            ReplacementTransform(vector3DT4[7], vector3DT5[7]),
            Write(text12[6]))

        self.wait(2)
        text13 = TexMobject(
                       "\\textbf{R}",   #0
                               " = ",   #1
   "\\textit{A}_{x}\\hat{\\textbf{i}}",   #2
                               " + ",   #3
   "\\textit{A}_{y}\\hat{\\textbf{j}}",   #4
                               " + ",   #5
   "\\textit{A}_{z}\\hat{\\textbf{k}}",   #6
                               " + ",   #7
   "\\textit{B}_{x}\\hat{\\textbf{i}}",   #8
                               " + ",   #9
   "\\textit{B}_{y}\\hat{\\textbf{j}}",   #10
                               " + ",   #11
   "\\textit{B}_{z}\\hat{\\textbf{k}}"    #12
             )

        text13.set_color(BLACK)
        text13.scale(0.5)
        text13.rotate(PI/2, axis = UP)
        text13.rotate(PI/2, axis = RIGHT)

        text13.move_to(np.array([5, 4, 1]))

        self.play(
            ReplacementTransform(text12[6], text13[0]),
                                      Write(text13[1]),
            ReplacementTransform(text12[0], text13[2]),
                                      Write(text13[3]),
            ReplacementTransform(text12[1], text13[4]),
                                      Write(text13[5]),
            ReplacementTransform(text12[2], text13[6]),
                                      Write(text13[7]),
            ReplacementTransform(text12[3], text13[8]),
                                      Write(text13[9]),
            ReplacementTransform(text12[4], text13[10]),
                                      Write(text13[11]),
            ReplacementTransform(text12[5], text13[12]))
        self.wait(3)

        self.move_camera(phi = 25 * DEGREES, theta = 65 * DEGREES, run_time = 3)
        self.move_camera(phi = 65 * DEGREES, theta = 25 * DEGREES, run_time = 3)
        self.wait(1)

        deleteVector(vector3DT5)
        deleteVector(vector3D5)
        self.play(
            FadeOut(text13[12]),
            FadeOut(text13[11]))
        deleteVector(vector3D4)
        self.play(
            FadeOut(text13[10]),
            FadeOut(text13[ 9]))
        deleteVector(vector3D3)
        self.play(
            FadeOut(text13[8]),
            FadeOut(text13[7]))
        deleteVector(vector3D2)
        self.play(
            FadeOut(text13[6]),
            FadeOut(text13[5]))
        deleteVector(vector3D1)
        self.play(
            FadeOut(text13[4]),
            FadeOut(text13[3]))

        self.wait(1)

        self.move_camera(phi = 65 * DEGREES, theta = 17 * DEGREES, run_time = 3)
        self.wait(1)

        vector3D6 = edgeGo(np.array([-1, 0, 0]), center, w, BLUE)
        self.play(
            ReplacementTransform(vector3D0[0], vector3D6[0]),
            ReplacementTransform(vector3D0[1], vector3D6[1]),
            ReplacementTransform(vector3D0[2], vector3D6[2]),
            ReplacementTransform(vector3D0[3], vector3D6[3]),
            ReplacementTransform(vector3D0[4], vector3D6[4]),
            ReplacementTransform(vector3D0[5], vector3D6[5]),
            ReplacementTransform(vector3D0[6], vector3D6[6]),
            ReplacementTransform(vector3D0[7], vector3D6[7]))
        self.wait(1)

        text14 = TexMobject(
            "\\textbf{R}",                                                #0
            " = ",                                              #1
   "(\\textit{A}_{x} + \\textit{B}_{x})\\hat{\\textbf{i}}",     #2
                                                     " + ",     #3
   "(\\textit{A}_{y} + \\textit{B}_{y})\\hat{\\textbf{j}}",     #4
                                                     " + ",     #5
   "(\\textit{A}_{z} + \\textit{B}_{z})\\hat{\\textbf{k}}"      #6
             )

        text14.set_color(BLACK)
        text14.scale(0.5)
        text14.rotate(PI/2, axis = UP)
        text14.rotate(PI/2, axis = RIGHT)

        text14.move_to(np.array([5, 4, 1]))
        self.play(
            ReplacementTransform(text13[0], text14[0]),
            ReplacementTransform(text13[1], text14[1]),
            ReplacementTransform(text13[2], text14[2]))
        self.wait(1)

        vector3D7 = edgeGo(np.array([-1, 4, 0]), np.array([-1, 0, 0]), w, GREEN)
        playVector(vector3D7)
        self.wait(0.5)
        self.play(
            Write(text14[3]),
            Write(text14[4]))
        self.wait(0.5)
        vector3D8 = edgeGo(np.array([-1, 4, 4]), np.array([-1, 4, 0]), w, ORANGE)
        playVector(vector3D8)
        self.play(
            Write(text14[5]),
            Write(text14[6]))
        self.wait(1)

        vector3DT_0 = edgeGo(np.array([-1, 0, 0]), center, w, RED)
        vector3DT_1 = edgeGo(np.array([-1, 4, 0]), center, w, RED)
        vector3DT_2 = edgeGo(np.array([-1, 4, 4]), center, w, RED)

        playVector(vector3DT_0)

        self.play(
            ReplacementTransform(vector3DT_0[0], vector3DT_1[0]),
            ReplacementTransform(vector3DT_0[1], vector3DT_1[1]),
            ReplacementTransform(vector3DT_0[2], vector3DT_1[2]),
            ReplacementTransform(vector3DT_0[3], vector3DT_1[3]),
            ReplacementTransform(vector3DT_0[4], vector3DT_1[4]),
            ReplacementTransform(vector3DT_0[5], vector3DT_1[5]),
            ReplacementTransform(vector3DT_0[6], vector3DT_1[6]),
            ReplacementTransform(vector3DT_0[7], vector3DT_1[7]))
        self.wait(0.5)

        self.play(
            ReplacementTransform(vector3DT_1[0], vector3DT_2[0]),
            ReplacementTransform(vector3DT_1[1], vector3DT_2[1]),
            ReplacementTransform(vector3DT_1[2], vector3DT_2[2]),
            ReplacementTransform(vector3DT_1[3], vector3DT_2[3]),
            ReplacementTransform(vector3DT_1[4], vector3DT_2[4]),
            ReplacementTransform(vector3DT_1[5], vector3DT_2[5]),
            ReplacementTransform(vector3DT_1[6], vector3DT_2[6]),
            ReplacementTransform(vector3DT_1[7], vector3DT_2[7]))
        self.wait(0.5)

        text15 = TexMobject(
            "\\textbf{R}",                                                #0
            " = ",                                              #1
   "\\textit{R}_{x}\\hat{\\textbf{i}}",     #2
                                                     " + ",     #3
   "\\textit{R}_{y}\\hat{\\textbf{j}}",     #4
                                                     " + ",     #5
   "\\textit{R}_{z}\\hat{\\textbf{k}}"      #6
             )

        text15.set_color(BLACK)
        text15.scale(0.5)
        text15.rotate(PI/2, axis = UP)
        text15.rotate(PI/2, axis = RIGHT)

        text15.move_to(np.array([5, 4, 1]))

        text16 = TexMobject(
            "\\textbf{R}",                                                #0
            " = ",                                              #1
   "\\textit{R}_{x}\\hat{\\textbf{i}}",     #2
                                                     " + ",     #3
   "\\textit{R}_{y}\\hat{\\textbf{j}}",     #4
                                                     " + ",     #5
   "\\textit{R}_{z}\\hat{\\textbf{k}}"      #6
             )

        text16.set_color(BLACK)
        text16.scale(1)
        text16.rotate(PI/2, axis = UP)
        text16.rotate(PI/2, axis = RIGHT)

        text16[0].move_to(np.array([-1, 2, 2.5]))
        text16[2].move_to(np.array([-0.5, 0, 0.5]))
        text16[4].move_to(np.array([-1, 2, 0.5]))
        text16[6].move_to(np.array([-1, 4.5, 2]))

        self.play(
            Write(text16[0]),
            Write(text16[2]),
            Write(text16[4]),
            Write(text16[6])
            )

        self.wait(0.5)

        self.play(
            ReplacementTransform(text14[0], text15[0]),
            ReplacementTransform(text14[1], text15[1]),
            ReplacementTransform(text14[2], text15[2]),
            ReplacementTransform(text14[3], text15[3]),
            ReplacementTransform(text14[4], text15[4]),
            ReplacementTransform(text14[5], text15[5]),
            ReplacementTransform(text14[6], text15[6]))
        self.wait(2)
        self.move_camera(phi = 65 * DEGREES, theta = 105 * DEGREES, run_time = 3)
        self.move_camera(phi = 45 * DEGREES, theta = 25 * DEGREES, run_time = 3)
        self.move_camera(phi = 65 * DEGREES, theta = 25 * DEGREES, run_time = 3)
        self.wait(3)