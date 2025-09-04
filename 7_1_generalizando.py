from manim import *
from utils import *
import numpy as np

# Toggle Dark Mode here
DARK_MODE = False

# Define the color palettes
if DARK_MODE:
    BG_COLOR = "#000000"
    PRIMARY_COLOR = WHITE
    ARROW_COLOR = GRAY_E      # or any suitable arrow color in dark mode
    ERROR_COLOR = RED
    SPECIAL_FUNC_COLOR = rgb_to_color(hex_to_rgb("#C00000"))
    TANGENT_LINE_GREEN = GREEN
    TANGENT_LINE_BLUE = BLUE
else:
    BG_COLOR = "#FAE6C2"
    PRIMARY_COLOR = BLACK
    ARROW_COLOR = GRAY_E
    ERROR_COLOR = RED
    SPECIAL_FUNC_COLOR = rgb_to_color(hex_to_rgb("#C00000"))
    TANGENT_LINE_GREEN = GREEN
    TANGENT_LINE_BLUE = BLUE


class generalizando_1(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = BG_COLOR

        generalize_label = Text("Generalizando").set_color(PRIMARY_COLOR)

        self.add(generalize_label)

        self.wait(1)

        _ = generalize_label.copy()
        _.to_edge(UP).shift(DOWN * 1.5).scale(0.5).to_corner(UR, buff=0.5)
        title_box = SurroundingRectangle(_, color=PRIMARY_COLOR, buff=0.1)
        title_box.set_stroke(opacity=0.5, width=1)

        self.play(LaggedStart(
            generalize_label.animate.to_edge(UP).shift(DOWN * 1.5).scale(0.5).to_corner(UR, buff=0.5),
            Create(title_box),
            lag_ratio=0.8
        ))
        

        # New number plane for polynomial exploration
        plane = NumberPlane(
            x_range=(-4, 8),
            y_length=7,
            axis_config={"color": PRIMARY_COLOR, "stroke_opacity": 0.8},
            background_line_style={"stroke_color": PRIMARY_COLOR, "stroke_width": 1, "stroke_opacity": 0.5},
        ).set_opacity(0.7)

        # Polynomial function definition
        def polynomial(x):
            x = x - 1.2
            return (x + 1) * (x - 2.5) * (x - 4) / 10

        # Derivative of the polynomial
        def derivative(x):
            x = x - 1.2
            return 0.1 * (3 * x ** 2 - 11 * x + 3.5)
        
        # Second derivative of the polynomial
        def second_derivative(x):
            x = x - 1.2
            return 0.1 * (6 * x - 11)
        
        # Second derivative of the polynomial
        def third_derivative(x):
            x = x - 1.2
            return 0.1 * 6 

        # Initial point for tangent line x0 = 0.2
        x0 = 0.2
        xf = 1.6              # Target x for analysis
        f_x0 = polynomial(x0)
        f_prime_x0 = derivative(x0)

        # Plot polynomial function
        graph = plane.plot(polynomial, x_range=[-1.05, 6.51], color=SPECIAL_FUNC_COLOR)

        # Define zoom point
        zoom_point = plane.c2p(0.6, polynomial(0.6))

        # Animate appearance of plane and polynomial graph
        self.play(FadeIn(plane), Create(graph), run_time=2)
        self.wait(1)

        # Zoom into the function around zoom_point
        self.play(
            plane.animate.scale(4, about_point=zoom_point).shift(1.7*DOWN),
            graph.animate.scale(4, about_point=zoom_point).shift(1.7*DOWN)
        )

        self.wait(1)

        
        # Compute another tangent line at x0 = 0.6
        x0_2 = (x0 + xf) / 2
        f_x0_2 = polynomial(x0_2)
        f_prime_x0_2 = derivative(x0_2)
        u = (xf-x0)/3
        x0_3 = x0 + 2*u
        

        # Define first tangent line at x0
        def tangent_line(x, x0):
            return polynomial(x0) + derivative(x0) * (x - x0)
        
        def g2(x):
            return polynomial(x0) + (x-x0)*derivative(x0) + ((x-x0)/2)**2*second_derivative(x0)

        def line_g3(x):
            return polynomial(x0) + 2*u*derivative(x0) + u**2*second_derivative(x0) + (x-x0_3)*(derivative(x0) + 2*u*second_derivative(x0) + u**2*third_derivative(x0))

        def g3(x):
            return polynomial(x0) + (x-x0)*derivative(x0) + 3*((x-x0)/3)**2*second_derivative(x0) + (((x-x0)/3)**3)*third_derivative(x0)

        # Create first tangent line graph
        tangent_line_graph = plane.plot(lambda x: tangent_line(x, x0_3), x_range=[x0_3, xf], color=ORANGE)
        line_g3_graph = plane.plot(line_g3, x_range=[x0_3, xf], color=PURPLE)
        g2_graph = plane.plot(g2, x_range=[x0, x0_3], color=TANGENT_LINE_BLUE)
        g3_graph = plane.plot(g3, x_range=[x0, xf], color=TANGENT_LINE_GREEN)
        end_dot = Dot(point=plane.c2p(xf, tangent_line(xf, x0_3)), color=PRIMARY_COLOR, radius=0.03)
        end_dot_g3 = Dot(point=plane.c2p(xf, line_g3(xf)), color=PRIMARY_COLOR, radius=0.03)
        
        # Add label for first approximation function r1(x)
        r_tan_label = MathTex("r_{tan}(x)", font_size=24).set_color(PRIMARY_COLOR)
        r_tan_label.next_to(plane.c2p(xf, tangent_line(xf, x0_3)), UP, buff=0.2)

        line_xf = DashedLine(plane.c2p(xf, 0),plane.c2p(xf, polynomial(xf)), color=PRIMARY_COLOR, stroke_width = 2)
        line_x02 = DashedLine(plane.c2p(x0 + ((xf-x0)/3), 0),plane.c2p(x0 + ((xf-x0)/3), polynomial(x0 + ((xf-x0)/3))),color=PRIMARY_COLOR,stroke_width = 2)
        line_x03 = DashedLine(plane.c2p(x0_3, 0),plane.c2p(x0_3, polynomial(x0_3)),color=PRIMARY_COLOR,stroke_width = 2)
        label_xf = MathTex("x_0+3u=x", font_size=24).set_color(PRIMARY_COLOR)
        label_xf.next_to(plane.c2p(xf, 0), DOWN, buff=0.2)
        label_x0 = MathTex("x_0", font_size=24).set_color(PRIMARY_COLOR)
        label_x0.next_to(plane.c2p(x0, 0), DOWN, buff=0.2)
        label_x03 = MathTex("x_0+2u", font_size=24).set_color(PRIMARY_COLOR)
        label_x03.next_to(plane.c2p(x0_3, 0), DOWN, buff=0.2)
        label_x02 = MathTex("x_0+u", font_size=24).set_color(PRIMARY_COLOR)
        label_x02.next_to(plane.c2p(x0 + ((xf-x0)/3), 0), DOWN, buff=0.2)
        label_r3 = MathTex("r_3(x)", font_size=24).set_color(PRIMARY_COLOR).next_to(end_dot, RIGHT, buff=0.2)
        label_g2= MathTex("g_2(x)", font_size=24).set_color(PRIMARY_COLOR).next_to(plane.c2p(x0_3, g2(x0_3)), DL, buff=0.5).shift(0.6*LEFT)
        label_g3= MathTex("g_3(x)", font_size=24).set_color(PRIMARY_COLOR).next_to(plane.c2p(xf, g3(xf)), UP, buff=0.2)
        dx_u_equation = MathTex("u= \\frac{\\Delta x}{3}", font_size=24).set_color(PRIMARY_COLOR).move_to(plane.c2p(x0_3+0.25, 0.5))

        r3_equation = MathTex("f(x_0+3u)", "\\approx", "r_3(x_0+3u)", " = ", "f(x_0 + 2u)", "+", "u", "f'(x_0 + 2u)", font_size=24).set_color(PRIMARY_COLOR).next_to(plane.c2p(0, 1.7), RIGHT)
        eq_bg = Rectangle(width=r3_equation.width,height=r3_equation.height + 0.1,color=BG_COLOR,fill_opacity=0.9).move_to(r3_equation)
        r3_equation_g2 = MathTex("f(x_0+3u)", "\\approx", "r_3(x_0+3u)", "\\approx", "g_2(x_0 + 2u)", "+", "u", "f'(x_0 + 2u)", font_size=24).set_color(PRIMARY_COLOR).move_to(r3_equation, LEFT)
        r3_equation_g2_all = MathTex("f(x_0+3u)", "\\approx", "r_3(x_0+3u)", "\\approx", "g_2(x_0 + 2u)", "+", "u", "g_2'(x_0 + 2u)", font_size=24).set_color(PRIMARY_COLOR).move_to(r3_equation, LEFT)
        g3_equation_g2 = MathTex("f(x_0+3u)", "\\approx", "g_2(x_0 + 2u)", "+", "u", "g_2'(x_0 + 2u)", font_size=24).set_color(PRIMARY_COLOR).move_to(r3_equation, LEFT)
        g3_equation_g2_all = MathTex("f(x_0+3u)", "\\approx", "f(x_0)+2uf'(x_0)+u^2f''(x_0)", "+", "u", "(f'(x_0)+2uf''(x_0)+u^2f'''(x_0))", font_size=24).set_color(PRIMARY_COLOR).move_to(r3_equation, LEFT)
        g3_equation_aux = MathTex("f(x_0+3u)", "\\approx", "f(x_0)+3uf'(x_0)+3u^2","f''(x_0)","+u^3","f'''(x_0)", font_size=24).set_color(PRIMARY_COLOR).move_to(r3_equation, LEFT)
        g3_equation = MathTex("f(x_0+3u)", "\\approx", "f(x_0)+3uf'(x_0)+3u^2","f^2(x_0)","+u^3","f^3(x_0)", "=g_3(x_0+3u)", font_size=24).set_color(PRIMARY_COLOR).move_to(r3_equation, LEFT)
        g3_equation_deltax = MathTex("f(x_0+\\Delta x)", "\\approx", "f(x_0)+\\Delta xf'(x_0)+\\frac{\\Delta x^2}{3}","f^2(x_0)","+\\frac{\\Delta x^3}{27}","f^3(x_0)", font_size=24).set_color(PRIMARY_COLOR).move_to(r3_equation, LEFT)
        g3_equation_deltax_ = MathTex("f(x_0+\\Delta x)", "\\approx", "f(x_0)","+","\\Delta xf'(x_0)","+","\\frac{\\Delta x^2}{3}f^2(x_0)","+","\\frac{\\Delta x^3}{27}f^3(x_0)", font_size=24).set_color(PRIMARY_COLOR).move_to(r3_equation, LEFT)

        g3_sqrt_equation = MathTex("\\sqrt{x_0+\\Delta x}", "\\approx", "\\sqrt{x_0}","+","\\frac{\\Delta x}{2\\sqrt x_0}","-","\\frac{\\Delta x^2}{12\\sqrt{x_0^3}}","+","\\frac{\\Delta x^3}{72\\sqrt{x_0^5}}", font_size=30).set_color(PRIMARY_COLOR).move_to(ORIGIN)
        g3_sqrt_5 = MathTex("\\sqrt{4+1}", "\\approx", "\\sqrt 4","+","\\frac{1}{2\\sqrt 4}","-","\\frac{1}{12\\sqrt{4^3}}","+","\\frac{1}{72\\sqrt{4^5}}", font_size=30).set_color(PRIMARY_COLOR).move_to(ORIGIN)
        g3_sqrt_5_simplified = MathTex("\\sqrt 5", "\\approx", "2","+","\\frac{1}{4}","-","\\frac{1}{96}","+","\\frac{1}{2304}", font_size=30).set_color(PRIMARY_COLOR).move_to(ORIGIN)
        g3_sqrt_5_value = MathTex("\\sqrt 5", "\\approx", "2.24001736", font_size=30).set_color(PRIMARY_COLOR).move_to(ORIGIN)
        g3_sqrt_5_value_sqrd = MathTex("\\sqrt 5 ^2", "\\approx", "2.24001736^2", font_size=30).set_color(PRIMARY_COLOR).move_to(ORIGIN)
        g3_5_value = MathTex("5", "\\approx", "5.01767777", font_size=30).set_color(PRIMARY_COLOR).move_to(ORIGIN)
        g3_equation_copy = MathTex("g_3(x_0+3u)", "=", "f(x_0)+3uf'(x_0)+3u^2","f^2(x_0)","+u^3","f^3(x_0)", font_size=24).set_color(PRIMARY_COLOR).move_to(ORIGIN).set_opacity(0)

        g3_equation_boxed = MathTex("g_3(x_0+3u)", "=", "f(x_0)+3uf'(x_0)+3u^2","f^2(x_0)","+u^3","f^3(x_0)", font_size=24).set_color(PRIMARY_COLOR).scale(0.8).to_corner(UL, buff=0.5)
        eq_box = SurroundingRectangle(g3_equation_boxed, color=PRIMARY_COLOR, buff=0.1)
        eq_box.set_stroke(opacity=0.5, width=1)

        info = MathTex("f'(x)","=","f^1(x)", font_size=24).set_color(PRIMARY_COLOR).next_to(r3_equation, DOWN, aligned_edge=LEFT)
        info_1 = MathTex("f''(x)","=","f^2(x)", font_size=24).set_color(PRIMARY_COLOR).next_to(r3_equation, DOWN, aligned_edge=LEFT)
        info_2 = MathTex("f'''(x)","=","f^3(x)", font_size=24).set_color(PRIMARY_COLOR).next_to(r3_equation, DOWN, aligned_edge=LEFT)
        info_3 = MathTex("\\frac{d^nf(x)}{dx^n}","=","f^n(x)", font_size=24).set_color(PRIMARY_COLOR).next_to(r3_equation, DOWN, aligned_edge=LEFT)

        self.play(FadeIn(label_xf, label_x0, label_x03, label_x02), Create(line_x02), Create(line_xf), Create(line_x03))
        self.wait(1)
        self.play(Write(dx_u_equation))
        self.wait(2)

        self.play(
            HighlightWithRect(label_x03),
            Indicate(line_x03, scale_factor=1, color=SPECIAL_FUNC_COLOR),
            Indicate(label_x03, scale_factor=1.4 , color=SPECIAL_FUNC_COLOR),
            run_time=1.5
        )

        self.wait(5)

        self.play(LaggedStart(
            Create(tangent_line_graph),
            FadeIn(end_dot),
            FadeIn(label_r3),
            lag_ratio=0.6
        ))

        self.wait(3)

        self.play(HighlightWithRect(dx_u_equation))

        self.wait(3)

        self.play(HighlightWithRect(label_x03))
        self.wait(2)
        self.play(HighlightWithRect(label_xf))

        self.wait(1)

        self.play(FadeIn(eq_bg), Write(r3_equation))

        self.wait(4)
        self.play(HighlightWithRect(r3_equation[4]))
        self.wait(2)
        self.play(HighlightWithRect(r3_equation[7]))

        self.wait(2)

        self.play(
            ReplacementTransform(r3_equation[0], r3_equation_g2[0]),
            ReplacementTransform(r3_equation[1], r3_equation_g2[1]),
            ReplacementTransform(r3_equation[2], r3_equation_g2[2]),
            ReplacementTransform(r3_equation[3], r3_equation_g2[3]),
            FadeOut(r3_equation[4], shift=DOWN),
            FadeIn(r3_equation_g2[4], shift=DOWN),
            ReplacementTransform(r3_equation[5], r3_equation_g2[5]),
            ReplacementTransform(r3_equation[6], r3_equation_g2[6]),
            ReplacementTransform(r3_equation[7], r3_equation_g2[7])
        )
        self.wait(1)


        self.wait(2)

        self.play(Create(g2_graph), FadeIn(label_g2))
        self.wait(2)

        self.play(
            ReplacementTransform(r3_equation_g2[0], r3_equation_g2_all[0]),
            ReplacementTransform(r3_equation_g2[1], r3_equation_g2_all[1]),
            ReplacementTransform(r3_equation_g2[2], r3_equation_g2_all[2]),
            ReplacementTransform(r3_equation_g2[3], r3_equation_g2_all[3]),
            ReplacementTransform(r3_equation_g2[4], r3_equation_g2_all[4]),
            ReplacementTransform(r3_equation_g2[5], r3_equation_g2_all[5]),
            ReplacementTransform(r3_equation_g2[6], r3_equation_g2_all[6]),
            FadeOut(r3_equation_g2[7], shift=DOWN),
            FadeIn(r3_equation_g2_all[7], shift=DOWN),
        )
        self.wait(1)

        self.play(HighlightWithRect(r3_equation_g2_all[7]))

        self.wait(1)
        
        self.play(Create(line_g3_graph))

        self.wait(5.5)
        self.play(
            ReplacementTransform(r3_equation_g2_all[0], g3_equation_g2[0]),
            FadeOut(r3_equation_g2_all[1], shift=DOWN),
            FadeOut(r3_equation_g2_all[2], shift=DOWN),
            ReplacementTransform(r3_equation_g2_all[3], g3_equation_g2[1]),
            ReplacementTransform(r3_equation_g2_all[4], g3_equation_g2[2]),
            ReplacementTransform(r3_equation_g2_all[5], g3_equation_g2[3]),
            ReplacementTransform(r3_equation_g2_all[6], g3_equation_g2[4]),
            ReplacementTransform(r3_equation_g2_all[7], g3_equation_g2[5]),
            run_time=1.5
        )

        self.wait(5)

        self.play(
            ReplacementTransform(g3_equation_g2[0], g3_equation_g2_all[0]),
            ReplacementTransform(g3_equation_g2[1], g3_equation_g2_all[1]),
            ReplacementTransform(g3_equation_g2[2], g3_equation_g2_all[2]),
            ReplacementTransform(g3_equation_g2[3], g3_equation_g2_all[3]),
            ReplacementTransform(g3_equation_g2[4], g3_equation_g2_all[4]),
            ReplacementTransform(g3_equation_g2[5], g3_equation_g2_all[5]),
        )
        self.wait(3)

        self.play(
            ReplacementTransform(g3_equation_g2_all[0], g3_equation_aux[0]),
            ReplacementTransform(g3_equation_g2_all[1], g3_equation_aux[1]),
            ReplacementTransform(g3_equation_g2_all[2], g3_equation_aux[2]),
            ReplacementTransform(g3_equation_g2_all[3], g3_equation_aux[3]),
            ReplacementTransform(g3_equation_g2_all[4], g3_equation_aux[4]),
            ReplacementTransform(g3_equation_g2_all[5], g3_equation_aux[5]),
        )
        self.wait(1)

        # self.play(Write(info))
        # self.wait(1)
        # self.play(
        #     ReplacementTransform(info[0], info_1[0]),
        #     ReplacementTransform(info[1], info_1[1]),
        #     ReplacementTransform(info[2], info_1[2])
        # )
        # self.wait(1)
        # self.play(
        #     ReplacementTransform(info_1[0], info_2[0]),
        #     ReplacementTransform(info_1[1], info_2[1]),
        #     ReplacementTransform(info_1[2], info_2[2])
        # )
        # self.wait(1)
        # self.play(
        #     ReplacementTransform(info_2[0], info_3[0]),
        #     ReplacementTransform(info_2[1], info_3[1]),
        #     ReplacementTransform(info_2[2], info_3[2])
        # )
        # self.wait(1)

        self.play(
            ReplacementTransform(g3_equation_aux[0], g3_equation[0]),
            ReplacementTransform(g3_equation_aux[1], g3_equation[1]),
            ReplacementTransform(g3_equation_aux[2], g3_equation[2]),
            ReplacementTransform(g3_equation_aux[3], g3_equation[3]),
            ReplacementTransform(g3_equation_aux[4], g3_equation[4]),
            ReplacementTransform(g3_equation_aux[5], g3_equation[5]),
            FadeIn(g3_equation[6], shift=LEFT)
        )
        self.wait(1)

        self.play(Indicate(g3_equation[6], scale_factor=1.3, color=SPECIAL_FUNC_COLOR))
        self.play(Create(g3_graph), FadeIn(end_dot_g3), FadeIn(label_g3))
        self.wait(2)
        
        self.play(
            ReplacementTransform(g3_equation[0], g3_equation_deltax[0]),
            ReplacementTransform(g3_equation[1], g3_equation_deltax[1]),
            ReplacementTransform(g3_equation[2], g3_equation_deltax[2]),
            ReplacementTransform(g3_equation[3], g3_equation_deltax[3]),
            ReplacementTransform(g3_equation[4], g3_equation_deltax[4]),
            ReplacementTransform(g3_equation[5], g3_equation_deltax[5]),
            FadeOut(g3_equation[6]),

        )
        self.play(FadeTransform(g3_equation_deltax, g3_equation_deltax_))
        self.wait(2)
 

        self.play(FadeOut(line_g3_graph, g2_graph, label_g2))

        self.wait(2)
        self.play(
            FadeOut(graph, plane, g3_graph, tangent_line_graph, end_dot, end_dot_g3),
            FadeOut(line_xf, line_x03, line_x02, eq_bg, label_r3, label_x0, label_x02, label_x03, label_xf, dx_u_equation, label_g3),
            g3_equation_deltax_.animate.move_to(ORIGIN).scale(1.25),
        )

        self.wait(1)
        self.play(LaggedStart(
            g3_equation_copy.animate.move_to(g3_equation_boxed).scale(0.8).set_opacity(1),
            Create(eq_box),
            lag_ratio=0.6
        ))

        f_eq = MathTex("f(x) = \\sqrt{x}", font_size=24).set_color(PRIMARY_COLOR)
        f_prime_eq = MathTex("f'(x) = \\frac{1}{2\\sqrt{x}}", font_size=24).set_color(PRIMARY_COLOR)
        f_double_prime_eq = MathTex("f''(x) = -\\frac{1}{4x^{3/2}}", font_size=24).set_color(PRIMARY_COLOR)

        sqrt_group = VGroup(f_eq, f_prime_eq, f_double_prime_eq).arrange(buff=1.5).next_to(g3_equation_deltax_, UP)

        self.wait(1)

        self.play(LaggedStart(
            Write(f_eq),
            Write(f_prime_eq),
            Write(f_double_prime_eq),
            lag_ratio=0.2
        ))

        self.wait(1)

        self.play(
            ReplacementTransform(g3_equation_deltax_[0], g3_sqrt_equation[0]),
            ReplacementTransform(g3_equation_deltax_[1], g3_sqrt_equation[1]),
            ReplacementTransform(g3_equation_deltax_[2], g3_sqrt_equation[2]),
            ReplacementTransform(g3_equation_deltax_[3], g3_sqrt_equation[3]),
            ReplacementTransform(g3_equation_deltax_[4], g3_sqrt_equation[4]),
            ReplacementTransform(g3_equation_deltax_[5], g3_sqrt_equation[5]),
            ReplacementTransform(g3_equation_deltax_[6], g3_sqrt_equation[6]),
            ReplacementTransform(g3_equation_deltax_[7], g3_sqrt_equation[7]),
            ReplacementTransform(g3_equation_deltax_[8], g3_sqrt_equation[8]),
        )

        self.wait(3)
        self.play(
            ReplacementTransform(g3_sqrt_equation[0], g3_sqrt_5[0]),
            ReplacementTransform(g3_sqrt_equation[1], g3_sqrt_5[1]),
            ReplacementTransform(g3_sqrt_equation[2], g3_sqrt_5[2]),
            ReplacementTransform(g3_sqrt_equation[3], g3_sqrt_5[3]),
            ReplacementTransform(g3_sqrt_equation[4], g3_sqrt_5[4]),
            ReplacementTransform(g3_sqrt_equation[5], g3_sqrt_5[5]),
            ReplacementTransform(g3_sqrt_equation[6], g3_sqrt_5[6]),
            ReplacementTransform(g3_sqrt_equation[7], g3_sqrt_5[7]),
            ReplacementTransform(g3_sqrt_equation[8], g3_sqrt_5[8]),
            FadeOut(sqrt_group)        
        )

        self.wait(0.5)
        self.play(
            ReplacementTransform(g3_sqrt_5[0], g3_sqrt_5_simplified[0]),
            ReplacementTransform(g3_sqrt_5[1], g3_sqrt_5_simplified[1]),
            ReplacementTransform(g3_sqrt_5[2], g3_sqrt_5_simplified[2]),
            ReplacementTransform(g3_sqrt_5[3], g3_sqrt_5_simplified[3]),
            ReplacementTransform(g3_sqrt_5[4], g3_sqrt_5_simplified[4]),
            ReplacementTransform(g3_sqrt_5[5], g3_sqrt_5_simplified[5]),
            ReplacementTransform(g3_sqrt_5[6], g3_sqrt_5_simplified[6]),
            ReplacementTransform(g3_sqrt_5[7], g3_sqrt_5_simplified[7]),
            ReplacementTransform(g3_sqrt_5[8], g3_sqrt_5_simplified[8]) 
        )

        self.wait(0.5)
        self.play(
            ReplacementTransform(g3_sqrt_5_simplified[0], g3_sqrt_5_value[0]),
            ReplacementTransform(g3_sqrt_5_simplified[1], g3_sqrt_5_value[1]),
            ReplacementTransform(g3_sqrt_5_simplified[2], g3_sqrt_5_value[2]),
            FadeOut(g3_sqrt_5_simplified[3], shift=LEFT/2),
            FadeOut(g3_sqrt_5_simplified[4], shift=1.1*LEFT/2),
            FadeOut(g3_sqrt_5_simplified[5], shift=1.2*LEFT/2),
            FadeOut(g3_sqrt_5_simplified[6], shift=1.3*LEFT/2),
            FadeOut(g3_sqrt_5_simplified[7], shift=1.4*LEFT/2),
            FadeOut(g3_sqrt_5_simplified[8], shift=1.5*LEFT/2)
        )

        self.wait(3)

        self.play(
            ReplacementTransform(g3_sqrt_5_value[0], g3_sqrt_5_value_sqrd[0]),
            ReplacementTransform(g3_sqrt_5_value[1], g3_sqrt_5_value_sqrd[1]),
            ReplacementTransform(g3_sqrt_5_value[2], g3_sqrt_5_value_sqrd[2])
        )

        self.wait(1)

        self.play(
            ReplacementTransform(g3_sqrt_5_value_sqrd[0], g3_5_value[0]),
            ReplacementTransform(g3_sqrt_5_value_sqrd[1], g3_5_value[1]),
            ReplacementTransform(g3_sqrt_5_value_sqrd[2], g3_5_value[2])
        )


        

        self.wait(2)