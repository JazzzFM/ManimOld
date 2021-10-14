from manimlib.imports import *

class Uno(GraphScene):
    CONFIG = {
        "y_max" : 10,
        "y_min" : 0,
        "x_max" : 10,
        "x_min" : 0,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "axes_color" : WHITE,
        "graph_origin": 3 * DOWN + 6 * LEFT,
        "x_label_direction":DOWN,
        "y_label_direction":RIGHT,       
        "x_axis_label": None,
        "x_axis_width":10
    }

    def construct(self):
        origin = 3 * DOWN + 6 * LEFT
        
        self.setup_axes(animate=False) #animate=True to add animation
        self.x_axis.shift(LEFT*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))
        self.y_axis.shift(DOWN*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))
        self.y_axis_label_mob.next_to(self.y_axis[0].get_end(),UP)
        
        p=Dot().move_to(self.coords_to_point(self.x_min, self.y_min))
        
        self.add(p)
        
        P = Dot(np.array([-1.2,0.8,0]))
        P_t = TexMobject("P").move_to(np.array([-0.5,1.1,0]))
        
        self.play(ShowCreation(P), Write(P_t))

        V1 = Arrow(origin-0.15*np.array([1,1,0]), np.array([-1,1,0]), color = RED)
        V1_x = Arrow(origin-0.15*np.array([1,0,0]), origin + np.array([5,0,0]) , color = BLUE)
        V1_y = Arrow(V1_x.get_end() -0.25*np.array([-0.2,1,0]) , V1_x.get_end() + np.array([0.25*0.2, 4.1, 0]), color = GREEN)

        r = TexMobject("\\vec{r}").move_to(V1.get_center() + np.array([-0.5, 0.5, 0]))
        theta = TexMobject("\\theta").move_to(origin + 0.15*np.array([6.5,2.5,0]))
        x_i = TexMobject("x\\hat{i}").move_to(V1_x.get_center() - np.array([0, 0.5, 0]))
        y_j = TexMobject("y\\hat{j}").move_to(V1_y.get_center() + np.array([0.5, 0, 0]))
        
        self.play(
            ShowCreation(V1),
            ShowCreation(V1_x),
            ShowCreation(V1_y),
            Write(r),
            Write(theta),
            Write(x_i),
            Write(y_j),
            run_time = 3
        )
        
        xy = TexMobject("(x, y)").move_to(np.array([-0.7,1.2,0]))
        self.play(ReplacementTransform(P_t, xy), run_time = 3)
        self.wait(3)
        
        seno = TexMobject("sen(\\theta)","=","{y","\\over"," r}")
        seno.shift(np.array([-4,2.8,0]))
        seno.set_color(WHITE)
        
        self.play(Write(seno[0]))
        self.play(Write(seno[1]))
        self.play(Write(seno[3]))
        self.wait(1) 
        
        self.play(ReplacementTransform(y_j.copy(), seno[2]), run_time=2)
        self.play(ReplacementTransform(r.copy(), seno[4]), run_time=2)
        self.wait()
        
        despeje_1 = TexMobject("r sen(\\theta)","=","y")
        despeje_1.set_color(WHITE)
        despeje_1.move_to(np.array([-4,2.8,0]))
        self.play(ReplacementTransform(seno, despeje_1))
        self.wait(1)
        
        coseno = TexMobject("cos(\\theta)", "=","{x","\\over","r}")
        coseno.shift(np.array([-0.5,2.8,0]))
        coseno.set_color(WHITE)
        self.play(Write(coseno[0]))
        self.play(Write(coseno[1]))
        self.play(Write(coseno[3]))
        self.wait(1)
        
        self.play(ReplacementTransform(x_i.copy(), coseno[2]), run_time=2)
        self.play(ReplacementTransform(r.copy(), coseno[4]), run_time=2)
        self.wait(1)

        despeje_2 = TexMobject("r cos(\\theta)","=","x")
        despeje_2.set_color(WHITE)
        despeje_2.move_to(np.array([-0.5,2.8,0]))
        self.play(ReplacementTransform(coseno, despeje_2))
        self.wait(1)
        
        ec_1 = TexMobject("\\theta", "=", "arcsen(","{y","\\over"," r})")
        ec_1.move_to(np.array([3.8,2.8,0]))
        
        ec_2 = TexMobject("\\theta", "=", "arccos(","{x","\\over"," r})")
        ec_2.move_to(np.array([3.8,1.8,0]))
        
        self.play(
            ReplacementTransform(despeje_1.copy(), ec_1),
            ReplacementTransform(despeje_2.copy(), ec_2)
            )
        
        self.wait(3)
        
        r_ec = TexMobject("r", "=", "\\sqrt{x^{2}", "+", "y^{2}}")
        r_ec.move_to(np.array([3.5,-0.5,0]))
        
        ec_3 = TexMobject("\\theta", "=", "arctan(","{y","\\over"," x})")
        ec_3.move_to(np.array([3.5,-1.5,0]))
        
        
        self.play(ReplacementTransform(r.copy(), r_ec[0]),
                  ReplacementTransform(x_i.copy(), r_ec[2]),
                  ReplacementTransform(y_j.copy(), r_ec[4]),
                  Write(r_ec[1]),
                  Write(r_ec[3]),
                  ReplacementTransform(theta.copy(), ec_3[0]),
                  ReplacementTransform(x_i.copy(), ec_3[5]),
                  ReplacementTransform(y_j.copy(), ec_3[3]),
                  Write(ec_3[1]),
                  Write(ec_3[2]),
                  Write(ec_3[4]),
                  run_time=2.5
                  )
        
        self.wait(3)
        
        self.play(
            FadeOut(despeje_1[1]),
            FadeOut(despeje_1[2]),
            FadeOut(despeje_2[1]),
            FadeOut(despeje_2[2]),
            FadeOut(ec_1),
            FadeOut(ec_2)
        )
        
        xy_p = TexMobject("= (", "r cos(\\theta)", ", ", "r sen(\\theta)",")").move_to(np.array([2.2,1.2,0]))
        
        self.play(
            Write(xy_p[0]),
            ReplacementTransform(despeje_1[0], xy_p[1]),
            Write(xy_p[2]),
            ReplacementTransform(despeje_2[0], xy_p[3]),
            Write(xy_p[4])
            )   
        
        self.wait(1)
        
        rt = TexMobject("(", "r", ", ","\\theta",")").move_to(np.array([-0.7,1.2,0]))
        
        self.play(
            FadeOut(xy),
            FadeOut(xy_p),
            Write(rt),
        )
        r_c = rt[1].copy()
        r_c.scale(2)
        t_c = rt[3].copy()
        t_c.scale(2)
        
        self.play(
            FadeOut(rt[1]),
            ReplacementTransform(rt[1].copy(), r_c),
        run_time=2
        )
        
        self.play(
            FadeOut(r_c),
            FadeIn(rt[1]),
        run_time=2
        )
        
        #####
        
        self.play(
            FadeOut(rt[3]),
            ReplacementTransform(rt[3].copy(), t_c),
        run_time=2
        )
        
        self.play(
            FadeOut(t_c),
            FadeIn(rt[3]),
        run_time=2
        )
        #ReplacementTransform(rt[3], t_c)

        self.wait(2)
               

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
        "grid_stroke": 0.1,
        "grid_color": WHITE,
        "axis_color": BLUE,
        "axis_stroke": 2,
        "labels_scale": 0.25,
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
                    label = Text(f"{coord_point}",font="Arial",stroke_width=0).scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes)
   
    
