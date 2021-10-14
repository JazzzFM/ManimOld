from manimlib.imports import *
import math

class MyBox(Cube):
    
    CONFIG = {
        'pos': ORIGIN,
        'box_height': 2,
        'bottom_size': [1, 1],
        'fill_opacity': 1,
    }

    def __init__(self, **kwargs):
        Cube.__init__(self, **kwargs)
        self.box_size = np.array([self.bottom_size[0], self.bottom_size[1], self.box_height])
        self.scale(self.box_size/2)
        # self.move_to(self.pos + self.box_height * OUT/2)
        self.move_to(self.pos)
        self.reset_color()

    def update_height(self, new_height):
        self.scale(np.array([1, 1, new_height/self.box_height])) #.shift(OUT * (new_height - self.height)/2)
        self.box_height = new_height

    def update_top_and_bottom(self, top, bottom):
        new_height = abs(top-bottom)
        old_center = self.get_center()
        self.update_height(new_height)
        self.shift(((top+bottom)/2 - old_center[-1]) * OUT)

    def update_top(self, top):
        bottom = self.get_center()[-1] - self.box_height/2
        self.update_top_and_bottom(top, bottom)

    def update_bottom(self, bottom):
        top = self.get_center()[-1] + self.box_height/2
        self.update_top_and_bottom(top, bottom)

    def reset_color(self):
        colors = color_gradient([WHITE, self.get_color(), BLACK], 11)
        self[0].set_fill(color=colors[8])
        self[1].set_fill(color=colors[3])
        self[2].set_fill(color=colors[8])
        self[3].set_fill(color=colors[2])
        self[4].set_fill(color=colors[5])
        self[5].set_fill(color=colors[7])

class MyBoxes(VGroup):

    CONFIG = {
        'center': ORIGIN,
        'bottom_size': [0.25, 0.25],
        'box_height': 2,
        'gap': 0,
        'fill_color': BLUE,
        'resolution': (20, 20),
    }

    def __init__(self, **kwargs):

        VGroup.__init__(self, **kwargs)
        self.create_boxes(self.resolution)
        self.mask_array = np.zeros(self.resolution)
        self.colors = color_gradient([BLUE_D, YELLOW, RED, RED_D], 110)

    def create_boxes(self, resolution=(20, 20)):
        a, b = self.bottom_size[0] + self.gap, self.bottom_size[1] + self.gap
        m, n = resolution[0], resolution[1]
        for i in range(m):
            for j in range(n):
                box_ij = MyBox(pos=a * (j - n/2 + 1/2) * RIGHT + b * (i - m/2 + 1/2) * UP, bottom_size=self.bottom_size,
                               box_height=self.box_height, fill_color=self.fill_color)
                box_ij.reset_color()
                self.add(box_ij)

    def update_height_by_2darray(self, arr_2d):
        m, n = self.resolution[0], self.resolution[1]
        if len(arr_2d)>=m and len(arr_2d[0])>=n:
            for i in range(m):
                for j in range(n):
                    self[i*n+j].update_height(arr_2d[i, j])

    def update_height_by_func(self, func, s=1):
        for box in self:
            center = box.get_center()
            box.update_height(func(center[0], center[1]) * s)

    def update_top_and_bottom_by_2darray(self, arr_top, arr_bottom):
        m, n = self.resolution[0], self.resolution[1]
        if len(arr_top)>=m and len(arr_top[0])>=n and len(arr_bottom)>=m and len(arr_bottom[0])>=n:
            for i in range(m):
                for j in range(n):
                    self[i*n+j].update_top_and_bottom(arr_top[i, j], arr_bottom[i, j])

    def update_top_and_bottom_by_func(self, func_top, func_bottom, s=1):
        for box in self:
            center = box.get_center()
            box.update_top_and_bottom(func_top(center[0], center[1]) * s, func_bottom(center[0], center[1]) * s)

    def update_top_by_func(self, func_top, s=1):
        for box in self:
            center = box.get_center()
            box.update_top(func_top(center[0], center[1]) * s)

    def update_bottom_by_func(self, func_bottom, s=1):
        for box in self:
            center = box.get_center()
            box.update_top(func_bottom(center[0], center[1]) * s)

    def update_color_by_func(self, func):

        a, b = self.bottom_size[0] + self.gap, self.bottom_size[1] + self.gap
        m, n = self.resolution[0], self.resolution[1]
        x, y = np.linspace(-a * n/2, a * n/2, n), np.linspace(-b * m/2, b * m/2, m)
        X, Y = np.meshgrid(x, y)
        Z = func(X, Y)
        z_min, z_max = Z.min(), Z.max()
        # print(z_min, z_max)

        for box in self:
            center = box.get_center() + box.box_height/2 * OUT
            # print(int((func(center[0], center[1]) - z_min)/(z_max-z_min) * 100))
            box.set_color(self.colors[int((func(center[0], center[1]) - z_min)/(z_max-z_min) * 100)])
            box.reset_color()

    def update_color_by_2darray(self, top_array):
        Z = top_array
        m, n = self.resolution[0], self.resolution[1]
        z_min, z_max = Z.min(), Z.max()
        if len(Z) >= m and len(Z) >= n:
            for i in range(m):
                for j in range(n):
                    self[i*n+j].set_color(self.colors[int((Z[i, j] - z_min)/(z_max-z_min) * 100)])
                    self[i*n+j].reset_color()

    def set_mask_array(self, mask):
        self.mask_array = mask

    def apply_mask(self):

        m, n = self.resolution[0], self.resolution[1]
        for i in range(m):
            for j in range(n):
                if self.mask_array[i, j] == 1.: # if self.mask_array[i, j]:
                    self[i*n+j].set_fill(opacity=0)
        
