from manimlib.imports import *

class Prelude(Scene):
    def construct(self):
        # Introducción
        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/dark.jpg")
        logo =  ImageMobject("/home/jazzzfm/ManimOld/Fondos/ESCUDO_ESFM.png")
        logo.scale(0.5)
        logo.move_to(np.array([-6.5, 3.4, 0]))
        image.scale(4)
        self.add(image)
        
        h_line = Line(LEFT, RIGHT).scale(FRAME_X_RADIUS)
        pos = np.array([1, 3.3, 0])
        ESFM = TextMobject("Escuela Superior de Física y Matemáticas - IPN")
        ESFM.move_to(pos)

        self.play(FadeIn(logo), Write(ESFM))
        self.wait(3)  
                  
        title = TextMobject("Hoy les presentamos: El Dragon Heighway")
        title.move_to(pos)
        h_line.next_to(title, DOWN)
        self.play(ReplacementTransform(ESFM, title), Write(h_line))
        
        t1 = TextMobject("Asignatura: Topología II.")
        t2 = TextMobject("Profesora: Flor de Maria Correa Romero.")
        t3 = TextMobject("Alumno: Jaziel David Flores Rodríguez.")

        
        t1.move_to(pos + np.array([-2.2, -2.5, 0.0]))
        t2.move_to(pos + np.array([-2.3, -3.5, 0.0]))
        t3.move_to(pos + np.array([-2.4, -4.5, 0.0]))
        
        self.play(Write(t1),
                  Write(t2),
                  Write(t3))
        self.wait(3)
        
        self.play(FadeOut(title),
                  FadeOut(t1),
                  FadeOut(t2),
                  FadeOut(t3))
        
        self.wait(1)
        
        # Siguiente Slide      
        t_slide2 = TextMobject("Construcción Matemática")
        t_slide2.move_to(pos + np.array([-1.5, 0, 0]))
        self.play(FadeIn(t_slide2))
        self.wait()
            
        text_1 = TextMobject("Comenzamos definendo su sistema de funciones iteradas:")
        text_1.scale(0.7) 
        text_1.next_to(t1, 6*DOWN, buff=0.1)
        text_1.move_to(LEFT + 2*UP)
        self.play(Write(text_1))
        
        f1_t = TexMobject("f_{1}(x, y) = \\frac{1}{\\sqrt{2}} \\begin{bmatrix} cos(45^{\\circ}) & -sen(45^{\\circ}) \\\ sen(45^{\\circ}) & cos(45^{\\circ}) \\end{bmatrix} \\begin{bmatrix} x \\\ y \\end{bmatrix}")
        f1_t.scale(0.7)
        f1_t.next_to(text_1, 6*DOWN, buff=0.1)    
        self.play(Write(f1_t))
        self.wait()

        f2_t = TexMobject("f_{2}(x, y) = \\frac{1}{\\sqrt{2}} \\begin{bmatrix} cos(135^{\\circ}) & -sen(135^{\\circ}) \\\ sen(135^{\\circ}) & cos(135^{\\circ}) \\end{bmatrix} \\begin{bmatrix} x \\\ y \\end{bmatrix} +  \\begin{bmatrix} 1 \\\ 0 \\end{bmatrix}")
        f2_t.scale(0.7)
        f2_t.next_to(f1_t, 6*DOWN, buff=0.1)    
        self.play(Write(f2_t))
        self.wait(2)
        
        text_2 = TextMobject("Es decir su SFI es el siguiente:")
        text_2.scale(0.7) 
        text_2.next_to(t1, 6*DOWN, buff=0.1)
        text_2.move_to(LEFT + 2*UP)
        self.play(ReplacementTransform(text_1, text_2))
        self.wait(2)
        
        f1_tn = TexMobject("f_{1}(x, y) = \\frac{1}{\\sqrt{2}} \\begin{bmatrix} \\sqrt{2} / 2  & - \\sqrt{2}/2 \\\ \\sqrt{2} / 2 &  \\sqrt{2} / 2 \\end{bmatrix} \\begin{bmatrix} x \\\ y \\end{bmatrix}")
        f1_tn.scale(0.7)
        f1_tn.next_to(text_1, 6*DOWN, buff=0.1)    
        self.play(ReplacementTransform(f1_t, f1_tn))
        self.wait()

        f2_tn = TexMobject("f_{2}(x, y) = \\frac{1}{\\sqrt{2}} \\begin{bmatrix} - \\sqrt{2} / 2  & - \\sqrt{2} / 2  \\\ \\sqrt{2} / 2  & -\\sqrt{2} / 2  \\end{bmatrix} \\begin{bmatrix} x \\\ y \\end{bmatrix} +  \\begin{bmatrix} 1 \\\ 0 \\end{bmatrix}")
        f2_tn.scale(0.7)
        f2_tn.next_to(f1_t, 6*DOWN, buff=0.1)    
        self.play(ReplacementTransform(f2_t, f2_tn))
        self.wait(2)
        
        text_3 = TextMobject("Sea $r = 1 / \\sqrt{2}$. Finalmente tenemos")
        text_3.scale(0.7) 
        text_3.next_to(t1, 6*DOWN, buff=0.1)
        text_3.move_to(LEFT + 2*UP)
        self.play(ReplacementTransform(text_2, text_3))
        self.wait(2)
        
        f1_tnn = TexMobject("f_{1}(x, y) =  \\begin{bmatrix} 1/2 & -1/2 \\\ 1/2 & \\ 1/2 \\end{bmatrix} \\begin{bmatrix} x \\\ y \\end{bmatrix}")
        f1_tnn.scale(0.7)
        f1_tnn.next_to(text_3, 6*DOWN, buff=0.1)    
        self.play(ReplacementTransform(f1_tn, f1_tnn))
        self.wait()
        
        f2_tnn = TexMobject("f_{2}(x, y) =  \\begin{bmatrix} -1/2  & -1/2  \\\ 1/2 & -1/2  \\end{bmatrix} \\begin{bmatrix} x \\\ y \\end{bmatrix} +  \\begin{bmatrix} 1 \\\ 0 \\end{bmatrix}")
        f2_tnn.scale(0.7)
        f2_tnn.next_to(f1_t, 6*DOWN, buff=0.1)    
        self.play(ReplacementTransform(f2_tn, f2_tnn))
        self.wait(2)
        
        L1 = Line(np.array([0.5, 1.25, 0]), np.array([0.5, 0.25, 0]), stroke_width = 3, color = BLUE)
        b1 = Brace(L1, direction = L1.copy().rotate(PI/2).get_unit_vector()).set_color(WHITE)
        
        L2 = Line(np.array([-0.5, -0.25, 0]), np.array([-0.5, -1.25, 0]), stroke_width = 3, color = BLUE)
        b2 = Brace(L2, direction = L2.copy().rotate(PI/2).get_unit_vector()).set_color(WHITE)
                
        text_4 = TextMobject("Escalar por $r$ y rotar $45^{\\circ}$")
        text_4.scale(0.7)
        text_4.move_to(np.array([3.5, 0.75, 0]))
        
        text_5 = TextMobject("Escalar por $r$, rotar $135^{\\circ}$ y transladar")
        text_5.scale(0.7)
        text_5.move_to(np.array([3.5, -0.75, 0]))
                
        self.play(FadeOut(f1_tnn), FadeOut(f2_tnn))
        self.wait()

        f1_tnn2 = f1_tnn.move_to(f1_tnn.get_center() + np.array([-2.5, 0, 0]))
        f2_tnn2 = f2_tnn.move_to(f2_tnn.get_center() + np.array([-3.0, 0, 0]))
        

         
        self.play(
            ReplacementTransform(f1_tnn.copy(), f1_tnn2),
            ReplacementTransform(f2_tnn.copy(), f2_tnn2),
            Write(b1),
            Write(b2),
            Write(text_4),
            Write(text_5)
        )
  
        self.wait(4)
        
        
        # Vamos a borrar todo alv
        self.play(   
            FadeOut(b1),
            FadeOut(b2),      
            FadeOut(text_4),
            FadeOut(text_5),
            FadeOut(f1_tnn2),
            FadeOut(f2_tnn2),
            FadeOut(text_3)
            )
        
        XD =  TextMobject("El atractor de este IFS será el Dragón Heighway. Consta de dos piezas auto-similares correspondientes a las dos funciones en el SFI.")
        XD.scale(0.7)
        XD.next_to(t1, 6*DOWN, buff=0.1)
        XD.move_to(LEFT + 2*UP)
        
        self.play(Write(XD))
        self.wait(3)

        attr = ImageMobject("/home/jazzzfm/ManimOld/Fondos/attr.png")
        attr.scale(2.5)
        attr.move_to(np.array([0, -1.2, 0]))
        self.play(FadeIn(attr))
        self.wait(4)
        self.play(FadeOut(attr), FadeOut(XD))
        
        ## Vamos a los siguientes pasos
        
        text_6 = TextMobject("Si $\\mathcal{H}$ es el conjunto de puntos en el Dragón Heighway, entonces tenemos que:")
        text_6.scale(0.7) 
        text_6.next_to(t1, 6*DOWN, buff=0.1)
        text_6.move_to(LEFT + 2*UP)
        self.play(Write(text_6))
        self.wait(2)
        

        ec_1 = TexMobject("\\mathcal{H} = f_{1}(\\mathcal{H}) \\cup f_{2}(\\mathcal{H})")
        ec_1.scale(0.7)
        ec_1.next_to(text_6, 6*DOWN, buff=0.1)    
        self.play(Write(ec_1))
        self.wait()
        
        text_7 = TextMobject("Lo que significa que $\\mathcal{H}$ es la unión de los dos conjuntos obtenidos al aplicar la transformación geométrica de cada función en el SFI al conjunto $\\mathcal{H}$.")
        text_7.scale(0.7) 
        text_7.next_to(ec_1, 6*DOWN, buff=0.1)
        self.play(Write(text_7))
        self.wait(1)
        
        text_8 = TextMobject("Además: $f_1(\\mathcal{H})$ y $f_2(\\mathcal{H})$ son solo versiones escaladas de $\\mathcal{H}$")
        text_8.scale(0.7) 
        text_8.next_to(text_7, 6*DOWN, buff=0.1)
        self.play(Write(text_8))
        self.wait(2)
        
        # Un resumen e imagen
        self.play(FadeOut(text_6),FadeOut(ec_1), FadeOut(text_7), FadeOut(text_8))
        self.wait()
        
        text_9 = TextMobject("Debido a esta auto-similitud, el Dragón Heighway puede adoquinarse usando cuatro copias de sí mismo, cada una escalada por 1/2 y rotada $90^{\\circ}$ (verde), $180^{\\circ}$ (naranja) o $270^{\\circ}$ (azul). Por similitud, cada una de las cuatro copias se puede colocar en adoquinado con copias aún más pequeñas del Dragón.")
        text_9.scale(0.65) 
        text_9.next_to(t1, 6*DOWN, buff=0.1)
        text_9.move_to(1.5*LEFT + 2*UP)
        self.play(Write(text_9))
        self.wait(2)
        
        adoq =  ImageMobject("/home/jazzzfm/ManimOld/Fondos/adoquinado.png")
        adoq.scale(2.4)
        adoq.move_to(np.array([0, -1.5, 0]))
        self.play(FadeIn(adoq))
        self.wait(4)
        
        # Se borra todo alv
        self.play(FadeOut(text_9), FadeOut(adoq))
        
        # Final
        text_10 = TextMobject("Esto funciona porque $f_{1}(\\mathcal{H}) \\cup f_{2}(\\mathcal{H})$ implica que:")
        text_10.scale(0.65) 
        text_10.next_to(t1, 8*DOWN, buff=0.1)
        text_10.move_to(1.5*LEFT + UP)
        self.play(Write(text_10))
        self.wait(2)
        
        ec_2 = TexMobject("\\mathcal{H} = f_{1}((f_{1}(\\mathcal{H}) \\cup f_{2}(\\mathcal{H})) \\cup f_{2}((f_{1}(\\mathcal{H}) \\cup f_{2}(\\mathcal{H}))")
        ec_2.scale(0.7)
        ec_2.next_to(text_10, 6*DOWN, buff=0.1)   
         
        ec_3 = TexMobject("= f_{1}((f_{1}(\\mathcal{H})) \\cup f_{1}(f_{2}(\\mathcal{H})) \\cup f_{2}((f_{1}(\\mathcal{H})) \\cup f_{2}(f_{2}(\\mathcal{H}))")
        ec_3.scale(0.7)
        ec_3.next_to(ec_2, 6*DOWN, buff=0.1)   

        self.play(Write(ec_2))
        self.wait()
        self.play(Write(ec_3))
        self.wait(3)
        
        self.play(FadeOut(text_10), FadeOut(ec_2), FadeOut(ec_3) )
    
        
        text_12 = TextMobject("Aplicar cada función dos veces se escalará en $(\\frac{1}{\\sqrt{2}})^{2} = \\frac{1}{2}$.")
        text_12.scale(0.65) 
        text_12.next_to(t1, 8*DOWN, buff=0.1)
        text_12.move_to(1.5*LEFT + UP)
        self.play(Write(text_12))
        self.wait(1)
        
        text_13 = TextMobject("Dado que $f_{1}$ rotará $45^{\\circ}$, la aplicación de $f_{1}$ dos veces rotará $90^{\\circ}$")
        text_13.scale(0.65) 
        text_13.next_to(text_12, 8*DOWN, buff=0.1)
        self.play(Write(text_13))
        self.wait(1)
        
        text_14 = TextMobject("De manera similar, la aplicación de $f_{1}$ y $f_{2}$ en cualquier orden rotará $45^{\\circ} + 135^{\\circ} = 180^{\\circ}$")
        text_14.scale(0.65) 
        text_14.move_to(text_13.get_center() + np.array([0, -1, 0]))
        self.play(Write(text_14))
        self.wait(1)
        
        text_15 = TextMobject("Finalmente, la aplicación de $f_2$ dos veces rotará $270^{\\circ}$")
        text_15.scale(0.65) 
        text_15.move_to(text_14.get_center() + np.array([0, -1, 0]))
        self.play(Write(text_15))
        self.wait(4)


  
