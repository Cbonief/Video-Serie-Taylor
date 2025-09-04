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


class how_to_go_beyond_2(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = BG_COLOR

        do_better_label = Text("Como ir além?").set_color(PRIMARY_COLOR)
        do_better_label.to_edge(UP).shift(DOWN * 1.5).scale(0.5).to_corner(UR, buff=0.5)

        title_box = SurroundingRectangle(do_better_label, color=PRIMARY_COLOR, buff=0.1)
        title_box.set_stroke(opacity=0.5, width=1)


        self.add(do_better_label, title_box)

        _ = MathTex("\Delta x", font_size=24).set_color(BLACK)
        
        self.wait(1)

        plane_width = self.camera.frame_width / 2  # Half the screen width
        plane_height = self.camera.frame_height / 2  # Half the screen height
        plane = NumberPlane(
            x_range=[4, 14],
            y_range=[0, 1],
            x_length=plane_width,  # Dynamically set width
            y_length=plane_height,
            axis_config={"color": PRIMARY_COLOR, "stroke_opacity": 0.8},
            background_line_style={
                "stroke_color": PRIMARY_COLOR,
                "stroke_width": 1,
                "stroke_opacity": 0.4,
            },
        ).set_opacity(0.8)

        # Add x-ticks and y-ticks
        plane.add_coordinates(
            {x: str(x-4) for x in range(4, 15, 2)},  # x-ticks
        )
        plane.coordinate_labels.set_color(PRIMARY_COLOR)

        # Add custom x-axis label
        x_label = Text("x", font_size=24).set_color(PRIMARY_COLOR)
        x_label.next_to(plane.x_axis, RIGHT, buff=0.5)

        y_label = Text("Erro", font_size=24).set_color(PRIMARY_COLOR)
        y_label.next_to(plane.y_axis, UP, buff=0.5)

        sqrt_error = plane.plot(
            lambda x: (1 + (x / 4) - np.sqrt(x)),
            x_range=[4, 14],
            color=ERROR_COLOR,
        )

        error_graph_group = VGroup(plane, sqrt_error, x_label, y_label)

        self.play(Create(plane), FadeIn(sqrt_error), FadeIn(x_label, y_label))
        self.wait(1)

        self.play(
            error_graph_group.animate.shift(LEFT)
        )

        target_position = [1.1*config.frame_x_radius / 2, config.frame_y_radius / 2,  0]
        
        error_approx = MathTex("erro(\Delta x)", "\\approx", "\Delta x", "^2", font_size=24).set_color(PRIMARY_COLOR).move_to(target_position)
        error_approx_1 = MathTex("erro(2\Delta x)", "\\approx", "(2\Delta x)", "^2", font_size=24).set_color(PRIMARY_COLOR).next_to(error_approx, DOWN).align_to(error_approx, LEFT)
        error_approx_1_1 = MathTex("erro(2\Delta x)", "\\approx", "4\Delta x", "^2", font_size=24).set_color(PRIMARY_COLOR).next_to(error_approx, DOWN).align_to(error_approx, LEFT)
        error_approx_1_2 = MathTex("erro(2\Delta x)", "\\approx", "4erro(\Delta x)", font_size=24).set_color(PRIMARY_COLOR).next_to(error_approx, DOWN).align_to(error_approx, LEFT)
        error_approx_2 = MathTex("erro \left(\\frac{\Delta x}{2}\\right)", "\\approx", "\left(\\frac{\Delta x}{2} \\right)^2", font_size=24).set_color(PRIMARY_COLOR).next_to(error_approx_1, DOWN).align_to(error_approx, LEFT)
        error_approx_2_1 = MathTex("erro \left(\\frac{\Delta x}{2}\\right)", "\\approx", "\\frac{\Delta x^2}{4}", font_size=24).set_color(PRIMARY_COLOR).next_to(error_approx_1, DOWN).align_to(error_approx, LEFT)
        error_approx_2_2 = MathTex("erro \left(\\frac{\Delta x}{2}\\right)", "\\approx", "\\frac{erro(\Delta x)}{4}", font_size=24).set_color(PRIMARY_COLOR).next_to(error_approx_1, DOWN).align_to(error_approx, LEFT)
        error_approx_3 = MathTex("erro \left(\\frac{\Delta x}{3}\\right)", "\\approx", "\\frac{erro(\Delta x)}{9}", font_size=24).set_color(PRIMARY_COLOR).next_to(error_approx_1, DOWN).align_to(error_approx, LEFT)
        error_approx_4 = MathTex("erro \left(\\frac{\Delta x}{4}\\right)", "\\approx", "\\frac{erro(\Delta x)}{16}", font_size=24).set_color(PRIMARY_COLOR).next_to(error_approx_1, DOWN).align_to(error_approx, LEFT)


        self.wait(3)
        self.play(Write(error_approx))
        self.wait(3)
        self.play(
            FadeIn(error_approx_1, shift=0.5*DOWN)
        )
        self.wait(1.5)
        
        self.play(
            ReplacementTransform(error_approx_1[0], error_approx_1_1[0]),
            ReplacementTransform(error_approx_1[1], error_approx_1_1[1]),
            ReplacementTransform(error_approx_1[2], error_approx_1_1[2]),
            ReplacementTransform(error_approx_1[3], error_approx_1_1[3])
        )
        self.wait(0.2)

        self.play(
            ReplacementTransform(error_approx_1_1[0], error_approx_1_2[0]),
            ReplacementTransform(error_approx_1_1[1], error_approx_1_2[1]),
            ReplacementTransform(error_approx_1_1[2], error_approx_1_2[2]),
            FadeOut(error_approx_1_1[3])
        )
        self.wait(0.1)

        self.play(
            Indicate(error_approx_1_2, scale_factor=1.4, color=SPECIAL_FUNC_COLOR)
        )

        self.wait(1)
        self.play(
            FadeIn(error_approx_2, shift=0.5*DOWN)
        )
        self.wait(0.3)
        
        self.play(
            ReplacementTransform(error_approx_2[0], error_approx_2_1[0]),
            ReplacementTransform(error_approx_2[1], error_approx_2_1[1]),
            ReplacementTransform(error_approx_2[2], error_approx_2_1[2])
        )
        self.wait(0.2)

        self.play(
            ReplacementTransform(error_approx_2_1[0], error_approx_2_2[0]),
            ReplacementTransform(error_approx_2_1[1], error_approx_2_2[1]),
            ReplacementTransform(error_approx_2_1[2], error_approx_2_2[2])
        )
        self.wait(0.1)

        self.play(
            Indicate(error_approx_2_2, scale_factor=1.4, color=SPECIAL_FUNC_COLOR)
        )

        self.wait(2.5)

        self.play(
            ReplacementTransform(error_approx_2_2[0], error_approx_3[0]),
            ReplacementTransform(error_approx_2_2[1], error_approx_3[1]),
            ReplacementTransform(error_approx_2_2[2], error_approx_3[2])
        )

        self.wait(2.5)
        
        self.play(
            ReplacementTransform(error_approx_3[0], error_approx_4[0]),
            ReplacementTransform(error_approx_3[1], error_approx_4[1]),
            ReplacementTransform(error_approx_3[2], error_approx_4[2])
        )

        self.wait(4)
        self.play(FadeOut(plane, sqrt_error, x_label, y_label))

        self.wait(4)

        self.play(VGroup(error_approx, error_approx_1_2, error_approx_4).animate.move_to(ORIGIN))

        self.wait(5)

        self.play(FadeOut(error_approx, error_approx_1_2, error_approx_4))

        plane = NumberPlane(
            x_range=(-4, 8),
            y_length=7,
            axis_config={
                "color": PRIMARY_COLOR,
                "stroke_opacity": 0.8
            },
            background_line_style={
                "stroke_color": PRIMARY_COLOR,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            },
        ).set_opacity(0.7)

        # Define a translated third-degree polynomial function
        def polynomial(x):
            x = x - 1.2
            return (x + 1) * (x - 2.5) * (x - 4) / 10

        def derivative(x):
            # Calculate the derivative of the function (x+1)*(x-2.5)*(x-4)/10
            x = x - 1.2
            return 0.1 * (3 * x**2 - 11 * x + 3.5)

        # Tangent line at the initial point x_0 = 0.2
        x0 = 0.2
        xf = 1.1
        f_x0 = polynomial(x0)
        f_prime_x0 = derivative(x0)

        graph = plane.plot(polynomial, x_range=[-1.05, 6.51], color=SPECIAL_FUNC_COLOR)
        zoom_point = plane.c2p(0.6, polynomial(0.6))
        graph.scale(3, about_point=zoom_point).shift(DOWN).shift(2*RIGHT)
        plane.scale(3, about_point=zoom_point).shift(DOWN).shift(2*RIGHT)

        self.play(FadeIn(plane), FadeIn(graph), run_time=1)

        def tangent_line(x):
            return f_x0 + f_prime_x0 * (x - x0)

        # Change x_range to go up to x instead of 1
        tangent_line_graph = plane.plot(
            tangent_line,
            x_range=[0.1, xf],
            color=ORANGE
        )

        r_tan_label = MathTex("r_{tan}(x)", font_size=24).set_color(PRIMARY_COLOR)
        r_tan_label.next_to(
            plane.c2p(xf, tangent_line(xf)), UP, buff=0.2
        )

        eq_location = [
            -1.0 * config.frame_x_radius / 2,
            0.9 * config.frame_y_radius / 2,
            0
        ]

        tangent_line_equation = MathTex(
            "f(x_0 + \\Delta x) \\approx f(x_0+u) + uf'(x_0+u) = r_2(x_0 + \\Delta x)",
            font_size=24
        ).set_color(PRIMARY_COLOR)
        f_prime_approx = MathTex(
            "f'(x_0 + u) \\approx f'(x_0) + uf''(x_0)",
            font_size=24
        ).set_color(PRIMARY_COLOR)
        f_mid_approx = MathTex(
            "f(x_0 + u) \\approx f(x_0) + uf'(x_0)",
            font_size=24
        ).set_color(PRIMARY_COLOR)

        tangent_line_equation.move_to(eq_location)
        f_mid_approx.next_to(tangent_line_equation, DOWN).align_to(tangent_line_equation, LEFT)
        f_prime_approx.next_to(f_mid_approx, DOWN).align_to(tangent_line_equation, LEFT)


        label_x0 = MathTex("x_0", font_size=24).set_color(PRIMARY_COLOR)
        label_x0.next_to(plane.c2p(x0, f_x0), DOWN, buff=0.15)

        # Make the final x = x
        label_x = MathTex("x", font_size=24).set_color(PRIMARY_COLOR)
        label_x_x_0_2u = MathTex("x", "= x_0 + 2u", font_size=24).set_color(PRIMARY_COLOR)
        end_point = plane.c2p(xf, polynomial(xf))
        label_x.next_to(end_point, DOWN, buff=0.15)
        label_x.align_to(label_x0, UP)

        label_x_x_0_2u.move_to(label_x, LEFT)

        # Change the end dot so it goes to x=x
        end_dot = Dot(
            point=plane.c2p(xf, tangent_line(xf)), color=PRIMARY_COLOR, radius=0.03
        )

        # Compute another tangent line starting from x0 = 0.6
        x0_2 = 0.6
        f_x0_2 = polynomial(x0_2)
        f_prime_x0_2 = derivative(x0_2)

        def tangent_line_2(x):
            return f_x0_2 + f_prime_x0_2 * (x - x0_2)
        

        # Extend the blue line to x
        tangent_line_graph_2 = plane.plot(tangent_line_2, x_range=[x0_2+0.1, xf], color=TANGENT_LINE_BLUE)

        # Adjust the midpoint to go halfway between x0 and x
        x_mid = (x0 + xf) / 2
        y_mid = tangent_line_2(x_mid)

        dot_mid = Dot(point=plane.c2p(x_mid, y_mid), color=PRIMARY_COLOR, radius=0.03)

        dot_f_xou = Dot(point=plane.c2p(0, y_mid), color=PRIMARY_COLOR, radius=0.03)
        dot_f_xou_approx = Dot(point=plane.c2p(0, tangent_line(x_mid)), color=PRIMARY_COLOR, radius=0.03)
        dot_mid_approx = Dot(point=plane.c2p(x_mid, tangent_line(x_mid)), color=PRIMARY_COLOR, radius=0.03)
        label_dot_f_xou = MathTex("f(x_0+u)", font_size=24).set_color(PRIMARY_COLOR).next_to(dot_f_xou, LEFT)
        label_dot_f_xou_approx= MathTex("f(x_0) + uf'(x_0)", font_size=24).set_color(PRIMARY_COLOR).next_to(dot_f_xou_approx, LEFT)

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


        end_dot_r2 = Dot(
            point=plane.c2p(xf, tangent_line_2(xf)), color=PRIMARY_COLOR, radius=0.03
        )

        vline_fxu = DashedLine(
            plane.c2p(x_mid, y_mid),  # (x_0+u, f(x_0+u))
            plane.c2p(x_mid, 0),      # (x_0+u, 0)
            color=PRIMARY_COLOR,
        )

        vline_fxu_approx = DashedLine(
            plane.c2p(x_mid, y_mid),  # (x_0+u, f(x_0+u))
            plane.c2p(x_mid, tangent_line(x_mid)),      # (x_0+u, 0)
            color=PRIMARY_COLOR,
            stroke_width = 2
        )

        r2_label = MathTex("r_2(x)", font_size=24).set_color(PRIMARY_COLOR)
        r2_label.next_to(
            plane.c2p(xf, tangent_line_2(xf)), UP, buff=0.2
        )

        label_x_mid = MathTex("x_0 + u", font_size=24).set_color(PRIMARY_COLOR)
        label_x_mid.next_to(dot_mid, DOWN, buff=0.15)
        label_x_mid.align_to(label_x0, UP)

        error_approx.next_to(tangent_line_equation, UP)

        error_equation_bg = Rectangle(
            width=error_approx.width + 2, #-Add some padding
            height=error_approx.height + 1,  # Add some padding
            color=BG_COLOR,
            fill_opacity=0.9
        )
        error_equation_bg.move_to(error_approx.get_center())

        tangent_line_eq_bg = Rectangle(
            width=tangent_line_equation.width + 2, #-Add some padding
            height=tangent_line_equation.height + 1,  # Add some padding
            color=BG_COLOR,
            fill_opacity=0.9
        )
        tangent_line_eq_bg.move_to(tangent_line_equation.get_center())
        
        f_mid_approx_bg = Rectangle(
            width=f_mid_approx.width + 2, #-Add some padding
            height=f_mid_approx.height + 1,  # Add some padding
            color=BG_COLOR,
            fill_opacity=0.9
        )
        f_mid_approx_bg.move_to(f_mid_approx.get_center())
        
        f_prime_approx_bg = Rectangle(
            width=f_prime_approx.width + 2, #-Add some padding
            height=f_prime_approx.height + 0.3,  # Add some padding
            color=BG_COLOR,
            fill_opacity=0.9
        )
        f_prime_approx_bg.move_to(f_prime_approx.get_center())
        

        self.play(
            Create(tangent_line_graph),
            Create(tangent_line_graph_2),
            FadeIn(label_x0, label_x, end_dot, end_dot_r2, r_tan_label, r2_label),
            FadeIn(dot_mid_approx, dot_f_xou, dot_f_xou_approx, line_fxou, line_fxou_approx, vline_fxu_approx),
            FadeIn(label_dot_f_xou, label_dot_f_xou_approx),
            FadeIn(dot_mid),
            Create(vline_fxu),
            FadeIn(label_x_mid)
        )
        self.wait(1)

        self.play(
            FadeIn(error_equation_bg, tangent_line_eq_bg, f_mid_approx_bg, f_prime_approx_bg),
            LaggedStart(
                FadeIn(error_approx),
                FadeIn(tangent_line_equation),
                FadeIn(f_mid_approx),
                FadeIn(f_prime_approx),
                lag_ratio=0.5
            )
        )

        self.wait(2)
        
        self.play(Indicate(label_x_mid, scale_factor=1.4, color=SPECIAL_FUNC_COLOR))

        self.wait(3)

        self.play(HighlightWithRect(f_prime_approx))

        self.wait(10)

        self.play(FadeOut(
            error_equation_bg, tangent_line_eq_bg, f_mid_approx_bg, f_prime_approx_bg,
            error_approx, tangent_line_equation, f_mid_approx, f_prime_approx,
            tangent_line_graph, tangent_line_graph_2,
            label_x0, label_x, end_dot, end_dot_r2, r_tan_label, r2_label,
            dot_mid_approx, dot_f_xou, dot_f_xou_approx, line_fxou, line_fxou_approx, vline_fxu_approx,
            label_dot_f_xou, label_dot_f_xou_approx,
            dot_mid,
            vline_fxu,
            label_x_mid,
            graph,
            plane
        ))

        

        g2_equation_delta_x = MathTex(
            "g", "_{2}", "(x_0 + \\Delta x) =", "f(", "x_0", ")", "+", "\\Delta_x", "f'(x_0)", "+ \\frac{\\Delta_x^2}{4}", "f''(x_0)", 
            font_size=24
        ).set_color(PRIMARY_COLOR).move_to(ORIGIN)

        g3_equation = MathTex(
            "g_{3}(x_0 + \\Delta x) = [f(x_0) + \\Delta_xf'(x_0) \\dots", 
            font_size=24
        ).set_color(PRIMARY_COLOR).next_to(g2_equation_delta_x, UP).align_to(g2_equation_delta_x, LEFT)

        g3_equation_end = MathTex(
            "]", 
            font_size=24
        ).set_color(PRIMARY_COLOR).move_to(g3_equation, UP).align_to(g2_equation_delta_x, RIGHT).shift(RIGHT)
        
        r_tan_equation = MathTex(
            "r_{1}(x_0 + \\Delta x) = f(x_0) + \\Delta_xf'(x_0)", 
            font_size=24
        ).set_color(PRIMARY_COLOR).next_to(g2_equation_delta_x, DOWN).align_to(g2_equation_delta_x, LEFT)


        self.play(Write(
            g2_equation_delta_x
        ))
        self.wait(0.5)

        self.play(Write(
            r_tan_equation
        ))
        self.wait(0.5)

        self.play(FadeIn(
            g3_equation, g3_equation_end, shit=1.5*UP, run_time=1
        ))

        self.wait(2.5)

        self.play(HighlightWithRect(g2_equation_delta_x, run_time=1.5))

        self.wait(0.5)

        self.play(FadeOut(r_tan_equation, g2_equation_delta_x))

        self.wait(1)

        self.play(FadeOut(g3_equation, g3_equation_end))

        self.play(
            FadeOut(title_box),
            do_better_label.animate.move_to(ORIGIN).scale(2)
        )

        generalize_label = Text("Generalizando").set_color(PRIMARY_COLOR)

        self.play(
            FadeIn(generalize_label),
            do_better_label.animate.scale(15).set_opacity(0),
            run_time=2
        )

        self.wait(2)