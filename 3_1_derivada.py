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
    BG_COLOR = "#FAE6C2"
    PRIMARY_COLOR = BLACK
    ARROW_COLOR = GRAY_E
    ERROR_COLOR = RED
    SPECIAL_FUNC_COLOR = rgb_to_color(hex_to_rgb("#C00000"))
    TANGENT_LINE_GREEN = GREEN
    TANGENT_LINE_BLUE = BLUE

class derivada_1(Scene):
    def construct(self):
        # Set up the background color for the scene
        self.camera.background_color = BG_COLOR

        # Create the coordinate plane with faint grid lines and black axes
        plane = NumberPlane(
            x_range=(-4, 8),
            y_length=7,
            axis_config={"color": BLACK},
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 0.5,
                "stroke_opacity": 0.2
            }
        )

        # Add axis labels for x and f(x) (the y-axis)
        labels = plane.get_axis_labels(x_label="x", y_label="f(x)").set_color(BLACK)
        x_label = labels[0] # Extract y-axis label
        y_label = labels[1] # Extract y-axis label

        # Create a title label and position it in the center, then animate to upper right
        title_label = Text("Definição de Derivada", font_size=36).set_color(BLACK)
        title_label.to_edge(UP).shift(DOWN * 1.5)
        definicao_derivada = Text("*Inclinação da reta tangente", font_size=30).set_color(BLACK)
        definicao_derivada.next_to(title_label, DOWN)
        self.play(Write(title_label))
        self.play(Write(definicao_derivada))
        self.wait(1)

        aux1 = title_label.copy()
        aux1.scale(0.5).to_corner(UR, buff=0.5),
        aux2 = definicao_derivada.copy()
        aux2.scale(0.5).next_to(aux1, DOWN, buff=0.2)

        # Draw a rectangle around the title for emphasis
        title_box = SurroundingRectangle(VGroup(aux1, aux2), color=BLACK, buff=0.1)
        title_box.set_stroke(opacity=0.5, width=1)

        
        # Define the polynomial function and its derivative for plotting
        def polynomial(x):
            x = x - 1.2
            return (x + 1) * (x - 2.5) * (x - 4) / 10

        def derivative(x):
            x = x - 1.2
            return 0.1 * (3 * x**2 - 11 * x + 3.5)

        # Plot the polynomial function in red on the plane
        function_graph = plane.plot(polynomial, x_range=[-1.05, 6.51], color=rgb_to_color(hex_to_rgb("#C00000")))

        # Animate title to move to  the top right and shrink
        self.play(LaggedStart(
            AnimationGroup(
                title_label.animate.scale(0.5).to_corner(UR, buff=0.5),
                definicao_derivada.animate.scale(0.5).next_to(aux1, DOWN, buff=0.2),
            ),
            Create(title_box),
            lag_ratio = 0.5
        ))

        self.wait(1)

        self.play(Create(plane), FadeIn(labels))
        self.play(FadeIn(function_graph))
        self.wait(1)

        # Initial x-value and initial delta x for secant line
        x0 = 0.5
        delta_x_initial = 1
        y_initial = polynomial(x0)
        point_initial = plane.coords_to_point(x0, y_initial)

        # Create the first point (x_0) on the graph with label
        x0_dot = Dot(point=point_initial, color=BLACK, radius=0.04)
        x0_label = MathTex("x_0", font_size=24, color=BLACK).next_to(plane.coords_to_point(x0, 0), DOWN, buff=0.1)

        # Secondary point (x_0 + Δx) for secant line calculations
        xf = x0 + delta_x_initial
        yf = polynomial(xf)
        point_xf = plane.coords_to_point(xf, yf)

        # Create the secondary point and label it (x_0 + Δx)
        xf_dot = Dot(point=point_xf, color=BLACK, radius=0.04)
        xf_label = MathTex("x_0 + \\Delta x", font_size=24, color=BLACK).next_to(plane.coords_to_point(xf, 0), DOWN, buff=0.1)
        x0_label.align_to(xf_label, DOWN)

        x0_vertical_line = DashedLine(
            start=plane.coords_to_point(x0, 0),
            end=point_initial,
            color=GREY
        )

        # Draw a vertical dashed line to the secondary point
        xf_vertical_line = DashedLine(
            start=plane.coords_to_point(xf, 0),
            end=point_xf,
            color=GREY
        )

        self.play(LaggedStart(
            FadeIn(x0_vertical_line),
            FadeIn(x0_dot),
            FadeIn(x0_label),
            lag_ratio=0.3
        ))
        self.wait(1)

        self.play(LaggedStart(
            FadeIn(xf_vertical_line),
            FadeIn(xf_dot),
            FadeIn(xf_label),
            lag_ratio=0.3
        ))

        self.wait(1)

        # Secant line connecting the initial and secondary points
        secant_line = Line(start=point_initial, end=point_xf, color=TANGENT_LINE_BLUE).set_length(4)

        # Dashed line and label for Δx along the x-axis
        dx_line = DashedLine(
            start=plane.coords_to_point(x0 + 0.01, 0.1),
            end=plane.coords_to_point(xf - 0.01, 0.1),
            color=GREY
        )
        delta_x_label = MathTex(r"\Delta x", font_size=16, color=PRIMARY_COLOR).next_to(dx_line, UP, buff=0.1)
        secant_tangent_line_label = MathTex("r_{sec}", "\\approx","r_{tan}", font_size=24, color=PRIMARY_COLOR).next_to(secant_line, UR, buff=0.2).set_opacity(0)
        secant_tangent_line_label[0].set_opacity(1)

        self.play(FadeIn(dx_line), FadeIn(delta_x_label))
        self.wait(2)
        self.play(LaggedStart(
            Create(secant_line),
            Write(secant_tangent_line_label[0]),
            lag_ratio=0.5
        ))
        self.play(HighlightWithRect(secant_tangent_line_label[0], run_time=1.7))
        self.wait(0.5)

        # Tangent line at the initial point x_0
        tangent_dx_range = 0.7
        tangent_start = plane.coords_to_point(
            x0 - tangent_dx_range / 2,
            polynomial(x0) - derivative(x0) * tangent_dx_range / 2
        )
        tangent_end = plane.coords_to_point(
            x0 + tangent_dx_range,
            polynomial(x0) + derivative(x0) * tangent_dx_range
        )
        tangent_line = DashedLine(start=tangent_start, end=tangent_end, color=GREEN)


                # Error indication line and label
        secant_point = plane.coords_to_point(xf, y_initial + derivative(x0) * delta_x_initial)
        error_line = DashedLine(start=secant_point, end=point_xf, color=GREEN)
        error_brace = BraceLabel(error_line, "Erro", RIGHT, brace_config={'color':BLACK}, font_size=12)

        # ValueTracker for dynamic Δx adjustment and zoom
        delta_x_tracker = ValueTracker(delta_x_initial)
        scale_tracker = ValueTracker(1)

        # Add updaters to elements to dynamically adjust their position with changing Δx
        xf_label.add_updater(lambda mob: mob.next_to(plane.coords_to_point(x0 + delta_x_tracker.get_value(), 0), DOWN, buff=0.1).set_opacity(smooth_decay_np(delta_x_tracker.get_value())))

        x0_label.add_updater(lambda mob: mob.next_to(plane.coords_to_point(x0, 0), DOWN, buff=0.1).align_to(xf_label, DOWN) if delta_x_tracker.get_value() > 0.01 else mob.next_to(plane.coords_to_point(x0, 0), DOWN, buff=0.17))

        x0_vertical_line.add_updater(lambda line: line.put_start_and_end_on(
            plane.coords_to_point(x0, 0), plane.coords_to_point(x0, polynomial(x0)))
        )
        
        def decay_0_2_to_0(x):
            """
            Smoothly decreases from 0.2 (at x = 1) to 0 (at x = 3).
            Uses a smoothstep cubic interpolation.
            """
            x = np.clip(x, 1.0, 3.0)
            t = (x - 1.0) / 2.0  # Normalize so x=1 -> t=0 and x=3 -> t=1
            return 0.2 * (1 - (3 * t**2 - 2 * t**3))


        xf_vertical_line.add_updater(lambda line: line.put_start_and_end_on(
            plane.coords_to_point(x0 + delta_x_tracker.get_value(), 0), plane.coords_to_point(x0 + delta_x_tracker.get_value(), polynomial(x0 + delta_x_tracker.get_value())))
        )
        y_label.add_updater(lambda mob: mob.set_opacity(max(0, min(1, 1 - (scale_tracker.get_value() - 1) / 2))))
        x_label.add_updater(lambda mob: mob.set_opacity(max(0, min(1, 1 - (scale_tracker.get_value() - 1) / 2))))

        # Add updaters to fade the grid lines dynamically
        for line in plane.background_lines:
            line.add_updater(
                lambda mob: mob.set_stroke(opacity=decay_0_2_to_0(scale_tracker.get_value()))
            ) 


        def smooth_decay_np(x):
            x = np.clip(x, 0.1, 1.0)  # Clip values to the [0.1, 1] range
            t = (1 - x) / 0.9
            return 1 - (3 * t ** 2 - 2 * t ** 3)
        
        def cutoff_decay(x):
            """
            Returns 1 for x >= 0.1.
            For x < 0.1, smoothly decays from 1 to 0 as x approaches 0.
            """
            if x >= 0.1:
                return 1
            else:
                t = x / 0.1  # Normalize so x = 0.1 -> t = 1 and x = 0 -> t = 0
                return 3*t**2 - 2*t**3  # Smoothstep from 0 to 1, flip to go from 1 to 0


        x0_dot.add_updater(lambda mob: mob.move_to(plane.coords_to_point(x0, polynomial(x0))))
        xf_dot.add_updater(lambda mob: mob.move_to(plane.coords_to_point(
            x0 + delta_x_tracker.get_value(), polynomial(x0 + delta_x_tracker.get_value())
        )))
        secant_line.add_updater(lambda line: 
            line.put_start_and_end_on(
                plane.coords_to_point(x0, polynomial(x0)), plane.coords_to_point(x0 + delta_x_tracker.get_value(), polynomial(x0 + delta_x_tracker.get_value()))
            ).set_length(4)
        )
        secant_tangent_line_label.add_updater(lambda mob: mob.next_to(secant_line, UR, buff=0.2))
        tangent_line.add_updater(lambda mob: mob.put_start_and_end_on(
            point_initial, plane.coords_to_point(x0 + delta_x_tracker.get_value(), polynomial(x0) + derivative(x0) * delta_x_tracker.get_value())
        ))
        error_line.add_updater(lambda line: line.put_start_and_end_on(
            plane.coords_to_point(x0 + delta_x_tracker.get_value(), y_initial + derivative(x0) * delta_x_tracker.get_value()),
            plane.coords_to_point(x0 + delta_x_tracker.get_value(), polynomial(x0 + delta_x_tracker.get_value()))
        ))
        dx_line.add_updater(lambda line: 
            line.put_start_and_end_on(
                plane.coords_to_point(x0 + 0.01, 0.1/scale_tracker.get_value()),
                plane.coords_to_point(x0 + delta_x_tracker.get_value() - 0.01, 0.1/scale_tracker.get_value())
            ).set_opacity(cutoff_decay(delta_x_tracker.get_value()))
        )
        delta_x_label.add_updater(lambda label: label.next_to(dx_line, UP, buff=0.1).set_opacity(cutoff_decay(delta_x_tracker.get_value())))
        error_brace.add_updater(lambda mob: mob.become(BraceLabel(error_line, "Erro", RIGHT, brace_config={'color':BLACK}, font_size=12)))

        graph_group = VGroup(plane, function_graph, labels, secant_tangent_line_label)
        self.play(
            graph_group.animate(rate_func=rate_functions.ease_in_out_sine).shift(LEFT)
        )

        # self.play(FadeIn(tangent_line))
        self.wait(3.5)


        # Define the initial equation
        identity_sec = MathTex(" ", "a_{sec}", " ", "=", " ", "\\frac{\Delta y}{\Delta x}", font_size=24).set_color(BLACK)
        identity_sec.move_to([0.35 * config.frame_width / 2, -0.3 * config.frame_height / 2, 0])

        left_side = MathTex(" ", "a_{sec}", " ", "=", " ", "\\frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}", font_size=24).set_color(BLACK)
        left_side.set_y(identity_sec.get_y())  # Match the y-position with the original equation
        left_side.align_to(identity_sec, RIGHT)  # Align to the right
    

        # Define where "a_{sec}" should move to in the transformed equation's layout
        # Create a dummy transformed equation for reference (not displayed)
        left_side_2 = MathTex("\lim_{\Delta x \\to 0}", "a_{sec}", "(\Delta x)", "=", "\lim_{\Delta x \\to 0}", "\\frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}", font_size=24).set_color(BLACK)
        left_side_2.set_y(left_side.get_y())  # Match the y-position with the original equation
        left_side_2.align_to(left_side, RIGHT)  # Align to the right

        # Define where "a_{sec}" should move to in the transformed equation's layout
        # Create a dummy transformed equation for reference (not displayed)
        left_side_3 = MathTex("a_{tan}", "=" , "f'(x_0)", "=", "\lim_{\Delta x \\to 0}", "\\frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}", font_size=24).set_color(BLACK)
        left_side_3.set_y(left_side.get_y())  # Match the y-position with the original equation
        left_side_3.align_to(left_side, RIGHT)  # Align to the right


        # Extract the new position for "a_{sec}" in the transformed layout
        n_position = {}
        n_position[1] = left_side[1].get_center()
        n_position[3] = left_side[3].get_center()
        n_position[5] = left_side[5].get_center()



        # Display the initial equation
        self.play(FadeIn(identity_sec))
        self.wait(1)
        self.play(HighlightWithRect(VGroup(identity_sec[5][0], identity_sec[5][1]), buff=0.05))
        self.wait(0.2)
        self.play(HighlightWithRect(VGroup(identity_sec[5][3], identity_sec[5][4]), buff=0.05))
        self.wait(2)
        self.play(HighlightWithRect(identity_sec[1]))


        # Animate "a_{sec}" moving to its new position
        self.play(
            identity_sec[1].animate.move_to(n_position[1]),
            identity_sec[3].animate.move_to(n_position[3]),
            identity_sec[5].animate.move_to(n_position[5]), run_time=1
        )
        self.play(FadeOut(identity_sec),FadeIn(left_side), run_time=1)
        
        self.wait(6.5)

        # Animate the shrinking of Δx and the zoom effect
        # Zoom in by scaling around the origin
        zoom_factor = 3
        self.play(
            delta_x_tracker.animate.set_value(0.01),
            function_graph.animate.scale(zoom_factor, about_point=point_initial),
            scale_tracker.animate.set_value(3),
            plane.animate.scale(zoom_factor, about_point=point_initial),
            left_side.animate.shift(DOWN),
            run_time=10
        )
        self.wait(6.2)
    
        left_side_2.set_y(left_side.get_y())  # Match the y-position with the original equation
        left_side_2.align_to(left_side, RIGHT)  # Align to the right

        left_side_3.set_y(left_side.get_y())  # Match the y-position with the original equation
        left_side_3.align_to(left_side, RIGHT)  # Align to the right

        new_position = {}
        new_position[1] = left_side_2[1].get_center()
        new_position[3] = left_side_2[3].get_center()

        new_position_1 = {}
        new_position_1[1] = left_side_3[0].get_center()
        new_position_1[3] = left_side_3[1].get_center()

        secant_tangent_line_label[1].set_opacity(1)
        secant_tangent_line_label[2].set_opacity(1)

        dx_tends_zero = MathTex("\\Delta x \\to 0", font_size=24).set_color(BLACK).next_to(secant_tangent_line_label, UP, aligned_edge=LEFT)

        reta_tangente = Text("Reta Tangente", font_size=36).set_color(BLACK).scale(0.5).next_to(definicao_derivada, DOWN, buff=0.5)
        limite_da_secante = Text("*Limite das retas secantes", font_size=30).set_color(BLACK).scale(0.5).next_to(reta_tangente, DOWN,buff=0.2).align_to(definicao_derivada, LEFT)

        tangente_box = SurroundingRectangle(VGroup(reta_tangente, limite_da_secante), color=BLACK, buff=0.1)
        tangente_box.set_stroke(opacity=0.5, width=1)


        self.play(LaggedStart(FadeIn(secant_tangent_line_label[1], shift=LEFT), FadeIn(secant_tangent_line_label[2], shift=LEFT), lag_ratio=0.4))
        self.play(
            Write(dx_tends_zero),
            Write(reta_tangente),
            FadeIn(limite_da_secante),
            Create(tangente_box)
        )
        # Animate "a_{sec}" moving to its new position
        self.wait(2.8)
        self.play(
            left_side[1].animate.move_to(new_position[1]),
            left_side[3].animate.move_to(new_position[3])
        )
        self.play(FadeOut(left_side),FadeIn(left_side_2), run_time=1)

        self.wait(2)

        # Animate "a_{sec}" moving to its new position
        self.play(
            FadeOut(left_side_2[0],run_time=0.4), FadeOut(left_side_2[2],run_time=0.4),
            left_side_2[1].animate.move_to(new_position_1[1]),
            left_side_2[3].animate.move_to(new_position_1[3]),
            FadeOut(left_side_2[1], run_time=4), FadeOut(left_side_2[3]), FadeOut(left_side_2[4]), FadeOut(left_side_2[5]), FadeIn(left_side_3, run_time=4), run_time=2
        )
        self.wait(0.5)
        
        _ = left_side_3.copy()
        _.scale(0.8).to_corner(DR, buff=0.8)
        # Draw a rectangle around the final equation
        eq_box_ = SurroundingRectangle(_, color=BLACK, buff=0.1)
        eq_box_.set_stroke(opacity=0.5, width=1)

         # Animate the last equation shrinking and moving to the bottom-left corner
        self.play(LaggedStart(
            left_side_3.animate.scale(0.8).to_corner(DR, buff=0.8),
            Create(eq_box_),
            lag_ratio=0.8
        ))

        # Hold the scene
        self.wait(1)
        
        # Create the new equation tangent_line_equation
        tangent_line_equation = MathTex("r_{tan}(x)", "=", "a_{tan}","x", "+", "b_{tan}", font_size=24).set_color(BLACK)
        tangent_line_equation.next_to(identity_sec, LEFT, aligned_edge=LEFT).shift(DOWN)
        tangent_line_equation_copy = tangent_line_equation.copy()
        

        # Store the original position
        original_position = tangent_line_equation.get_center()

        # # Create the new equation
        tangent_line_equation2 = MathTex("r_{tan}(x)", "=", "f'(x_{0})","x", "+", "b_{tan}", font_size=24).set_color(BLACK)
        tangent_line_equation2.set_y(tangent_line_equation.get_y())  # Match the y-position with the original equation
        tangent_line_equation2.align_to(tangent_line_equation, RIGHT)  # Align to the right

        # # Create the new equation
        tangent_line_equation3 = MathTex("f(x_{0})", "=", "f'(x_{0})","x_{0}", "+", "b_{tan}", font_size=24).set_color(BLACK)
        tangent_line_equation3.set_y(tangent_line_equation.get_y())  # Match the y-position with the original equation
        tangent_line_equation3.align_to(tangent_line_equation, RIGHT)  # Align to the right

        # # Create the new equation
        tangent_line_equation4 = MathTex("f(x_{0})", "-", "f'(x_{0})","x_{0}", "=", "b_{tan}", font_size=24).set_color(BLACK)
        tangent_line_equation4.set_y(tangent_line_equation.get_y())  # Match the y-position with the original equation
        tangent_line_equation4.align_to(tangent_line_equation, RIGHT)  # Align to the right

        # # Create the new equation
        tangent_line_equation5 = MathTex("b_{tan}","=", "f(x_{0})", "-", "f'(x_{0})","x_{0}", font_size=24).set_color(BLACK)
        tangent_line_equation5.set_y(tangent_line_equation.get_y())  # Match the y-position with the original equation
        tangent_line_equation5.align_to(tangent_line_equation, RIGHT)  # Align to the right

        new_position_eq = {}
        new_position_eq[0] = tangent_line_equation2[0].get_center()
        new_position_eq[1] = tangent_line_equation2[1].get_center()

        new_position_eq1 = {}
        new_position_eq1[1] = tangent_line_equation3[1].get_center()
        new_position_eq1[2] = tangent_line_equation3[2].get_center()

        new_position_eq2 = {}
        new_position_eq2[0] = tangent_line_equation4[0].get_center()
        new_position_eq2[2] = tangent_line_equation4[2].get_center()
        new_position_eq2[3] = tangent_line_equation4[3].get_center()


        # Animate the display of the new equation
        self.wait(5)
        self.play(Write(tangent_line_equation), run_time=2)

        self.wait(1.5)
        self.play(LaggedStart(
            Indicate(tangent_line_equation[0],scale_factor=1.2, color="#C00000"),
            Indicate(tangent_line_equation[2],scale_factor=1.2, color="#C00000"),
            Indicate(tangent_line_equation[5],scale_factor=1.2, color="#C00000"),
            lag_ratio=0.6
        ))

        self.wait(0.5)

        _ = tangent_line_equation_copy.copy()
        _.scale(0.8).next_to(left_side_3, UP, buff=0.2)

        eq_box = SurroundingRectangle(VGroup(_, left_side_3), color=BLACK, buff=0.2)
        eq_box.set_stroke(opacity=0.5, width=1)
        
        self.play(LaggedStart(
            tangent_line_equation_copy.animate.scale(0.8).next_to(left_side_3, UP, buff=0.2).set_opacity(1),
            Transform(eq_box_, eq_box),
            lag_ratio=0.6
        ))
        self.wait(0.5)

        self.play(
            Indicate(VGroup(left_side_3[0], left_side_3[1], left_side_3[2]), scale_factor=1.2, color="#C00000")
        )
        
        self.wait(1)
        self.play(Indicate(tangent_line_equation[2], scale_factor=1.2, color="#C00000"))

        self.wait(2)

        self.play(LaggedStart(
            AnimationGroup(
                ReplacementTransform(tangent_line_equation[0], tangent_line_equation2[0]),
                ReplacementTransform(tangent_line_equation[1], tangent_line_equation2[1]),
            ),
            AnimationGroup(
                FadeIn(tangent_line_equation2[2], shift=DOWN),
                FadeIn(tangent_line_equation2[3]),
                FadeIn(tangent_line_equation2[4]),
                FadeIn(tangent_line_equation2[5]),
                FadeOut(tangent_line_equation[2], run_time=0.5),
                FadeOut(tangent_line_equation[3]),
                FadeOut(tangent_line_equation[4]),
                FadeOut(tangent_line_equation[5]),
            ),
            lag_ratio=0.4  
        ))
        self.wait(7)

        fx0_horizontal_line = DashedLine(
            start=plane.coords_to_point(0, polynomial(x0)),
            end=plane.coords_to_point(x0, polynomial(x0)),
            color=GREY
        )
        fx0_label = MathTex("f(x_0)", font_size=24, color=PRIMARY_COLOR).next_to(plane.coords_to_point(0, polynomial(x0)), LEFT, buff=0.1)
        self.play(
            HighlightWithRect(tangent_line_equation2)
        )

        self.wait(2)

        p_x0_fx0_label = MathTex("P=(x_0, f(x_0))", font_size=24, color=PRIMARY_COLOR).next_to(tangent_line_equation, UP, buff=0.4)
        self.play(LaggedStart(
            Create(fx0_horizontal_line),
            Write(fx0_label),
            lag_ratio=0.8
        ))
        
        self.wait(3)
        self.play(
            Write(p_x0_fx0_label)
        )


        self.wait(4)
        # Animate "a_{sec}" moving to its new position
        self.play(
            tangent_line_equation2[1].animate.move_to(new_position_eq1[1]),
            tangent_line_equation2[2].animate.move_to(new_position_eq1[2]),
            FadeIn(tangent_line_equation3[0], shift=DOWN),
            FadeIn(tangent_line_equation3[3], shift=DOWN),
            FadeIn(tangent_line_equation3[4]),
            FadeIn(tangent_line_equation3[5]),
            FadeOut(tangent_line_equation2[0], run_time=0.5),
            FadeOut(tangent_line_equation2[3], run_time=0.5),
            FadeOut(tangent_line_equation2[4]),
            FadeOut(tangent_line_equation2[5]),
            run_time=1
        )

        self.play(
            FadeIn(tangent_line_equation3[1]),
            FadeIn(tangent_line_equation3[2]),
            FadeOut(tangent_line_equation2[1]),
            FadeOut(tangent_line_equation2[2]),
        )

        self.wait(5.2)

        # Animate "a_{sec}" moving to its new position
        self.play(
            tangent_line_equation3[0].animate.move_to(new_position_eq2[0]),
            tangent_line_equation3[2].animate.move_to(new_position_eq2[2]),
            tangent_line_equation3[3].animate.move_to(new_position_eq2[3]),
            Transform(tangent_line_equation3[4], tangent_line_equation4[1], path_arc=120*DEGREES),
            Transform(tangent_line_equation3[1], tangent_line_equation4[4], path_arc=120*DEGREES),
            FadeIn(tangent_line_equation4[5]),
            FadeOut(tangent_line_equation3[5]),
            run_time=1
        )
        self.play(
            FadeIn(tangent_line_equation4[1]),
            FadeIn(tangent_line_equation4[0]),
            FadeIn(tangent_line_equation4[2]),
            FadeIn(tangent_line_equation4[3]),
            FadeIn(tangent_line_equation4[4]),
            FadeOut(tangent_line_equation3[0]),
            FadeOut(tangent_line_equation3[2]),
            FadeOut(tangent_line_equation3[3]),
            FadeOut(tangent_line_equation3[4]),
            FadeOut(tangent_line_equation3[1]),
            run_time=1
        )

        self.play(
            HighlightWithRect(tangent_line_equation4)
        )

        self.play(Transform(tangent_line_equation4, tangent_line_equation5))

        _ = tangent_line_equation4.copy()
        _.scale(0.8).next_to(left_side_3, DOWN, buff=0.2)

        # Expand bounding box to fit all three labels
        final_label_box = SurroundingRectangle(VGroup(tangent_line_equation_copy, left_side_3, _), color=BLACK, buff=0.2)
        final_label_box.set_stroke(opacity=0.5, width=1)

         # Animate the last equation shrinking and moving to the bottom-left corner
        self.play(LaggedStart(
            tangent_line_equation4.animate.scale(0.8).next_to(left_side_3, DOWN, buff=0.2).set_opacity(1),
            Transform(eq_box_, final_label_box),
            lag_ratio=0.6,
        ))

        self.wait(1)


        tangent_line_equation = tangent_line_equation_copy.copy()
        self.play(
            tangent_line_equation.animate.scale(1.25).move_to(original_position)
        )

        tangent_line_equation_w_a = MathTex("r_{tan}(x)", "=", "f'(x_{0})","x", "+", "b_{tan}", font_size=24).set_color(BLACK)
        tangent_line_equation_w_a.set_y(tangent_line_equation.get_y())  # Match the y-position with the original equation
        tangent_line_equation_w_a.align_to(tangent_line_equation, RIGHT)  # Align to the right
        tangent_line_equation_w_a_keep = VGroup(
            tangent_line_equation_w_a[0],
            tangent_line_equation_w_a[1],
            tangent_line_equation_w_a[2],
            tangent_line_equation_w_a[3],
            tangent_line_equation_w_a[4],
        )

        self.play(
            tangent_line_equation[0].animate.move_to(new_position_eq[0]),
            tangent_line_equation[1].animate.move_to(new_position_eq[1]),
            FadeIn(tangent_line_equation_w_a[2], shift=DOWN),
            FadeIn(tangent_line_equation_w_a[3]),
            FadeIn(tangent_line_equation_w_a[4]),
            FadeIn(tangent_line_equation_w_a[5]),
            FadeOut(tangent_line_equation[2], run_time=0.5),
            FadeOut(tangent_line_equation[3]),
            FadeOut(tangent_line_equation[4]),
            FadeOut(tangent_line_equation[5]),
            run_time=1
        )

        self.play(
            FadeIn(tangent_line_equation_w_a[0]),
            FadeIn(tangent_line_equation_w_a[1]),
            FadeOut(tangent_line_equation[0], run_time=0.6),
            FadeOut(tangent_line_equation[1], run_time=0.6),
            run_time=1.5
        )

        tangent_line_equation_w_a_b = MathTex("r_{tan}(x)", "=", "f'(x_{0})","x", "+", "f(x_{0})", "-", "f'(x_{0})","x_{0}", font_size=24).set_color(BLACK)
        tangent_line_equation_w_a_b2 = MathTex("r_{tan}(x)", "=", "f(x_{0})", "+", "f'(x_{0})","x", "-", "f'(x_{0})","x_{0}", font_size=24).set_color(BLACK)
        tangent_line_equation_w_a_b3 = MathTex("r_{tan}(x)", "=", "f(x_{0})", "+", "f'(x_{0})","(","x", "-","x_{0}",")", font_size=24).set_color(BLACK)
        tangent_line_equation_w_a_b4 = MathTex("r_{tan}(x)", "=", "f(x_{0})", "+", "f'(x_{0})","\Delta x", font_size=24).set_color(BLACK)
        tangent_line_equation_w_a_b5 = MathTex("r_{tan}(x_0 + \Delta x)", "=", "f(x_{0})", "+", "\Delta x", "f'(x_{0})",font_size=24).set_color(BLACK)
        tangent_line_equation_w_a_b_add_in = VGroup(tangent_line_equation_w_a_b[5],tangent_line_equation_w_a_b[6],tangent_line_equation_w_a_b[7],tangent_line_equation_w_a_b[8])
        tangent_line_equation_w_a_b3_brackets = VGroup(tangent_line_equation_w_a_b3[5], tangent_line_equation_w_a_b3[9])
        tangent_line_equation_w_a_b2_keep = VGroup(tangent_line_equation_w_a_b2[0],tangent_line_equation_w_a_b2[1],tangent_line_equation_w_a_b2[2],tangent_line_equation_w_a_b2[3], tangent_line_equation_w_a_b2[4])
        tangent_line_equation_w_a_b3_keep = VGroup(tangent_line_equation_w_a_b3[0],tangent_line_equation_w_a_b3[1],tangent_line_equation_w_a_b3[2],tangent_line_equation_w_a_b3[3], tangent_line_equation_w_a_b3[4])
        tangent_line_equation_w_a_b3_transform = VGroup(tangent_line_equation_w_a_b3[5], tangent_line_equation_w_a_b3[6],tangent_line_equation_w_a_b3[7], tangent_line_equation_w_a_b3[8], tangent_line_equation_w_a_b3[9])

        tangent_line_equation_w_a_b.set_y(tangent_line_equation.get_y())  # Match the y-position with the original equation
        tangent_line_equation_w_a_b2.set_y(tangent_line_equation.get_y())  # Match the y-position with the original equation
        tangent_line_equation_w_a_b3.set_y(tangent_line_equation.get_y())  # Match the y-position with the original equation
        tangent_line_equation_w_a_b4.set_y(tangent_line_equation.get_y())  # Match the y-position with the original equation
        tangent_line_equation_w_a_b5.set_y(tangent_line_equation.get_y())  # Match the y-position with the original equation

        tangent_line_equation_w_a_b.align_to(tangent_line_equation, RIGHT)  # Align to the right
        tangent_line_equation_w_a_b2.align_to(tangent_line_equation, RIGHT)  # Align to the right
        tangent_line_equation_w_a_b3.align_to(tangent_line_equation, RIGHT)  # Align to the right
        tangent_line_equation_w_a_b4.align_to(tangent_line_equation, RIGHT)  # Align to the right
        tangent_line_equation_w_a_b5.align_to(tangent_line_equation, RIGHT)  # Align to the right   


        self.play(
            tangent_line_equation_w_a_keep.animate.align_to(tangent_line_equation_w_a_b, LEFT),
            FadeIn(tangent_line_equation_w_a_b_add_in, shift=DOWN),
            FadeOut(tangent_line_equation_w_a[5])
        )
        self.play(
            FadeOut(tangent_line_equation_w_a_keep),
            FadeIn(tangent_line_equation_w_a_b[0]),
            FadeIn(tangent_line_equation_w_a_b[1]),
            FadeIn(tangent_line_equation_w_a_b[2]),
            FadeIn(tangent_line_equation_w_a_b[3]),
            FadeIn(tangent_line_equation_w_a_b[4])
        )

        self.play(
            tangent_line_equation_w_a_b[5].animate.move_to(tangent_line_equation_w_a_b2[2]),
            tangent_line_equation_w_a_b[2].animate.move_to(tangent_line_equation_w_a_b2[4]),
            tangent_line_equation_w_a_b[3].animate.move_to(tangent_line_equation_w_a_b2[5]),
            tangent_line_equation_w_a_b[4].animate.move_to(tangent_line_equation_w_a_b2[3])
        )
        self.play(
            FadeOut(tangent_line_equation_w_a_b),
            FadeIn(tangent_line_equation_w_a_b2)
        )

        self.play(
            tangent_line_equation_w_a_b2_keep.animate.align_to(tangent_line_equation_w_a_b3, LEFT),
            tangent_line_equation_w_a_b2[5].animate.move_to(tangent_line_equation_w_a_b3[6]),
            tangent_line_equation_w_a_b2[6].animate.move_to(tangent_line_equation_w_a_b3[7]),
            tangent_line_equation_w_a_b2[8].animate.move_to(tangent_line_equation_w_a_b3[8]),
            tangent_line_equation_w_a_b2[7].animate.move_to(tangent_line_equation_w_a_b3[4]).set_opacity(0),
            FadeIn(tangent_line_equation_w_a_b3_brackets)
        )

        self.play(
            FadeOut(tangent_line_equation_w_a_b2),
            FadeIn(tangent_line_equation_w_a_b3[0]),
            FadeIn(tangent_line_equation_w_a_b3[1]),
            FadeIn(tangent_line_equation_w_a_b3[2]),
            FadeIn(tangent_line_equation_w_a_b3[3]),
            FadeIn(tangent_line_equation_w_a_b3[4]),
            FadeIn(tangent_line_equation_w_a_b3[6]),
            FadeIn(tangent_line_equation_w_a_b3[7]),
            FadeIn(tangent_line_equation_w_a_b3[8]),
            FadeOut(p_x0_fx0_label)
        )

        self.wait(2)

        self.play(HighlightWithRect(tangent_line_equation_w_a_b3))

        self.wait(3)

        self.play(HighlightWithRect(VGroup(*tangent_line_equation_w_a_b3[5:])))
        self.play(
            tangent_line_equation_w_a_b3_keep.animate.align_to(tangent_line_equation_w_a_b4, LEFT),
            Transform(tangent_line_equation_w_a_b3_transform, tangent_line_equation_w_a_b4[5])
        )

        self.play(
            FadeOut(tangent_line_equation_w_a_b3_keep),
            FadeIn(tangent_line_equation_w_a_b4[0]),
            FadeIn(tangent_line_equation_w_a_b4[1]),
            FadeIn(tangent_line_equation_w_a_b4[2]),
            FadeIn(tangent_line_equation_w_a_b4[3]),
            FadeIn(tangent_line_equation_w_a_b4[4]),
            FadeOut(tangent_line_equation_w_a_b3_transform),
            FadeIn(tangent_line_equation_w_a_b4[5])
        )

        self.wait(5)

        self.play(
            Transform(tangent_line_equation_w_a_b4[4], tangent_line_equation_w_a_b5[5], path_arc=90*DEGREES),
            Transform(tangent_line_equation_w_a_b4[5], tangent_line_equation_w_a_b5[4], path_arc=90*DEGREES),
            Transform(tangent_line_equation_w_a_b4[0], tangent_line_equation_w_a_b5[0])
        )

        graph_and_obj = VGroup(
            plane, function_graph, dx_line, delta_x_label,
            secant_line, x0_dot,
            xf_dot, xf_vertical_line, x0_vertical_line,
            x0_label, xf_label, fx0_horizontal_line, fx0_label,
            dx_tends_zero,
            secant_tangent_line_label
        )

        self.wait(4)

        self.play(
            FadeOut(graph_and_obj),
            FadeOut(tangent_line_equation_w_a_b4[0]),
            FadeOut(tangent_line_equation_w_a_b4[1]),
            FadeOut(tangent_line_equation_w_a_b4[2]),
            FadeOut(tangent_line_equation_w_a_b4[3]),
            FadeOut(tangent_line_equation_w_a_b4[4]),
            FadeOut(tangent_line_equation_w_a_b4[5]),
            FadeIn(tangent_line_equation_w_a_b5[0]),
            FadeIn(tangent_line_equation_w_a_b5[1]),
            FadeIn(tangent_line_equation_w_a_b5[2]),
            FadeIn(tangent_line_equation_w_a_b5[3]),
            FadeIn(tangent_line_equation_w_a_b5[4]),
            FadeIn(tangent_line_equation_w_a_b5[5])
        )

        self.play(
            tangent_line_equation_w_a_b5.animate.move_to(ORIGIN).scale(1.25)
        )

        self.wait(8)

        self.play(
            Indicate(tangent_line_equation_w_a_b5[2],scale_factor=1.2, color="#C00000"),
            Indicate(tangent_line_equation_w_a_b5[5],scale_factor=1.2, color="#C00000")
        )

        self.wait(4.8 )

        self.play(
            Indicate(VGroup(*tangent_line_equation_w_a_b5[0][5:7]),scale_factor=1.2, color="#C00000"),
            Indicate(VGroup(*tangent_line_equation_w_a_b5[2][2:4]),scale_factor=1.2, color="#C00000"),
            Indicate(VGroup(*tangent_line_equation_w_a_b5[5 ][3:5]),scale_factor=1.2, color="#C00000"),
        )

        tangent_line_equation_fprime = MathTex("r'_{tan}(x_0 + \Delta x)", "=", "f'(x_{0})", "+", "\Delta x", "f''(x_{0})",font_size=24).set_color(BLACK)
        tangent_line_equation = MathTex("r_{tan}(x_0 + \Delta x)", "=", "f(x_{0})", "+", "\Delta x", "f'(x_{0})",font_size=24).set_color(BLACK)
        tangent_line_equation_fprime.move_to(ORIGIN).scale(1.25)
        tangent_line_equation.move_to(ORIGIN).scale(1.25)
        tangent_line_equation_fprime.set_y(tangent_line_equation_w_a_b5.get_y())
        tangent_line_equation.set_y(tangent_line_equation_w_a_b5.get_y())

        self.wait(11)

        self.play(
            tangent_line_equation_w_a_b5[0].animate.move_to(tangent_line_equation_fprime[0]),
            tangent_line_equation_w_a_b5[1].animate.move_to(tangent_line_equation_fprime[1]),
            Transform(tangent_line_equation_w_a_b5[2], tangent_line_equation_fprime[2]),
            tangent_line_equation_w_a_b5[3].animate.move_to(tangent_line_equation_fprime[3]),
            tangent_line_equation_w_a_b5[4].animate.move_to(tangent_line_equation_fprime[4]),
            Transform(tangent_line_equation_w_a_b5[5], tangent_line_equation_fprime[5]),
        )

        self.play(
            FadeOut(tangent_line_equation_w_a_b5[0]),
            FadeOut(tangent_line_equation_w_a_b5[1]),
            FadeOut(tangent_line_equation_w_a_b5[2]),
            FadeOut(tangent_line_equation_w_a_b5[3]),
            FadeOut(tangent_line_equation_w_a_b5[4]),
            FadeOut(tangent_line_equation_w_a_b5[5]),
            FadeIn(tangent_line_equation_fprime[0]),
            FadeIn(tangent_line_equation_fprime[1]),
            FadeIn(tangent_line_equation_fprime[2]),
            FadeIn(tangent_line_equation_fprime[3]),
            FadeIn(tangent_line_equation_fprime[4]),
            FadeIn(tangent_line_equation_fprime[5])
        )



        self.wait(6)

        self.play(
            tangent_line_equation_fprime[0].animate.move_to(tangent_line_equation[0]),
            tangent_line_equation_fprime[1].animate.move_to(tangent_line_equation[1]),
            Transform(tangent_line_equation_fprime[2], tangent_line_equation[2]),
            tangent_line_equation_fprime[3].animate.move_to(tangent_line_equation[3]),
            tangent_line_equation_fprime[4].animate.move_to(tangent_line_equation[4]),
            Transform(tangent_line_equation_fprime[5], tangent_line_equation[5]),
        )
        self.wait(1)

        self.play(
            FadeOut(tangent_line_equation_fprime[0]),
            FadeOut(tangent_line_equation_fprime[1]),
            FadeOut(tangent_line_equation_fprime[2]),
            FadeOut(tangent_line_equation_fprime[3]),
            FadeOut(tangent_line_equation_fprime[4]),
            FadeOut(tangent_line_equation_fprime[5]),
            FadeIn(tangent_line_equation[0]),
            FadeIn(tangent_line_equation[1]),
            FadeIn(tangent_line_equation[2]),
            FadeIn(tangent_line_equation[3]),
            FadeIn(tangent_line_equation[4]),
            FadeIn(tangent_line_equation[5])
        )

        r_tan_eq_copy = tangent_line_equation.copy()
        r_tan_eq_copy.scale(0.64).to_corner(DR, buff=0.8).set_opacity(0)

        # Expand bounding box to fit all three labels
        final_label_box = SurroundingRectangle(r_tan_eq_copy, color=BLACK, buff=0.2)
        final_label_box.set_stroke(opacity=0.5, width=1)
        self.play(
            tangent_line_equation.animate.scale(0.64).to_corner(DR, buff=0.8),
            FadeOut(tangent_line_equation_copy),
            FadeOut(left_side_3),
            FadeOut(tangent_line_equation4),
            Transform(eq_box_, final_label_box)
        )
        

        self.wait(5)