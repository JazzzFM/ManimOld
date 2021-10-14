from big_ol_pile_of_manim_imports import *

class NTRU_PolyConv(Scene):
    def construct(self):
        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/dark.jpg")
        logo =  ImageMobject("/home/jazzzfm/ManimOld/Fondos/CIBERSEG.png")
        logo.scale(0.5)
        logo.move_to(np.array([-6.5, 3.4, 0]))
        image.scale(4)
        self.add(image)
        
        h_line = Line(LEFT, RIGHT).scale(FRAME_X_RADIUS)
        pos = np.array([1, 3.3, 0])
        CIC = TextMobject("Centro de Investigación en Computación - IPN MX")
        CIC.move_to(pos)
        
        self.play(FadeIn(logo), Write(CIC))
        
        self.wait(1)            
        title = TextMobject("NTRU Cryptosystem: Mathematical Construction")
        title.move_to(pos)
        h_line.next_to(title, DOWN)
        self.play(ReplacementTransform(CIC, title), Write(h_line))
        
        t1 = TextMobject("1. The basics: What is a Ring and an Ideal over this?").set_color(RED)
        t2 = TextMobject("2. Notation and Parameters").set_color(PURPLE)
        t4 = TextMobject("4. Key Creation").set_color(BLUE)
        t5 = TextMobject("5. Encryption").set_color(BLUE)
        t3 = TextMobject("3. Parameter Selection").set_color(PURPLE)
        t6 = TextMobject("6. Decryption").set_color(BLUE)
        t7 = TextMobject("7. Syntesis").set_color(BLUE)
        t8 = TextMobject("8. Current NTRUEncrypt").set_color(YELLOW)
        t9 = TextMobject("9. NTRUEncrypt as a Lattice Cryptosystem").set_color(ORANGE)
        t10 = TextMobject("10. Lattice attack on a NTRU message").set_color(ORANGE)
        
        t1.move_to(pos + np.array([-2.0, -1.0, 0.0]))
        t2.move_to(pos + np.array([-4.8, -1.5, 0.0]))
        t3.move_to(pos + np.array([-5.4, -2.0, 0.0]))
        t4.move_to(pos + np.array([-6.2, -2.5, 0.0]))
        t5.move_to(pos + np.array([-6.4, -3.0, 0.0]))
        t6.move_to(pos + np.array([-6.4, -3.5, 0.0]))
        t7.move_to(pos + np.array([-6.7, -4.0, 0.0]))
        t8.move_to(pos + np.array([-5.0, -4.5, 0.0]))
        t9.move_to(pos + np.array([-3.0, -5.0, 0.0]))
        t10.move_to(pos + np.array([-3.8, -5.5, 0.0]))
        
        self.play(Write(t1), Write(t2), Write(t3), Write(t4), Write(t5), Write(t6),
                  Write(t7), Write(t8), Write(t9), Write(t10))

        self.wait(3)
        self.play(FadeOut(title), FadeOut(t1), FadeOut(t2), FadeOut(t3), FadeOut(t4), FadeOut(t5), FadeOut(t6), FadeOut(t7),
                  FadeOut(t8), FadeOut(t9), FadeOut(t10))
        self.wait(1)
        
        ##########################################################
        
        t1.move_to(pos)
        self.play(FadeIn(t1))
        self.wait(3)
        
        defR = TextMobject("\\justifying \\textbf{Definition:} A conmutative ring is a set R with two binary operations, addition and multiplication such that:")
        defR.scale(0.7) 
        defR.next_to(t1, 4*DOWN, buff=0.1)
        defR.move_to(LEFT + 2*UP)
        
        self.play(Write(defR))
        axiomsr1 = TextMobject("\\justifying 1) a + b = b + a $\\forall{a,b}\\in$R",
                              "\\justifying 2) a + (b + c) = (a + b) $\\forall{a,b,c}\\in$R")
        
        axiomsr2 = TextMobject("\\justifying 3)$\\exists$0$\\in$R with 0 + a = a $\\forall{a}\\in$R",
                               "\\justifying 4)$\\forall{a}\\in$R $\\exists$a'$\\in$R with a + a' = 0")
        axiomsr3 = TextMobject("\\justifying 5) a*b = b*a $\\forall{a,b}\\in$R",
                               "\\justifying 6) a*(b*c) = (a*b)*c $\\forall{a,b,c}\\in$R")
        axiomsr4 = TextMobject("\\justifying 7)$\\exists$1$\\in$R with a*1 = a $\\forall{a}\\in$R",
                               "\\justifying 8) a*(b+c) = (a*b)+(a*c) $\\forall{a,b,c}\\in$R")
        axiomsr1.scale(0.7)
        axiomsr2.scale(0.7)
        axiomsr3.scale(0.7)
        axiomsr4.scale(0.7)

        
        axiomsr1[0].next_to(defR, DOWN)     
        axiomsr1[1].next_to(axiomsr1[0], DOWN)
        
        axiomsr2[0].next_to(axiomsr1[1], DOWN)
        axiomsr2[1].next_to(axiomsr2[0], DOWN)
        
        axiomsr3[0].next_to(axiomsr2[1], DOWN)
        axiomsr3[1].next_to(axiomsr3[0], DOWN)
        
        axiomsr4[0].next_to(axiomsr3[1], DOWN)
        axiomsr4[1].next_to(axiomsr4[0], DOWN)

        
        self.play(Write(axiomsr1), Write(axiomsr2), Write(axiomsr3), Write(axiomsr4))
        self.wait(5)
        self.play(FadeOut(defR))
        self.play(FadeOut(axiomsr1), FadeOut(axiomsr2), FadeOut(axiomsr3), FadeOut(axiomsr4))
        
        ################################################################
        
        Examp1 = TextMobject("\\justifying Example 1: $(\\mathbb{Z}, +, *)$ is a ring, where:")
        set1 = TexMobject("\\mathbb{Z} = \\{ 0, 1, -1, 2, -2, 3, -3, ...\\}")
        Examp1.scale(0.7) 
        set1.scale(0.7)
        Examp1.next_to(t1, 4*DOWN, buff=0.1)
        Examp1.move_to(LEFT + 2*UP) 
        set1.move_to(LEFT + 1.5*UP) 
    
        self.play(Write(Examp1), Write(set1))
        
        Examp2 = TextMobject("\\justifying Example 2: $(\\mathbb{Z}[X], +, *)$ is a ring, where:")
        set2 = TexMobject("\\mathbb{Z}[X] = \\{f = \\sum_{i=0}^n a_{i}X^{N} |\\quad a_{i} \\in \\mathbb{Z}\\wedge N\\in\mathbb{N} \\}")
        Ops = TexMobject("(f + g)(X) = f(X) + g(X) \\quad (f * g)(X) = \\sum_{s + t = u} f(s)g(t)")
        Examp2.scale(0.7) 
        set2.scale(0.7)
        Ops.scale(0.7)
        
        Examp2.next_to(Examp1, 4*DOWN, buff=0.1)
        Examp2.move_to(LEFT ) 
        set2.move_to(LEFT + DOWN) 
        Ops.move_to(LEFT + 2.0*DOWN) 

    
        self.play(Write(Examp2), Write(set2), Write(Ops))
        self.wait(3)
        self.play(FadeOut(Examp1), FadeOut(set1), FadeOut(Examp2), FadeOut(set2), FadeOut(Ops))
        self.play()
        
        #####################################
        
        defI = TextMobject("\\justifying \\textbf{Definition:} Let be R a conmmutative ring. An Ideal I is a subset of R such that:")
        defI.scale(0.7) 
        defI.next_to(t1, 4*DOWN, buff=0.1)
        defI.move_to(LEFT + 2*UP)
        
        self.play(Write(defI))
        axiomsi1 = TextMobject("i) $0\\in$I",
                              "ii) if  ${a,b}\\in$I then a + b$\\in$I")
        
        axiomsi2 = TextMobject("iii) if ${a}\\in$R and ${b}\\in$I then a*b$\\in$I")
        
        axiomsi1.scale(0.7)
        axiomsi2.scale(0.7)
        
        axiomsi1[0].next_to(defI, DOWN)     
        axiomsi1[1].next_to(axiomsi1[0], DOWN)
        axiomsi2.next_to(axiomsi1[1], DOWN)
        self.play(Write(axiomsi1), Write(axiomsi2))
        
        defI2 = TextMobject("\\justifying \\textbf{Definition:} If a$\\in$I where the I is an Ideal, then we define the \\textbf{principal ideal generated by} a as the set:")
        defI2.scale(0.7) 
        defI2.move_to(LEFT + 1.3*DOWN)
        self.play(Write(defI2))
        axiomsig = TexMobject("aI = < a > = \\{ a*b | \\quad b\\in R\\}")
        axiomsig.scale(0.7)
        
        axiomsig.next_to(defI2, DOWN)
        obs = TextMobject("Actually $<a>$ is again an ideal over R").scale(0.7) 
        obs.next_to(axiomsig, DOWN)

        self.play(Write(axiomsig), Write(obs))
        self.wait(4)
        self.play(FadeOut(defI), FadeOut(axiomsi1), FadeOut(axiomsi2), FadeOut(defI2), FadeOut(axiomsig), FadeOut(obs))
        ##########################################################################
        
        Examp5 = TextMobject("\\justifying Example 3: consider the ring $\\mathbb{Z}[X]$ and I as the Ideal:")
        set5 = TexMobject("< X^{N} - 1 > = \\{ (X^{N} - 1)*f | \\quad f\\in\\mathbb{Z}[X]\\}")
        Examp5.scale(0.7) 
        set5.scale(0.7)
        Examp5.next_to(t1, 4*DOWN, buff=0.1)
        Examp5.move_to(LEFT + 2*UP) 
        set5.move_to(LEFT + 1.5*UP)     
        self.play(Write(Examp5), Write(set5))

        axiome = TextMobject("i) $0\\in < X^{N} - 1>$, because 0 = $(X^{N} - 1)*0(X)$")
        
        axiome1 = TextMobject("ii) if  ${a,b}\\in <X^{N} - 1 >$ then $\\exists f,g\\in\\mathbb{Z}[X]$ such that a = $(X^{N} - 1)*f$")
        axiome2 = TextMobject("and b = $(X^{N} - 1)*g$, hence a+b = $(X^{N} - 1)*(f+g)\\in<X^{N} - 1>$")
        axiome3 =  TextMobject("iii) if a$\\in\\mathbb{Z}[X]$ and $b\\in<X^{N} - 1>$ then $a*b\\in<X^{N} - 1>$")
        
        axiome.scale(0.7)
        axiome1.scale(0.7)
        axiome2.scale(0.7)
        axiome3.scale(0.7)
        
        axiome.next_to(set5, DOWN)
        axiome1.next_to(axiome, DOWN)
        axiome2.next_to(axiome1, DOWN)
        axiome3.next_to(axiome2, DOWN)

        self.play(Write(axiome))
        self.play(Write(axiome1)) 
        self.play(Write(axiome2))
        self.play(Write(axiome3))
        self.wait(5)
        self.play(FadeOut(Examp5), FadeOut(set5), FadeOut(axiome), FadeOut(axiome1), FadeOut(axiome2), FadeOut(axiome3))

        
       
