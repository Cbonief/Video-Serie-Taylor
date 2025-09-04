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

class intro(Scene):
    CONFIG = {
        "camera_config": {"frame_rate": 60},
    }

    def construct(self):
        self.camera.background_color = BG_COLOR
        self.wait(8) 


        # Linear Approximation Label
        serie_de_taylor_label = Text("Série de Taylor").set_color(BLACK)
        self.play(Write(serie_de_taylor_label), run_time=1.5)
        self.wait(2) 

        # Move "Série de Taylor" to halfway between the center and the top and fade it out
        self.play(
            serie_de_taylor_label.animate.to_edge(UP).shift(DOWN * 1.5).set_opacity(0.5),
            run_time=2
        )
        self.wait(10)

        # Write sqrt(4)=2 and sqrt(9)=3 in the center of the screen
        sqrt_4_eq = MathTex(r"\sqrt{4} = 2").set_color(BLACK)
        sqrt_9_eq = MathTex(r"\sqrt{9} = 3").set_color(BLACK)

        # Arrange the equations vertically
        equations = VGroup(sqrt_4_eq, sqrt_9_eq).arrange(DOWN, buff=0.6)
        self.play(Write(equations), run_time=2)

        self.play(
            HighlightWithRect(sqrt_4_eq)
        ) 
        self.play(
            HighlightWithRect(sqrt_9_eq)
        )

        self.wait(3)

        # Create a surrounding box and move equations to top-right while shrinking
        self.play(
            equations.animate.scale(0.5).to_corner(UR, buff=0.5),
            run_time=1.5
        )

        box = DashedVMobject(SurroundingRectangle(equations, color=BLACK, buff=0.1))
        box.set_stroke(opacity=0.5, width=1)
        self.play(Create(box), run_time=0.5)

        # Write sqrt(5)=? and sqrt(8)=? in the center
        sqrt_5_eq = MathTex(r"\sqrt{5} ", "= ?").set_color(BLACK)
        sqrt_8_eq = MathTex(r"\sqrt{8} ", "= ?").set_color(BLACK)

        new_equations = VGroup(sqrt_5_eq, sqrt_8_eq).arrange(DOWN, buff=0.6)
        self.play(Write(new_equations), run_time=2)
        self.wait(7)

        # Transform only the second part ("?") into irrational expressions, aligning them
        irrational_eq = MathTex(r"\neq \frac{p}{q}, \quad p, q \in \mathbb{N}").set_color(BLACK)

        # Align the transformed part to the original positions of "?" for each equation
        irrational_eq.align_to(sqrt_5_eq[1], LEFT)

        # Transform the second part "?" into the irrational part while keeping alignment
        self.play(Transform(sqrt_5_eq[1], irrational_eq), Transform(sqrt_8_eq[1], irrational_eq), run_time=2)
        self.wait(2)


        _ = serie_de_taylor_label.copy()
        _.scale(0.5).to_corner(UL, buff=0.5).set_opacity(1)
        label_box = SurroundingRectangle(_, color=BLACK, buff=0.1)
        label_box.set_stroke(opacity=0.5, width=1)

        # Move "Série de Taylor" to halfway between the center and the top and fade it out
        self.play(
            new_equations.animate.set_x(0).to_edge(UP).shift(DOWN*0.8).scale(0.8),
            Succession(serie_de_taylor_label.animate.scale(0.5).to_corner(UL, buff=0.5).set_opacity(1), Create(label_box)),
        )

        self.wait(1)

        self.play(FadeOut(equations), FadeOut(box), FadeOut(new_equations), run_time=2)

        # Display functions in sequence: sin(x), cos(x), ln(x), and e^x
        functions = VGroup(
            MathTex(r"\sin(x)").set_color(BLACK).to_edge(UP).shift(DOWN*0.8),
            MathTex(r"\cos(x)").set_color(BLACK).to_edge(UP).shift(DOWN*0.8),
            MathTex(r"\ln(x)").set_color(BLACK).to_edge(UP).shift(DOWN*0.8),
            MathTex(r"e^x").set_color(BLACK).to_edge(UP).shift(DOWN*0.8)
        )

        self.wait(4)
        self.play(Write(functions[0]))
        self.wait(0.15)
        self.play(ReplacementTransform(functions[0], functions[1]))
        self.wait(0.15)
        self.play(ReplacementTransform(functions[1], functions[2]))
        self.wait(0.15)
        self.play(ReplacementTransform(functions[2], functions[3]))

        # Fade out all the objects and wait for 2 seconds
        # self.play(FadeOut(serie_de_taylor_label, label_box), FadeOut(equations), FadeOut(box), FadeOut(new_equations), run_time=2)
        self.wait(10)
        self.play(FadeOut(serie_de_taylor_label, label_box, functions[3]))
        self.wait(10)
 


        