#########################################            

class Sierpinski1(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -45 * DEGREES,
            "distance": 50,
            },
        "camera_config": {
            "background_color":BLACK,
            },
        "iteration":4,
        "sponge_size":4,
        }
    def construct(self):
        self.set_camera_to_default_position()
        #self.add(self.get_axes())
        Sponge = MyBoxes(
            bottom_size=[self.sponge_size,self.sponge_size],
            box_height=self.sponge_size,
            resolution=(1,1),
            fill_color='#388E8E',
            )
        for _ in range(self.iteration-1):
            #mark = Sponge.scale(1/3).move_to(UL*self.sponge_size/3+IN*self.sponge_size/3)
            self.play(
                Sponge.scale,1/3,
                Sponge.move_to,UL*self.sponge_size/3+IN*self.sponge_size/3,
                rate_func=smooth,
                run_time=2,
                )
            mark = Sponge
            pos = [RIGHT,RIGHT,DOWN,DOWN,LEFT,LEFT,UP]
            a = VGroup(mark)
            for i in range(len(pos)):
                a.add(mark.copy().next_to(a[-1],pos[i],buff=0))
            for i in range(5):
                a.add(mark.copy().next_to(a[2*i],OUT,buff=0))
            for i in range(len(pos)):
                a.add(mark.copy().next_to(a[-1],pos[i],buff=0))
            Sponge = a
            self.play(ShowCreation(a[1:]),run_time=3)
        #self.add(Sponge)
        self.wait()
        self.move_camera(
            phi=90*DEGREES,
            theta=0*DEGREES,
            distance=40,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=45*DEGREES,
            theta=45*DEGREES,
            distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=15*DEGREES,
            theta=60*DEGREES,
            distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=30*DEGREES,
            theta=90*DEGREES,
            distance=5,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=30*DEGREES,
            theta=140*DEGREES,
            distance=6,
            rate_func=smooth,
            run_time=3,
            )
        self.wait(3)


class Sierpinski2(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -60 * DEGREES,
            "distance": 50,
            },
        "camera_config": {
            "background_color":BLACK,
            },
        "iteration":5,
        "sponge_size":4,
        }
    def construct(self):
        self.set_camera_to_default_position()
        #self.add(self.get_axes())
        Snowflake = MyBoxes(
            bottom_size=[self.sponge_size,self.sponge_size],
            box_height=self.sponge_size,
            resolution=(1,1),
            fill_color='#F08080',
            )
        self.play(ShowCreation(Snowflake))

        for _ in range(self.iteration-1):
            #mark = Snowflake.scale(1/3).move_to(UL*self.sponge_size/3+IN*self.sponge_size/3)
            self.play(
                Snowflake.scale,1/3,
                Snowflake.move_to,UL*self.sponge_size/3+IN*self.sponge_size/3,
                rate_func=smooth,
                run_time=2,
                )
            mark = Snowflake
            pos = [
                UR*self.sponge_size/3+IN*self.sponge_size/3,
                DL*self.sponge_size/3+IN*self.sponge_size/3,
                DR*self.sponge_size/3+IN*self.sponge_size/3,
                ORIGIN,
                UL*self.sponge_size/3+OUT*self.sponge_size/3,
                UR*self.sponge_size/3+OUT*self.sponge_size/3,
                DL*self.sponge_size/3+OUT*self.sponge_size/3,
                DR*self.sponge_size/3+OUT*self.sponge_size/3,
            ]
            a = VGroup(mark)
            for i in range(len(pos)):
                a.add(mark.copy().move_to(pos[i]))
            Snowflake = a
            self.play(ShowCreation(a[1:]),run_time=4)
        #self.add(Snowflake)
        self.wait()
        self.move_camera(
            phi=90*DEGREES,
            theta=0*DEGREES,
            distance=40,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=45*DEGREES,
            theta=45*DEGREES,
            distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=15*DEGREES,
            theta=60*DEGREES,
            distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=30*DEGREES,
            theta=90*DEGREES,
            distance=5,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=30*DEGREES,
            theta=140*DEGREES,
            distance=6,
            rate_func=smooth,
            run_time=3,
            )
        
        self.wait(3)