class Allegro(MovingCameraScene):
    CONFIG = {
        "iterations":15,
        "angle":90*DEGREES,
        "border_proportion":1.25,
        "colors":[RED_A,RED_C,RED_E,BLUE_A,
                  BLUE_C,BLUE_E,YELLOW_A,YELLOW_C,
                  YELLOW_E,PURPLE_A,PURPLE_C,PURPLE_E]
    }      
        
    def construct(self):
        # Introducción
        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/dark.jpg")
        logo =  ImageMobject("/home/jazzzfm/ManimOld/Fondos/ESCUDO_ESFM.png")
        logo.scale(0.5)
        logo.move_to(np.array([-6.5, 3.4, 0]))
        image.scale(4)
        self.add(image)
        
        h_line = Line(LEFT, RIGHT).scale(FRAME_X_RADIUS)
        pos = np.array([1, 3.3, 0])
        constr = TextMobject("Construcción por segmentos de línea.")
        constr.move_to(pos)
        
        lineas =  ImageMobject("/home/jazzzfm/ManimOld/Fondos/construction.png")
        lineas.scale(0.8)
        lineas.move_to(np.array([0, 1.5, 0]))
        

        self.play(FadeIn(logo), Write(constr))
        self.wait(3)  
        
        self.play(FadeIn(lineas))
        self.wait()

        text_1 = TextMobject("Comenzamos con un segmento de línea.")            
        text_2 = TextMobject("Después reemplazamos este segmento con dos segmentos, cada uno escalado por una razón $r = 1/\\sqrt{2}$ de tal manera que el segmento original hubiera sido la hipotenusa de un triángulo rectángulo isósceles.")
        text_3 = TextMobject("Siguiendo el segmento original, colocamos los dos nuevos segmentos a la izquierda.")
        
        text_4 = TextMobject("Luego, reemplazamos cada uno de los segmentos con dos nuevos segmentos en ángulo recto, cada uno escalado por la razón r")
        text_5 = TextMobject("Los nuevos segmentos se colocan a la izquierda y luego a la derecha a lo largo de los segmentos de la primera iteración")
        text_6 = TextMobject("Se continúa con esta construcción, siempre alternando los nuevos segmentos entre la izquierda y la derecha a lo largo de los segmentos de la iteración anterior")
        
        text_1.scale(0.7) 
        text_2.scale(0.7) 
        text_3.scale(0.7) 
        
        text_4.scale(0.7) 
        text_5.scale(0.7) 
        text_6.scale(0.7) 

        text_1.next_to(constr, 6*DOWN, buff=0.1)
        text_1.move_to(LEFT + 2*UP)
        text_1.move_to(text_1.get_center()+np.array([0,-2,0]))
        text_2.next_to(text_1, 6*DOWN, buff=0.1)
        text_3.next_to(text_2, 6*DOWN, buff=0.1)

        self.play(Write(text_1))
        self.wait()
        
        self.play(Write(text_2))
        self.wait()
        
        self.play(Write(text_3))
        self.wait()
        
        self.play(FadeOut(text_1))
        self.play(FadeOut(text_2))
        self.play(FadeOut(text_3))
        
        text_4.next_to(constr, 6*DOWN, buff=0.1)
        text_4.move_to(LEFT + 2*UP)
        text_4.move_to(text_4.get_center() + np.array([0,-2,0]))
        text_5.next_to(text_4, 6*DOWN, buff=0.1)
        text_6.next_to(text_5, 6*DOWN, buff=0.1)
        
        self.play(Write(text_4))
        self.wait()
        
        self.play(Write(text_5))
        self.wait()
        
        self.play(Write(text_6))
        self.wait()
        
        self.play(FadeOut(text_4))
        self.play(FadeOut(text_5))
        self.play(FadeOut(text_6))
        self.wait()
        
        self.play(FadeOut(lineas))

        XDD = TextMobject("Manos a la obra!")
        XDD.move_to(pos)
        self.play(ReplacementTransform(constr, XDD))
        self.wait(2)

        self.play(FadeOut(logo), FadeOut(XDD))
        self.wait()
        self.play(FadeOut(image))
        self.wait()
                          
        self.color = it.cycle(self.colors)
        path = VGroup()
        first_line = Line(ORIGIN, UP / 5, color = next(self.color))
        path.add(first_line)

        self.camera_frame.set_height(first_line.get_height() * self.border_proportion)
        self.camera_frame.move_to(first_line)
        self.play(ShowCreation(first_line))
        self.add_foreground_mobject(path)

        self.target_path = self.get_all_paths(path, self.iterations)
        for i in range(self.iterations):
            self.duplicate_path(path,i)
        self.wait()
        
    def duplicate_path(self,path,i):
        set_paths = self.target_path[:2**(i + 1)]
        height = set_paths.get_height() * self.border_proportion
        new_path = path.copy()
        new_path.set_color(next(self.color))
        self.add(new_path)
        point = self.get_last_point(path)
        self.play(
            Rotating(
                new_path,
                radians=self.angle,
                about_point=path[-1].points[point],
                rate_func=linear
                ),
            self.camera_frame.move_to,set_paths,
            self.camera_frame.set_height,height,
            run_time=1, rate_func=smooth
            )
        self.add_foreground_mobject(new_path)
        post_path = reversed([*new_path])
        path.add(*post_path)

    def get_all_paths(self, path, iterations):
        target_path = path.copy()
        for _ in range(iterations):
            new_path = target_path.copy()
            point = self.get_last_point(new_path)
            new_path.rotate(
                        self.angle, 
                        about_point=target_path[-1].points[point],
                    )
            post_path = reversed([*new_path])
            target_path.add(*post_path)

        return target_path

    def get_last_point(self, path):
        return 0 if len(path) > 1 else -1