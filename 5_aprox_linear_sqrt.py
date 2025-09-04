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

class aprox_linear_sqrt(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = BG_COLOR

        # Title and its box
        title_label = Text("Definição de Derivada", font_size=36).set_color(BLACK)
        title_label.scale(0.5).to_corner(UR, buff=0.5)
        definicao_derivada = Text("*Inclinação da reta tangente", font_size=30).set_color(BLACK)
        definicao_derivada.scale(0.5).next_to(title_label, DOWN, buff=0.2)
        title_box = SurroundingRectangle(VGroup(title_label, definicao_derivada), color=BLACK, buff=0.1)
        title_box.set_stroke(opacity=0.5, width=1)

        reta_tangente = Text("Reta Tangente", font_size=36).set_color(BLACK).scale(0.5).next_to(definicao_derivada, DOWN, buff=0.5)
        limite_da_secante = Text("*Limite das retas secantes", font_size=30).set_color(BLACK).scale(0.5).next_to(reta_tangente, DOWN,buff=0.2).align_to(definicao_derivada, LEFT)
        melhor_comportamento_local = Text("*Melhor comportamento local", color=PRIMARY_COLOR, font_size=30).scale(0.5).next_to(limite_da_secante, DOWN, aligned_edge=LEFT, buff=0.2)
        tangente_box = SurroundingRectangle(VGroup(reta_tangente, limite_da_secante, melhor_comportamento_local), color=BLACK, buff=0.1)
        tangente_box.set_stroke(opacity=0.5, width=1)

        derivada_def_group = VGroup(title_label, definicao_derivada, title_box)
        tangent_def_group = VGroup(tangente_box, reta_tangente, limite_da_secante, melhor_comportamento_local)

        

        # Tangent line equation and its box
        tangent_line_equation = MathTex(
            "r_{tan}(", "x_0", " + \Delta x)", "=", "f(x_0)", "+", "\Delta x", " f'(x_0)",
            font_size=24
        ).set_color(BLACK)
        tangent_line_equation.scale(0.8).to_corner(DR, buff=0.8)
        final_box = SurroundingRectangle(tangent_line_equation, color=BLACK, buff=0.2)
        final_box.set_stroke(opacity=0.5, width=1)

        tangent_line_equation_highlight = SurroundingRectangle(tangent_line_equation[7], color=RED, buff=0.1)
        tangent_line_equation_highlight.set_stroke(opacity=0.5, width=1)

        # Add the elements
        self.add(title_label, title_box, tangent_line_equation, final_box, definicao_derivada, reta_tangente, limite_da_secante, melhor_comportamento_local, tangente_box)

        # Set up the sqrt graph
        sqrt_plane = NumberPlane(
            x_range=(0, 10),
            y_range=(0, 4),
            x_length=10,
            y_length=6,
            axis_config={"color": BLACK},
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.4
            }
        )

        # Plot sqrt graph
        # After creating sqrt_plane and before plotting and fading it in, add:
        sqrt_graph = sqrt_plane.plot(np.sqrt, x_range=[0, 10], color=rgb_to_color(hex_to_rgb("#C00000")))
        zoom_point = sqrt_plane.c2p(4, np.sqrt(4))
        sqrt_plane.scale(1.2, about_point=zoom_point)
        sqrt_graph.scale(1.2, about_point=zoom_point)

        # Example label
        example_label = VGroup(
            Text("Exemplo ", font_size=36).set_color(BLACK),
            MathTex("\mathrm{f(x)}", "\mathrm{=}", "\mathrm{\sqrt{x}}", font_size=48).set_color(BLACK)
        )
        example_label.arrange(RIGHT, buff=0.2).to_edge(UP)
        target_position = ORIGIN + UP * (config.frame_y_radius / 2)
        example_label.move_to(target_position)

        example_label_sqrt = VGroup(
            Text("Exemplo ", font_size=36).set_color(BLACK),
            MathTex("\mathrm{\sqrt{x}}", font_size=48).set_color(BLACK)
        )
        example_label_sqrt.arrange(RIGHT, buff=0.2)
        example_label_sqrt.scale(0.5).to_corner(UL, buff=0.5)

        self.wait(2)

        self.play(FadeIn(example_label))
        self.wait(1)

        # Animate title
        self.play(
            example_label[1].animate.set(font_size=24).scale(0.8).next_to(tangent_line_equation, DOWN, buff=0.2),
            Transform(example_label[0], example_label_sqrt[0]),
            FadeIn(example_label_sqrt[1], shift=LEFT),
            run_time=1.5
        )

        ffx0 = MathTex("f(x)", "=", "\sqrt{x}", font_size=24).set_color(BLACK).scale(0.8).next_to(tangent_line_equation, DOWN, buff=0.2)

        # Final label box
        final_label_box = SurroundingRectangle(VGroup(tangent_line_equation, example_label[1]), color=BLACK, buff=0.2)
        final_label_box.set_stroke(opacity=0.5, width=1)

        # Draw rectangle around the title
        example_box = SurroundingRectangle(example_label_sqrt, color=BLACK, buff=0.1)
        example_box.set_stroke(opacity=0.5, width=1)
        self.play(Create(example_box), Transform(final_box, final_label_box), Transform(example_label[1], ffx0), run_time=0.5)
        self.wait(1)

        # Plot and show sqrt graph
        self.play(
            tangent_def_group.animate.next_to(derivada_def_group, LEFT, buff=0.2),
            FadeIn(sqrt_plane), Create(sqrt_graph),
            run_time=2
        )
        self.wait(1)
  
        # Zoom in around the point (4, 2)
        zoom_factor = 4.1666
        zoom_point = sqrt_plane.c2p(4, np.sqrt(4))
        self.play(
            sqrt_plane.animate.scale(zoom_factor, about_point=zoom_point),
            sqrt_graph.animate.scale(zoom_factor, about_point=zoom_point),
            run_time=2
        )

        # Create decimal ticks and labels after zoom and shift
        x_ticks_positions = np.arange(3, 5.1, 0.5)  # From 3 to 5 in steps of 0.5
        x_ticks = VGroup()
        x_labels = VGroup()
        for x in x_ticks_positions:
            # Add tick mark
            tick = Line(
                sqrt_plane.c2p(x, np.sqrt(3)-0.02), sqrt_plane.c2p(x, np.sqrt(3)+0.02),
                color=BLACK, stroke_width=1
            ).set_opacity(0.8)
            x_ticks.add(tick)

            # Create label
            label = MathTex(f"{x:.1f}", font_size=18).set_color(BLACK)
            label.next_to(tick, DOWN, buff=0.1).set_opacity(0.8)
            x_labels.add(label)

        # Similarly for y-axis
        y_ticks_positions = np.arange(1.70, 2.20, 0.1)
        y_ticks = VGroup()
        y_labels = VGroup()
        for y in y_ticks_positions:
            # Add tick mark
            tick = Line(
                sqrt_plane.c2p(3 - 0.02, y), sqrt_plane.c2p(3 + 0.02, y),
                color=BLACK, stroke_width=1
            ).set_opacity(0.8)
            y_ticks.add(tick)

            # Create label
            label = MathTex(f"{y:.2f}", font_size=18).set_color(BLACK)
            label.next_to(tick, LEFT, buff=0.1).set_opacity(0.8)
            y_labels.add(label)

        # Horizontal line at y = sqrt(3)
        y_value = np.sqrt(3)
        horizontal_line = Line(
            sqrt_plane.c2p(0, y_value), sqrt_plane.c2p(10, y_value),
            color=GRAY, stroke_width=1
        ).set_opacity(0.5)

        self.play(FadeIn(x_ticks), FadeIn(x_labels), FadeIn(y_ticks), FadeIn(y_labels), FadeIn(horizontal_line), run_time=1)
        self.wait(1)

        # Tangent line at the initial point x_0 = 4
        x0 = 4
        f_x0 = np.sqrt(x0)
        # Compute the derivative at x0
        f_prime_x0 = 1 / (2 * np.sqrt(x0))

        aux_equation_group = VGroup(tangent_line_equation, example_label[1])
        # Final label box adjustment
        final_label_box = SurroundingRectangle(aux_equation_group, color=BLACK, buff=0.2)
        final_label_box.set_stroke(opacity=0.5, width=1)

        second_quadrant_center = [-config.frame_x_radius / 2, config.frame_y_radius / 2,  0]
        target_position = second_quadrant_center
        # x0 equation
        x0_eq = MathTex("x_0 = 4", font_size=24).set_color(BLACK)
        x0_eq.next_to(target_position)

        self.play(
            Transform(final_box, final_label_box),
            aux_equation_group.animate.next_to(x0_eq, DOWN, buff=0.35).scale(1.25),
            FadeOut(final_box)
        )

        self.wait(1)

        self.play(HighlightWithRect(tangent_line_equation[-1]))

        self.wait(1)
        
        self.play(HighlightWithRect(example_label[1][2]))

        self.wait(2)
        

        ffx0_power = MathTex("f(x)", "=", "\sqrt{x}", "=", "x^{\\frac{1}{2}}", font_size=24).set_color(BLACK)
        ffx0_power.move_to(example_label[1])
        ffx0_power.align_to(example_label[1], LEFT)
        self.play(
            FadeIn(ffx0_power[3]),
            FadeIn(ffx0_power[4], shift=LEFT)
        )

        self.wait(2.2)

        self.play(HighlightWithRect(ffx0_power[-1]))

        # Tangent line equation and its box
        tangent_line_equation_subbed_fx0 = MathTex(
            "r_{tan}(", "x_0", " + \Delta x)", "=", "\sqrt x_0", "+", "\Delta x", " f'(x_0)",
            font_size=24
        ).set_color(BLACK)
        tangent_line_equation_subbed_fx0.move_to(tangent_line_equation)

        self.play(
            tangent_line_equation[0].animate.move_to(tangent_line_equation_subbed_fx0[0]),
            tangent_line_equation[1].animate.move_to(tangent_line_equation_subbed_fx0[1]),
            tangent_line_equation[2].animate.move_to(tangent_line_equation_subbed_fx0[2]),
            tangent_line_equation[3].animate.move_to(tangent_line_equation_subbed_fx0[3]),
            tangent_line_equation[5].animate.move_to(tangent_line_equation_subbed_fx0[5]),
            tangent_line_equation[6].animate.move_to(tangent_line_equation_subbed_fx0[6]),
            tangent_line_equation[7].animate.move_to(tangent_line_equation_subbed_fx0[7]),
            FadeOut(tangent_line_equation[4]),
            FadeIn(tangent_line_equation_subbed_fx0[4], shift=DOWN)
        )

        self.play(
            FadeOut(tangent_line_equation[0]),
            FadeOut(tangent_line_equation[1]),
            FadeOut(tangent_line_equation[2]),
            FadeOut(tangent_line_equation[3]),
            FadeOut(tangent_line_equation[5]),
            FadeOut(tangent_line_equation[6]),
            FadeOut(tangent_line_equation[7]),
            FadeIn(tangent_line_equation_subbed_fx0[0]),
            FadeIn(tangent_line_equation_subbed_fx0[1]),
            FadeIn(tangent_line_equation_subbed_fx0[2]),
            FadeIn(tangent_line_equation_subbed_fx0[3]),
            FadeIn(tangent_line_equation_subbed_fx0[5]),
            FadeIn(tangent_line_equation_subbed_fx0[6]),
            FadeIn(tangent_line_equation_subbed_fx0[7]),
        )

        self.wait(1)
        self.remove(final_box)
        self.wait(1)

        second_quadrant_center = [0.9*config.frame_x_radius / 2, 0.18*config.frame_y_radius / 2,  0]
        target_position = second_quadrant_center
        power_rule_title = Text("Regra da Potência", font_size=18).set_color(BLACK)
        power_rule_title.next_to(target_position, UP, buff=0.2)

        power_rule_title_box = SurroundingRectangle(power_rule_title, color=BLACK, buff=0.1)
        power_rule_title_box.set_stroke(opacity=0.5, width=1)

        # Create a rectangle with the same size as the text
        background_rect_1 = Rectangle(
            width=power_rule_title_box.width,  # Add some padding
            height=power_rule_title_box.height,  # Add some padding
            color=BG_COLOR,
            fill_opacity=0.9
        )
        
        # Position the rectangle at the text's position
        background_rect_1.move_to(power_rule_title_box.get_center())

        self.play(FadeIn(background_rect_1, power_rule_title, power_rule_title_box))
        self.wait(1)

        power_rule_equation = MathTex("f(x)=x^m","\implies","f'(x)=mx^{m-1}", font_size=24).set_color(BLACK)
        power_rule_equation.next_to(power_rule_title_box, DOWN, buff=0.2)

        # Create a rectangle with the same size as the text
        background_rect_2 = Rectangle(
            width=power_rule_equation.width,  # Add some padding
            height=power_rule_equation.height,  # Add some padding
            color=BG_COLOR,
            fill_opacity=0.75
        )
        
        # Position the rectangle at the text's position
        background_rect_2.move_to(power_rule_equation.get_center())

        self.play(FadeIn(background_rect_2, power_rule_equation[0]))
        self.play(HighlightWithRect(VGroup(*power_rule_equation[0][5:])))
        self.play(FadeIn(power_rule_equation[1], power_rule_equation[2], shift=LEFT))
        self.wait(1)
        self.play(HighlightWithRect(VGroup(*power_rule_equation[2][6:])))

        
        m_2_eq = MathTex("m=\\frac{1}{2}", font_size=24).set_color(BLACK)
        m_2_eq.next_to(power_rule_equation, DOWN, buff=0.2)

        self.play(FadeIn(m_2_eq))

        self.wait(1)

        power_rule_equation_2 = MathTex("f(x)=x^{\\frac{1}{2}}","\implies","f'(x_0)=","\\frac{1}{2}","x_{0}^","{\\frac{1}{2}-1}", font_size=24).set_color(BLACK)
        power_rule_equation_2_simplified = MathTex("f(x)=x^{\\frac{1}{2}}","\implies","f'(x_0)=","\\frac{1}{2}","x_{0}^","{-\\frac{1}{2}}", font_size=24).set_color(BLACK)
        derivative_sqrt_eq = MathTex("f'(x_0)=","\\frac{1}{2\\sqrt x_0}", font_size=24).set_color(BLACK)
        power_rule_equation_2.next_to(m_2_eq, DOWN, buff=0.2)
        power_rule_equation_2_simplified.next_to(m_2_eq, DOWN, buff=0.2)
        derivative_sqrt_eq.next_to(m_2_eq, DOWN, buff=0.2)
        derivative_sqrt_eq.align_to(power_rule_equation_2_simplified[2], LEFT)

        power_rule_equation_2_to_transform = VGroup(power_rule_equation_2[4], power_rule_equation_2[5])

        derivate_eq_highlight = SurroundingRectangle(derivative_sqrt_eq, color=RED, buff=0.1)
        derivate_eq_highlight.set_stroke(opacity=0.5, width=1)

        # Create a rectangle with the same size as the text
        background_rect_3 = Rectangle(
            width=power_rule_equation_2.width,  # Add some padding
            height=power_rule_equation_2.height,  # Add some padding
            color=BG_COLOR,
            fill_opacity=0.75
        )
        
        # Position the rectangle at the text's position
        background_rect_3.move_to(power_rule_equation_2.get_center())

        self.play(FadeIn(background_rect_3, power_rule_equation_2[0]))
        self.play(FadeIn(power_rule_equation_2[1], power_rule_equation_2[2], power_rule_equation_2[3], power_rule_equation_2[4], power_rule_equation_2[5], shift=LEFT))

        self.wait(1)

        self.play(
            power_rule_equation_2[0].animate.move_to(power_rule_equation_2_simplified[0]),
            power_rule_equation_2[1].animate.move_to(power_rule_equation_2_simplified[1]),
            power_rule_equation_2[2].animate.move_to(power_rule_equation_2_simplified[2]),
            power_rule_equation_2[3].animate.move_to(power_rule_equation_2_simplified[3]),
            Transform(power_rule_equation_2_to_transform, VGroup(power_rule_equation_2_simplified[4], power_rule_equation_2_simplified[5]))
        )

        self.play(
            FadeIn(power_rule_equation_2_simplified[0]),
            FadeIn(power_rule_equation_2_simplified[1]),
            FadeIn(power_rule_equation_2_simplified[2]),
            FadeIn(power_rule_equation_2_simplified[3]),
            FadeIn(power_rule_equation_2_simplified[4]),
            FadeIn(power_rule_equation_2_simplified[5]),
            FadeOut(power_rule_equation_2[0]),
            FadeOut(power_rule_equation_2[1]),
            FadeOut(power_rule_equation_2[2]),
            FadeOut(power_rule_equation_2[3]),
            FadeOut(power_rule_equation_2[4]),
            FadeOut(power_rule_equation_2[5])
        )

        self.wait(0.5)

        power_rule_equation_2_simplified_to_transform = VGroup(power_rule_equation_2_simplified[4], power_rule_equation_2_simplified[3])
        self.play(
            Transform(power_rule_equation_2_simplified_to_transform, derivative_sqrt_eq[1]),
            FadeOut(power_rule_equation_2_simplified[5]),
            FadeIn(derivative_sqrt_eq[0]),
            FadeOut(power_rule_equation_2_simplified[2])
        )

        power_rule_equation_2_simplified_remaining = VGroup(power_rule_equation_2_simplified[0], power_rule_equation_2_simplified[1])
        
        self.play(
            FadeOut(power_rule_equation_2_simplified_to_transform),
            FadeIn(derivative_sqrt_eq[1])
        )

        self.wait(1)
        
        self.play(HighlightWithRect(derivative_sqrt_eq[1]))

        self.play(
            FadeOut(power_rule_title, power_rule_title_box, power_rule_equation, m_2_eq, power_rule_equation_2_simplified_remaining),
            background_rect_1.animate.set_opacity(0),
            background_rect_2.animate.set_opacity(0),
            background_rect_3.animate.set_opacity(0)
        )

        tangent_line_equation_subbed = MathTex(
            "r_{tan}(", "x_0", " + \Delta x)", "=", "f(x_0)", "+", "\Delta x", "\\frac{1}{2\\sqrt x_0}",
            font_size=24
        ).set_color(BLACK)
        tangent_line_equation_subbed.move_to(tangent_line_equation_subbed_fx0)

        self.wait(1)

        self.play(
            FadeOut(derivative_sqrt_eq[0])
        )

        self.wait(1)

        self.play(
            FadeOut(tangent_line_equation_subbed_fx0[7]),
            derivative_sqrt_eq[1].animate.move_to(tangent_line_equation_subbed[7], LEFT).set_opacity(1)
        )

        self.wait(3)

        self.play(
            FadeIn(x0_eq, shift=DOWN),
        )
        self.wait(1)

        tangent_line_equation_sqrt_4 = MathTex(
            "r_{tan}(", "4", " + \Delta x)", "=", "\\sqrt 4", "+", "\Delta x", "\\frac{1}{2\\sqrt 4}",
            font_size=24
        ).set_color(BLACK)
        tangent_line_equation_sqrt_4.move_to(tangent_line_equation_subbed_fx0)

        self.play(
            tangent_line_equation_subbed_fx0[0].animate.move_to(tangent_line_equation_sqrt_4[0]),
            tangent_line_equation_subbed_fx0[2].animate.move_to(tangent_line_equation_sqrt_4[2]),
            tangent_line_equation_subbed_fx0[3].animate.move_to(tangent_line_equation_sqrt_4[3]),
            tangent_line_equation_subbed_fx0[5].animate.move_to(tangent_line_equation_sqrt_4[5]),
            tangent_line_equation_subbed_fx0[6].animate.move_to(tangent_line_equation_sqrt_4[6]),
            Transform(tangent_line_equation_subbed_fx0[1], tangent_line_equation_sqrt_4[1]),
            Transform(tangent_line_equation_subbed_fx0[4], tangent_line_equation_sqrt_4[4]),
            Transform(derivative_sqrt_eq[1], tangent_line_equation_sqrt_4[7])
        )

        self.play(
            # Combine all FadeOut elements into a single call
            FadeOut(
                tangent_line_equation_subbed_fx0[0],
                tangent_line_equation_subbed_fx0[1],
                tangent_line_equation_subbed_fx0[2],
                tangent_line_equation_subbed_fx0[3],
                tangent_line_equation_subbed_fx0[4],
                tangent_line_equation_subbed_fx0[5],
                tangent_line_equation_subbed_fx0[6],
                derivative_sqrt_eq[1]
            ),
            # Combine all FadeIn elements into a single call
            FadeIn(
                tangent_line_equation_sqrt_4[0],
                tangent_line_equation_sqrt_4[1],
                tangent_line_equation_sqrt_4[2],
                tangent_line_equation_sqrt_4[3],
                tangent_line_equation_sqrt_4[4],
                tangent_line_equation_sqrt_4[5],
                tangent_line_equation_sqrt_4[6],
                tangent_line_equation_sqrt_4[7]
            )
        )


        self.wait(1)

        tangent_line_equation_sqrt_4_simplified = MathTex(
            "r_{tan}(", "4", " + \Delta x)", "=", "2", "+", "\Delta x", "\\frac{1}{4}",
            font_size=24
        ).set_color(BLACK)
        tangent_line_equation_sqrt_4_simplified.move_to(tangent_line_equation_subbed_fx0)

        self.play(
            tangent_line_equation_sqrt_4[0].animate.move_to(tangent_line_equation_sqrt_4_simplified[0]),
            tangent_line_equation_sqrt_4[1].animate.move_to(tangent_line_equation_sqrt_4_simplified[1]),
            tangent_line_equation_sqrt_4[2].animate.move_to(tangent_line_equation_sqrt_4_simplified[2]),
            tangent_line_equation_sqrt_4[3].animate.move_to(tangent_line_equation_sqrt_4_simplified[3]),
            tangent_line_equation_sqrt_4[5].animate.move_to(tangent_line_equation_sqrt_4_simplified[5]),
            tangent_line_equation_sqrt_4[6].animate.move_to(tangent_line_equation_sqrt_4_simplified[6]),
            Transform(tangent_line_equation_sqrt_4[4], tangent_line_equation_sqrt_4_simplified[4]),
            Transform(tangent_line_equation_sqrt_4[7], tangent_line_equation_sqrt_4_simplified[7])
        )

        self.play(
            # Combine all FadeOut elements into a single call
            FadeOut(
                tangent_line_equation_sqrt_4[0],
                tangent_line_equation_sqrt_4[1],
                tangent_line_equation_sqrt_4[2],
                tangent_line_equation_sqrt_4[3],
                tangent_line_equation_sqrt_4[4],
                tangent_line_equation_sqrt_4[5],
                tangent_line_equation_sqrt_4[6],
                tangent_line_equation_sqrt_4[7]
            ),
            # Combine all FadeIn elements into a single call
            FadeIn(
                tangent_line_equation_sqrt_4_simplified[0],
                tangent_line_equation_sqrt_4_simplified[1],
                tangent_line_equation_sqrt_4_simplified[2],
                tangent_line_equation_sqrt_4_simplified[3],
                tangent_line_equation_sqrt_4_simplified[4],
                tangent_line_equation_sqrt_4_simplified[5],
                tangent_line_equation_sqrt_4_simplified[6],
                tangent_line_equation_sqrt_4_simplified[7]
            )
        )


        self.wait(1)

        tangent_line_equation_sqrt_x_x0 = MathTex(
            "r_{tan}(", "x)", "=", "2", "+", "\\frac{(x-4)}{4}",
            font_size=24
        ).set_color(BLACK)
        tangent_line_equation_sqrt_x_x0.move_to(tangent_line_equation_sqrt_4_simplified)

        tangent_line_equation_sqrt_4_to_transform_1 = VGroup(tangent_line_equation_sqrt_4_simplified[1], tangent_line_equation_sqrt_4_simplified[2])
        tangent_line_equation_sqrt_4_to_transform_2 = VGroup(tangent_line_equation_sqrt_4_simplified[6], tangent_line_equation_sqrt_4_simplified[7])

        self.play(
            tangent_line_equation_sqrt_4_simplified[0].animate.move_to(tangent_line_equation_sqrt_x_x0[0]),
            tangent_line_equation_sqrt_4_simplified[3].animate.move_to(tangent_line_equation_sqrt_x_x0[2]),
            tangent_line_equation_sqrt_4_simplified[4].animate.move_to(tangent_line_equation_sqrt_x_x0[3]),
            tangent_line_equation_sqrt_4_simplified[5].animate.move_to(tangent_line_equation_sqrt_x_x0[4]),
            Transform(tangent_line_equation_sqrt_4_to_transform_1, tangent_line_equation_sqrt_x_x0[1]),
            Transform(tangent_line_equation_sqrt_4_to_transform_2, tangent_line_equation_sqrt_x_x0[5])
        )

        self.play(
            # Combine all FadeIn elements into a single call
            FadeIn(
                tangent_line_equation_sqrt_x_x0[0],
                tangent_line_equation_sqrt_x_x0[1],
                tangent_line_equation_sqrt_x_x0[2],
                tangent_line_equation_sqrt_x_x0[3],
                tangent_line_equation_sqrt_x_x0[4],
                tangent_line_equation_sqrt_x_x0[5]
            ),
            # Combine all FadeOut elements into a single call
            FadeOut(
                tangent_line_equation_sqrt_4_simplified[0],
                tangent_line_equation_sqrt_4_to_transform_1,
                tangent_line_equation_sqrt_4_simplified[3],
                tangent_line_equation_sqrt_4_simplified[4],
                tangent_line_equation_sqrt_4_simplified[5],
                tangent_line_equation_sqrt_4_to_transform_2
            )
        )


        # Define the tangent line function
        def tangent_line(x):
            return f_x0 + f_prime_x0 * (x - x0)

        self.play(
            FadeOut(ffx0_power[3], ffx0_power[4], example_label[1]),
            FadeOut(x0_eq)
        )

        # Plot the tangent line
        tangent_line_graph = sqrt_plane.plot(
            tangent_line,
            x_range=[3, 5],
            color=TANGENT_LINE_BLUE
        )
        self.play(Create(tangent_line_graph))
        self.wait(10)

        second_quadrant_center = [-config.frame_x_radius / 2, config.frame_y_radius / 2,  0]
        target_position = second_quadrant_center
        # x0 equation
        x_eq = MathTex("x = 5", font_size=24).set_color(BLACK)
        x_eq.next_to(target_position)

        self.play(FadeIn(x_eq, shift=DOWN))

        tangent_line_equation_sqrt_4_5 = MathTex("r_{tan}(", "5", ")", "=", "2", "+", "\\frac{(5-4)}{4}", font_size=24).set_color(BLACK)
        tangent_line_equation_sqrt_4_5.move_to(tangent_line_equation_sqrt_x_x0)

        self.play(
            tangent_line_equation_sqrt_x_x0[0].animate.move_to(tangent_line_equation_sqrt_4_5[0]),
            FadeIn(tangent_line_equation_sqrt_4_5[1], shift=DOWN),
            FadeIn(tangent_line_equation_sqrt_4_5[2]),
            tangent_line_equation_sqrt_x_x0[1].animate.align_to(tangent_line_equation_sqrt_4_5[2], RIGHT).set_opacity(0),
            tangent_line_equation_sqrt_x_x0[2].animate.move_to(tangent_line_equation_sqrt_4_5[3]),
            tangent_line_equation_sqrt_x_x0[3].animate.move_to(tangent_line_equation_sqrt_4_5[4]),
            tangent_line_equation_sqrt_x_x0[4].animate.move_to(tangent_line_equation_sqrt_4_5[5]),
            Transform(tangent_line_equation_sqrt_x_x0[5], tangent_line_equation_sqrt_4_5[6])
        )

        self.play(
            FadeIn(
                tangent_line_equation_sqrt_4_5[0],
                tangent_line_equation_sqrt_4_5[3],
                tangent_line_equation_sqrt_4_5[4],
                tangent_line_equation_sqrt_4_5[5],
                tangent_line_equation_sqrt_4_5[6]
            ),
            FadeOut(
                tangent_line_equation_sqrt_x_x0[0],
                tangent_line_equation_sqrt_x_x0[2],
                tangent_line_equation_sqrt_x_x0[3],
                tangent_line_equation_sqrt_x_x0[4],
                tangent_line_equation_sqrt_x_x0[5],
            )
        )

        self.wait(1)

        tangent_line_sqrt_5 = MathTex("r_{tan}(", "5", ")", "=", "2", "+", "\\frac{1}{4}", font_size=24).set_color(BLACK)
        tangent_line_sqrt_5.move_to(tangent_line_equation_sqrt_4_5)

        tangent_line_sqrt_5_025 = MathTex("r_{tan}(", "5", ")", "=", "2", "+", "0.25", font_size=24).set_color(BLACK)
        tangent_line_sqrt_5_025.move_to(tangent_line_sqrt_5)

        aprox_sqrt_5 = MathTex("r_{tan}(", "5", ")", "=", "2.25", font_size=24).set_color(BLACK)
        aprox_sqrt_5.move_to(tangent_line_sqrt_5_025)


        self.play(
            FadeOut(x_eq),
            tangent_line_equation_sqrt_4_5[0].animate.move_to(tangent_line_sqrt_5[0]),
            tangent_line_equation_sqrt_4_5[1].animate.move_to(tangent_line_sqrt_5[1]),
            tangent_line_equation_sqrt_4_5[2].animate.move_to(tangent_line_sqrt_5[2]),
            tangent_line_equation_sqrt_4_5[3].animate.move_to(tangent_line_sqrt_5[3]),
            tangent_line_equation_sqrt_4_5[4].animate.move_to(tangent_line_sqrt_5[4]),
            tangent_line_equation_sqrt_4_5[5].animate.move_to(tangent_line_sqrt_5[5]),
            Transform(tangent_line_equation_sqrt_4_5[6], tangent_line_sqrt_5[6])
        )

        self.play(
            FadeOut(
                tangent_line_equation_sqrt_4_5[0],
                tangent_line_equation_sqrt_4_5[1],
                tangent_line_equation_sqrt_4_5[2],
                tangent_line_equation_sqrt_4_5[3],
                tangent_line_equation_sqrt_4_5[4],
                tangent_line_equation_sqrt_4_5[5],
                tangent_line_equation_sqrt_4_5[6],
            ),
            FadeIn(
                tangent_line_sqrt_5[0],
                tangent_line_sqrt_5[1],
                tangent_line_sqrt_5[2],
                tangent_line_sqrt_5[3],
                tangent_line_sqrt_5[4],
                tangent_line_sqrt_5[5],
                tangent_line_sqrt_5[6],
            ),
            run_time = 0.1
        )

        self.play(
            tangent_line_sqrt_5[0].animate.move_to(tangent_line_sqrt_5_025[0]),
            tangent_line_sqrt_5[1].animate.move_to(tangent_line_sqrt_5_025[1]),
            tangent_line_sqrt_5[2].animate.move_to(tangent_line_sqrt_5_025[2]),
            tangent_line_sqrt_5[3].animate.move_to(tangent_line_sqrt_5_025[3]),
            tangent_line_sqrt_5[4].animate.move_to(tangent_line_sqrt_5_025[4]),
            tangent_line_sqrt_5[5].animate.move_to(tangent_line_sqrt_5_025[5]),
            Transform(tangent_line_sqrt_5[6], tangent_line_sqrt_5_025[6])
        )

        self.play(
            FadeOut(
                tangent_line_sqrt_5[0],
                tangent_line_sqrt_5[1],
                tangent_line_sqrt_5[2],
                tangent_line_sqrt_5[3],
                tangent_line_sqrt_5[4],
                tangent_line_sqrt_5[5],
                tangent_line_sqrt_5[6],
            ),
            FadeIn(
                tangent_line_sqrt_5_025[0],
                tangent_line_sqrt_5_025[1],
                tangent_line_sqrt_5_025[2],
                tangent_line_sqrt_5_025[3],
                tangent_line_sqrt_5_025[4],
                tangent_line_sqrt_5_025[5],
                tangent_line_sqrt_5_025[6],
            ),
            run_time = 0.1
        )

        self.wait(0.3)

        tangent_line_sqrt_5_025_to_transform = VGroup(tangent_line_sqrt_5_025[4],tangent_line_sqrt_5_025[5],tangent_line_sqrt_5_025[6])

        self.play(
            tangent_line_sqrt_5_025[0].animate.move_to(aprox_sqrt_5[0]),
            tangent_line_sqrt_5_025[1].animate.move_to(aprox_sqrt_5[1]),
            tangent_line_sqrt_5_025[2].animate.move_to(aprox_sqrt_5[2]),
            tangent_line_sqrt_5_025[3].animate.move_to(aprox_sqrt_5[3]),
            Transform(tangent_line_sqrt_5_025_to_transform, aprox_sqrt_5[4])
        )

        self.play(
            FadeOut(
                tangent_line_sqrt_5_025[0],
                tangent_line_sqrt_5_025[1],
                tangent_line_sqrt_5_025[2],
                tangent_line_sqrt_5_025[3],
                tangent_line_sqrt_5_025_to_transform
            ),
            FadeIn(
                aprox_sqrt_5[0],
                aprox_sqrt_5[1],
                aprox_sqrt_5[2],
                aprox_sqrt_5[3],
                aprox_sqrt_5[4]
            )
        )

        self.wait(4)

        aprox_sqrt_comparison = MathTex("r_{tan}(5)", "=", "2.25", "\\approx", "\\sqrt 5", font_size=24).set_color(BLACK)
        aprox_sqrt_comparison.move_to(aprox_sqrt_5, LEFT)

        aprox_sqrt_comparison_squared = MathTex("r(5)^2", "=", "2.25^2", "\\approx", "5", font_size=24).set_color(BLACK)
        aprox_sqrt_comparison_squared.move_to(aprox_sqrt_5, LEFT)

        aprox_sqrt_comparison_squared_simplified = MathTex("r(5)^2", "=", "5.0625", "\\approx", "5", font_size=24).set_color(BLACK)
        aprox_sqrt_comparison_squared_simplified.move_to(aprox_sqrt_5, LEFT)

        self.play(
            FadeIn(aprox_sqrt_comparison[3], aprox_sqrt_comparison[4], shift=LEFT)
        )

        self.play(
            FadeIn(aprox_sqrt_comparison[0], aprox_sqrt_comparison[1], aprox_sqrt_comparison[2]),
            FadeOut(aprox_sqrt_5[0],aprox_sqrt_5[1],aprox_sqrt_5[2],aprox_sqrt_5[3], aprox_sqrt_5[4])
        )

        self.wait(1)

        self.play(
            Transform(aprox_sqrt_comparison[0], aprox_sqrt_comparison_squared[0]),
            Transform(aprox_sqrt_comparison[2], aprox_sqrt_comparison_squared[2]),
            Transform(aprox_sqrt_comparison[4], aprox_sqrt_comparison_squared[4]),
            aprox_sqrt_comparison[1].animate.move_to(aprox_sqrt_comparison_squared[1]),
            aprox_sqrt_comparison[3].animate.move_to(aprox_sqrt_comparison_squared[3]),
        )

        self.play(
            FadeOut(
                aprox_sqrt_comparison[0],
                aprox_sqrt_comparison[1],
                aprox_sqrt_comparison[2],
                aprox_sqrt_comparison[3],
                aprox_sqrt_comparison[4]
            ),
            FadeIn(
                aprox_sqrt_comparison_squared[0],
                aprox_sqrt_comparison_squared[1],
                aprox_sqrt_comparison_squared[2],
                aprox_sqrt_comparison_squared[3],
                aprox_sqrt_comparison_squared[4]
            )
        )

        self.wait(1.2)

        self.play(
            aprox_sqrt_comparison_squared[0].animate.move_to(aprox_sqrt_comparison_squared_simplified[0]),
            aprox_sqrt_comparison_squared[1].animate.move_to(aprox_sqrt_comparison_squared_simplified[1]),
            Transform(aprox_sqrt_comparison_squared[2], aprox_sqrt_comparison_squared_simplified[2]),
            aprox_sqrt_comparison_squared[3].animate.move_to(aprox_sqrt_comparison_squared_simplified[3]),
            aprox_sqrt_comparison_squared[4].animate.move_to(aprox_sqrt_comparison_squared_simplified[4])
        )

        self.play(
            FadeOut(
                aprox_sqrt_comparison_squared[0],
                aprox_sqrt_comparison_squared[1],
                aprox_sqrt_comparison_squared[2],
                aprox_sqrt_comparison_squared[3],
                aprox_sqrt_comparison_squared[4]
            ),
            FadeIn(
                aprox_sqrt_comparison_squared_simplified[0],
                aprox_sqrt_comparison_squared_simplified[1],
                aprox_sqrt_comparison_squared_simplified[2],
                aprox_sqrt_comparison_squared_simplified[3],
                aprox_sqrt_comparison_squared_simplified[4]
            )
        )

        # Add the following lines after the last self.wait(2) line:
        self.play(
            FadeOut(
                sqrt_graph,
                sqrt_plane,
                tangent_line_graph,
                example_box,
                example_label_sqrt,
                example_label[0],
                x_ticks,
                y_ticks,
                horizontal_line,
                x_labels,
                y_labels,
                derivada_def_group,
                tangent_def_group
            )
        )

        self.wait(1.5)

        self.play(FadeOut(aprox_sqrt_comparison_squared_simplified[0], aprox_sqrt_comparison_squared_simplified[1]))

        aprox_sqrt_comparison_squared_simplified_to_move = VGroup(aprox_sqrt_comparison_squared_simplified[2], aprox_sqrt_comparison_squared_simplified[3], aprox_sqrt_comparison_squared_simplified[4])

        # Title and its box
        do_better_label = Text("Como ir além?").set_color(BLACK)
        do_better_label.to_edge(UP).shift(DOWN * 1.5),

        self.play(
            aprox_sqrt_comparison_squared_simplified_to_move.animate.next_to(do_better_label, DOWN, buff=1).scale(1.5625)
        )

        self.wait(6)

        self.play(Write(do_better_label))

        self.wait(3)