class Dos(GraphScene, MovingCameraScene):
    def construct(self):
        MovingCameraScene.setup(self)
        screen_grid = ScreenGrid()
        self.add(screen_grid)
        
        r = Vector(np.array([3,2,0])).set_color(RED)
        r_t = TexMobject("\\vec{r}").move_to(r.get_center() + np.array([-0.5, 0.5, 0]))
        
        r_b = Arrow(0.92*np.array([3,2,0]), 1.5*np.array([3,2,0]))
        t_b = Arrow(np.array([3.1,1.75,0]), np.array([2,3.5,0]))
        
        teta = TexMobject("\\theta").move_to(np.array([1.45, 0.25, 0]))
        
        self.play(GrowArrow(r), Write(r_t), Write(teta))
        self.wait()
        
        r_bt = TexMobject("\\hat{r}").move_to(1.6*np.array([3,2,0]))
        t_bt = TexMobject("\\hat{\\theta}").move_to(np.array([1.5,3.2,0]))
        
        self.play(GrowArrow(r_b), GrowArrow(t_b)) 
        self.wait(2)
        self.play(Write(r_bt), Write(t_bt)) 
        self.wait(5)
               
        # ----------------------------------------------
        # Siete
    
        rc = Vector(0.5*np.array([3,2,0])).set_color(RED)
        r_tc = TexMobject("\\vec{r}").move_to(rc.get_center() + np.array([-0.5, 0.5, 0]))

        r_bc = r_b.copy()
        r_bc.move_to(1.4*rc.get_end())
        
        t_btc = t_bt.copy()
        t_btc.move_to(np.array([0.3,2,0]))
        
        r_btc = r_bt.copy()
        r_btc.move_to(np.array([2.5, 1, 0]))
        
        t_bc = t_b.copy()
        t_bc.move_to(rc.get_end() + np.array([-0.45,0.67,0]))
        
        self.play(
                  ReplacementTransform(r, rc),
                  ReplacementTransform(r_t, r_tc),
                  ReplacementTransform(r_b, r_bc),
                  ReplacementTransform(t_b, t_bc),
                  ReplacementTransform(t_bt, t_btc),
                  ReplacementTransform(r_bt, r_btc),
                  run_time = 2
                  )
       
        self.wait(3)

        r_2 = Vector(np.array([3,2,0])).set_color(RED)
        r_t2 = TexMobject("\\vec{r}").move_to(r_2.get_center() + np.array([-0.5, 0.5, 0]))
        r_b2 = Arrow(0.92*np.array([3,2,0]), 1.5*np.array([3,2,0]))
        t_b2 = Arrow(np.array([3.1,1.75,0]), np.array([2,3.5,0]))
        r_bt2 = TexMobject("\\hat{r}").move_to(1.6*np.array([3,2,0]))
        t_bt2 = TexMobject("\\hat{\\theta}").move_to(np.array([1.5,3.2,0]))
        
        self.play(
        ReplacementTransform(rc, r_2),
        ReplacementTransform(r_tc, r_t2),
        ReplacementTransform(r_bc, r_b2),
        ReplacementTransform(t_bc, t_b2),
        ReplacementTransform(t_btc, t_bt2),
        ReplacementTransform(r_btc, r_bt2),
        run_time = 2
        )
        
        self.wait(5)
             
        # ----------------------------------------------------
        
        v_cords = []
        v_cords2 = []
        t_cords = []
        t_cords2 = []

        for i in range(35, 385, 5):
            v_cords.append(np.sqrt(13)*np.array([np.cos(PI*i/180), np.sin(PI*i/180), 0]))
            v_cords2.append(np.sqrt(12.5)*np.array([np.cos(PI*(i-4)/180), np.sin(PI*(i-4)/180), 0]))
            t_cords.append(np.sqrt(15.7)*np.array([np.cos(PI*(i+28)/180), np.sin(PI*(i+28)/180), 0]) )
            t_cords2.append(np.sqrt(15.5)*np.array([np.cos(PI*(i+28)/180), np.sin(PI*(i+28)/180), 0]) )

        
        v_arrows = []
        r_arrows = []
        t_arrows = []
        v_tex = []
        r_tex = []
        t_tex = []
        
        dist_1 = np.sqrt(( (0.9*np.sqrt(13)*np.cos(PI*1/180)) - 1.5*np.sqrt(13)*np.cos(PI*1/180) )**2 + (0.9*np.sin(PI*1/180) - 1.5*np.sin(PI*1/180) )**2)
        
        for i in range(0, len(v_cords)):
            v_arrows.append(Vector(0.98*v_cords[i], tip_length = 0.2).set_color(RED))
            r_arrows.append(Arrow(0.9*v_cords[i], 1.5*v_cords[i], tip_length = 0.2) )
            t_arrows.append(Arrow(v_cords2[i], t_cords[i], tip_length = 0.2) )
        
        for i in range(0, len(v_arrows)):
            v_tex.append(TexMobject("\\vec{r}").move_to(v_arrows[i].get_center() + np.array([-0.5, 0.2, 0]) ))
            r_tex.append(TexMobject("\\hat{r}").move_to(1.5*v_arrows[i].get_end()) )
            t_tex.append(TexMobject("\\hat{\\theta}").move_to(t_cords2[i]))
        
        for i in range(0, len(v_arrows)):
            if i == 0:
                    self.play(
                    ReplacementTransform(r_2, v_arrows[0]),
                    ReplacementTransform(r_t2, v_tex[0]),
                    ReplacementTransform(r_b2, r_arrows[i]),
                    ReplacementTransform(t_b2, t_arrows[0]),
                    ReplacementTransform(t_bt2, t_tex[0]),
                    ReplacementTransform(r_bt2, r_tex[0]))
            else:
                self.play(
                    ReplacementTransform(r_arrows[i-1], r_arrows[i]),
                    ReplacementTransform(t_arrows[i-1], t_arrows[i]),
                    ReplacementTransform(v_arrows[i-1], v_arrows[i]),
                    ReplacementTransform(v_tex[i-1], v_tex[i]),
                    ReplacementTransform(r_tex[i-1], r_tex[i]),
                    ReplacementTransform(t_tex[i-1], t_tex[i]),
                        run_time=0.03
                )   

        self.wait(2)
    
        # ---------------------------------------------------------------------
        
        I = Arrow(np.array([2.73, 2, 0]), np.array([2.73 + 2.16, 2, 0]), tip_length = 0.2).set_color(YELLOW)
        J = Arrow(np.array([3, 1.75, 0]), np.array([3.0, 1.77 + 2.16, 0]), tip_length = 0.2).set_color(YELLOW)
        
        i_t = TexMobject("\\hat{i}").move_to(I.get_end() + np.array([0.2,  0.0, 0.0]))
        i_t.set_color(YELLOW)
        i_t.scale(0.4)
        
        j_t = TexMobject("\\hat{j}").move_to(J.get_end() + np.array([ 0.0, 0.2, 0.0]))
        j_t.set_color(YELLOW)
        j_t.scale(0.4)

        R = np.array([4.195, 2.161, 0])
        Base = VGroup(I, J, i_t, j_t).move_to(R)
        
        r_tn = r_tex[len(v_arrows)-1].copy()
        r_tn.scale(0.4)
        
        t_tn = t_tex[len(v_arrows)-1].copy()
        t_tn.scale(0.4)
        
        v_tn = v_tex[len(v_arrows)-1].copy()
        v_tn.scale(0.4)
        
        # ----------------------------------------------------
        
        self.camera_frame.save_state()

        self.play(
            self.camera_frame.scale,.3,
            self.camera_frame.move_to, Base,
            FadeOut(r_arrows[len(v_arrows)-1]),
            FadeOut(t_arrows[len(v_arrows)-1]),
            FadeOut(v_arrows[len(v_arrows)-1]),
            Write(Base)
        )
        
        # -----------------------------------------------------
        
        self.play(
            ReplacementTransform(r_tex[len(v_arrows)-1], r_tn),
            ReplacementTransform(t_tex[len(v_arrows)-1], t_tn),
            ReplacementTransform(v_tex[len(v_arrows)-1], v_tn),
            Write(r_arrows[len(v_arrows)-1].set_color(GRAY)),
            Write(t_arrows[len(v_arrows)-1].set_color(GRAY)),
            Write(v_arrows[len(v_arrows)-1])
        )
        
        self.wait()
        
        # ------------------------------------------------------------
        
        ult = len(v_arrows)-1
        
        py = DashedLine(1.43*v_cords[ult] - np.array([0, 0.5, 0]), 1.43*v_cords[ult])
        py.set_color(GREEN)
        
        ## Animar desde punta a eje
        px = DashedLine(1.43*v_cords[ult] - np.array([1.5, 0, 0]), 1.43*v_cords[ult])
        px.set_color(BLUE)
        
        Lx = Line(1.43*v_cords[ult] - np.array([1.55, 0.56, 0]), 1.43*v_cords[ult] - np.array([0, 0.56, 0]) ).set_color(GREEN)
        Ly = Line(1.43*v_cords[ult] - np.array([1.54, 0.53, 0]), 1.43*v_cords[ult] - np.array([1.54, 0.53, 0]) + np.array([0, 0.55, 0]) ).set_color(BLUE)
        
        
        # -------------------------------------------------------------
        
        tetilla_1 = TexMobject("\\theta").move_to(Lx.get_center() + np.array([0, 0.13, 0]))
        tetilla_2 = tetilla_1.copy().move_to(Ly.get_center() + np.array([-0.1, 0.3, 0]))
        tetilla_1.scale(0.4)
        tetilla_2.scale(0.4)
        
        cos = TexMobject("cos(\\theta)").set_color(BLUE)
        cos.scale(0.28)
        cos.move_to(Lx.get_center() + np.array([0.15, 0.7, 0]))
        
        sen = TexMobject("sen(\\theta)").set_color(GREEN)
        sen.scale(0.28)
        sen.move_to(Ly.get_center() + np.array([1.8, 0, 0]))
         
        self.play(
            Write(tetilla_1), Write(tetilla_2),
            Write(Lx), Write(cos), Write(px)
        )
        self.play(
            Write(Ly), Write(sen), Write(py)
        )
        
        self.play(FadeOut(Lx), FadeOut(Ly))
        self.wait()

        ec = TexMobject("\\hat{r}"," = ", "\\hat{i}","cos(\\theta)",
        "+", "\\hat{j}","sen(\\theta)").scale(0.4)
        
        ec.move_to(np.array([4.7, 2.5, 0]))
        ec[0].set_color(YELLOW)
        ec[1].set_color(WHITE)
        ec[2].set_color(YELLOW)
        ec[3].set_color(BLUE)
        ec[4].set_color(WHITE)
        ec[5].set_color(YELLOW)
        ec[6].set_color(GREEN)
        
        self.play(
            ReplacementTransform(r_tn.copy(), ec[0])
        )
        self.wait()
        self.play(
            Write(ec[1]),
            ReplacementTransform(i_t.copy(), ec[2])
        )
        self.wait()
        self.play(
            ReplacementTransform(cos.copy(), ec[3])
        )
        self.wait()
        self.play(
            Write(ec[4]),
            ReplacementTransform(j_t.copy(), ec[5])
        )
        self.play(
            ReplacementTransform(sen.copy(), ec[6])
        )
        self.wait(2)
        
        # Vamos a restaurar la cámara y borrar todo
        
        self.play(
            FadeOut(px), FadeOut(py),
            FadeOut(cos), FadeOut(sen),
            FadeOut(Base),
            Restore(self.camera_frame) 
        )
        
        # -------------------------------------------------------------
        # Slide 12
        
        _I = Arrow(
            0.98*v_cords[i] + np.array([0.25, 0, 0]), 
            0.98*v_cords[i] - np.array([1.85, 0, 0]),
            tip_length = 0.2
        ).set_color(YELLOW)
        
        _i_t = TexMobject("-\\hat{i}").move_to(
            _I.get_end() - np.array([ 0.2, -0.2, 0.0])
        )
        
        _i_t.scale(0.4)
        
        R = np.array([2.43, 2.15, 0])
        Base2 = VGroup(_I, J, _i_t, j_t).move_to(R)
        
        # Vamos a cambiar de base
        
        self.camera_frame.save_state()
        
        self.play(
            self.camera_frame.scale,.4,
            self.camera_frame.move_to, t_arrows[len(v_arrows)-1],
            FadeOut(tetilla_1),
            FadeOut(r_arrows[len(v_arrows)-1]),
            FadeOut(t_arrows[len(v_arrows)-1]),
            FadeOut(v_arrows[len(v_arrows)-1]),
            Write(Base2)
        )
        
        # ---------------------------------------------------
        
        self.play(
            Write(r_arrows[len(v_arrows)-1].set_color(GRAY)),
            Write(t_arrows[len(v_arrows)-1].set_color(GRAY)),
            Write(v_arrows[len(v_arrows)-1])
        )
    
        
        # -----------------------------------------------------------
        
        ult_2 = len(v_arrows)-1
        
        py_2 = DashedLine(
        t_cords[ult_2] + np.array([0.08, -1.71, 0]),
        t_cords[ult_2] + np.array([0.08, -0.23, 0])
        ).set_color(BLUE)
        
        ## Animar desde punta a eje
        px_2 = DashedLine(
        t_cords[ult_2] + np.array([0.08, -0.23, 0]) + np.array([0.5, 0,0]),
        t_cords[ult_2] + np.array([0.08, -0.23, 0])
        ).set_color(GREEN)
        
        Lx_2 = Line(
        t_cords[ult_2] + np.array([0.08, -0.23 -1.5, 0]),
        t_cords[ult_2] + np.array([0.08, -0.23, 0]) + np.array([0.6, -1.5,0])
        ).set_color(BLUE)
        
        Ly_2 = Line(
        t_cords[ult_2] + np.array([0.08 + 0.59, -1.72, 0]),
        t_cords[ult_2] + np.array([0.08 + 0.59, -0.23, 0])
        ).set_color(GREEN)
        
        # ----------------------------------------------------------
        # Vamos a poner las tetas JAJAJAJAJA
        
        
        cos_2 = TexMobject("cos(\\theta)").set_color(BLUE)
        cos_2.scale(0.4)
        cos_2.move_to(Lx_2.get_center() + np.array([0, 0.1, 0]))
        
        sen_2 = TexMobject("sen(\\theta)").set_color(GREEN)
        sen_2.scale(0.4)
        sen_2.move_to(Ly_2.get_center() + np.array([0.3,0, 0]))
         

        self.play(
            Write(Lx_2), Write(cos_2), Write(px_2)
        )
        self.play(
            Write(Ly_2), Write(sen_2), Write(py_2)
        )
        
        self.play(FadeOut(Lx_2), FadeOut(Ly_2))

        self.wait(2)
        
        
        # --------------------------------------------------
        
        ec_2 = TexMobject("\\hat{\\theta}"," = ", "-\\hat{i}","cos(\\theta)",
        "+", "\\hat{j}","sen(\\theta)").scale(0.4)
        
        ec_2.move_to(np.array([1.5, 2.5, 0]))
        ec_2[0].set_color(YELLOW)
        ec_2[1].set_color(WHITE)
        ec_2[2].set_color(YELLOW)
        ec_2[3].set_color(BLUE)
        ec_2[4].set_color(WHITE)
        ec_2[5].set_color(YELLOW)
        ec_2[6].set_color(GREEN)
        
        self.play(
            ReplacementTransform(t_tn.copy(), ec_2[0])
        )
        self.wait()
        self.play(
            Write(ec_2[1]),
            ReplacementTransform(_i_t.copy(), ec_2[2])
        )
        self.wait()
        self.play(
            ReplacementTransform(cos_2.copy(), ec_2[3])
        )
        self.wait()
        self.play(
            Write(ec_2[4]),
            ReplacementTransform(j_t.copy(), ec_2[5])
        )
        self.play(
            ReplacementTransform(sen_2.copy(), ec_2[6])
        )
        self.wait(2)
        
        # Vamos a restaurar la cámara y borrar todo
        
        self.play(
            FadeOut(px_2), FadeOut(py_2),
            FadeOut(tetilla_2),
            FadeOut(cos_2), FadeOut(sen_2),
            FadeOut(Base2)
        )
        self.wait()
        
        # Ecuaciones
        
        r_ec0 = TexMobject("\\vec{r} = r\\hat{r}").move_to(np.array([0.8, 2.25, 0]))
        
        r_ec1 = TexMobject("= r(\\hat{i}cos(\\theta) + \\hat{j}sen(\\theta) )").move_to(np.array([1.7, 2.0, 0]))
        
        r_ec2 = TexMobject("= \\hat{i}rcos(\\theta) + \\hat{j}rsen(\\theta)").move_to(np.array([1.7, 1.75, 0]))
        
        r_ec3 = TexMobject("\\vec{r}", "= (rcos(\\theta), rsen(\\theta))").move_to(np.array([1.7, 1.5, 0]))
        
        """
        self.camera_frame.save_state()
        
        self.play(
            self.camera_frame.scale, .35,
            self.camera_frame.move_to, Base
        )
        """
        
        self.play(
            Write(r_ec0.scale(0.4))
        )
        self.wait(2)
        self.play(
            #FadeOut(r_ec0),
            #ReplacementTransform(r_ec0.copy(), r_ec1)
            Write(r_ec1.scale(0.4))
            )
        self.wait(2)
        self.play(            
            #FadeOut(r_ec1),
            #ReplacementTransform(r_ec1.copy(), r_ec2),
            Write(r_ec2.scale(0.4))
        )
        self.wait(2)
        self.play(
            #FadeOut(r_ec2),
            #ReplacementTransform(r_ec2.copy(), r_ec3)
            Write(r_ec3[1].scale(0.4))
        )
        self.wait(2)
        self.play(
            Restore(self.camera_frame) 
        )
        
        # Slide 13
        r_ec4 = TexMobject("\\vec{r} = (rcos(\\theta), rsen(\\theta))")
        r_ec4.scale(0.9)
        r_ec4.move_to(np.array([-4.5, -3.7,0]))
        
        r_tnn = r_tex[len(v_arrows)-1].copy()
        r_tnn.scale(3)
        
        t_tnn = t_tex[len(v_arrows)-1].copy()
        t_tnn.scale(3)
        
        v_tnn = v_tex[len(v_arrows)-1].copy()
        v_tnn.scale(3)
        
        ec1_n = ec.copy()
        ec1_n.move_to(np.array([4.5, -3.5, 0]))
        ec1_n.scale(2)
        
        ec2_n = ec_2.copy()
        ec2_n.move_to(np.array([4.5, -3.0, 0]))
        ec2_n.scale(2)
        
        self.play(
            FadeOut(r_ec0),
            FadeOut(r_ec1),
            FadeOut(r_ec2),
            ReplacementTransform(t_tn, t_tnn),
            ReplacementTransform(v_tn, v_tnn),
            ReplacementTransform(r_tn, r_tnn),
            ReplacementTransform(ec, ec1_n),
            ReplacementTransform(ec_2, ec2_n),
            ReplacementTransform(r_ec3, r_ec4)
        )
        self.wait()
        
        I = Arrow(
            np.array([2.73, 2, 0]),
            np.array([2.73 + 2.16, 2, 0]),
            tip_length = 0.2).set_color(YELLOW)
        
        _I = Arrow(
            np.array([2.73+0.5, 2, 0]),
            np.array([2.73+0.5-2.16, 2, 0]),
            tip_length = 0.2).set_color(YELLOW)
        
        J = Arrow(
            np.array([3, 1.75, 0]),
            np.array([3.0, 1.77 + 2.16, 0]),
            tip_length = 0.2).set_color(YELLOW)
        
        _J = Arrow(
            np.array([3, 1.75+0.5, 0]),
            np.array([3.0, 1.77+0.5 - 2.16, 0]),
            tip_length = 0.2).set_color(YELLOW)
        
        i_t = TexMobject("\\hat{i}").move_to(
            I.get_end() + np.array([ 0.3,  0.0, 0.0])
            )
        i_t.scale(0.7)
        
        j_t = TexMobject("\\hat{j}").move_to(
            J.get_end() + np.array([ 0.3, 0.0, 0.0])
            )
        j_t.scale(0.7)

        R = np.array([3.0, 1.18, 0])
        Base3 = VGroup(I,_I, J, _J).move_to(R)
        
        self.play(
            FadeOut(r_arrows[len(v_arrows)-1]),
            FadeOut(t_arrows[len(v_arrows)-1]),
            FadeOut(v_arrows[len(v_arrows)-1])
        )
        #############################
        # Vamos a mover la colita
        def escribir_ec1(x, y):
            x = round(x, 2)
            y = round(y, 2)
            ec = TexMobject(
                "\\hat{r}",
                "= ",
                "\\hat{i}",
                "cos(",
                str(x)+"^{\\circ}",
                ")", 
                " + ",
                "\\hat{j}", 
                "sen(",
                str(y)+"^{\\circ}",
                ")"
            )
            ec[0].set_color(YELLOW)
            ec[2].set_color(YELLOW)
            ec[3].set_color(BLUE)
            ec[4].set_color(BLUE)
            ec[5].set_color(BLUE)
            ec[7].set_color(YELLOW)
            ec[8].set_color(GREEN)
            ec[9].set_color(GREEN)
            ec[10].set_color(GREEN)
            ec.move_to(np.array([4.5, -3.5, 0]))
            return ec.scale(0.8)
                
        def escribir_ec2(x, y):
            x = round(x, 2)
            y = round(y, 2)
            ec = TexMobject(
                "\\hat{\\theta}",
                "= ",
                "-\\hat{i}",
                "cos(",
                str(x)+"^{\\circ}",
                ")", 
                " + ",
                "\\hat{j}", 
                "sen(",
                str(y)+"^{\\circ}",
                ")"
                )
            ec[0].set_color(YELLOW)
            ec[2].set_color(YELLOW)
            ec[3].set_color(BLUE)
            ec[4].set_color(BLUE)
            ec[5].set_color(BLUE)
            ec[7].set_color(YELLOW)
            ec[8].set_color(GREEN)
            ec[9].set_color(GREEN)
            ec[10].set_color(GREEN)
            ec.move_to(np.array([4.5, -3.0, 0]))
            return ec.scale(0.8)
        
        def escribir_ec3(x, y):
            x = round(x, 2)
            y = round(y, 2)
            ec = TexMobject(
               "\\vec{r} = (rcos(",
               str(x)+"^{\\circ}",
               "), "
               "rsen(",
               str(y)+"^{\\circ}",
               "))").move_to(np.array([-4, -3.7,0]))
            return ec.scale(0.8)
        
        v_cords3 = []
        v_cords32 = []
        t_cords3 = []
        t_cords32 = []
        cruz_cords = []
        ecuas1 = []
        ecuas2 = []
        ecuas3 = []

        for i in range(21, 386, 5):
            cruz_cords.append(3.51*np.array([np.cos(PI*(i)/180), np.sin(PI*(i)/180), 0]))
            v_cords3.append(np.sqrt(13)*np.array([np.cos(PI*i/180), np.sin(PI*i/180), 0]))
            v_cords32.append(np.sqrt(12.5)*np.array([np.cos(PI*(i-4)/180), np.sin(PI*(i-4)/180), 0]))
            t_cords3.append(np.sqrt(15.7)*np.array([np.cos(PI*(i+28)/180), np.sin(PI*(i+28)/180), 0]) )
            t_cords32.append(np.sqrt(15.5)*np.array([np.cos(PI*(i+28)/180), np.sin(PI*(i+28)/180), 0]) )
            ecuas1.append(escribir_ec1(i%360, i%360) )
            ecuas2.append(escribir_ec2(i%360, i%360) )
            ecuas3.append(escribir_ec3(i%360, i%360) )

        cruz = [Base3.copy() for i in range(0, len(v_cords3))]
        v_arrows3 = []
        r_arrows3 = []
        t_arrows3 = []

        cruz_mover = []
        v_tex3 = []
        r_tex3 = []
        t_tex3 = []
        i_tex3 = []
        j_tex3 = []
                
        for i in range(0, len(v_cords3)):
            v_arrows3.append(Vector(0.98*v_cords3[i], tip_length = 0.2).set_color(RED))
            r_arrows3.append(Arrow(0.9*v_cords3[i], 1.5*v_cords3[i], tip_length = 0.2) )
            t_arrows3.append(Arrow(v_cords32[i], t_cords3[i], tip_length = 0.2) )            
            cruz_mover.append(cruz[i].move_to(cruz_cords[i]))
            

        for i in range(0, len(v_arrows3)):
            v_tex3.append(TexMobject("\\vec{r}").move_to(v_arrows3[i].get_center() + np.array([-0.5, 0.2, 0]) ))
            r_tex3.append(TexMobject("\\hat{r}").move_to(1.5*v_arrows3[i].get_end()) )
            t_tex3.append(TexMobject("\\hat{\\theta}").move_to(t_cords32[i]))
            i_tex3.append(TexMobject("\\hat{i}").move_to(cruz_mover[i].get_center()+ np.array([2.1, -0.2,0]) ))
            j_tex3.append(TexMobject("\\hat{j}").move_to(cruz_mover[i].get_center()+ np.array([0.2, 2.1,0]) ))

        
        for i in range(0, len(v_arrows3)):
            if i == 0:
                    self.play(
                    Write(cruz_mover[i]),
                    Write(i_tex3[i]),
                    Write(j_tex3[i]),
                    FadeOut(v_arrows[len(v_arrows)-1]),
                    ReplacementTransform(v_arrows[len(v_arrows)-1], v_arrows3[i]),
                    ReplacementTransform(v_tnn, v_tex3[0]),
                    FadeOut(r_arrows[len(v_arrows)-1]),
                    ReplacementTransform(r_arrows[len(v_arrows)-1], r_arrows3[i].set_color(GRAY)),
                    FadeOut(t_arrows[len(v_arrows)-1]),
                    ReplacementTransform(t_arrows[len(v_arrows)-1], t_arrows3[i].set_color(GRAY)),
                    ReplacementTransform(t_tnn, t_tex3[0]),
                    ReplacementTransform(r_tnn, r_tex3[0]),
                    ReplacementTransform(ec1_n, ecuas1[i]),
                    ReplacementTransform(ec2_n, ecuas2[i]),
                    ReplacementTransform(r_ec4, ecuas3[i]),
                    FadeOut(teta)
                    )
            else:
                self.play(
                    ReplacementTransform(cruz_mover[i-1], cruz_mover[i]),
                    ReplacementTransform(i_tex3[i-1], i_tex3[i]),
                    ReplacementTransform(j_tex3[i-1], j_tex3[i]),
                    ReplacementTransform(r_arrows3[i-1], r_arrows3[i].set_color(GRAY)),
                    ReplacementTransform(t_arrows3[i-1], t_arrows3[i].set_color(GRAY)),
                    ReplacementTransform(v_arrows3[i-1], v_arrows3[i].set_color(RED)),
                    ReplacementTransform(v_tex3[i-1], v_tex3[i]),
                    ReplacementTransform(r_tex3[i-1], r_tex3[i]),
                    ReplacementTransform(t_tex3[i-1], t_tex3[i]),
                    ReplacementTransform(ecuas1[i-1], ecuas1[i]),
                    ReplacementTransform(ecuas2[i-1], ecuas2[i]),
                    ReplacementTransform(ecuas3[i-1], ecuas3[i]),
                run_time=0.05
                )   

        self.wait(2)
        