class Sierpinski3(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -60 * DEGREES,
            "distance": 50,
            },
        "camera_config": {
            "background_color":BLACK,
            },
        "iteration":7,
        "sponge_size":4,
        }
    def getTetra(self, color='#8B5F65', size=6):
        pos = [
            UP*np.sqrt(3)/3,
            LEFT*0.5+np.sqrt(3)/6*DOWN,
            RIGHT*0.5+np.sqrt(3)/6*DOWN,
            np.sqrt(6)/3*OUT,
        ]
        tetra = VGroup()
        for i in range(4):
            face =  Polygon(
                pos[(i+0)%4],
                pos[(i+1)%4],
                pos[(i+2)%4],
                stroke_width=0,
                fill_opacity=1,
                shade_in_3d=True,
                )
            tetra.add(face)
        tetra.scale(size)
        colors = color_gradient([WHITE, color, BLACK], 11)
        tetra[0].set_fill(color=colors[8])
        tetra[1].set_fill(color=colors[3])
        tetra[2].set_fill(color=colors[8])
        tetra[3].set_fill(color=colors[2])
        return tetra

    def construct(self):
        self.set_camera_to_default_position()
        #self.add(self.get_axes())

        tetra = self.getTetra().shift(OUT/2)
        pos = [
            tetra[0].get_vertices()[0],
            tetra[1].get_vertices()[0],
            tetra[2].get_vertices()[0],
            tetra[3].get_vertices()[0],
        ]
        self.play(ShowCreation(tetra))

        for _ in range(self.iteration-1):
            #mark = Snowflake.scale(1/3).move_to(UL*self.sponge_size/3+IN*self.sponge_size/3)
            mark = tetra.copy()
            self.play(
                tetra.scale,1/2,{"about_point":pos[0]},
                rate_func=smooth,
                run_time=2,
                )
            a = VGroup(tetra)
            for i in range(3):
                a.add(mark.copy().scale(1/2,about_point=pos[i+1]))
            tetra = a
            self.play(ShowCreation(a[1:]),run_time=3)
        
        self.wait()
        self.move_camera(
            phi=55*DEGREES,
            theta=-30*DEGREES,
            distance=50,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=90*DEGREES,
            theta=0*DEGREES,
            distance=40,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=45*DEGREES,
            theta=45*DEGREES,
            distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=15*DEGREES,
            theta=60*DEGREES,
            distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=30*DEGREES,
            theta=120*DEGREES,
            distance=6,
            rate_func=smooth,
            run_time=3,
            )
        
        self.wait(3)


class Sierpinski4(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -30 * DEGREES,
            "distance": 50,
            },
        "camera_config": {
            "background_color":BLACK,
            },
        "iteration":6,
        "sponge_size":4,
        }
    def getPyramid(self, color='#8B5F65', size=6):
        pos = [
            UL,UR,DR,DL,OUT*np.sqrt(3),
        ]
        pyramid = VGroup(
            Polygon(
                *pos[:4],
                stroke_width=0,
                fill_opacity=1,
                shade_in_3d=True,
            ))
        for i in range(4):
            face =  Polygon(
                pos[(i+0)%4],
                pos[(i+1)%4],
                pos[4],
                stroke_width=0,
                fill_opacity=1,
                shade_in_3d=True,
                )
            pyramid.add(face)
        pyramid.scale(size/2)
        colors = color_gradient([WHITE, color, BLACK], 11)
        pyramid[0].set_fill(color=colors[8])
        pyramid[1].set_fill(color=colors[3])
        pyramid[2].set_fill(color=colors[8])
        pyramid[3].set_fill(color=colors[2])
        pyramid[4].set_fill(color=colors[5])
        return pyramid

    def construct(self):
        self.set_camera_to_default_position()
        #self.add(self.get_axes())

        pyramid = self.getPyramid()#.shift(OUT/2)
        self.play(ShowCreation(pyramid))
        
        
        pos = [
            *pyramid[0].get_vertices()[:4],
            pyramid[1].get_vertices()[2],
        ]

        for _ in range(self.iteration-1):
            #mark = Snowflake.scale(1/3).move_to(UL*self.sponge_size/3+IN*self.sponge_size/3)
            mark = pyramid.copy()
            self.play(
                pyramid.scale,1/2,{"about_point":pos[0]},
                rate_func=smooth,
                run_time=2,
                )
            a = VGroup(pyramid)
            for i in range(4):
                a.add(mark.copy().scale(1/2,about_point=pos[i+1]))
            pyramid = a
            self.play(ShowCreation(a[1:]),run_time=3)
        
        self.wait()
        self.move_camera(
            phi=55*DEGREES,
            theta=-30*DEGREES,
            distance=50,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=90*DEGREES,
            theta=0*DEGREES,
            distance=40,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=45*DEGREES,
            theta=45*DEGREES,
            distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=15*DEGREES,
            theta=60*DEGREES,
            distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=30*DEGREES,
            theta=120*DEGREES,
            distance=6,
            rate_func=smooth,
            run_time=3,
            )
        
        self.wait(3)