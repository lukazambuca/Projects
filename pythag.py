from big_ol_pile_of_manim_imports import *
import math
import numpy as np

class DrawPolygon(Scene):
    def construct(self):



        #########################
        #                       #
        #     INTRODUCTION      #
        #                       #
        #########################

        sentence = TexMobject("\\text{Pythagoras' Theorem}")
        sentence.move_to(3*UP)

        pythag = TexMobject("a^2 + b^2 = c^2")
        pythag.move_to(3*RIGHT + 1.3*UP)
        pythag.scale(0.85)
        pythag[0].set_color(BLUE)
        pythag[3].set_color(GREEN)
        pythag[6].set_color(RED)



        
        START_1 = (-1.5,-1.5,0)
        END_1 =   (-1.5,1.5,0)

        START_2 = (-1.5,1.5,0)
        END_2 =   (1.5,-1.5,0)

        START_3 = (1.5,-1.5,0)
        END_3 =   (-1.5025,-1.5,0)

        START_4 = (-1.2,-1.5,0)
        END_4 =   (-1.2,-1.2,0)

        START_5 = (-1.2,-1.2,0)
        END_5 =   (-1.5025,-1.2,0)




        line_1 = Line(START_1,END_1)
        line_2 = Line(START_2,END_2)
        line_3 = Line(START_3,END_3)
        line_4 = Line(START_4,END_4)
        line_5 = Line(START_5,END_5)


        x = TexMobject("a")
        x.set_color_by_tex("a", BLUE)
        x.next_to(line_1, LEFT)
        x.scale(0.75)

        y = TexMobject("b")
        y.set_color_by_tex("b", GREEN)
        y.next_to(line_3, DOWN)
        y.scale(0.75)

        z = TexMobject("c")
        z.set_color_by_tex("c", RED)
        z.move_to(0.4*RIGHT)
        z.scale(0.75)

        #brace_1=Brace(line_1,LEFT)
        #brace_2=Brace(line_2,RIGHT)

        

        #self.play(Write(brace_1))
        #self.play(Write(brace_2))
        
        self.play(Write(sentence))
        self.wait(2)

        self.play(ShowCreation(line_1))
        self.play(ShowCreation(line_2))
        self.play(ShowCreation(line_3))
        self.wait(1.5)
        self.play(ShowCreation(line_4))
        self.play(ShowCreation(line_5))


        self.play(Write(x))
        self.play(Write(y))
        self.play(Write(z))
        self.wait(1.5)

        self.play(Write(pythag), run_time = 2)

        self.play(ReplacementTransform(x.copy(), pythag[0]))
        self.play(ReplacementTransform(y.copy(), pythag[3]))
        self.play(ReplacementTransform(z.copy(), pythag[6]))
        self.wait(2)

        #Remove INTRODUCTION

        self.play(FadeOut(line_1), FadeOut(line_2),  FadeOut(line_3), FadeOut(line_4), 
        FadeOut(line_5), FadeOut(x), FadeOut(y), FadeOut(z), FadeOut(sentence),FadeOut(pythag))
        

        ######################################
        #               PROOF                #
        ######################################

        START_6 = (-2,2,0)
        END_6 =   (2,2,0)

        START_7 = (-2,2,0)
        END_7 =   (-2,-2,0)

        START_8 = (-2,-2,0)
        END_8 =   (2,-2,0)

        START_9 = (2,-2,0)
        END_9 =   (2,2.025,0)

        ### square in square

        START_10 = (1,2,0)
        END_10 =   (-2,1,0)

        START_11 = (-2,1,0)
        END_11 =   (-1,-2,0)

        START_12 = (-1,-2,0)
        END_12 =   (2,-1,0)

        START_13 = (2,-1,0)
        END_13 =   (1,2,0)

        line_6 = Line(START_6,END_6)
        line_7 = Line(START_7,END_7)
        line_8 = Line(START_8,END_8)
        line_9 = Line(START_9,END_9)
        line_10 = Line(START_10,END_10, color = YELLOW)
        line_11 = Line(START_11,END_11, color = YELLOW)
        line_12 = Line(START_12,END_12, color = YELLOW)
        line_13 = Line(START_13,END_13, color = YELLOW)



        point_1 = Dot((1,2,0),color = RED)
        point_2 = Dot((-1,2,0),color = RED)
        point_3 = Dot((1,2,0),color = RED)

        point_4 = Dot((-2,1,0),color = RED)
        point_5 = Dot((-1,-2,0),color = RED)
        point_6 = Dot((2,-1,0),color = RED)

        

        

        a_1 = TexMobject("a")
        a_1.set_color_by_tex("a", BLUE)
        a_1.move_to((0.5*LEFT + 2.3*UP))
        a_1.scale(0.75)

        a_2 = TexMobject("a")
        a_2.set_color_by_tex("a", BLUE)
        a_2.move_to((2.5*LEFT + 0.5*DOWN))
        a_2.scale(0.75)

        a_3 = TexMobject("a")
        a_3.set_color_by_tex("a", BLUE)
        a_3.move_to((0.5*RIGHT + 2.5*DOWN))
        a_3.scale(0.75)

        a_4 = TexMobject("a")
        a_4.set_color_by_tex("a", BLUE)
        a_4.move_to((2.5*RIGHT + 0.5*UP))
        a_4.scale(0.75)





        b_1 = TexMobject("b")
        b_1.set_color_by_tex("b", GREEN)
        b_1.move_to(1.5*RIGHT + 2.3*UP)
        b_1.scale(0.75)

        b_2 = TexMobject("b")
        b_2.set_color_by_tex("b", GREEN)
        b_2.move_to(2.5*LEFT + 1.5*UP)
        b_2.scale(0.75)

        b_3 = TexMobject("b")
        b_3.set_color_by_tex("b", GREEN)
        b_3.move_to(1.5*LEFT + 2.5*DOWN)
        b_3.scale(0.75)

        b_4 = TexMobject("b")
        b_4.set_color_by_tex("b", GREEN)
        b_4.move_to(2.5*RIGHT + 1.5*DOWN )
        b_4.scale(0.75)


        c_1 = TexMobject("c")
        c_1.set_color_by_tex("c", RED)
        c_1.move_to(0.5*LEFT + 1.2*UP)
        c_1.scale(0.75)

        c_2 = TexMobject("c")
        c_2.set_color_by_tex("c", RED)
        c_2.move_to(0.5*DOWN + LEFT)
        c_2.scale(0.75)

        c_3 = TexMobject("c")
        c_3.set_color_by_tex("c", RED)
        c_3.move_to(1*DOWN + 0.5*RIGHT)
        c_3.scale(0.75)

        c_4 = TexMobject("c")
        c_4.set_color_by_tex("c", RED)
        c_4.move_to(RIGHT + 0.5*UP)
        c_4.scale(0.75)





        brace_1=Brace(line_6,DOWN)

        ab_1 = TexMobject("(a + b)")
        ab_1[1].set_color(BLUE)
        ab_1[3].set_color(GREEN)
        ab_1.next_to(brace_1, DOWN)
        ab_1.scale(0.75)


        #formulas

        aos = TexMobject("\\text{Area of total square}"," = ")
        aos[0].set_color(PURPLE)
        aos.move_to(3.5*UP + 4*LEFT)
        aos.scale(0.65)

        four_tri = TextMobject("Area of the 4 triangles"," + ")
        four_tri.set_color_by_tex("Area of the 4 triangles", YELLOW)
        four_tri.move_to(3.5*UP+ 0.5*LEFT)
        four_tri.scale(0.65)

        innerSquare = TextMobject("Area of inner square")
        innerSquare.set_color_by_tex("Area of inner square", ORANGE)
        innerSquare.move_to(3.5*UP + 3*RIGHT)
        innerSquare.scale(0.65)


        aots = TexMobject("(a + b)(a + b) = ")
        aots[1].set_color(BLUE)
        aots[6].set_color(BLUE)
        aots[3].set_color(GREEN)
        aots[8].set_color(GREEN)
        aots.next_to(aos, DOWN)
        aots.scale(0.65)

        n_aots = TexMobject("a^2 + 2ab + b^2 = ")
        n_aots[0].set_color(BLUE)
        n_aots[4].set_color(BLUE)
        n_aots[5].set_color(GREEN)
        n_aots[7].set_color(GREEN)
        n_aots.next_to(aos, DOWN)
        n_aots.scale(0.65)

        cross1 = Cross(n_aots[3:5])
        cross1.set_stroke(RED, 3)




        ao4t = TexMobject("4\\frac{1 }{2 }(ab) \\quad + ")
        ao4t[0].set_color(YELLOW)
        ao4t[5].set_color(BLUE)
        ao4t[6].set_color(GREEN)
        ao4t.next_to(aots, RIGHT)
        ao4t.scale(0.65)

        n_ao4t = TexMobject("2(ab) \\quad + ")
        n_ao4t[2].set_color(BLUE)
        n_ao4t[3].set_color(GREEN)
        n_ao4t.next_to(aots, RIGHT)
        n_ao4t.scale(0.65)

        cross2 = Cross(n_ao4t[0:4])
        cross2.set_stroke(RED, 3)



        innerS = TexMobject("c^2")
        innerS[0].set_color(RED)
        innerS.next_to(ao4t, RIGHT)
        innerS.scale(0.65)

        solve = TexMobject("\\text{Solve for } c")
        solve[8].set_color(RED)
        solve.next_to(aots, DOWN)
        solve.scale(0.65)

        solved = TexMobject("a^2 + b^2 = c^2")
        solved[0].set_color(BLUE)
        solved[3].set_color(GREEN)
        solved[6].set_color(RED)
        solved.move_to(UP)
        #solved.scale(0.95)

        solved2 = TexMobject("a^2 + b^2 = c^2")
        solved2[0].set_color(BLUE)
        solved2[3].set_color(GREEN)
        solved2[6].set_color(RED)
        solved2.move_to(UP)

        n_solved = TexMobject("a^2 + b^2 = c^2")
        n_solved[0].set_color(BLUE)
        n_solved[3].set_color(GREEN)
        n_solved[6].set_color(RED)
        n_solved.move_to(UP)
        n_solved.scale(2)


        



    




        












        self.play(ShowCreation(line_6))
        self.wait(1)
        self.play(FadeIn(point_1))

        self.play(Transform(point_1, point_2), run_time = 2.5)
        self.play(Transform(point_1, point_3), run_time = 1.8)

        self.play(Write(a_1))
        self.play(Write(b_1))
        self.play(GrowFromCenter(brace_1))
        self.play(Write(ab_1), run_time = 1.5)
        self.wait(1.5)

        self.play(FadeOut(ab_1), FadeOut(brace_1))

        #add rest of rectangle

        self.play(ShowCreation(line_7))
        self.play(ShowCreation(line_8))
        self.play(ShowCreation(line_9))
        self.wait(1.5)

        self.play(FadeIn(point_4))
        self.play(FadeIn(point_5))
        self.play(FadeIn(point_6))

        self.play(Write(a_2), Write(b_2))
        self.play(Write(a_3), Write(b_3))
        self.play(Write(a_4), Write(b_4))

        #play square inside square

        self.play(ShowCreation(line_10))
        self.play(ShowCreation(line_11))
        self.play(ShowCreation(line_12))
        self.play(ShowCreation(line_13))

        self.play(Write(c_1))
        self.play(Write(c_2))
        self.play(Write(c_3))
        self.play(Write(c_4))

        #PURPLE RECT
        rect = Rectangle(height=4,width=4, fill_color = PURPLE, fill_opacity = 0.4) 

        #INNER SQUARE
        square = Polygon(
            [1, 2, 0],
            [-2,1, 0],
            [-1, -2, 0],
            [2,-1,0],
            color=ORANGE
        )

        square.set_fill(ORANGE, 0.3) 

       

        triangle1 = Polygon(
            [1, 2, 0],
            [-2,2, 0],
            [-2, 1, 0],
            color=YELLOW
        )

        triangle2 = Polygon(
            [-2, 1, 0],
            [-2,-2, 0],
            [-1, -2, 0],
            color=YELLOW
        )



        triangle3 = Polygon(
            [-1, -2, 0],
            [2,-2, 0],
            [2, -1, 0],
            color=YELLOW
        )

        triangle4 = Polygon(
            [2, -1, 0],
             [2, 2, 0],
            [1, 2, 0],
            color=YELLOW
        )

        triangle1.set_fill(YELLOW, 0.3) 
        triangle2.set_fill(YELLOW, 0.3) 
        triangle3.set_fill(YELLOW, 0.3) 
        triangle4.set_fill(YELLOW, 0.3)   



        self.play(Write(aos))
        self.play(FadeIn(rect), run_time = 1.5)
        self.wait(1.2)

        self.play(Write(four_tri))
        self.play(FadeIn(triangle1), FadeIn(triangle2), FadeIn(triangle3),FadeIn(triangle4), run_time = 1.5)
        self.wait(1)

        self.play(Write(innerSquare))
        self.play(FadeIn(square), run_time = 1.5)
        self.wait(1.5)

        self.play(FadeOut(rect), FadeOut(square), FadeOut(triangle1), FadeOut(triangle2), FadeOut(triangle3), FadeOut(triangle4))

        
        #self.play(Write(aots))
        #self.play(ReplacementTransform(aos.copy(), aots), run_time = 1)
        #self.play(ReplacementTransform(a_1.copy(), aots[19]), run_time = 1)
        #self.play(ReplacementTransform(b_1.copy(), aots[21]), run_time = 1)
        self.wait(2)

        #og = VGroup(a_1,a_2,a_3,a_4,line_10,line_11,
        #line_12,line_9,line_8,line_7,line_6,line_13, c_1,c_2,c_3,c_4, b_1, b_2,b_3,b_4,
        #point_1, point_2,point_3, point_4,point_5,point_6,)

        #self.play(FadeOut(og))
        ##self.wait(0)
        #self.remove(og)

        #new = VGroup(a_1,a_2,a_3,a_4,line_10,line_11,
        #line_12,line_9,line_8,line_7,line_6, line_13,
         #c_1,c_2,c_3,c_4, b_1, b_2,b_3,b_4,point_1,point_2, point_3, point_4,point_5,point_6,)

        #new.move_to(4*RIGHT)

        #self.play(FadeIn(new))
        #self.wait(1)

        #self.play(Transform(aos.copy(), aots), run_time = 1)
        #self.wait(1.2)
        #self.play(ReplacementTransform(a_1.copy(), aots[19]))
        #self.play(ReplacementTransform(b_1.copy(), aots[21]))
        #self.wait(1.2)

        #self.play(ReplacementTransform(four_tri.copy(), ao4t), run_time = 1)
        #self.wait(1.2)
        #self.play(ReplacementTransform(c_1.copy(), ao4t[20]))
        #self.play(ReplacementTransform(a_1.copy(), ao4t[25]))
        #self.play(ReplacementTransform(b_1.copy(), ao4t[26]))

        #self.play(Write(aots))
        #self.wait(1.2)
        #self.play(Write(ao4t))

    

        #self.play(ReplacementTransform(og,new), run_time = 2)
        #Area of total square

        self.play(ReplacementTransform(aos.copy(), aots), FadeIn(rect), run_time = 1)
        self.wait(1.5)
        self.play(ReplacementTransform(a_1.copy(), aots[1]),ReplacementTransform(b_1.copy(), aots[3]), run_time = 1)
        self.play(ReplacementTransform(a_2.copy(), aots[6]),ReplacementTransform(b_2.copy(), aots[8]), run_time = 1)
        self.play(FadeOut(rect))
        self.wait(1.5)


        #area of triangle
        self.play(ReplacementTransform(four_tri.copy(), ao4t), FadeIn(triangle1), FadeIn(triangle2), FadeIn(triangle3), FadeIn(triangle4), run_time = 1)
        self.wait(1.5)
        self.play(ReplacementTransform(a_1.copy(), ao4t[5]), ReplacementTransform(b_2.copy(), ao4t[6]), run_time = 1)
        self.play(ReplacementTransform(a_2.copy(), ao4t[5]), ReplacementTransform(b_3.copy(), ao4t[6]), run_time = 1)
        self.play(ReplacementTransform(a_3.copy(), ao4t[5]), ReplacementTransform(b_4.copy(), ao4t[6]), run_time = 1)
        self.play(ReplacementTransform(a_4.copy(), ao4t[5]), ReplacementTransform(b_1.copy(), ao4t[6]), run_time = 1)

        self.play(FadeOut(triangle4), FadeOut(triangle1), FadeOut(triangle2), FadeOut(triangle3))
        self.wait(1.5)

        #area of inner square

        self.play(ReplacementTransform(innerSquare.copy(), innerS), FadeIn(square), run_time = 1)
        self.wait(1.2)
        self.play(ReplacementTransform(c_1.copy(), innerS[0]), ReplacementTransform(c_2.copy(), innerS[0]), run_time = 1)
        self.play(FadeOut(square))
        self.wait(1.7)


        #a^2 +2ab + b^2

        self.play(ReplacementTransform(aots, n_aots), run_time = 1)
        self.wait(1)

        #2ab
        self.play(ReplacementTransform(ao4t, n_ao4t), run_time = 1)
        self.wait(1.5)

        #cancel
        self.play(ShowCreation(cross1), ShowCreation(cross2), run_time = 2)
        self.wait(1)

        self.play(FadeOut(cross2), FadeOut(cross1), FadeOut(n_ao4t[0:5]), FadeOut(n_aots[2:6]))
        self.wait(1.5)

        self.play(FadeOut(point_1), FadeOut(point_3), FadeOut(point_4), FadeOut(point_5), FadeOut(line_6), 
        FadeOut(line_7), FadeOut(line_8), FadeOut(line_9), FadeOut(line_10),  FadeOut(line_11), FadeOut(line_12), FadeOut(line_13), 
        FadeOut(a_1), FadeOut(a_2),FadeOut(a_3),FadeOut(a_4),FadeOut(b_1),FadeOut(b_2), FadeOut(b_3),FadeOut(b_4), FadeOut(point_6),
        FadeOut(c_1), FadeOut(c_2),FadeOut(c_3),FadeOut(c_4))
        self.wait(1)















        #self.play(Write(solve), run_time = 2)
        #self.wait(1)

        self.play(ReplacementTransform(n_aots[0:1].copy(), solved[0:1]), ReplacementTransform(n_aots[7:8].copy(), solved[3:4]), ReplacementTransform(innerS[0:1].copy(), solved[6:7]), run_time = 2)
        self.play(Write(solved2), run_time = 2)

    
        self.play(FadeOut(aos), FadeOut(four_tri), FadeOut(innerSquare), FadeOut(n_aots[0:2]), FadeOut(n_aots[6:10]),FadeOut(n_ao4t[5]), FadeOut(innerS), FadeOut(solved))

        #self.play(ReplacementTransform(four_tri, ao4t), run_time = 1)
        #self.play(ReplacementTransform(innerSquare, innerS), run_time = 1)

        self.play(Transform(solved2, n_solved), run_time = 2)


        

        self.wait(4)



    







        


       







        


  