class Tres(GraphScene, MovingCameraScene):
    def construct(self):
        def escribir(x):
            if(x == 90):
                ec = TexMobject("\\pi/2").scale(0.6)
                ec.move_to(3.7*np.array([0.08, 1.04, 0]) )
                return ec
            if(x==45 or x==60 or x==75 or x==105 or x==120 or x==135):
                ec = TexMobject(str(x)+"^{\\circ}").scale(0.6)
                ec.move_to(6.7*np.array([np.cos(PI*(i)/180),0.57,0]) )
                return ec
            if(x==225 or x==240 or x==255 or x==270 or x==285 or x==300 or x==300 or x==315):
                ec = TexMobject(str(x)+"^{\\circ}").scale(0.6)
                ec.move_to(6.7*np.array([np.cos(PI*(i)/180),-0.57,0]) )
                return ec
            else:
                ec = TexMobject(str(x)+"^{\\circ}").scale(0.6)
                ec.move_to(6.7*np.array([np.cos(PI*(i)/180), np.sin(PI*(i)/180), 0]) )
                return ec
        
        MovingCameraScene.setup(self)
        screen_grid = ScreenGrid()
        self.add(screen_grid)
        
        Circs = []
        Lines = []
        text = []
        
        for i in range(0, 16):
            Circs.append(
                Circle(color=WHITE,radius=i/2,
                        width=0.5, stroke_width=0.5)
            )
        for c in Circs:
            self.play(ShowCreation(c), run_time=0.05)
        
        for i in range(0, 360, 15):
            text.append(escribir(i))
            Lines.append(
            Line(np.array([0,0,0]), 
            8*np.array([np.cos(PI*(i)/180), np.sin(PI*(i)/180), 0]),
             width=0.5, stroke_width=0.5)
            )
            
        for i in range(0, len(Lines)):
            self.play(
                ShowCreation(Lines[i]),
                ShowCreation(text[i]),
                run_time=0.1)
        
        self.wait(4)
        
        v_cords = []
        v_cords2 = []
        t_cords = []
        t_cords2 = []

        for i in range(35, 385, 5):
            v_cords.append(np.sqrt(13)*np.array([np.cos(PI*i/180), np.sin(PI*i/180), 0]))
            v_cords2.append(np.sqrt(12.5)*np.array([np.cos(PI*(i-4)/180), np.sin(PI*(i-4)/180), 0]))
            t_cords.append(np.sqrt(15.7)*np.array([np.cos(PI*(i+28)/180), np.sin(PI*(i+28)/180), 0]) )
            t_cords2.append(np.sqrt(15.5)*np.array([np.cos(PI*(i+28)/180), np.sin(PI*(i+28)/180), 0]) )

        
        v_arrows = []
        r_arrows = []
        t_arrows = []
        v_tex = []
        r_tex = []
        t_tex = []
                
        self.wait(8)
        
        for i in range(0, len(v_cords)):
            v_arrows.append(Vector(0.98*v_cords[i], tip_length = 0.2).set_color(RED))
            r_arrows.append(Arrow(0.9*v_cords[i], 1.5*v_cords[i], tip_length = 0.2) )
            t_arrows.append(Arrow(v_cords2[i], t_cords[i], tip_length = 0.2) )
        
        for i in range(0, len(v_arrows)):
            v_tex.append(TexMobject("\\vec{r}").move_to(v_arrows[i].get_center() + np.array([-0.5, 0.2, 0]) ))
            r_tex.append(TexMobject("\\hat{r}").move_to(1.5*v_arrows[i].get_end()) )
            t_tex.append(TexMobject("\\hat{\\theta}").move_to(t_cords2[i]))
        
        for i in range(0, len(v_arrows)):
            if i == 0:
                    self.play(
                    Write(v_arrows[0]),
                    Write(v_tex[0]),
                    Write(r_arrows[i]),
                    Write(t_arrows[0]),
                    Write(t_tex[0]),
                    Write(r_tex[0])
                    )
            else:
                self.play(
                    ReplacementTransform(r_arrows[i-1], r_arrows[i]),
                    ReplacementTransform(t_arrows[i-1], t_arrows[i]),
                    ReplacementTransform(v_arrows[i-1], v_arrows[i]),
                    ReplacementTransform(v_tex[i-1], v_tex[i]),
                    ReplacementTransform(r_tex[i-1], r_tex[i]),
                    ReplacementTransform(t_tex[i-1], t_tex[i]),
                        run_time=0.05
                )   

        self.wait(2)
        # Poner bien los labels, que se vean todos los text
        # poner la animación de girar con los vector, v, r, t
                    
        
        
