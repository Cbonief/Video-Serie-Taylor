from manim import *
from utils import *
import numpy as np

# Toggle Dark Mode here
DARK_MODE = False

# Define the color palettes
if DARK_MODE:
    BG_COLOR = "#000000"
    PRIMARY_COLOR = WHITE
    ARROW_COLOR = GRAY_E  # Arrow color in dark mode
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


class how_to_go_beyond(Scene):
    def construct(self):
        # Set the background color of the scene
        self.camera.background_color = BG_COLOR

        # === Step 1: Title and Initial Approximation ===

        # Title text "Como ir além?" ("How to go beyond?")
        do_better_label = Text("Como ir além?").set_color(PRIMARY_COLOR)
        do_better_label.to_edge(UP).shift(DOWN * 1.5)  # Position at the top with downward shift

        # Approximation equation "5.0625 ≈ 5"
        aprox_sqrt_comparison_squared_simplified = MathTex(
            "5.0625", "\\approx", "5", font_size=24
        ).set_color(PRIMARY_COLOR).scale(1.5625).next_to(do_better_label, DOWN, buff=1)

        # Add approximation equation to the scene (appears immediately)
        self.add(aprox_sqrt_comparison_squared_simplified, do_better_label)

        self.wait(1)

        # Prepare a smaller version of the title to move to the corner
        aux_label = do_better_label.copy().scale(0.5).to_corner(UR, buff=0.5)

        # Create a rectangle around the corner title
        title_box = SurroundingRectangle(aux_label, color=PRIMARY_COLOR, buff=0.1)
        title_box.set_stroke(opacity=0.5, width=1)

        # Animate shrinking the title, creating the box, and fading out the initial approximation
        self.play(LaggedStart(
            AnimationGroup(
                do_better_label.animate.scale(0.5).to_corner(UR, buff=0.5),
                FadeOut(aprox_sqrt_comparison_squared_simplified)
            ),
            Create(title_box),
            lag_ratio=0.8
        ))

        # === Step 2: Advantages and Disadvantages Labels ===

        # Create "Vantagem" (Advantage) and "Desvantagem" (Disadvantage) labels
        vantagem_label = Text("Vantagem", font_size=32).set_color(PRIMARY_COLOR)
        desvantagem_label = Text("Desvantagem", font_size=32).set_color(PRIMARY_COLOR)

        # Arrange labels side by side at the top
        labels = VGroup(vantagem_label, desvantagem_label).arrange(RIGHT, buff=3.5).to_edge(UP).shift(DOWN * 1.5)

        # Create description under "Vantagem"
        local_label = Text("Bom comportamento local", font_size=24, t2w={"local": BOLD}).set_color(PRIMARY_COLOR)
        local_label.next_to(vantagem_label, DOWN, buff=1)

        # Create description under "Desvantagem"
        do_what_label = Text("Sem respeito pelo resto da função", font_size=24, t2w={"local": BOLD}).set_color(PRIMARY_COLOR)
        do_what_label.next_to(desvantagem_label, DOWN, buff=1)

        # Animate the appearance of the "Vantagem" section
        self.play(FadeIn(vantagem_label, local_label))
        self.wait(1)

        # Add arrow from advantage to disadvantage
        arrow = Arrow(
            start=local_label.get_right(),
            end=do_what_label.get_left(),
            color=ARROW_COLOR,
            buff=0.15,
        ).set_opacity(0.8)

        # Animate the appearance of the "Desvantagem" section and the arrow
        self.play(
            FadeIn(desvantagem_label, do_what_label),
            Create(arrow),
        )
        self.wait(11 )

        # Fade out both labels and the arrow
        self.play(
            FadeOut(vantagem_label, desvantagem_label, local_label, do_what_label, arrow)
        )
        self.wait(1)

        # === Step 3: Plotting sqrt error on NumberPlane ===

        # Create number plane for error plot
        plane_width = 1.2 * self.camera.frame_width / 2
        plane_height = 1.2 * self.camera.frame_height / 2
        plane = NumberPlane(
            x_range=[4, 14],
            y_range=[0, 1],
            x_length=plane_width,
            y_length=plane_height,
            axis_config={"color": PRIMARY_COLOR, "stroke_opacity": 0.8},
            background_line_style={
                "stroke_color": PRIMARY_COLOR,
                "stroke_width": 1,
                "stroke_opacity": 0.4,
            },
        ).set_opacity(0.8)

        plane_2 = NumberPlane(
            x_range=[0, 2],
            y_range=[0, 1],
            x_length=plane_width,
            y_length=plane_height,
            axis_config={"color": PRIMARY_COLOR, "stroke_opacity": 0.8},
            background_line_style={
                "stroke_color": PRIMARY_COLOR,
                "stroke_width": 1,
                "stroke_opacity": 0.4,
            },
        ).set_opacity(0.8)

        plane_3 = NumberPlane(
            x_range=[0, 2],
            y_range=[0, 1],
            x_length=plane_width,
            y_length=plane_height,
            axis_config={"color": PRIMARY_COLOR, "stroke_opacity": 0.8},
            background_line_style={
                "stroke_color": PRIMARY_COLOR,
                "stroke_width": 1,
                "stroke_opacity": 0.4,
            },
        ).set_opacity(0.8)

        sqr_x_label = MathTex("f(x)=\sqrt (x)", font_size=24, color=PRIMARY_COLOR).next_to(plane, RIGHT)

        # Add x-axis labels
        plane.add_coordinates({x: str(x-4) for x in range(4, 15, 2)})
        plane.coordinate_labels.set_color(PRIMARY_COLOR)

        # Create axis labels
        x_label = MathTex("\\Delta x", font_size=24).set_color(PRIMARY_COLOR).next_to(plane.x_axis, RIGHT, buff=0.5)
        y_label = Text("Erro", font_size=24).set_color(PRIMARY_COLOR).next_to(plane.y_axis, UP, buff=0.5)

        # Plot sqrt error function
        sqrt_error = plane.plot(lambda x: (1 + (x / 4) - np.sqrt(x)), x_range=[4, 14], color=ERROR_COLOR)

        # Animate creation of plane, error plot, and axis labels
        self.play(Create(plane), FadeIn(sqrt_error), FadeIn(x_label, y_label), Write(sqr_x_label))
        self.wait(21)

        # Fade out the error plot and its components
        self.play(FadeOut(plane, sqrt_error, x_label, y_label, sqr_x_label))

        # === Step 4: Polynomial Function and Tangent Line Exploration ===

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

        # Initial point for tangent line x0 = 0.2
        x0 = 0.2
        xf = 1.1  # Target x for analysis
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
            plane.animate.scale(4, about_point=zoom_point).shift(DOWN),
            graph.animate.scale(4, about_point=zoom_point).shift(DOWN)
        )

        
        # Compute another tangent line at x0 = 0.6
        x0_2 = (x0 + xf) / 2
        f_x0_2 = polynomial(x0_2)
        f_prime_x0_2 = derivative(x0_2)

        # Define first tangent line at x0
        def tangent_line(x):
            return f_x0 + f_prime_x0 * (x - x0)
        
                 # === Step 5: Second tangent line ===

        def tangent_line_2(x):
            return f_x0_2 + f_prime_x0_2 * (x - x0_2)
        
        # Define first tangent line at x0
        def g2_approx(x):
            return tangent_line(x0_2) + (derivative(x0)+(x0_2-x0)*second_derivative(x0)) * (x - x0_2)
        
        def g2(x):
            return f_x0 + (x-x0)*f_prime_x0 + second_derivative(x0)*(x-x0)**2/4

        # Create first tangent line graph
        tangent_line_graph = plane.plot(tangent_line, x_range=[0.1, xf], color=ORANGE)
        # Dot marking end point on the first tangent line
        end_dot = Dot(point=plane.c2p(xf, tangent_line(xf)), color=PRIMARY_COLOR, radius=0.03)
        
        # Add label for first approximation function r1(x)
        r_tan_label = MathTex("r_{tan}(x)", font_size=24).set_color(PRIMARY_COLOR)
        r_tan_label.next_to(plane.c2p(xf, tangent_line(xf)), UP, buff=0.2)
    
        # Position tangent line equation
        _pos = [-1.2 * config.frame_x_radius / 2, 0.8 * config.frame_y_radius / 2, 0]
        
        # Tangent line equation display (generic form)
        tangent_line_equation = MathTex(
            "r", "_{tan}", "(x_0 + \\Delta x) =", "f(", "x_0", ")", "+", "\\Delta x", "f'", "(", "x_0", ")", 
            font_size=24
        ).set_color(PRIMARY_COLOR).move_to(_pos)

        # Display updated tangent line equation for r2(x)
        r2_equation = MathTex(
            "r", "_{2}", "(x_0+2u) =", "f(", "x_0", "+ u", ")", "+", "u", "f'(", "x_0", "+ u", ")", 
            font_size=24
        ).set_color(PRIMARY_COLOR).move_to(_pos)

        # Background rectangle for equation
        background_rect_1 = Rectangle(
            width=tangent_line_equation.width + 2,
            height=tangent_line_equation.height + 2,
            color=BG_COLOR,
            fill_opacity=0.9
        )
        background_rect_1.move_to(tangent_line_equation.get_center())

        # Labels for specific points x0 and x
        label_x0 = MathTex("x_0", font_size=24).set_color(PRIMARY_COLOR).next_to(plane.c2p(x0, f_x0), DOWN, buff=0.15)

        end_point = plane.c2p(xf, polynomial(xf))
        label_x = MathTex("x", font_size=24).set_color(PRIMARY_COLOR).next_to(end_point, DOWN, buff=0.15)
        label_x.align_to(label_x0, UP)

        # Prepare label for x in terms of x0 and step size (u)
        label_x_x_0_2u = MathTex("x", "= x_0 + 2u", font_size=24).set_color(PRIMARY_COLOR)
        label_x_x_0_2u.move_to(label_x, LEFT)


        # Create second tangent line graph
        tangent_line_graph_2 = plane.plot(tangent_line_2, x_range=[x0_2+0.01, xf], color=TANGENT_LINE_BLUE)

        # Create second tangent line graph
        g2_line = plane.plot(g2_approx, x_range=[x0_2+0.01, xf], color=PURPLE)

        g2_graph = plane.plot(g2, x_range=[x0, xf], color=TANGENT_LINE_GREEN)

        end_dot_r2 = Dot(
            point=plane.c2p(xf, tangent_line_2(xf)), color=PRIMARY_COLOR, radius=0.03
        )

        end_dot_g2 = Dot(
            point=plane.c2p(xf, g2_approx(xf)), color=PRIMARY_COLOR, radius=0.03
        )

        # Midpoint between x0 and x
        x_mid = (x0 + xf) / 2
        y_mid = tangent_line_2(x_mid)

        # Dot at the midpoint (approximation target)
        dot_mid = Dot(point=plane.c2p(x_mid, y_mid), color=PRIMARY_COLOR, radius=0.03)
        
        dot_f_xou = Dot(point=plane.c2p(0, y_mid), color=PRIMARY_COLOR, radius=0.03)
        dot_f_xou_approx = Dot(point=plane.c2p(0, tangent_line(x_mid)), color=PRIMARY_COLOR, radius=0.03)
        dot_mid_approx = Dot(point=plane.c2p(x_mid, tangent_line(x_mid)), color=PRIMARY_COLOR, radius=0.03)
        label_dot_f_xou = MathTex("f(x_0+u)", font_size=20).set_color(PRIMARY_COLOR).next_to(dot_f_xou, LEFT)
        label_dot_f_xou_approx= MathTex("r_{tan}(x_0+u)", font_size=20).set_color(PRIMARY_COLOR).next_to(dot_f_xou_approx, LEFT)
        label_g2 = MathTex("g_2 \\approx r_2", font_size=24).set_color(PRIMARY_COLOR).next_to(end_dot_g2, UR, buff=0.2)


        line_fxou = DashedLine(
            plane.c2p(0, y_mid),  # (x_0+u, f(x_0+u))
            plane.c2p(x_mid, y_mid),      # (x_0+u, 0)
            color=PRIMARY_COLOR,
            stroke_width = 2
        )
        line_fxou_approx = DashedLine(
            plane.c2p(0, tangent_line(x_mid)),  # (x_0+u, f(x_0+u))
            plane.c2p(x_mid, tangent_line(x_mid)),      # (x_0+u, 0)
            color=PRIMARY_COLOR,
            stroke_width = 2
        )

        vline_fxu_approx = DashedLine(
            plane.c2p(x_mid, y_mid),  # (x_0+u, f(x_0+u))
            plane.c2p(x_mid, tangent_line(x_mid)),      # (x_0+u, 0)
            color=PRIMARY_COLOR,
            stroke_width = 2
        )


        # Vertical dashed line from midpoint down to x-axis
        vertical_line_mid = DashedLine(
            plane.c2p(x_mid, y_mid),
            plane.c2p(x_mid, 0),
            color=PRIMARY_COLOR,
            stroke_width = 2
        )

        # Label for second approximation function r2(x)
        r2_label = MathTex("r_2(x)", font_size=24).set_color(PRIMARY_COLOR)
        r2_label.next_to(plane.c2p(xf, tangent_line_2(xf)), RIGHT, buff=0.2)

        # Label for midpoint x = x0 + u
        label_x_mid = MathTex("x_0 + u", font_size=24).set_color(PRIMARY_COLOR)
        label_x_mid.next_to(dot_mid, DOWN, buff=0.15)
        label_x_mid.align_to(label_x0, UP)

        # Braces and labels to show "u" segments on x-axis
        brace_1 = BraceBetweenPoints(plane.c2p(x0, 0), plane.c2p(x_mid, 0), direction=UP, stroke_width = 0.5).set_color(PRIMARY_COLOR).shift(DOWN / 10).set_opacity(0.7)
        brace_label_1 = brace_1.get_tex("u", buff=0.2).set_color(PRIMARY_COLOR).scale(0.6)
        brace_label_1.next_to(brace_1, UP / 10)

        brace_2 = BraceBetweenPoints(plane.c2p(x_mid, 0), plane.c2p(xf, 0), direction=UP, stroke_width = 0.5).set_color(PRIMARY_COLOR).shift(DOWN / 10).set_opacity(0.7)
        brace_label_2 = brace_2.get_tex("u", buff=0.2).set_color(PRIMARY_COLOR).scale(0.6)
        brace_label_2.next_to(brace_2, UP / 10)

        
        _ = VGroup(r2_equation[3], r2_equation[4], r2_equation[5], r2_equation[6])
        # Show approximation symbol and sqrt of 4.5
        aprox_symbol = MathTex("=", font_size=24).set_color(PRIMARY_COLOR).rotate(-PI / 2).next_to(_, DOWN)
        sqrt_45 = MathTex("\sqrt{4.5}", "=", "?", font_size=24).set_color(PRIMARY_COLOR).next_to(aprox_symbol, DOWN)

                # === Step 6: Substitute approximations into r2(x) equation ===

        # Intermediate substitution steps
        f_x0_u = MathTex("f(x_0 + u) \\approx", "f(x_0) + uf'(x_0)", font_size=24).set_color(PRIMARY_COLOR).next_to(tangent_line_equation, UP, buff=0.2).align_to(r2_equation, LEFT)
        fprime_x0_u = MathTex("f'(x_0 + u) \\approx", "f'(x_0) + uf''(x_0)", font_size=24).set_color(PRIMARY_COLOR).next_to(f_x0_u, UP, buff=0.2).align_to(f_x0_u, LEFT)

        aux_r_tan= MathTex("r_{tan}(x_0+u)", font_size=24).set_color(PRIMARY_COLOR).move_to(f_x0_u[1], LEFT)
        aux_question_mark_1 = MathTex("?", font_size=24).set_color(PRIMARY_COLOR).move_to(f_x0_u[1], LEFT)
        aux_question_mark_2 = MathTex("?", font_size=24).set_color(PRIMARY_COLOR).move_to(fprime_x0_u[1], LEFT)

        # === Step 7: Simplify and transform the equation progressively ===

        # Substituting f(x0 + u) and f'(x0 + u) in r2(x)
        # "r", "_{2}", "(x) =", "f(", "x_0", "+ u", ")", "+", "u", "f'(", "x_0", "+ u", ")"
        r2_equation_subbed_f = MathTex(
            "g", "_{2}", "(x_0+2u) =", "f(", "x_0", ")", "+ uf'(x_0)", "+", "u", "f'(", "x_0", "+ u", ")", 
            font_size=24
        ).set_color(PRIMARY_COLOR).move_to(r2_equation, LEFT)

                # Substitute f'(x0 + u) with its expansion
        # "g", "_{2}", "(x) =", "f(", "x_0", ")", "+ uf'(x_0)", "+", "u", "f'(", "x_0", "+ u", ")"
        r2_equation_subbed_ff = MathTex(
            "g", "_{2}", "(x_0+2u) =", "f(", "x_0", ")", "+ uf'(x_0)", "+", "u", "(", "f'(x_0)", "+ u", "f''(x_0)", ")", 
            font_size=24
        ).set_color(PRIMARY_COLOR).move_to(r2_equation, LEFT)

        # Distribute and simplify the expression
        g2_pre = MathTex(
            "g", "_{2}", "(x_0+2u) =", "f(", "x_0", ")", "+", "uf'(x_0)", "+", "u", "f'(x_0)", "+ u^2", "f''(x_0)", 
            font_size=24
        ).set_color(PRIMARY_COLOR).move_to(r2_equation, LEFT)
        
        # Combine like terms to finalize polynomial form
        g2_equation = MathTex(
            "g", "_{2}", "(x_0+2u) =", "f(", "x_0", ")", "+", "2u f'(x_0)", "+ u^2", "f''(x_0)", 
            font_size=24
        ).set_color(PRIMARY_COLOR).move_to(r2_equation, LEFT)

        
        # Show u = Δx/2 label
        target_position = [0.7 * config.frame_x_radius / 2, -0.5 * config.frame_y_radius / 2, 0]
        u_equation = MathTex("u = \\frac{\\Delta_x}{2}", font_size=32).set_color(PRIMARY_COLOR).move_to(target_position)

        # === Step 8: Substitute u = Δx/2 into the g2 equation ===

        g2_equation_pos = MathTex(
            "g", "_{2}", "(x_0+2u) =", "f(", "x_0", ")", "+", "2", "u", "f'(x_0)", "+ u^2", "f''(x_0)", 
            font_size=24
        ).set_color(PRIMARY_COLOR).move_to(r2_equation, LEFT)

        
        g2_equation_delta_x_pre = MathTex(
            "g", "_{2}", "(x_0+2u) =", "f(", "x_0", ")", "+", "2", "\\frac{\\Delta_x}{2}", "f'(x_0)", "+ \\left( \\frac{\\Delta_x}{2} \\right)^2", "f''(x_0)", 
            font_size=24
        ).set_color(PRIMARY_COLOR).move_to(r2_equation, LEFT)


        g2_equation_delta_x = MathTex(
            "g", "_{2}", "(x_0 + \\Delta x",")","=", "f(", "x_0", ")", "+", "\\Delta_x", "f'(x_0)", "+ \\frac{\\Delta_x^2}{4}", "f''(x_0)", 
            font_size=24
        ).set_color(PRIMARY_COLOR).move_to(r2_equation, LEFT)

        # === Step 9: Square root specific example ===

        # Convert g2 polynomial form to square root expansion
        g2_equation_sqrt = MathTex(
            "g_2(", "x_0", " + ", "\\Delta x", ")","= ", "\\sqrt{x_0}", " + ", "\\frac{\\Delta x}{2 \\sqrt{x_0}}", " - ", "\\frac{\\Delta x^2}{16 (\\sqrt{x_0})^3}",
            font_size=24
        ).set_color(PRIMARY_COLOR).move_to(ORIGIN)

        # Add "Exemplo Raiz Quadrada" label and box
        example_label = Text("Exemplo Raiz Quadrada").set_color(PRIMARY_COLOR).scale(0.5).to_corner(UL, buff=0.5)
        example_label_box = SurroundingRectangle(example_label, color=PRIMARY_COLOR, buff=0.1).set_stroke(opacity=0.5, width=1)

        # Substitute x0 = 4 and Δx = 1 into the square root formula
        g2_equation_sqrt_subbed_partial = MathTex(
            "g_2(", "x_0", " + ", "1", ")","= ", "\\sqrt{x_0}", " + ", "\\frac{1}{2 \\sqrt{x_0}}", " - ", "\\frac{1}{16 (\\sqrt{x_0})^3}",
            font_size=24
        ).set_color(PRIMARY_COLOR).move_to(g2_equation_sqrt)

        # Substitute x0 = 4 and Δx = 1 into the square root formula
        g2_equation_sqrt_subbed = MathTex(
            "g_2(", "4", " + ", "1", ")","= ", "2", " + ", "\\frac{1}{4}", " - ", "\\frac{1}{128}",
            font_size=24
        ).set_color(PRIMARY_COLOR).move_to(g2_equation_sqrt)

        # Simplify expression step by step
        g2_equation_sqrt_example = MathTex(
            "g_2(", "5", ")","= ", "2.2421875",
            font_size=24
        ).set_color(PRIMARY_COLOR).move_to(g2_equation_sqrt_subbed)

        # Show squared result of the approximation
        g2_equation_sqrt_squared = MathTex(
            "g_2(", "5", ")^2"," = ", "5.0274047",
            font_size=24
        ).set_color(PRIMARY_COLOR).move_to(g2_equation_sqrt_example)

        # Add comparison with original squared approximation
        aprox_sqrt_comparison = MathTex("r(5)", "=", "2.25", font_size=24).set_color(BLACK).next_to(g2_equation_sqrt_squared, DOWN, aligned_edge=LEFT)
        aprox_sqrt_comparison_squared = MathTex("r(5)^2", "=", "5.0625", font_size=24).set_color(BLACK).next_to(g2_equation_sqrt_squared, DOWN, aligned_edge=LEFT)


        # Animate drawing of the tangent line
        self.play(Create(tangent_line_graph))
        
        # Animate appearance of all these labels and end dot
        self.play(FadeIn(end_dot, r_tan_label))


        # Display equation background and point labels
        self.play(FadeIn(background_rect_1, label_x0, label_x, tangent_line_equation))

        self.wait(2)

        self.play(HighlightWithRect(label_x0))
        self.play(HighlightWithRect(label_x))

        self.play(Create(vertical_line_mid), Create(line_fxou), FadeIn(label_x_mid, label_dot_f_xou, dot_f_xou))
        self.play(FadeIn(dot_mid))
        self.wait(2)

        # Animate drawing of the second tangent line

        self.play(Create(tangent_line_graph_2))
        self.play(FadeIn(end_dot_r2, r2_label))
        self.play(HighlightWithRect(r2_label))
        self.wait(2)


        self.wait(1)
        self.play(Write(u_equation))
        self.play(FadeIn(brace_1), FadeIn(brace_label_1))
        self.play(Indicate(VGroup(brace_1, brace_label_1), scale_factor=1.2, color=SPECIAL_FUNC_COLOR))
        self.wait(1)

        # Update label_x to show expression x = x0 + 2u
        self.play(
            FadeIn(brace_2),
            FadeIn(brace_label_2),
            run_time=0.8
        )
        self.wait(1)
        self.play(
            Transform(label_x, label_x_x_0_2u[1]),
            FadeIn(label_x_x_0_2u[0], run_time=0.3)
        )
        self.wait(1)
        self.play(HighlightWithRect(label_x_mid))
        self.play(HighlightWithRect(label_x_x_0_2u))

        self.wait(12.2)

        # Transition from previous tangent line equation to r2(x)
        self.play(
            ReplacementTransform(tangent_line_equation, r2_equation)
        )
        self.play(HighlightWithRect(r2_equation))

        self.wait(15)

        self.play(HighlightWithRect(VGroup(*r2_equation[3:7])))

        self.wait(5)

        self.play(FadeIn(aprox_symbol, sqrt_45[0]))
        self.wait(4)
        self.play(LaggedStart(
            FadeIn(sqrt_45[1], shift=LEFT),
            FadeIn(sqrt_45[2], shift=LEFT),
            lag_ratio=0.8
        ))


        self.wait(4)
        # Show the substitution step question marks
        self.play(FadeIn(f_x0_u[0], aux_question_mark_1, shift=LEFT), FadeIn(fprime_x0_u[0], aux_question_mark_2, shift=LEFT))
        self.wait(12)

        # Replace question marks with expressions
        self.play(
            Create(line_fxou_approx),
            Create(vline_fxu_approx),
            FadeIn(label_dot_f_xou_approx, dot_mid_approx),
        )
        self.play(FadeIn(dot_f_xou_approx))
        self.wait(2)

        self.play(
            Transform(aux_question_mark_1, aux_r_tan),
        )
        self.wait(2)


        self.play(ReplacementTransform(aux_question_mark_1, f_x0_u[1]))
        self.wait(3)
        self.play(ReplacementTransform(aux_question_mark_2, fprime_x0_u[1]))
        self.wait(3)

        self.remove(dot_mid_approx)
        self.play(Create(g2_line))
        self.play(FadeIn(end_dot_g2, dot_mid_approx, label_g2))
        self.play(HighlightWithRect(label_g2))
        # self.wait(0.5)


        self.play(
            ReplacementTransform(r2_equation[0], r2_equation_subbed_f[0]),
            ReplacementTransform(r2_equation[1], r2_equation_subbed_f[1]),
            ReplacementTransform(r2_equation[2], r2_equation_subbed_f[2]),
            ReplacementTransform(r2_equation[3], r2_equation_subbed_f[3]),
            ReplacementTransform(r2_equation[4], r2_equation_subbed_f[4]),
            ReplacementTransform(r2_equation[5], r2_equation_subbed_f[6]),
            ReplacementTransform(r2_equation[6], r2_equation_subbed_f[5]),
            ReplacementTransform(r2_equation[7], r2_equation_subbed_f[7]),
            ReplacementTransform(r2_equation[8], r2_equation_subbed_f[8]),
            ReplacementTransform(r2_equation[9], r2_equation_subbed_f[9]),
            ReplacementTransform(r2_equation[10], r2_equation_subbed_f[10]),
            ReplacementTransform(r2_equation[11], r2_equation_subbed_f[11]),
            ReplacementTransform(r2_equation[12], r2_equation_subbed_f[12]),
            FadeOut(sqrt_45, aprox_symbol)
        )
        self.wait(1)

        self.play(
            ReplacementTransform(r2_equation_subbed_f[0], r2_equation_subbed_ff[0]),
            ReplacementTransform(r2_equation_subbed_f[1], r2_equation_subbed_ff[1]),
            ReplacementTransform(r2_equation_subbed_f[2], r2_equation_subbed_ff[2]),
            ReplacementTransform(r2_equation_subbed_f[3], r2_equation_subbed_ff[3]),
            ReplacementTransform(r2_equation_subbed_f[4], r2_equation_subbed_ff[4]),
            ReplacementTransform(r2_equation_subbed_f[5], r2_equation_subbed_ff[5]),
            ReplacementTransform(r2_equation_subbed_f[6], r2_equation_subbed_ff[6]),
            ReplacementTransform(r2_equation_subbed_f[7], r2_equation_subbed_ff[7]),
            ReplacementTransform(r2_equation_subbed_f[8], r2_equation_subbed_ff[8]),
            ReplacementTransform(r2_equation_subbed_f[9], r2_equation_subbed_ff[9]),
            ReplacementTransform(r2_equation_subbed_f[10], r2_equation_subbed_ff[10]),
            ReplacementTransform(r2_equation_subbed_f[11], r2_equation_subbed_ff[11]),
            FadeIn(r2_equation_subbed_ff[12], shift=DOWN),
            ReplacementTransform(r2_equation_subbed_f[12], r2_equation_subbed_ff[13])
        )
        self.wait(1)


        self.play(
            FadeTransform(r2_equation_subbed_ff, g2_pre),
            run_time=2
        )
        self.wait(1)

        self.play(
            FadeTransform(g2_pre, g2_equation)
        )
        self.wait(1)

        self.play(HighlightWithRect(g2_equation))

        self.play(FadeOut(g2_equation), FadeIn(g2_equation_pos))
        self.wait(10)

        self.play(
            FadeTransform(g2_equation_pos, g2_equation_delta_x_pre),
        )
        self.wait(2)


        self.play(
            FadeTransform(g2_equation_delta_x_pre, g2_equation_delta_x),
        )
        self.wait(4)

        self.play(FadeTransform(g2_equation_delta_x, g2_equation_pos))

        self.wait(15.5)

        self.play(
            Indicate(g2_equation_pos[2][5], scale_factor=1.5, color=SPECIAL_FUNC_COLOR),
            Indicate(g2_equation_pos[8], scale_factor=1.5, color=SPECIAL_FUNC_COLOR),
            Indicate(g2_equation_pos[10][1], scale_factor=1.5, color=SPECIAL_FUNC_COLOR),
        )

        self.wait(3)

        self.play(
            Indicate(VGroup(*g2_equation_pos[2][1:3]), scale_factor=1.2, color=SPECIAL_FUNC_COLOR),
            Indicate(g2_equation_pos[4], scale_factor=1.2, color=SPECIAL_FUNC_COLOR),
            Indicate(VGroup(*g2_equation_pos[9][3:5]), scale_factor=1.2, color=SPECIAL_FUNC_COLOR),
            Indicate(VGroup(*g2_equation_pos[11][4:6]), scale_factor=1.2, color=SPECIAL_FUNC_COLOR)
        )

        self.wait(3)

        # Indicate final form of the polynomial approximation
        # self.play(Indicate(VGroup(g2_equation_delta_x[0], g2_equation_delta_x[1], g2_equation_delta_x[2])))

        # self.wait(1)

        self.play(Create(g2_graph))

        self.wait(6)

        # Clean the scene: fade out previous elements, keep g2_equation_delta_x and center it
        self.play(
            FadeOut(
                u_equation, fprime_x0_u, f_x0_u,
                graph, plane,
                tangent_line_graph, tangent_line_graph_2, g2_line, g2_graph,
                background_rect_1,
                label_x, label_x0, label_x_mid, label_x_x_0_2u, label_dot_f_xou, label_dot_f_xou_approx, label_g2,
                brace_1, brace_2,
                brace_label_1, brace_label_2,
                vertical_line_mid, line_fxou, vline_fxu_approx, line_fxou_approx, dot_f_xou_approx,
                dot_mid, end_dot, end_dot_r2, end_dot_g2, dot_mid, dot_f_xou_approx, dot_f_xou, dot_mid_approx,
                r_tan_label, r2_label,
                sqrt_45, aprox_symbol,
                end_dot, run_time=0.5
            ),
            g2_equation_pos.animate.move_to(ORIGIN)
        )
        self.wait(5)


        g2_equation_delta_x.move_to(g2_equation_pos, LEFT)
        g2_equation_sqrt.move_to(g2_equation_pos, LEFT)


        # Add comparison with original squared approximation
        substitution_tex = MathTex("u = \\frac{\\Delta x}{2}", font_size=24).set_color(BLACK).next_to(g2_equation_pos, DOWN, buff=0.3)
        self.play(Write(substitution_tex))
        self.play(LaggedStart(FadeTransform(g2_equation_pos, g2_equation_delta_x), FadeOut(substitution_tex), lag_ratio=0.8))

        self.wait(2)

        # Animate: show example label and transform polynomial to sqrt form
        self.play(
            Create(example_label),
            Create(example_label_box),
            ReplacementTransform(g2_equation_delta_x, g2_equation_sqrt)
        )

        self.wait(2.2)

        self.play(HighlightWithRect(g2_equation_sqrt))
        
        self.wait(0.5)

        self.play(Indicate(g2_equation_sqrt[:5], scale_factor=1.4, color=SPECIAL_FUNC_COLOR, run_time=2))
        self.play(Succession(
            Wait(1.2),
            Indicate(g2_equation_sqrt[6], scale_factor=1.4, color=SPECIAL_FUNC_COLOR),
            Wait(1),
            Indicate(g2_equation_sqrt[8], scale_factor=1.4, color=SPECIAL_FUNC_COLOR),
            Wait(1),
            Indicate(g2_equation_sqrt[10], scale_factor=1.4, color=SPECIAL_FUNC_COLOR),
        ))

        self.wait(4)

        # Animate substitutions into partial numeric form
        substitution_tex_1 = MathTex("\\Delta x = 1", font_size=24).set_color(BLACK).next_to(g2_equation_sqrt_subbed_partial, DOWN, aligned_edge=LEFT, buff=0.3)
        substitution_tex_2 = MathTex("x_0 = 4", font_size=24).set_color(BLACK).next_to(substitution_tex_1, RIGHT, buff=0.3)
        self.play(
            Write(substitution_tex_1),
        )
        self.play(
            MathSubstitutionTransform(g2_equation_sqrt, g2_equation_sqrt_subbed_partial),
        )

        self.wait(2)
        self.play(
            Write(substitution_tex_2),
        )
        self.play(LaggedStart(
            MathSubstitutionTransform(g2_equation_sqrt_subbed_partial, g2_equation_sqrt_subbed),
            FadeOut(substitution_tex_1, substitution_tex_2),
            lag_ratio=0.8
        ))
        
        self.wait(3)

        # Animate further simplification to final numerical value
        #"g_2(", "4", " + ", "\\Delta x", ")","= ", "2", " + ", "\\frac{\\Delta x}{4}", " - ", "\\frac{\\Delta x^2}{128}",
        #"g_2(", "4", " + ", "1", ")", "= ", "2", " + ", "\\frac{1}{4}", " - ", "\\frac{1}{128}",
        #"g_2(", "5", ")", "= ", "2.2421875"
        
        self.play(
            ReplacementTransform(g2_equation_sqrt_subbed[0], g2_equation_sqrt_example[0]),
            ReplacementTransform(g2_equation_sqrt_subbed[1], g2_equation_sqrt_example[1]),
            g2_equation_sqrt_subbed[2].animate.move_to(g2_equation_sqrt_example[1]).set_opacity(0),
            g2_equation_sqrt_subbed[3].animate.move_to(g2_equation_sqrt_example[1]).set_opacity(0),
            ReplacementTransform(g2_equation_sqrt_subbed[4], g2_equation_sqrt_example[2]),
            ReplacementTransform(g2_equation_sqrt_subbed[5], g2_equation_sqrt_example[3]),
            ReplacementTransform(g2_equation_sqrt_subbed[6], g2_equation_sqrt_example[4]),
            g2_equation_sqrt_subbed[7].animate.move_to(g2_equation_sqrt_example[4]).set_opacity(0),
            g2_equation_sqrt_subbed[8].animate.move_to(g2_equation_sqrt_example[4]).set_opacity(0),
            g2_equation_sqrt_subbed[9].animate.move_to(g2_equation_sqrt_example[4]).set_opacity(0),
            g2_equation_sqrt_subbed[10].animate.move_to(g2_equation_sqrt_example[4]).set_opacity(0),
        )
        self.wait(4)

        self.play(HighlightWithRect(g2_equation_sqrt_example))

        self.wait(2)


        self.play(
            MathSubstitutionTransform(g2_equation_sqrt_example, g2_equation_sqrt_squared)
        )
        self.wait(2)

        aprox_sqrt_comparison_squared.align_to(g2_equation_sqrt_squared, LEFT)
        self.play(HighlightWithRect(g2_equation_sqrt_squared))

        self.wait(2)

        self.play(Write(aprox_sqrt_comparison))
        self.wait(1)
        self.play(MathSubstitutionTransform(aprox_sqrt_comparison, aprox_sqrt_comparison_squared))
        self.wait(3)

        # Fade out final example elements to clean the scene
        self.play(
            FadeOut(
                g2_equation_sqrt_squared,
                aprox_sqrt_comparison_squared,
                example_label,
                example_label_box
            )
        )
