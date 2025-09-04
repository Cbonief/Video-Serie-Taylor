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


class generalizando_2(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = BG_COLOR

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

        
        # Define first tangent line at xt
        def tangent_line(x, xt):
            return polynomial(xt) + derivative(xt) * (x - xt)

        
        n = 4
        x0 = 0.2
        xn = 1.6              # Target x for analysis
        delta_x = xn-x0
        u = delta_x/n
        xn_1 = xn-u
        xarray = np.linspace(x0, xn)


        generalize_label = Text("Generalizando").set_color(PRIMARY_COLOR)
        generalize_label.to_edge(UP).shift(DOWN * 1.5).scale(0.5).to_corner(UR, buff=0.5)

        title_box = SurroundingRectangle(generalize_label, color=PRIMARY_COLOR, buff=0.1)
        title_box.set_stroke(opacity=0.5, width=1)

        g3_equation = MathTex("g_3(x_0+3u)", "=", "f(x_0)", "+", "3u","f'(x_0)","+","3u^2","f^2(x_0)","+","u^3","f^3(x_0)", font_size=24).set_color(PRIMARY_COLOR).scale(0.8).to_corner(UL, buff=0.5)
        
        eq_box = SurroundingRectangle(g3_equation, color=PRIMARY_COLOR, buff=0.1)
        eq_box.set_stroke(opacity=0.5, width=1)

        self.add(title_box, generalize_label, eq_box, g3_equation)


        # New number plane for polynomial exploration
        plane = NumberPlane(
            x_range=(-4, 8),
            y_length=7,
            axis_config={"color": PRIMARY_COLOR, "stroke_opacity": 0.8},
            background_line_style={"stroke_color": PRIMARY_COLOR, "stroke_width": 1, "stroke_opacity": 0.5},
        ).set_opacity(0.7)


        # Plot polynomial function
        graph = plane.plot(polynomial, x_range=[-1.05, 6.51], color=SPECIAL_FUNC_COLOR)

        # Define zoom point
        zoom_point = plane.c2p(0.6, polynomial(0.6))

        # Animate appearance of plane and polynomial graph
        self.play(FadeIn(plane), Create(graph), g3_equation.animate.set_opacity(0.5), run_time=2)
        self.wait(1)

        # Zoom into the function around zoom_point
        self.play(
            plane.animate.scale(4.5, about_point=zoom_point).shift(DOWN),
            graph.animate.scale(4.5, about_point=zoom_point).shift(DOWN)
        )

                # Create the tangent at xn_1
        tangent_line_graph = plane.plot(lambda x: tangent_line(x, xn_1), x_range=[xn_1, xn], color=ORANGE)
        
        # Add label for first approximation function r1(x)
        r_tan_label = MathTex("r_{n}(x)", font_size=24).set_color(PRIMARY_COLOR)
        r_tan_label.next_to(plane.c2p(xn, tangent_line(xn, xn_1)), UP, buff=0.2)
        end_dot = Dot(point=plane.c2p(xn, tangent_line(xn, xn_1)), color=PRIMARY_COLOR, radius=0.03)

    
        vertical_doted_lines = {}

        braces = BraceBetweenPoints(plane.c2p(x0, 0), plane.c2p(xn, 0), fill_opacity=0.8, buff=0.3, sharpness=1).set_color(PRIMARY_COLOR)
        braces_text = braces.get_text("n divisões").set_color(PRIMARY_COLOR).set_font_size(24)
        braces_text.next_to(braces, DOWN)
        x0_label = MathTex(f"x_0", font_size=24).set_color(PRIMARY_COLOR)
        x0_label.next_to(plane.c2p(x0, 0), DOWN, buff=0.1).shift(RIGHT )
        xn_1_label = MathTex("x_0 + u(n-1)", font_size=24).set_color(PRIMARY_COLOR)
        xn_1_label.next_to(plane.c2p(xn-u, 0), DOWN, buff=0.1)
        xn_label = MathTex("x_0 + nu", font_size=24).set_color(PRIMARY_COLOR)
        xn_label.next_to(plane.c2p(xn, 0), DOWN, buff=0.1)

        x0_dot = Dot(point=plane.c2p(x0, 0), color=PRIMARY_COLOR, radius=0.03)
        # xn_1_dot = Dot(point=plane.c2p(xn-u, 0), color=PRIMARY_COLOR, radius=0.03)
        # xn_dot = Dot(point=plane.c2p(xn, 0), color=PRIMARY_COLOR, radius=0.03)

        labels = [x0_label]
        dots = [x0_dot]

        for i in range(1, n+1):
            new_line = DashedLine(plane.c2p(x0+i*u, 0),plane.c2p(x0+i*u, polynomial(x0+i*u)), color=PRIMARY_COLOR, stroke_width = 2)
            vertical_doted_lines[i] = new_line

            new_dot = Dot(point=plane.c2p(x0+i*u, 0), color=PRIMARY_COLOR, radius=0.03)
            dots.append(new_dot)
            if i < n-1:
                new_label = MathTex(f"x_{i}", font_size=24).set_color(PRIMARY_COLOR)
                new_label.next_to(plane.c2p(x0+i*u, 0), DOWN, buff=0.1)
                labels.append(new_label)
            elif i < n:
                labels.append(xn_1_label)

        labels.append(xn_label)

        position = (vertical_doted_lines[n-1].get_x()+vertical_doted_lines[n-2].get_x())/2
        three_dots = MathTex("\\dots", font_size=36).set_color(PRIMARY_COLOR).next_to(vertical_doted_lines[n-1]).set_x(position)

        r_n_equation = MathTex("r_n(x_0+nu)", "=", "f(x_0+(n-1)u)", "+", "u", "f'(x_0+(n-1)u)", font_size=24).set_color(PRIMARY_COLOR).next_to(plane.c2p(0, 1.3), RIGHT)
        eq_bg = Rectangle(width=r_n_equation.width,height=r_n_equation.height + 0.1,color=BG_COLOR,fill_opacity=0.9).move_to(r_n_equation)
        r_n_equation_dx = MathTex("r_n(x_0+\\Delta x)", "=", "f(x_0+(n-1)u)", "+", "u", "f'(x_0+(n-1)u)", font_size=24).set_color(PRIMARY_COLOR).move_to(r_n_equation, aligned_edge=LEFT)
        r_n_equation_dx_approx = MathTex("r_n(x_0+\\Delta x)", "\\approx", "g_{n-1}(x_0+(n-1)u)", "+", "u", "g'_{n-1}(x_0+(n-1)u)", font_size=24).set_color(PRIMARY_COLOR).move_to(r_n_equation, aligned_edge=LEFT)
        g_n_equation = MathTex("g_n(x_0+nu)", "=", "g_{n-1}(x_0+(n-1)u)", "+", "u", "g'_{n-1}(x_0+(n-1)u)", font_size=24).set_color(PRIMARY_COLOR).move_to(r_n_equation, aligned_edge=LEFT)
        g_4_equation = MathTex("g_4(x_0+4u)", "=", "g_3(x_0+3u)", "+", "u", "g'_3(x_0+3u)", font_size=30).set_color(PRIMARY_COLOR).move_to(ORIGIN)
        g_3_prime_equation = MathTex("g'_3(x_0+3u)", "=", "f'(x_0)", "+", "3u","f^2(x_0)","+","3u^2","f^3(x_0)","+","u^3","f^4(x)", font_size=24).set_color(PRIMARY_COLOR).scale(1.25)
        u_g_3_prime_equation = MathTex("ug'_3(x_0+3u)", "=", "u","f'(x_0)", "+", "3u^2","f^2(x_0)","+","3u^3","f^3(x_0)","+","u^4","f^4(x)", font_size=24).set_color(PRIMARY_COLOR).scale(1.25)
        g_4_equation = MathTex("g_4(x_0+4u)", "=", "g_3(x_0+3u)", "+", "u", "g'_3(x_0+3u)", font_size=30).set_color(PRIMARY_COLOR).move_to(ORIGIN)
        g4_full = MathTex("g_4(x_0+4u)", "=", "f(x_0)", "+4uf^1(x_0)", "+6u^2f^2(x_0)","+4u^3f^3(x_0)","+u^4f^4(x)", font_size=24).set_color(PRIMARY_COLOR).scale(1.25)

        plus_left = MathTex("+", font_size=24).set_color(PRIMARY_COLOR).scale(1.25)
        plus_right = MathTex("+", font_size=24).set_color(PRIMARY_COLOR).scale(1.25)

        n_eq_4 = MathTex("n=4", font_size=30).set_color(PRIMARY_COLOR).next_to(g_4_equation, UP)

        # g_4_equation_g3 = MathTex("g_4(x_0+4u)", "=", "f(x_0)", "+", "3u","f'(x_0)","+","3u^2","f^2(x_0)","+","u^3","f^3(x_0)", font_size=30).set_color(PRIMARY_COLOR).move_to(ORIGIN)
        # g_4_equation_g3_g3_prime = MathTex("g_4(x_0+4u)", "=", "f(x_0)", "+", "3u","f'(x_0)","+","3u^2","f^2(x_0)","+","u^3","f^3(x_0)", font_size=30).set_color(PRIMARY_COLOR).move_to(ORIGIN)

        self.wait(1)

        create_lines_animations = [Create(line) for line in vertical_doted_lines.values()]
        create_labels_animations = [Create(label) for label in labels]
        create_dots_animations = [Create(dot) for dot in dots]



        self.play(
            AnimationGroup(*create_lines_animations,lag_ratio=0.2),
            AnimationGroup(*create_labels_animations,lag_ratio=0.2),
            AnimationGroup(*create_dots_animations,lag_ratio=0.2),
            FadeIn(braces),
            FadeIn(braces_text)
        )

        self.wait(1)

        self.play(LaggedStart(
            Create(tangent_line_graph),
            Create(end_dot),
            Create(r_tan_label),
            Create(three_dots),
            lag_ratio=0.2  
        ))

        self.wait(1)

        self.play(
            FadeIn(eq_bg),
            Write(r_n_equation)
        )

        self.wait(1)
        self.play(HighlightWithRect(r_n_equation))

        self.wait(4.5)
        xn_label_ = MathTex("x_0 + \\Delta x", font_size=24).set_color(PRIMARY_COLOR)
        xn_label_.move_to(labels[-1])

        self.play(HighlightWithRect(labels[n-1]))
        self.wait(2)
        self.play(HighlightWithRect(labels[-1]))
        self.wait(2)
        self.play(Transform(xn_label[0][-2:], xn_label_[0][-2:]))
        self.wait(1)
        self.play(
            ReplacementTransform(r_n_equation[0], r_n_equation_dx[0]),
            ReplacementTransform(r_n_equation[1], r_n_equation_dx[1]),
            ReplacementTransform(r_n_equation[2], r_n_equation_dx[2]),
            ReplacementTransform(r_n_equation[3], r_n_equation_dx[3]),
            ReplacementTransform(r_n_equation[4], r_n_equation_dx[4]),
            ReplacementTransform(r_n_equation[5], r_n_equation_dx[5])
        )
        self.wait(1)
        self.play(
            ReplacementTransform(r_n_equation_dx[0], r_n_equation_dx_approx[0]),
            ReplacementTransform(r_n_equation_dx[1], r_n_equation_dx_approx[1]),
            FadeOut(r_n_equation_dx[2], shift=DOWN),
            FadeIn(r_n_equation_dx_approx[2], shift=DOWN),
            ReplacementTransform(r_n_equation_dx[3], r_n_equation_dx_approx[3]),
            ReplacementTransform(r_n_equation_dx[4], r_n_equation_dx_approx[4]),
            r_n_equation_dx[5].animate.move_to(r_n_equation_dx_approx[5], aligned_edge=LEFT)
        )
        self.wait(1)
        self.play(
            FadeOut(r_n_equation_dx[5], shift=DOWN),
            FadeIn(r_n_equation_dx_approx[5], shift=DOWN),
        )
        self.wait(1)        
        self.play(
            ReplacementTransform(r_n_equation_dx_approx[0], g_n_equation[0]),
            ReplacementTransform(r_n_equation_dx_approx[1], g_n_equation[1]),
            ReplacementTransform(r_n_equation_dx_approx[2], g_n_equation[2]),
            ReplacementTransform(r_n_equation_dx_approx[3], g_n_equation[3]),
            ReplacementTransform(r_n_equation_dx_approx[4], g_n_equation[4]),
            ReplacementTransform(r_n_equation_dx_approx[5], g_n_equation[5])
        )
        self.wait(1)
        fade_lines_animations = [FadeOut(line) for line in vertical_doted_lines.values()]
        fade_labels_animations = [FadeOut(label) for label in labels]
        fade_dots_animations = [FadeOut(dot) for dot in dots]

        self.play(
            AnimationGroup(*fade_lines_animations),
            AnimationGroup(*fade_labels_animations),
            AnimationGroup(*fade_dots_animations),
            FadeOut(graph, plane, tangent_line_graph, end_dot, three_dots, braces, braces_text, r_tan_label),
            g_n_equation.animate.move_to(ORIGIN).scale(1.25),
            g3_equation.animate.set_opacity(1)
        )
        self.wait(11)
        n_1_group = VGroup(g_n_equation[2], g_n_equation[5])
        ngroup = VGroup(g_n_equation[0])

        self.play(
            HighlightWithRect(ngroup),
        )
        self.wait(0.5)
        self.play(
            HighlightWithRect(g_n_equation[2]),
        )
        self.wait(0.5)
        self.play(Indicate(g_n_equation[4], scale_factor=1.5, color=SPECIAL_FUNC_COLOR))

        self.wait(0.5)
        self.play(
            HighlightWithRect(g_n_equation[5])
        )
        

        g3_sym = MathTex("g_3", font_size=42).set_color(PRIMARY_COLOR).to_edge(DOWN).shift(1.5*UP).shift(5*RIGHT)
        g3_sym_box = SurroundingRectangle(g3_sym, color=PRIMARY_COLOR, buff=0.1)
        g3_sym_box.set_stroke(opacity=0.5, width=1)

        g2_sym = MathTex("g_2", font_size=42).set_color(PRIMARY_COLOR).next_to(g3_sym_box, LEFT, buff=2)
        g2_sym_box = SurroundingRectangle(g2_sym, color=PRIMARY_COLOR, buff=0.1)
        g2_sym_box.set_stroke(opacity=0.5, width=1)

        arrow_g2_g3 = Arrow(start=g2_sym_box.get_right(), end=g3_sym_box.get_left(), buff=0.1, color=BLACK, stroke_width=4)

        g1_sym = MathTex("g_1=r_{tan}", font_size=42).set_color(PRIMARY_COLOR).next_to(g2_sym_box, LEFT, buff=2)
        g1_sym_box = SurroundingRectangle(g1_sym, color=PRIMARY_COLOR, buff=0.1)
        g1_sym_box.set_stroke(opacity=0.5, width=1)

        arrow_g1_g2 = Arrow(start=g1_sym_box.get_right(), end=g2_sym_box.get_left(), buff=0.1, color=BLACK, stroke_width=4)

        g0_sym = MathTex("g_0=f(x_0)", font_size=42).set_color(PRIMARY_COLOR).next_to(g1_sym_box, LEFT, buff=2)
        g0_sym_box = SurroundingRectangle(g0_sym, color=PRIMARY_COLOR, buff=0.1)
        g0_sym_box.set_stroke(opacity=0.5, width=1)

        arrow_g0_g1 = Arrow(start=g0_sym_box.get_right(), end=g1_sym_box.get_left(), buff=0.1, color=BLACK, stroke_width=4)

        self.wait(13)

        self.play(
            HighlightWithRect(ngroup),
        )
        self.wait(1.2)
        self.play(
            HighlightWithRect(n_1_group),
        )

        self.wait(2)
        relacao_de_recursividade = Text("Relação de Recursividade").set_color(PRIMARY_COLOR).next_to(g_n_equation, UP, buff=1).scale(0.75)
        self.play(Write(relacao_de_recursividade))
        self.wait(9)
 
        self.play(
            FadeIn(g3_sym_box, g3_sym)
        )
        self.wait(1)

        self.play(
            FadeIn(g2_sym_box, g2_sym),
            Create(arrow_g2_g3)
        )
        self.wait(2)

        self.play(
            FadeIn(g1_sym_box, g1_sym),
            Create(arrow_g1_g2)
        )
        self.wait(3.5)

        self.play(LaggedStart(
            Create(arrow_g0_g1),
            FadeIn(g0_sym_box, g0_sym),
            lag_ratio=0.6
        ))
        self.wait(15)

        self.play(FadeOut(g3_sym_box, g3_sym, g2_sym_box, g2_sym, arrow_g2_g3, g1_sym, g1_sym_box, arrow_g1_g2, g0_sym, g0_sym_box, arrow_g0_g1))

        self.wait(1)
        self.play(
            Write(n_eq_4),
            FadeOut(relacao_de_recursividade)
        )
        self.wait(10.5)

        self.play(HighlightWithRect(g_n_equation))
        self.wait(3.2)
        self.play(
            ReplacementTransform(g_n_equation[0], g_4_equation[0]),
            ReplacementTransform(g_n_equation[1], g_4_equation[1]),
            ReplacementTransform(g_n_equation[2], g_4_equation[2]),
            ReplacementTransform(g_n_equation[3], g_4_equation[3]),
            ReplacementTransform(g_n_equation[4], g_4_equation[4]),
            ReplacementTransform(g_n_equation[5], g_4_equation[5])
        )

        self.wait(2)
        self.play(
            FadeOut(eq_box, run_time=0.2),
            g3_equation.animate.scale(1.5625).next_to(g_4_equation, DOWN, aligned_edge=LEFT)
        )
        g_3_prime_equation.next_to(g3_equation, DOWN, aligned_edge=LEFT)
        u_g_3_prime_equation.next_to(g3_equation, DOWN, aligned_edge=LEFT)
        self.play(
            g3_equation[0].animate.set_x(g_3_prime_equation[0].get_x()),
            g3_equation[1].animate.set_x(g_3_prime_equation[1].get_x()),
            g3_equation[2].animate.set_x(g_3_prime_equation[2].get_x()),
            g3_equation[3].animate.set_x(g_3_prime_equation[3].get_x()),
            g3_equation[4].animate.set_x(g_3_prime_equation[4].get_x()),
            g3_equation[5].animate.set_x(g_3_prime_equation[5].get_x()),
            g3_equation[6].animate.set_x(g_3_prime_equation[6].get_x()),
            g3_equation[7].animate.set_x(g_3_prime_equation[7].get_x()),
            g3_equation[8].animate.set_x(g_3_prime_equation[8].get_x()),
            g3_equation[9].animate.set_x(g_3_prime_equation[9].get_x()),
            g3_equation[10].animate.set_x(g_3_prime_equation[10].get_x()),
            g3_equation[11].animate.set_x(g_3_prime_equation[11].get_x())
        )
        self.wait(1.5)
        
        self.play(LaggedStart(
            FadeIn(g_3_prime_equation[0], shift=DOWN),
            FadeIn(g_3_prime_equation[1], shift=DOWN),
            FadeIn(g_3_prime_equation[2], shift=DOWN),
            FadeIn(g_3_prime_equation[3], shift=DOWN),
            FadeIn(g_3_prime_equation[4], shift=DOWN),
            FadeIn(g_3_prime_equation[5], shift=DOWN),
            FadeIn(g_3_prime_equation[6], shift=DOWN),
            FadeIn(g_3_prime_equation[7], shift=DOWN),
            FadeIn(g_3_prime_equation[8], shift=DOWN),
            FadeIn(g_3_prime_equation[9], shift=DOWN),
            FadeIn(g_3_prime_equation[10], shift=DOWN),
            FadeIn(g_3_prime_equation[11], shift=DOWN),
            lag_ratio=0.2
        ))
        self.wait(1)

        g_3_prime_equation_copy = g_3_prime_equation.copy()
        g_3_prime_equation_copy[2].align_to(g3_equation[5], RIGHT)
        g_3_prime_equation_copy[3].set_x(g3_equation[6].get_x())
        g_3_prime_equation_copy[4].align_to(g3_equation[7], LEFT)
        g_3_prime_equation_copy[5].align_to(g3_equation[8], LEFT)
        g_3_prime_equation_copy[6].align_to(g3_equation[9], LEFT)

        g_3_prime_equation_copy[7].next_to(g_3_prime_equation_copy[6], RIGHT, buff=0.1)
        g_3_prime_equation_copy[8].next_to(g_3_prime_equation_copy[7], RIGHT, buff=0.1)
        g_3_prime_equation_copy[9].next_to(g_3_prime_equation_copy[8], RIGHT, buff=0.1)
        g_3_prime_equation_copy[10].next_to(g_3_prime_equation_copy[9], RIGHT, buff=0.1)
        g_3_prime_equation_copy[11].next_to(g_3_prime_equation_copy[10], RIGHT, buff=0.1)

        u_g_3_prime_equation.move_to(g_3_prime_equation_copy, aligned_edge=LEFT)
        u_g_3_prime_equation[3].move_to(g_3_prime_equation_copy[2])
        u_g_3_prime_equation[2].align_to(g3_equation[4], RIGHT)
        u_g_3_prime_equation[4].move_to(g_3_prime_equation_copy[3])
        u_g_3_prime_equation[5].align_to(g_3_prime_equation_copy[4], LEFT)
        u_g_3_prime_equation[6].align_to(g_3_prime_equation_copy[5], RIGHT)
        u_g_3_prime_equation[7].move_to(g_3_prime_equation_copy[6])
        u_g_3_prime_equation[8].align_to(g_3_prime_equation_copy[7], LEFT)
        u_g_3_prime_equation[9].align_to(g_3_prime_equation_copy[8], RIGHT)
        u_g_3_prime_equation[10].move_to(g_3_prime_equation_copy[9])
        u_g_3_prime_equation[11].move_to(g_3_prime_equation_copy[10])
        u_g_3_prime_equation[12].move_to(g_3_prime_equation_copy[11])

        self.play(
            g_3_prime_equation[2].animate.set_x(g_3_prime_equation_copy[2].get_x()),
            g_3_prime_equation[3].animate.set_x(g_3_prime_equation_copy[3].get_x()),
            g_3_prime_equation[4].animate.set_x(g_3_prime_equation_copy[4].get_x()),
            g_3_prime_equation[5].animate.set_x(g_3_prime_equation_copy[5].get_x()),
            g_3_prime_equation[6].animate.set_x(g_3_prime_equation_copy[6].get_x()),
            g_3_prime_equation[7].animate.set_x(g_3_prime_equation_copy[7].get_x()),
            g_3_prime_equation[8].animate.set_x(g_3_prime_equation_copy[8].get_x()),
            g_3_prime_equation[9].animate.set_x(g_3_prime_equation_copy[9].get_x()),
            g_3_prime_equation[10].animate.set_x(g_3_prime_equation_copy[10].get_x()),
            g_3_prime_equation[11].animate.set_x(g_3_prime_equation_copy[11].get_x()),
            g3_equation[10].animate.align_to(g_3_prime_equation_copy[7], RIGHT),
            g3_equation[11].animate.align_to(g_3_prime_equation_copy[8], RIGHT)
        )

        u_g_3_prime_equation[0].align_to(g3_equation[0], RIGHT)
        u_g_3_prime_equation[1].align_to(g3_equation[1], RIGHT)
        self.wait(1)
        self.play(
            FadeIn(u_g_3_prime_equation[2], shift=UP),
            ReplacementTransform(g_3_prime_equation[0], u_g_3_prime_equation[0]),
            ReplacementTransform(g_3_prime_equation[1], u_g_3_prime_equation[1]),
            ReplacementTransform(g_3_prime_equation[2], u_g_3_prime_equation[3]),
            ReplacementTransform(g_3_prime_equation[3], u_g_3_prime_equation[4]),
            ReplacementTransform(g_3_prime_equation[4], u_g_3_prime_equation[5]),
            ReplacementTransform(g_3_prime_equation[5], u_g_3_prime_equation[6]),
            ReplacementTransform(g_3_prime_equation[6], u_g_3_prime_equation[7]),
            ReplacementTransform(g_3_prime_equation[7], u_g_3_prime_equation[8]),
            ReplacementTransform(g_3_prime_equation[8], u_g_3_prime_equation[9]),
            ReplacementTransform(g_3_prime_equation[9], u_g_3_prime_equation[10]),
            ReplacementTransform(g_3_prime_equation[10], u_g_3_prime_equation[11]),
            ReplacementTransform(g_3_prime_equation[11], u_g_3_prime_equation[12]),   
        )

        plus_left.next_to(g3_equation[0], DOWN)
        plus_right.next_to(VGroup(g3_equation[7], g3_equation[8]), DOWN)

        u_g_3_prime_equation_aux = u_g_3_prime_equation.copy()
        u_g_3_prime_equation_aux.next_to(u_g_3_prime_equation, DOWN)

        self.play(
            FadeIn(plus_left, shift=RIGHT),
            FadeIn(plus_right, shift=RIGHT),
            Transform(u_g_3_prime_equation[0], u_g_3_prime_equation_aux[0]),
            Transform(u_g_3_prime_equation[1], u_g_3_prime_equation_aux[1]),
            Transform(u_g_3_prime_equation[2], u_g_3_prime_equation_aux[2]),
            Transform(u_g_3_prime_equation[3], u_g_3_prime_equation_aux[3]),
            Transform(u_g_3_prime_equation[4], u_g_3_prime_equation_aux[4]),
            Transform(u_g_3_prime_equation[5], u_g_3_prime_equation_aux[5]),
            Transform(u_g_3_prime_equation[6], u_g_3_prime_equation_aux[6]),
            Transform(u_g_3_prime_equation[7], u_g_3_prime_equation_aux[7]),
            Transform(u_g_3_prime_equation[8], u_g_3_prime_equation_aux[8]),
            Transform(u_g_3_prime_equation[9], u_g_3_prime_equation_aux[9]),
            Transform(u_g_3_prime_equation[10], u_g_3_prime_equation_aux[10]),
            Transform(u_g_3_prime_equation[11], u_g_3_prime_equation_aux[11]),
            Transform(u_g_3_prime_equation[12], u_g_3_prime_equation_aux[12])
        )

        bar_line = Line(u_g_3_prime_equation_aux[0].get_bottom(), u_g_3_prime_equation_aux[12].get_bottom(), color=PRIMARY_COLOR)
        bar_line.set_length(u_g_3_prime_equation_aux.width+0.5).next_to(u_g_3_prime_equation_aux, DOWN)

        demonstration = VGroup(n_eq_4, g_4_equation, g3_equation, u_g_3_prime_equation, plus_left, plus_right, bar_line)

        self.play(Create(bar_line))
        self.play(demonstration.animate.move_to(ORIGIN))

        g4_full.next_to(bar_line, DOWN).align_to(u_g_3_prime_equation, RIGHT)
        g4_full_copy = g4_full.copy()
        g4_full[0].align_to(g3_equation[0], RIGHT)
        g4_full[1].align_to(g3_equation[1], RIGHT)
        g4_full[2].align_to(g3_equation[2], RIGHT)
        g4_full[3].align_to(g3_equation[3], LEFT)
        g4_full[4].align_to(g3_equation[6], LEFT)
        g4_full[5].align_to(g3_equation[9], LEFT)
        g4_full[6].align_to(u_g_3_prime_equation[10], LEFT)
        self.play(LaggedStart(
            FadeIn(g4_full[0], g4_full[1], shift=DOWN),
            FadeIn(g4_full[2], shift=DOWN),
            FadeIn(g4_full[3], shift=DOWN),
            FadeIn(g4_full[4], shift=DOWN),
            FadeIn(g4_full[5], shift=DOWN),
            FadeIn(g4_full[6], shift=DOWN),
            lag_ratio=0.8
        ))

        # "g_4(x_0+4u)", "=", "f(x_0)", "+4uf'(x_0)", "+6u^2f^2(x_0)","+4u^3f^3(x_0)","+u^4f^4(x)"
        g3_full = MathTex("g_3(x_0+3u)", "=", "f(x_0)", "+","3uf^1(x_0)", "+","3u^2f^2(x_0)","+","u^3f^3(x_0)", font_size=24).set_color(PRIMARY_COLOR).scale(1.25).next_to(g4_full_copy, UP, aligned_edge=LEFT)
        g2_full = MathTex("g_2(x_0+2u)", "=", "f(x_0)", "+","2uf^1(x_0)", "+","u^2f^2(x_0)", font_size=24).set_color(PRIMARY_COLOR).scale(1.25).next_to(g3_full, UP, aligned_edge=LEFT)
        g1_full = MathTex("g_1(x_0+u)", "=", "f(x_0)", "+","uf^1(x_0)", font_size=24).set_color(PRIMARY_COLOR).scale(1.25).next_to(g2_full, UP, aligned_edge=LEFT)

        g_group_aux = VGroup(g4_full_copy, g3_full, g2_full, g1_full)
        g_group_aux.move_to(ORIGIN)

        g1_full[1].align_to(g2_full[1], RIGHT)
        g1_full[2].align_to(g2_full[2], RIGHT)
        g1_full[3].align_to(g2_full[3], RIGHT)
        g1_full[4].align_to(g2_full[4], RIGHT)

        g2_full[6].align_to(g3_full[6], RIGHT)

        g3_full[7].align_to(g4_full[5], LEFT)
        g3_full[8].align_to(g4_full[5], RIGHT)

        g4_full_copy[4].align_to(g3_full[5], LEFT)
        g4_full_copy[5].align_to(g3_full[8], RIGHT)
        g4_full_copy[6].next_to(g4_full_copy[5], RIGHT, buff=0.1)

        self.wait(1)
        self.play(
            FadeOut(demonstration),
            TransformMatchingTex(g4_full,g4_full_copy)
        )

        self.play(HighlightWithRect(g4_full_copy))

        self.wait(6)

        self.play(LaggedStart(
            Write(g3_full),
            Write(g2_full),
            Write(g1_full),
            lag_ratio = 0.5
        ))

        # "g_4(x_0+4u)", "=", "f(x_0)", "+4uf'(x_0)", "+6u^2f^2(x_0)","+4u^3f^3(x_0)","+u^4f^4(x)"
        g4_full_highlight = MathTex("g_4(x_0+4u)", "=", "1f(x_0)", "+4uf^1(x_0)", "+6u^2f^2(x_0)","+4u^3f^3(x_0)","+1u^4f^4(x)", font_size=24).set_color(PRIMARY_COLOR).scale(1.25).move_to(g4_full_copy, aligned_edge=LEFT)
        g3_full_highlight = MathTex("g_3(x_0+3u)", "=", "1f(x_0)", "+","3uf^1(x_0)", "+","3u^2f^2(x_0)","+","1u^3f^3(x_0)", font_size=24).set_color(PRIMARY_COLOR).scale(1.25).move_to(g3_full, aligned_edge=LEFT)
        g2_full_highlight = MathTex("g_2(x_0+2u)", "=", "1f(x_0)", "+","2uf^1(x_0)", "+","1u^2f^2(x_0)", font_size=24).set_color(PRIMARY_COLOR).scale(1.25).move_to(g2_full, aligned_edge=LEFT)
        g1_full_highlight = MathTex("g_1(x_0+u)", "=", "1f(x_0) ", "+","1uf^1(x_0)", font_size=24).set_color(PRIMARY_COLOR).scale(1.25).move_to(g1_full, aligned_edge=LEFT)

        g4_full_highlight_power = MathTex("g_4(x_0+4u)", "=", "u^0f^0(x_0)", "+4u^1f^1(x_0)", "+6u^2f^2(x_0)","+4u^3f^3(x_0)","+1u^4f^4(x)", font_size=24).set_color(PRIMARY_COLOR).scale(1.25).move_to(g4_full_copy, aligned_edge=LEFT)
        g3_full_highlight_power = MathTex("g_3(x_0+3u)", "=", "u^0f^0(x_0)", "+","3u^1f^1(x_0)", "+","3u^2f^2(x_0)","+","1u^3f^3(x_0)", font_size=24).set_color(PRIMARY_COLOR).scale(1.25).move_to(g3_full, aligned_edge=LEFT)
        g2_full_highlight_power = MathTex("g_2(x_0+2u)", "=", "u^0f^0(x_0)", "+","2u^1f^1(x_0)", "+","1u^2f^2(x_0)", font_size=24).set_color(PRIMARY_COLOR).scale(1.25).move_to(g2_full, aligned_edge=LEFT)
        g1_full_highlight_power = MathTex("g_1(x_0+u)", "=", "u^0f^0(x_0) ", "+","u^1f^1(x_0)", font_size=24).set_color(PRIMARY_COLOR).scale(1.25).move_to(g1_full, aligned_edge=LEFT)

        self.wait(8)
        gs = [g1_full, g2_full, g3_full, g4_full_copy]
        fx0_rect = [SurroundingRectangle(gi[2], color=SPECIAL_FUNC_COLOR, buff=0.1).set_stroke(opacity=1, width=2) for gi in gs]
        highlight_on = FadeIn(*fx0_rect)
        highlight_off = FadeOut(*fx0_rect)
        self.play(highlight_on)
        self.wait(0.5)
        self.play(highlight_off)

        g1_full_highlight_power[1].align_to(g2_full_highlight_power[1], RIGHT)
        g1_full_highlight_power[2].align_to(g2_full_highlight_power[2], RIGHT)  
        g1_full_highlight_power[3].align_to(g2_full_highlight_power[3], RIGHT)
        g1_full_highlight_power[4].align_to(g2_full_highlight_power[4], RIGHT)

        g2_full_highlight_power[6].align_to(g3_full_highlight_power[6], RIGHT)

        g3_full_highlight_power[7].align_to(g4_full_highlight_power[5], LEFT)
        g3_full_highlight_power[8].align_to(g4_full_highlight_power[5], RIGHT)

        g4_full_highlight_power[4].align_to(g3_full_highlight_power[5], LEFT)
        g4_full_highlight_power[5].align_to(g3_full_highlight_power[8], RIGHT)
        g4_full_highlight_power[6].next_to(g4_full_highlight_power[5], RIGHT, buff=0.1)

        self.wait(5)
        
        g1_transform_animations = []
        for g1, g1_hi in zip(g1_full, g1_full_highlight_power):
            g1_transform_animations.append(ReplacementTransform(g1,g1_hi))

        g2_transform_animations = []
        for g2, g2_hi in zip(g2_full, g2_full_highlight_power):
            g2_transform_animations.append(ReplacementTransform(g2,g2_hi))

        g3_transform_animations = []
        for g3, g3_hi in zip(g3_full, g3_full_highlight_power):
            g3_transform_animations.append(ReplacementTransform(g3,g3_hi))

        g4_transform_animations = []
        for g4, g4_hi in zip(g4_full_copy, g4_full_highlight_power):
            g4_transform_animations.append(ReplacementTransform(g4,g4_hi))


        self.play(LaggedStart(
            AnimationGroup(*g1_transform_animations),
            AnimationGroup(*g2_transform_animations),
            AnimationGroup(*g3_transform_animations),
            AnimationGroup(*g4_transform_animations),
            lag_ratio=0.2
        ))

        power_highlight = [
            [
                g4_full_highlight_power[2][1], g4_full_highlight_power[3][3], g4_full_highlight_power[4][3], g4_full_highlight_power[5][3], g4_full_highlight_power[6][3],
                g4_full_highlight_power[2][3], g4_full_highlight_power[3][5], g4_full_highlight_power[4][5], g4_full_highlight_power[5][5], g4_full_highlight_power[6][5]
            ],
            [
                g3_full_highlight_power[2][1], g3_full_highlight_power[4][2], g3_full_highlight_power[6][2], g3_full_highlight_power[8][2],
                g3_full_highlight_power[2][3], g3_full_highlight_power[4][4], g3_full_highlight_power[6][4], g3_full_highlight_power[8][4]
            ],
            [
                g2_full_highlight_power[2][1], g2_full_highlight_power[4][2], g2_full_highlight_power[6][2],
                g2_full_highlight_power[2][3], g2_full_highlight_power[4][4], g2_full_highlight_power[6][4]
            ],
            [
                g1_full_highlight_power[2][1], g1_full_highlight_power[4][1],
                g1_full_highlight_power[2][3], g1_full_highlight_power[4][3]
            ]
        ]

        power_highlight_rects = [
            VGroup(*[SurroundingRectangle(highlighted_mob, color=SPECIAL_FUNC_COLOR, buff=0.1).set_stroke(opacity=1, width=2) for highlighted_mob in highligh_rect_group]) for highligh_rect_group in power_highlight        
        ]

        self.wait(1.5)


        power_highlight_on = [FadeIn(power_highlight_rect) for power_highlight_rect in power_highlight_rects]
        power_highlight_off = [FadeOut(power_highlight_rect) for power_highlight_rect in power_highlight_rects]

        self.play(LaggedStart(*power_highlight_on, lag_ratio=0.2))
        self.wait(1)
        self.play(LaggedStart(*power_highlight_off, lag_ratio=0.2))


        self.wait(4)

        g1_full_highlight[1].align_to(g2_full_highlight[1], RIGHT)
        g1_full_highlight[2].align_to(g2_full_highlight[2], RIGHT)
        g1_full_highlight[3].align_to(g2_full_highlight[3], RIGHT)
        g1_full_highlight[4].align_to(g2_full_highlight[4], RIGHT)

        g2_full_highlight[6].align_to(g3_full_highlight[6], RIGHT)

        g3_full_highlight[7].align_to(g4_full_highlight[5], LEFT)
        g3_full_highlight[8].align_to(g4_full_highlight[5], RIGHT)

        g4_full_highlight[4].align_to(g3_full_highlight[5], LEFT)
        g4_full_highlight[5].align_to(g3_full_highlight[8], RIGHT)
        g4_full_highlight[6].next_to(g4_full_highlight[5], RIGHT, buff=0.1)

        g1_transform_animations = []
        for g1, g1_hi in zip(g1_full_highlight_power, g1_full_highlight):
            g1_transform_animations.append(ReplacementTransform(g1,g1_hi))

        g2_transform_animations = []
        for g2, g2_hi in zip(g2_full_highlight_power, g2_full_highlight):
            g2_transform_animations.append(ReplacementTransform(g2,g2_hi))

        g3_transform_animations = []
        for g3, g3_hi in zip(g3_full_highlight_power, g3_full_highlight):
            g3_transform_animations.append(ReplacementTransform(g3,g3_hi))

        g4_transform_animations = []
        for g4, g4_hi in zip(g4_full_highlight_power, g4_full_highlight):
            g4_transform_animations.append(ReplacementTransform(g4,g4_hi))

        self.play(LaggedStart(
            AnimationGroup(*g1_transform_animations),
            AnimationGroup(*g2_transform_animations),
            AnimationGroup(*g3_transform_animations),
            AnimationGroup(*g4_transform_animations),
            lag_ratio=0.2
        ))

        self.wait(4)
        self.play(
            g4_full_highlight[2][0].animate.set_color(SPECIAL_FUNC_COLOR).set_opacity(1),
            g4_full_highlight[3][1].animate.set_color(SPECIAL_FUNC_COLOR).set_opacity(1),
            g4_full_highlight[4][1].animate.set_color(SPECIAL_FUNC_COLOR).set_opacity(1),
            g4_full_highlight[5][1].animate.set_color(SPECIAL_FUNC_COLOR).set_opacity(1),
            g4_full_highlight[6][1].animate.set_color(SPECIAL_FUNC_COLOR).set_opacity(1),
            g3_full_highlight[2][0].animate.set_color(SPECIAL_FUNC_COLOR).set_opacity(1),
            g3_full_highlight[4][0].animate.set_color(SPECIAL_FUNC_COLOR).set_opacity(1),
            g3_full_highlight[6][0].animate.set_color(SPECIAL_FUNC_COLOR).set_opacity(1),
            g3_full_highlight[8][0].animate.set_color(SPECIAL_FUNC_COLOR).set_opacity(1),
            g2_full_highlight[2][0].animate.set_color(SPECIAL_FUNC_COLOR).set_opacity(1),
            g2_full_highlight[4][0].animate.set_color(SPECIAL_FUNC_COLOR).set_opacity(1),
            g2_full_highlight[6][0].animate.set_color(SPECIAL_FUNC_COLOR).set_opacity(1),
            g1_full_highlight[2][0].animate.set_color(SPECIAL_FUNC_COLOR).set_opacity(1),
            g1_full_highlight[4][0].animate.set_color(SPECIAL_FUNC_COLOR).set_opacity(1)
        )

        g4_full_highlight_20 = g4_full_highlight[2][0].copy()
        g4_full_highlight_31 = g4_full_highlight[3][1].copy()
        g4_full_highlight_41 = g4_full_highlight[4][1].copy()
        g4_full_highlight_51 = g4_full_highlight[5][1].copy()
        g4_full_highlight_61 = g4_full_highlight[6][1].copy()
        g3_full_highlight_20 = g3_full_highlight[2][0].copy()
        g3_full_highlight_40 = g3_full_highlight[4][0].copy()
        g3_full_highlight_60 = g3_full_highlight[6][0].copy()
        g3_full_highlight_80 = g3_full_highlight[8][0].copy()
        g2_full_highlight_20 = g2_full_highlight[2][0].copy()
        g2_full_highlight_40 = g2_full_highlight[4][0].copy()
        g2_full_highlight_60 = g2_full_highlight[6][0].copy()
        g1_full_highlight_20 = g1_full_highlight[2][0].copy()
        g1_full_highlight_40 = g1_full_highlight[4][0].copy()

        self.add(
            g4_full_highlight_20, g4_full_highlight_31, g4_full_highlight_41, g4_full_highlight_51,
            g4_full_highlight_61, g3_full_highlight_20, g3_full_highlight_40, g3_full_highlight_60,
            g3_full_highlight_80, g2_full_highlight_20, g2_full_highlight_40, g2_full_highlight_60,
            g1_full_highlight_20, g1_full_highlight_40
        )
        self.wait(1)
        
        self.play(
            g1_full_highlight.animate.set_opacity(0),
            g2_full_highlight.animate.set_opacity(0),
            g3_full_highlight.animate.set_opacity(0),
            g4_full_highlight.animate.set_opacity(0)
        )
        self.wait(2)

        group1 = VGroup(g1_full_highlight_20, g1_full_highlight_40)
        group2 = VGroup(g2_full_highlight_20, g2_full_highlight_40, g2_full_highlight_60)
        group3 = VGroup(g3_full_highlight_20, g3_full_highlight_40, g3_full_highlight_60, g3_full_highlight_80)
        group4 = VGroup(g4_full_highlight_20, g4_full_highlight_31, g4_full_highlight_41, g4_full_highlight_51, g4_full_highlight_61)

        self.play(
            group1.animate.arrange(RIGHT, buff=0.5, center=False).set_x(0).set_color(BLACK),
            group2.animate.arrange(RIGHT, buff=0.5, center=False).set_x(0).set_color(BLACK),
            group3.animate.arrange(RIGHT, buff=0.5, center=False).set_x(0).set_color(BLACK),
            group4.animate.arrange(RIGHT, buff=0.5, center=False).set_x(0).set_color(BLACK)
        )
        self.wait(3)

        pascal_triangle_label = Text("Triângulo de Pascal", font_size=32).set_color(PRIMARY_COLOR)
        pascal_triangle_label.to_edge(UP).shift(DOWN * 1.5)
        pascal_triangle = VGroup(group1, group2, group3, group4)
        self.play(LaggedStart(
            pascal_triangle.animate.next_to(pascal_triangle_label, 3*DOWN),
            FadeIn(pascal_triangle_label),
            lag_ratio=0.2
        ))

        self.wait(12)

        highlight_example = [g2_full_highlight_20, g2_full_highlight_40]
        highligh_res = g3_full_highlight_40
        aux_group = VGroup(g2_full_highlight_20, g2_full_highlight_40)
        example_plus_sign = MathTex("+",font_size=30).set_color(PRIMARY_COLOR).move_to(aux_group)
        highligh_example_rects = [SurroundingRectangle(ex, color=SPECIAL_FUNC_COLOR, buff=0.1).set_stroke(opacity=1, width=2) for ex in highlight_example]
        highligh_example_rect_res = SurroundingRectangle(highligh_res, color=TANGENT_LINE_BLUE, buff=0.1).set_stroke(opacity=1, width=2)

        self.play(FadeIn(highligh_example_rect_res))
        self.wait(1)
        self.play(FadeIn(*highligh_example_rects))
        self.play(FadeIn(example_plus_sign))
        self.wait(1)
        self.play(FadeOut(*highligh_example_rects, example_plus_sign, highligh_example_rect_res))
        self.wait(1)
 
        g5_coefs = [1, 5, 10, 10, 5, 1]
        group5 = VGroup(*[MathTex(f"{coef}",font_size=30).set_color(PRIMARY_COLOR).next_to(group4, 1.5*DOWN) for coef in g5_coefs])
        group5.arrange(RIGHT, buff=0.5, center=False).set_x(0).set_color(BLACK)

        left01 = MathTex("0",font_size=30).set_color(PRIMARY_COLOR).next_to(group1[0], LEFT, buff=0.5)
        right01 = MathTex("0",font_size=30).set_color(PRIMARY_COLOR).next_to(group1[1], RIGHT, buff=0.5)
        left02 = MathTex("0",font_size=30).set_color(PRIMARY_COLOR).next_to(group2[0], LEFT, buff=0.5)
        right02 = MathTex("0",font_size=30).set_color(PRIMARY_COLOR).next_to(group2[2], RIGHT, buff=0.5)
        left03 = MathTex("0",font_size=30).set_color(PRIMARY_COLOR).next_to(group3[0], LEFT, buff=0.5)
        right03 = MathTex("0",font_size=30).set_color(PRIMARY_COLOR).next_to(group3[3], RIGHT, buff=0.5)
        left04 = MathTex("0",font_size=30).set_color(PRIMARY_COLOR).next_to(group4[0], LEFT, buff=0.5)
        right04 = MathTex("0",font_size=30).set_color(PRIMARY_COLOR).next_to(group4[4], RIGHT, buff=0.5)
        left05 = MathTex("0",font_size=30).set_color(PRIMARY_COLOR).next_to(group5[0], LEFT, buff=0.5)
        right05 = MathTex("0",font_size=30).set_color(PRIMARY_COLOR).next_to(group5[5], RIGHT, buff=0.5)

        aux_groups = [
            VGroup(g4_full_highlight_20, g4_full_highlight_31),
            VGroup(g4_full_highlight_31, g4_full_highlight_41),
            VGroup(g4_full_highlight_41, g4_full_highlight_51),
            VGroup(g4_full_highlight_51, g4_full_highlight_61)
        ]
        
        highlight_rect_20 = SurroundingRectangle(g4_full_highlight_20, color=SPECIAL_FUNC_COLOR, buff=0.1).set_stroke(opacity=1, width=2)
        highlight_rect_31 = SurroundingRectangle(g4_full_highlight_31, color=SPECIAL_FUNC_COLOR, buff=0.1).set_stroke(opacity=1, width=2)
        highlight_rect_41 = SurroundingRectangle(g4_full_highlight_41, color=SPECIAL_FUNC_COLOR, buff=0.1).set_stroke(opacity=1, width=2)
        highlight_rect_51 = SurroundingRectangle(g4_full_highlight_51, color=SPECIAL_FUNC_COLOR, buff=0.1).set_stroke(opacity=1, width=2)
        highlight_rect_61 = SurroundingRectangle(g4_full_highlight_61, color=SPECIAL_FUNC_COLOR, buff=0.1).set_stroke(opacity=1, width=2)    

        aux_highlight_rect_group = [
            VGroup(highlight_rect_20, highlight_rect_31),
            VGroup(highlight_rect_31, highlight_rect_41),
            VGroup(highlight_rect_41, highlight_rect_51),
            VGroup(highlight_rect_51, highlight_rect_61)
        ]

        plus_signs = [MathTex("+",font_size=30).set_color(PRIMARY_COLOR).move_to(aux_group) for aux_group in aux_groups]
        results = [MathTex(f"{g5_coefs[i+1]}",font_size=30).set_color(PRIMARY_COLOR).next_to(plus_signs[i], DOWN) for i in range(0, 4)]

        results_rects = [SurroundingRectangle(res, color=TANGENT_LINE_BLUE, buff=0.1).set_stroke(opacity=1, width=2) for res in results]

        for i in range(0, 4):
            self.play(
                FadeIn(plus_signs[i]),
                FadeIn(aux_highlight_rect_group[i])
            )
            self.wait(0.25)
            self.play(FadeIn(results[i], results_rects[i]))
            self.wait(0.25)
            self.play(
                LaggedStart(
                    FadeOut(plus_signs[i], results_rects[i], aux_highlight_rect_group[i]),
                    ReplacementTransform(results[i], group5[i+1]),
                    lag_ratio=0.2
                )
            )
        
        zeroes = [
            VGroup(left01, right01),
            VGroup(left02, right02),
            VGroup(left03, right03),
            VGroup(left04, right04),
            VGroup(left05, right05)
        ]

        self.wait(1)
        self.play(
            LaggedStart(*[FadeIn(zero) for zero in zeroes], lag_ratio=0.2)
        )

        aux_groups_0 = [VGroup(left04, g4_full_highlight_20), VGroup(right04, g4_full_highlight_61)]

        plus_signs = [MathTex("+",font_size=30).set_color(PRIMARY_COLOR).move_to(aux_group) for aux_group in aux_groups_0]
        results = [MathTex("1",font_size=30).set_color(PRIMARY_COLOR).next_to(plus_sign, DOWN) for plus_sign in plus_signs]
        idx_1 = [0, 5]

        for i in range(0, 2):
            self.play(
                FadeIn(plus_signs[i])
            )
            self.wait(0.35)
            self.play(FadeIn(results[i]))
            self.wait(0.35)
            self.play(
                FadeOut(plus_signs[i]),
                ReplacementTransform(results[i], group5[idx_1[i]])
            )

        self.wait(1)
        self.play(
            LaggedStart(*[FadeOut(zero) for zero in zeroes], lag_ratio=0.2)
        )

        c_n_k = MathTex("{n \\choose k}", "=", "\\frac{n!}{k!(n-k)!}",font_size=32).set_color(PRIMARY_COLOR).next_to(group2, 6*RIGHT)
        self.wait(1)
        self.play(
            Write(c_n_k),
        )

        self.wait(0.5)
        self.play(HighlightWithRect(c_n_k))

        line_indicator_5 = Text("5", font_size=22, slant=ITALIC, color=SPECIAL_FUNC_COLOR).next_to(group5, 2*LEFT)
        line_indicator_4 = Text("4", font_size=22, slant=ITALIC, color=SPECIAL_FUNC_COLOR).move_to(line_indicator_5).set_y(group4.get_y())
        line_indicator_3 = Text("3", font_size=22, slant=ITALIC, color=SPECIAL_FUNC_COLOR).move_to(line_indicator_4).set_y(group3.get_y())
        line_indicator_2 = Text("2", font_size=22, slant=ITALIC, color=SPECIAL_FUNC_COLOR).move_to(line_indicator_3).set_y(group2.get_y())
        line_indicator_1 = Text("1", font_size=22, slant=ITALIC, color=SPECIAL_FUNC_COLOR).move_to(line_indicator_2).set_y(group1.get_y())        
        line_indicators = VGroup(line_indicator_1, line_indicator_2, line_indicator_3, line_indicator_4, line_indicator_5)

        self.wait(2)
        self.play(FadeIn(*line_indicators))
        self.play(Indicate(c_n_k[0][1], scale_factor=1.5, color=SPECIAL_FUNC_COLOR))
        self.wait(2)


        k_indicators = [
            VGroup(*[Text(f"{num}", font_size=16, slant=ITALIC, color=TANGENT_LINE_BLUE).next_to(group1[num], 0.5*UP) for num in range(0, 2)]),
            VGroup(*[Text(f"{num}", font_size=16, slant=ITALIC, color=TANGENT_LINE_BLUE).next_to(group2[num], 0.5*UP) for num in range(0, 3)]),
            VGroup(*[Text(f"{num}", font_size=16, slant=ITALIC, color=TANGENT_LINE_BLUE).next_to(group3[num], 0.5*UP) for num in range(0, 4)]),
            VGroup(*[Text(f"{num}", font_size=16, slant=ITALIC, color=TANGENT_LINE_BLUE).next_to(group4[num], 0.5*UP) for num in range(0, 5)]),
            VGroup(*[Text(f"{num}", font_size=16, slant=ITALIC, color=TANGENT_LINE_BLUE).next_to(group5[num], 0.5*UP) for num in range(0, 6)])
        ]

        self.play(Indicate(c_n_k[0][2], scale_factor=1.5, color=TANGENT_LINE_BLUE))
        self.wait(1.5)
        self.play(LaggedStart(
            FadeIn(k_indicators[0]),
            FadeIn(k_indicators[1]),
            FadeIn(k_indicators[2]),
            FadeIn(k_indicators[3]),
            FadeIn(k_indicators[4]),
            lag_ratio=0.2
        ))

        self.wait(2)
        self.play(FadeIn(highlight_rect_41))
        self.wait(0.5)
        self.play(FadeOut(highlight_rect_41))
        self.wait(0.5)

        self.play(HighlightWithRect(line_indicators[3]))
        self.play(HighlightWithRect(k_indicators[3][2]))

        self.wait(1)

        n_eq_4 = MathTex("n=4",font_size=32).set_color(PRIMARY_COLOR).next_to(c_n_k, DOWN, aligned_edge=LEFT)
        k_eq_2 = MathTex("k=2",font_size=32).set_color(PRIMARY_COLOR).next_to(n_eq_4, DOWN, aligned_edge=LEFT)

        self.play(Write(n_eq_4))
        self.wait(0.2)
        self.play(Write(k_eq_2))

        c_4_k = MathTex("{4 \\choose k}", "=", "\\frac{4!}{k!(4-k)!}",font_size=32).set_color(PRIMARY_COLOR).move_to(c_n_k, aligned_edge=LEFT)
        c_4_2 = MathTex("{4 \\choose 2}", "=", "\\frac{4!}{2!(4-2)!}",font_size=32).set_color(PRIMARY_COLOR).move_to(c_n_k, aligned_edge=LEFT)
        c_4_2_0 = MathTex("{4 \\choose 2}", "=", "\\frac{4!}{2!2!}",font_size=32).set_color(PRIMARY_COLOR).move_to(c_n_k, aligned_edge=LEFT)
        c_4_2_1 = MathTex("{4 \\choose 2}", "=", "\\frac{4\\cdot 3\\cdot 2!}{2!2!}",font_size=32).set_color(PRIMARY_COLOR).move_to(c_n_k, aligned_edge=LEFT)
        c_4_2_2 = MathTex("{4 \\choose 2}", "=", "\\frac{4\\cdot 3}{2!}",font_size=32).set_color(PRIMARY_COLOR).move_to(c_n_k, aligned_edge=LEFT)
        c_4_2_3 = MathTex("{4 \\choose 2}", "=", "6",font_size=32).set_color(PRIMARY_COLOR).move_to(c_n_k, aligned_edge=LEFT)

        c_array = [c_n_k, c_4_k, c_4_2, c_4_2_0, c_4_2_1, c_4_2_2, c_4_2_3]

        for i in range(0, len(c_array)-1):
            self.play(
                ReplacementTransform(c_array[i][0], c_array[i+1][0]),
                ReplacementTransform(c_array[i][1], c_array[i+1][1]),
                ReplacementTransform(c_array[i][2], c_array[i+1][2]),
            )
            self.wait(0.5)

        highlight_6_rect = SurroundingRectangle(c_4_2_3[2], color=TANGENT_LINE_BLUE, buff=0.1).set_stroke(opacity=1, width=2)
        highligh_rects = VGroup(highlight_rect_41, highlight_6_rect)

        self.wait(1)
        self.play(FadeIn(highligh_rects))
        self.wait(0.5)
        self.play(FadeOut(highligh_rects))
        self.wait(0.5)

        self.play(FadeOut(*line_indicators), FadeOut(*k_indicators))
        self.wait(8)

        self.play(FadeOut(
            group1, group2, group3, group4, group5, pascal_triangle_label, n_eq_4, k_eq_2, c_4_2_3
        ))
        self.wait(1)