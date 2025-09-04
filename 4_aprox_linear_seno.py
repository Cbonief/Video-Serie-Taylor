from manim import *

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

class aprox_linear_seno(Scene):
    def construct(self):
        # Re-create elements from the previous scene
        # 1. Title: "Definição de Derivada" and its box
        self.camera.background_color = BG_COLOR

        title_label = Text("Definição de Derivada", font_size=36).set_color(BLACK)
        title_label.scale(0.5).to_corner(UR, buff=0.5)

        definicao_derivada = Text("*Inclinação da reta tangente", font_size=30).set_color(BLACK)
        definicao_derivada.scale(0.5).next_to(title_label, DOWN, buff=0.2)
        title_box = SurroundingRectangle(VGroup(title_label, definicao_derivada), color=BLACK, buff=0.1)
        title_box.set_stroke(opacity=0.5, width=1)

        reta_tangente = Text("Reta Tangente", font_size=36).set_color(BLACK).scale(0.5).next_to(definicao_derivada, DOWN, buff=0.5)
        limite_da_secante = Text("*Limite das retas secantes", font_size=30).set_color(BLACK).scale(0.5).next_to(reta_tangente, DOWN,buff=0.2).align_to(definicao_derivada, LEFT)

        tangente_box = SurroundingRectangle(VGroup(reta_tangente, limite_da_secante), color=BLACK, buff=0.1)
        tangente_box.set_stroke(opacity=0.5, width=1)
        
        # 2. Tangent line equation and its box
        tangent_line_equation = MathTex(
            "r_{tan}(", "x_0", " + \Delta x)", "=", "f(x_0)", "+", "\Delta x", " f'(x_0)",
            font_size=24
        ).set_color(BLACK)
        tangent_line_equation.scale(0.8).to_corner(DR, buff=0.8)
        final_box = SurroundingRectangle(tangent_line_equation, color=BLACK, buff=0.2)
        final_box.set_stroke(opacity=0.5, width=1)
        
        # Add the previously present elements
        self.add(title_label, definicao_derivada, title_box, tangent_line_equation, final_box, reta_tangente, limite_da_secante, tangente_box)

        # Set up and display the sine graph from -2pi to 2pi
        sine_plane = NumberPlane(
            x_range=(-2 * PI, 2 * PI),
            y_range=(-7, 7),
            axis_config={"color": BLACK},
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.4
            }
        )

        # Create initial pi-based ticks and labels
        pi_ticks, pi_labels = self.create_pi_ticks_with_labels(np.arange(-2 * PI, 2 * PI + 0.1, PI / 4), sine_plane)
        sine_plane.x_axis.add(pi_ticks, pi_labels)

        # Create a title label and position it in the center, then animate to upper right
        example_label = VGroup(Text("Exemplo ", font_size=36).set_color(BLACK),MathTex("\mathrm{f(x)}","\mathrm{=}","\mathrm{sen(x)}", font_size=48).set_color(BLACK))
        example_label.arrange(RIGHT, buff=0.2).to_edge(UP)
        
        # Animate the item to halfway down and center it horizontally
        target_position = ORIGIN + UP * (config.frame_y_radius / 2)
        example_label.move_to(target_position)

        example_label_sin = VGroup(Text("Exemplo ", font_size=36).set_color(BLACK),MathTex("\mathrm{sen(x)}", font_size=48).set_color(BLACK))
        example_label_sin.arrange(RIGHT, buff=0.2)
        example_label_sin.scale(0.5).to_corner(UL, buff=0.5)
        self.wait(2)
        self.play(FadeIn(example_label))
        self.wait(1)

        # Animate title to move to the top right and shrink
        self.play(
            example_label[1].animate.set(font_size=24).scale(0.8).next_to(tangent_line_equation, DOWN, buff=0.2),
            Transform(example_label[0], example_label_sin[0]),
            FadeIn(example_label_sin[1], shift=LEFT),
            run_time=1.5
        )

        ffx0 = MathTex("f(x)","=","sen(x)", font_size=24).set_color(BLACK).scale(0.8).next_to(tangent_line_equation, DOWN, buff=0.2)

        # Expand bounding box to fit all three labels
        final_label_box = SurroundingRectangle(VGroup(tangent_line_equation, example_label[1]), color=BLACK, buff=0.2)
        final_label_box.set_stroke(opacity=0.5, width=1)

        # Draw a rectangle around the title for emphasis
        example_box = SurroundingRectangle(example_label_sin, color=BLACK, buff=0.1)
        example_box.set_stroke(opacity=0.5, width=1)
        self.play(Create(example_box), Transform(final_box, final_label_box), Transform(example_label[1], ffx0), run_time=0.5)
        self.wait(1)

        # Plot and show sine graph
        sine_graph = sine_plane.plot(np.sin, x_range=[-2 * PI, 2 * PI], color=rgb_to_color(hex_to_rgb("#C00000")))
        self.play(FadeIn(sine_plane), Create(sine_graph))
        self.wait(1)

        # Define an updater for the linked_circle
        initial_width = sine_plane.width
        def update_labels(labels):
            # Use the plane's scale to adjust the circle's size and opacity
            current_width = sine_plane.get_width()  # Get current width
            scale_factor = current_width / initial_width
            for label in labels:
                label.scale(1/scale_factor)
        
        pi_labels.add_updater(update_labels)

        # Zoom in by scaling around the origin
        zoom_factor = 5
        self.play(
            sine_plane.animate.scale(zoom_factor, about_point=sine_plane.c2p(0, 0)),
            sine_graph.animate.scale(zoom_factor, about_point=sine_plane.c2p(0, 0)),
        )

        # Define a tick at x=0
        zero_tick = Line(
            sine_plane.c2p(0, -0.1), sine_plane.c2p(0, 0.1),  # Start and end points for the tick
            color=BLACK, stroke_width=2
        )

        # Define the label for the tick
        zero_label = MathTex("0", font_size=24).set_color(BLACK)
        zero_label.next_to(zero_tick, DOWN, buff=0.1)  # Position it below the tick

        # Create a rectangle background for the label
        background_rect = Rectangle(
            width=zero_label.width + 0.1,  # Slightly larger than the label's width
            height=zero_label.height + 0.1,  # Slightly larger than the label's height
            color=BG_COLOR,  # Scene background color
            fill_opacity=1,  # Solid fill
            stroke_width=0   # No border
        )

        background_rect.move_to(zero_label.get_center())
        # self.add(background_rect, zero_label)  # Add background rectangle first to appear behind


        # Add the tick and label to the scene after the zoom
        self.play(FadeIn(background_rect), FadeIn(zero_tick), FadeIn(zero_label), run_time=1)
        self.wait(1)

        self.wait(1)

        # Tangent line at the initial point x_0
        tangent_start = sine_plane.coords_to_point(
            -4,-4
        )
        tangent_end = sine_plane.coords_to_point(
            4,4
        )
        tangent_line = DashedLine(start=tangent_start, end=tangent_end, color=TANGENT_LINE_BLUE)
        self.play(FadeIn(tangent_line))
        
        second_quadrant_center = [-config.frame_x_radius / 2, config.frame_y_radius / 2,  0]
        target_position = second_quadrant_center

        x0_eq = MathTex("x_0 = 0", font_size=24).set_color(BLACK)
        x0_eq.next_to(target_position)


        # Expand bounding box to fit all three labels
        final_label_box = SurroundingRectangle(ffx0, color=BLACK, buff=0.2)
        final_label_box.set_stroke(opacity=0.5, width=1)

        self.play(
            Transform(final_box, final_label_box),
            tangent_line_equation.animate.next_to(x0_eq, DOWN, buff=0.2).scale(1.25)
        )

        self.wait(2)

        tangent_line_equation_sin = MathTex("r_{tan}(","x_0"," + \Delta x)", "=", "sen(x_{0})", "+", "\Delta x", "cos(x_{0})",font_size=24).set_color(BLACK)
        tangent_line_equation_sin_0 = MathTex("r_{tan}(","0"," + \Delta x)", "=", "sen(0)", "+", "\Delta x", " cos(0)",font_size=24).set_color(BLACK)
        tangent_line_equation_sin_0_sub = MathTex("r_{tan}(","0"," +"," \Delta x)", "=", "0", "+", "\Delta x", " \cdot1",font_size=24).set_color(BLACK)
        tangent_line_equation_sin_0_simplified = MathTex("r_{tan}(","\Delta x)", "=", "\Delta x",font_size=24).set_color(BLACK)
        sine_tangent_line_equation = MathTex("r_{tan}(\Delta x)", "=", "\Delta x",font_size=24).set_color(BLACK)
        aux = VGroup(tangent_line_equation_sin_0_simplified[0], tangent_line_equation_sin_0_simplified[1])
        tangent_line_equation_sin.move_to(tangent_line_equation)
        tangent_line_equation_sin_0.move_to(tangent_line_equation)
        tangent_line_equation_sin_0_sub.move_to(tangent_line_equation)
        tangent_line_equation_sin_0_simplified.move_to(tangent_line_equation)
        sine_tangent_line_equation.move_to(tangent_line_equation)

        self.play(
            tangent_line_equation[0].animate.align_to(tangent_line_equation_sin, LEFT),
            tangent_line_equation[1].animate.move_to(tangent_line_equation_sin[1]),
            tangent_line_equation[2].animate.move_to(tangent_line_equation_sin[2]),
            tangent_line_equation[3].animate.move_to(tangent_line_equation_sin[3]),
            Transform(tangent_line_equation[4], tangent_line_equation_sin[4]),
            tangent_line_equation[5].animate.move_to(tangent_line_equation_sin[5]),
            tangent_line_equation[6].animate.move_to(tangent_line_equation_sin[6]),
            Transform(tangent_line_equation[7], tangent_line_equation_sin[7])
        )

        self.wait(1)

        self.play(
            FadeOut(tangent_line_equation[0]),
            FadeOut(tangent_line_equation[1]),
            FadeOut(tangent_line_equation[2]),
            FadeOut(tangent_line_equation[3]),
            FadeOut(tangent_line_equation[4]),
            FadeOut(tangent_line_equation[5]),
            FadeOut(tangent_line_equation[6]),
            FadeOut(tangent_line_equation[7]),
            FadeIn(tangent_line_equation_sin[0]),
            FadeIn(tangent_line_equation_sin[1]),
            FadeIn(tangent_line_equation_sin[2]),
            FadeIn(tangent_line_equation_sin[3]),
            FadeIn(tangent_line_equation_sin[4]),
            FadeIn(tangent_line_equation_sin[5]),
            FadeIn(tangent_line_equation_sin[6]),
            FadeIn(tangent_line_equation_sin[7])
        )

        self.wait(17)

        self.play(
            FadeIn(x0_eq, shift=DOWN),
        )

        self.wait(1)

        self.play(
            tangent_line_equation_sin[0].animate.move_to(tangent_line_equation_sin_0[0]),
            Transform(tangent_line_equation_sin[1], tangent_line_equation_sin_0[1]),
            tangent_line_equation_sin[2].animate.move_to(tangent_line_equation_sin_0[2]),
            tangent_line_equation_sin[3].animate.move_to(tangent_line_equation_sin_0[3]),
            FadeOut(tangent_line_equation_sin[4]),
            FadeIn(tangent_line_equation_sin_0[4]),
            tangent_line_equation_sin[5].animate.move_to(tangent_line_equation_sin_0[5]),
            tangent_line_equation_sin[6].animate.move_to(tangent_line_equation_sin_0[6]),
            FadeOut(tangent_line_equation_sin[7]),
            FadeIn(tangent_line_equation_sin_0[7])
        )

        self.play(
            FadeOut(tangent_line_equation_sin[0]),
            FadeOut(tangent_line_equation_sin[1]),
            FadeOut(tangent_line_equation_sin[2]),
            FadeOut(tangent_line_equation_sin[3]),
            FadeOut(tangent_line_equation_sin[5]),
            FadeOut(tangent_line_equation_sin[6]),
            FadeIn(tangent_line_equation_sin_0[0]),
            FadeIn(tangent_line_equation_sin_0[1]),
            FadeIn(tangent_line_equation_sin_0[2]),
            FadeIn(tangent_line_equation_sin_0[3]),
            FadeIn(tangent_line_equation_sin_0[5]),
            FadeIn(tangent_line_equation_sin_0[6]),
        )

        self.wait(4)

        self.play(
            tangent_line_equation_sin_0[0].animate.move_to(tangent_line_equation_sin_0_sub[0]),
            tangent_line_equation_sin_0[1].animate.move_to(tangent_line_equation_sin_0_sub[1]),
            tangent_line_equation_sin_0[2].animate.align_to(tangent_line_equation_sin_0_sub[2], LEFT),
            tangent_line_equation_sin_0[3].animate.move_to(tangent_line_equation_sin_0_sub[4]),
            Transform(tangent_line_equation_sin_0[4], tangent_line_equation_sin_0_sub[5]),
            tangent_line_equation_sin_0[5].animate.move_to(tangent_line_equation_sin_0_sub[6]),
            tangent_line_equation_sin_0[6].animate.move_to(tangent_line_equation_sin_0_sub[7]),
            Transform(tangent_line_equation_sin_0[7], tangent_line_equation_sin_0_sub[8])
        )

        self.play(
            FadeOut(tangent_line_equation_sin_0[0]),
            FadeOut(tangent_line_equation_sin_0[1]),
            FadeOut(tangent_line_equation_sin_0[2]),
            FadeOut(tangent_line_equation_sin_0[3]),
            FadeOut(tangent_line_equation_sin_0[4]),
            FadeOut(tangent_line_equation_sin_0[5]),
            FadeOut(tangent_line_equation_sin_0[6]),
            FadeOut(tangent_line_equation_sin_0[7]),
            FadeIn(tangent_line_equation_sin_0_sub[0]),
            FadeIn(tangent_line_equation_sin_0_sub[1]),
            FadeIn(tangent_line_equation_sin_0_sub[2]),
            FadeIn(tangent_line_equation_sin_0_sub[3]),
            FadeIn(tangent_line_equation_sin_0_sub[4]),
            FadeIn(tangent_line_equation_sin_0_sub[5]),
            FadeIn(tangent_line_equation_sin_0_sub[6]),
            FadeIn(tangent_line_equation_sin_0_sub[7]),
            FadeIn(tangent_line_equation_sin_0_sub[8])
        )

        self.wait(1)

        self.play(
            FadeOut(tangent_line_equation_sin_0_sub[1]),
            FadeOut(tangent_line_equation_sin_0_sub[5]),
            FadeOut(tangent_line_equation_sin_0_sub[8])
        )

        self.play(
            FadeOut(tangent_line_equation_sin_0_sub[2], run_time=0.2),
            FadeOut(tangent_line_equation_sin_0_sub[6], run_time=0.2),
            tangent_line_equation_sin_0_sub[0].animate.align_to(sine_tangent_line_equation[0], LEFT),
            tangent_line_equation_sin_0_sub[3].animate.align_to(sine_tangent_line_equation[0], RIGHT),
            tangent_line_equation_sin_0_sub[4].animate.move_to(sine_tangent_line_equation[1]),
            tangent_line_equation_sin_0_sub[7].animate.move_to(sine_tangent_line_equation[2]),
            FadeOut(x0_eq),
            run_time=1
        )

        self.play(
            FadeOut(tangent_line_equation_sin_0_sub[0]),
            FadeOut(tangent_line_equation_sin_0_sub[3]),
            FadeOut(tangent_line_equation_sin_0_sub[4]),
            FadeOut(tangent_line_equation_sin_0_sub[7]),
            FadeIn(sine_tangent_line_equation[0]),
            FadeIn(sine_tangent_line_equation[1]),
            FadeIn(sine_tangent_line_equation[2])
        )

        # # Create animations
        # move_animation = x0_eq.animate.next_to(ffx0, UP, buff=0.2)    # Move to target position
        # fade_out_in_animation = AnimationGroup(
        #     FadeOut(x0_eq, scale=1),                # Fade out
        #     FadeIn(x0_eq, scale=1),                 # Fade back in
        #     lag_ratio=1.0                           # Ensures fade-in starts after fade-out
        # )

        # # Play animations together
        # self.play(
        #     AnimationGroup(
        #         move_animation, 
        #         fade_out_in_animation,
        #         lag_ratio=0                         # Run both simultaneously
        #     )
        # )

        self.wait(6)

        aux = ffx0.copy()
        aux.scale(1.25)
        aux[0].next_to(sine_tangent_line_equation[0], DOWN, buff=0.3)
        aux[1].align_to(sine_tangent_line_equation[1], LEFT)
        aux[2].align_to(sine_tangent_line_equation[2], LEFT)
        aux[1].move_to([aux[1].get_center()[0], aux[0].get_center()[1], 0])
        aux[2].move_to([aux[2].get_center()[0], aux[0].get_center()[1], 0])

        aprox_1 = MathTex("\\approx",font_size=24).set_color(BLACK)
        aprox_2 = MathTex("\\approx",font_size=24).set_color(BLACK)
        coords_1_x = sine_tangent_line_equation[0].get_center()[0]
        coords_2_x = sine_tangent_line_equation[2].get_center()[0]
        coords_1_y = (sine_tangent_line_equation[0].get_center()[1] + aux[0].get_center()[1])/2
        coords_2_y = (sine_tangent_line_equation[2].get_center()[1] + aux[2].get_center()[1])/2
        aprox_1.move_to([coords_1_x, coords_1_y, 0]).rotate(PI/2).set_opacity(0.8)
        aprox_2.move_to([coords_2_x, coords_2_y, 0]).rotate(PI/2).set_opacity(0.8)

        self.play(FadeOut(example_label[1]))

        self.play(
            FadeOut(final_box),
            ffx0[0].animate.move_to(aux[0]).scale(1.25),
            ffx0[1].animate.move_to(aux[1]).scale(1.25),
            ffx0[2].animate.move_to(aux[2]).scale(1.25)
        )

        self.play(
            FadeIn(aprox_1, aprox_2)
        )

        # Hold the scene
        self.wait(10)

        melhor_comportamento_local = Text("*Melhor comportamento local", color=PRIMARY_COLOR, font_size=30).scale(0.5).next_to(limite_da_secante, DOWN, aligned_edge=LEFT, buff=0.2)
        tangente_box_new = SurroundingRectangle(VGroup(reta_tangente, limite_da_secante, melhor_comportamento_local), color=BLACK, buff=0.1)
        tangente_box_new.set_stroke(opacity=0.5, width=1)

        self.play(LaggedStart(
            Transform(tangente_box, tangente_box_new),
            Write(melhor_comportamento_local),
            lag_ratio=0.8
        ))

        self.wait(40)

        self.play(
            FadeOut(ffx0, example_box, example_label, example_label_sin, sine_graph, sine_plane, sine_tangent_line_equation, tangent_line, zero_tick, zero_label, aprox_1, aprox_2)
        )
 
    def create_pi_ticks_with_labels(self, positions, plane):
        """Creates ticks and labels for positions at multiples of pi, with tolerance to avoid float precision errors."""
        ticks = VGroup()
        labels = VGroup()
        for pos in positions:
            # Add tick mark
            tick = Line(
                plane.c2p(pos, -0.1), plane.c2p(pos, 0.1),
                color=GRAY, stroke_width=1
            ).set_opacity(0.8)
            ticks.add(tick)

            # Define labels using np.isclose for robust comparison
            if np.isclose(pos, 0):
                label = MathTex("0")
            elif np.isclose(pos, PI):
                label = MathTex("\\pi")
            elif np.isclose(pos, -PI):
                label = MathTex("-\\pi")
            elif np.isclose(pos, PI / 2):
                label = MathTex("\\frac{\\pi}{2}")
            elif np.isclose(pos, -PI / 2):
                label = MathTex("-\\frac{\\pi}{2}")
            elif np.isclose(pos, PI / 4):
                label = MathTex("\\frac{\\pi}{4}")
            elif np.isclose(pos, -PI / 4):
                label = MathTex("-\\frac{\\pi}{4}")
            elif np.isclose(pos, 3 * PI / 4):
                label = MathTex("\\frac{3\\pi}{4}")
            elif np.isclose(pos, -3 * PI / 4):
                label = MathTex("-\\frac{3\\pi}{4}")
            elif np.isclose(pos, 3 * PI / 2):
                label = MathTex("\\frac{3\\pi}{2}")
            elif np.isclose(pos, -3 * PI / 2):
                label = MathTex("-\\frac{3\\pi}{2}")
            else:
                # General case for integer multiples of pi
                multiple = round(pos / PI)
                label = MathTex(f"{multiple}\\pi")

            # Position label under the tick
            label.scale(0.5).next_to(tick, DOWN).set_opacity(0.8).set_color(BLACK)
            labels.add(label)

        return ticks, labels

    