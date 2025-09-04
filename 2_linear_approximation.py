from manim import *
from utils import *

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
    BG_COLOR = "#FCF2E0"
    PRIMARY_COLOR = BLACK
    ARROW_COLOR = GRAY_E
    ERROR_COLOR = RED
    SPECIAL_FUNC_COLOR = rgb_to_color(hex_to_rgb("#C00000"))
    TANGENT_LINE_GREEN = GREEN
    TANGENT_LINE_BLUE = BLUE

class linear_approximation(Scene):
    CONFIG = {
        "camera_config": {"frame_rate": 60},
    }

    def construct(self):
        # Set background color
        self.camera.background_color = "#FAE6C2"

        # Title label for the tangent line
        tangent_line_label = Text("Reta Tangente").set_color(BLACK)
        tangent_line_label.to_edge(UP).shift(DOWN * 1.5)
        self.play(Write(tangent_line_label), run_time=1.5)
        self.wait(0.5)

        # Create a NumberPlane for graphing
        number_plane = NumberPlane(
            x_range=(-4, 8),
            y_range=(-2, 2),
            axis_config={"stroke_width": 0, "color": PRIMARY_COLOR},
            background_line_style={"stroke_color": PRIMARY_COLOR, "stroke_width": 0, "stroke_opacity": 0}
        ).set_color(PRIMARY_COLOR)

        # Define the polynomial function and its derivative
        def polynomial_function(x):
            x_adjusted = x - 1.2
            return (x_adjusted + 1) * (x_adjusted - 2.5) * (x_adjusted - 4) / 10

        def derivative_function(x):
            x_adjusted = x - 1.2
            return 0.1 * (3 * x_adjusted**2 - 11 * x_adjusted + 3.5)

        # Plot the polynomial function
        polynomial_graph = number_plane.plot(polynomial_function, x_range=[-1.05, 6.51], color=rgb_to_color(hex_to_rgb("#C00000")))

        # Calculate points for the tangent line
        tangent_point_x = 1.2
        tangent_line_offset = 4
        dy_tan = derivative_function(tangent_point_x)
        fx_tan = polynomial_function(tangent_point_x)
        angle_tracker = ValueTracker(dy_tan)
        tangent_start = number_plane.coords_to_point(tangent_point_x - tangent_line_offset,  fx_tan - dy_tan * tangent_line_offset)
        tangent_end = number_plane.coords_to_point(tangent_point_x + tangent_line_offset, fx_tan + dy_tan * tangent_line_offset)

        # Create the tangent line
        tangent_line = Line(start=tangent_start, end=tangent_end, color=BLACK)
        tangent_line.add_updater(lambda line: line.put_start_and_end_on(
            number_plane.coords_to_point(tangent_point_x - tangent_line_offset, polynomial_function(tangent_point_x) - angle_tracker.get_value() * tangent_line_offset),
            number_plane.coords_to_point(tangent_point_x + tangent_line_offset, polynomial_function(tangent_point_x) + angle_tracker.get_value() * tangent_line_offset)
        ))

        # Group the graph and tangent line
        graph_container = VGroup(number_plane, polynomial_graph, tangent_line)
        graph_container.scale(0.6).move_to(DOWN * 1.5)

        # Show the graph and tangent line
        self.play(FadeIn(graph_container))
        self.wait(1)

        # Position and animate the "Reta Tangente" label
        self.play(
            tangent_line_label.animate.scale(0.5).to_corner(UR, buff=0.5),
        )

        # Create a bounding box around the label
        label_box = SurroundingRectangle(tangent_line_label, color=BLACK, buff=0.1)
        label_box.set_stroke(opacity=0.5, width=1)

        # Add "Derivada" text where the "Reta Tangente" label was originally
        derivative_label = Text("Derivada").set_color(BLACK)
        derivative_label.to_edge(UP).shift(DOWN * 1.5)
        self.play(Create(label_box), Write(derivative_label))
        self.wait(0.5)

        # Position "Derivada" below "Reta Tangente" in the corner
        self.play(
            derivative_label.animate.scale(0.5).next_to(tangent_line_label, DOWN, buff=0.2),
            run_time=1.5
        )

        # Expand bounding box to fit both labels
        combined_label_box = SurroundingRectangle(VGroup(tangent_line_label, derivative_label), color=BLACK, buff=0.2)
        combined_label_box.set_stroke(opacity=0.5, width=1)
        self.wait(0.5)

        # Introduce "Aproximação Linear" label at the top
        linear_approximation_label = Text("Aproximação Linear").set_color(BLACK)
        linear_approximation_label.to_edge(UP).shift(DOWN * 1.5)
        self.play(Write(linear_approximation_label), Transform(label_box, combined_label_box))

        # Shorten label and position it below "Derivada"
        linear_approximation_short = Text("Aprox Linear").set_color(BLACK).scale(0.5)
        linear_approximation_short.next_to(derivative_label, DOWN, buff=0.2)
        self.play(
            linear_approximation_label.animate.scale(0.5).next_to(derivative_label, DOWN, buff=0.2),
            Transform(linear_approximation_label, linear_approximation_short),
            run_time=1
        )

        # Expand bounding box to fit all three labels
        final_label_box = SurroundingRectangle(VGroup(tangent_line_label, derivative_label, linear_approximation_short), color=BLACK, buff=0.2)
        final_label_box.set_stroke(opacity=0.5, width=1)
        self.play(Transform(label_box, final_label_box), run_time=0.5)

        self.wait(5)
        self.play(Indicate(linear_approximation_label, color=SPECIAL_FUNC_COLOR))
        
        linear_approximation_label_full = Text("Aproximação Linear").set_color(BLACK)
        linear_approximation_label_full.scale(0.5).to_corner(UR, buff=0.5)
        final_label_box = SurroundingRectangle(linear_approximation_label_full, color=BLACK, buff=0.2)
        final_label_box.set_stroke(opacity=0.5, width=1)


        # Fade out previous elements
        self.play(Transform(label_box, final_label_box), FadeOut(tangent_line_label), FadeOut(derivative_label), Transform(linear_approximation_label, linear_approximation_label_full), run_time=1)
        self.wait(6)

        self.play(
            polynomial_graph.animate(rate_func=rate_functions.ease_in_out_sine).scale(5, about_point=number_plane.coords_to_point(tangent_point_x, fx_tan)),
            run_time = 3
        )

        self.play(
            angle_tracker.animate(rate_func=rate_functions.ease_in_out_sine).set_value(0.8*dy_tan),
            run_time = 1.5
        )
        self.play(
            angle_tracker.animate(rate_func=rate_functions.ease_in_out_sine).set_value(1.2*dy_tan),
            run_time = 1.5
        )

        self.play(FadeOut(graph_container))

        # Set up and display the sine graph from -2pi to 2pi
        sine_plane = NumberPlane(
            x_range=(-2 * PI, 2 * PI),
            y_range=(-1.5, 1.5),
            axis_config={"stroke_color": PRIMARY_COLOR, "stroke_width": 1},
            background_line_style={"stroke_color": PRIMARY_COLOR, "stroke_width": 1, "stroke_opacity": 0.5}
        ).set_color(PRIMARY_COLOR)

        # Create initial pi-based ticks and labels
        pi_ticks, pi_labels = self.create_pi_ticks_with_labels(np.arange(-2 * PI, 2 * PI + 0.1, PI / 4), sine_plane)
        sine_plane.x_axis.add(pi_ticks, pi_labels)

        # Plot and show sine graph
        sine_graph = sine_plane.plot(np.sin, x_range=[-2 * PI, 2 * PI], color=SPECIAL_FUNC_COLOR)
        self.play(FadeIn(sine_plane), Create(sine_graph), run_time=2)
        sine_label = MathTex("f(x)=sin(x)").set_color(BLACK)
        sine_label.to_edge(UP).shift(DOWN * 1.5)
        self.play(Write(sine_label), run_time=1.5)
        self.wait(8)

        # Zoom in by scaling around the origin
        zoom_factor = 3
        _ = sine_label.copy()
        _.scale(0.75).to_corner(UL, buff=0.5)
        sine_label_box = SurroundingRectangle(_, color=BLACK, buff=0.2).set_stroke(opacity=0.5, width=1)
        self.play(
            FadeOut(pi_ticks),
            FadeOut(pi_labels),
            LaggedStart(sine_label.animate.scale(0.75).to_corner(UL, buff=0.5), FadeIn(sine_label_box), lag_ratio=0.4),
            sine_plane.animate.scale(zoom_factor, about_point=sine_plane.c2p(0, 0)),
            sine_graph.animate.scale(zoom_factor, about_point=sine_plane.c2p(0, 0)),
            run_time=4
        )

        # Add tick and label at x = 0.4 after scaling
        decimal_tick_04 = Line(
            sine_plane.c2p(0.4, -0.1), sine_plane.c2p(0.4, 0.1),
            color=PRIMARY_COLOR, stroke_width=1
        )
        label_04 = MathTex("0.4", color=PRIMARY_COLOR).scale(0.5).next_to(decimal_tick_04, DOWN)
        label_04.add_updater(lambda m: m.next_to(decimal_tick_04, DOWN))
        sine_plane.x_axis.add(decimal_tick_04, label_04)

        self.wait(5)

        # Add the line y = x to the sine plane
        y_equals_x_line = sine_plane.plot(lambda x: x, x_range=[-1, 1], color=TANGENT_LINE_BLUE)
        line_label = MathTex("y=r(x)=x", font_size=26).set_color(PRIMARY_COLOR).next_to(y_equals_x_line, UP, buff=0.2).shift(1.5*RIGHT)
        self.play(Create(y_equals_x_line), Write(line_label), run_time=2)

        self.wait(2)

        self.play(FadeIn(decimal_tick_04), FadeIn(label_04))
        self.wait(8)

        self.play(FadeOut(decimal_tick_04, label_04), FadeOut(y_equals_x_line, line_label), FadeOut(sine_label, sine_label_box))

        self.wait(8)

    def create_pi_ticks_with_labels(self, positions, plane):
        """Creates ticks and labels for positions at multiples of pi, with tolerance to avoid float precision errors."""
        ticks = VGroup()
        labels = VGroup()
        for pos in positions:
            # Add tick mark
            tick = Line(
                plane.c2p(pos, -0.1), plane.c2p(pos, 0.1),
                color=PRIMARY_COLOR, stroke_width=1
            )
            ticks.add(tick)

            # Define labels using np.isclose for robust comparison
            if np.isclose(pos, 0):
                label = MathTex("0", color=PRIMARY_COLOR)
            elif np.isclose(pos, PI):
                label = MathTex("\\pi", color=PRIMARY_COLOR)
            elif np.isclose(pos, -PI):
                label = MathTex("-\\pi")
            elif np.isclose(pos, PI / 2):
                label = MathTex("\\frac{\\pi}{2}", color=PRIMARY_COLOR)
            elif np.isclose(pos, -PI / 2):
                label = MathTex("-\\frac{\\pi}{2}", color=PRIMARY_COLOR)
            elif np.isclose(pos, PI / 4):
                label = MathTex("\\frac{\\pi}{4}", color=PRIMARY_COLOR)
            elif np.isclose(pos, -PI / 4):
                label = MathTex("-\\frac{\\pi}{4}", color=PRIMARY_COLOR)
            elif np.isclose(pos, 3 * PI / 4):
                label = MathTex("\\frac{3\\pi}{4}", color=PRIMARY_COLOR)
            elif np.isclose(pos, -3 * PI / 4):
                label = MathTex("-\\frac{3\\pi}{4}", color=PRIMARY_COLOR)
            elif np.isclose(pos, 3 * PI / 2):
                label = MathTex("\\frac{3\\pi}{2}", color=PRIMARY_COLOR)
            elif np.isclose(pos, -3 * PI / 2):
                label = MathTex("-\\frac{3\\pi}{2}", color=PRIMARY_COLOR)
            else:
                # General case for integer multiples of pi
                multiple = round(pos / PI)
                label = MathTex(f"{multiple}\\pi", color=PRIMARY_COLOR)

            # Position label under the tick
            label.scale(0.5).next_to(tick, DOWN)
            labels.add(label)

        return ticks, labels

    
