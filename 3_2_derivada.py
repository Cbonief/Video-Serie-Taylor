from manim import *
from utils import *

# ──────────────────────────────────────────────────────────────────────────────
# COLOUR / STYLE PRESETS  (kept identical to every previous file)
# ──────────────────────────────────────────────────────────────────────────────
DARK_MODE = False

if DARK_MODE:          #  dark‑mode palette
    BG_COLOR           = "#000000"
    PRIMARY_COLOR      = WHITE
    ARROW_COLOR        = GRAY_E
    ERROR_COLOR        = RED
    SPECIAL_FUNC_COLOR = rgb_to_color(hex_to_rgb("#C00000"))
    TANGENT_LINE_GREEN = GREEN
    TANGENT_LINE_BLUE  = BLUE
else:                   #  light‑mode palette  ← derivada_1 used this
    BG_COLOR           = "#FAE6C2"
    PRIMARY_COLOR      = BLACK
    ARROW_COLOR        = GRAY_E
    ERROR_COLOR        = RED
    SPECIAL_FUNC_COLOR = rgb_to_color(hex_to_rgb("#C00000"))
    TANGENT_LINE_GREEN = GREEN
    TANGENT_LINE_BLUE  = BLUE


class derivada_2(Scene):
    """Continuation of `derivada_1` – everything that was visible at the
    *end* of that scene is reconstructed here so the transition feels
    seamless.  After the static rebuild you are free to advance the story.
    """

    # ------------------------------------------------------------------
    #   BASIC BUILD‑BLOCKS (same helpers derivada_1 used)
    # ------------------------------------------------------------------
    def polynomial(self, x):
        x -= 1.2
        return (x + 1) * (x - 2.5) * (x - 4) / 10

    def derivative(self, x):
        x -= 1.2
        return 0.1 * (3 * x**2 - 11 * x + 3.5)

    # ------------------------------------------------------------------
    #   CONSTRUCT
    # ------------------------------------------------------------------
    def construct(self):
        self.camera.background_color = BG_COLOR

        # (1) PARAMETERS frozen in the last frame of derivada_1
        x0            = 0.5      # base x‑value that was being zoomed on
        delta_x_final = 0.01     # ValueTracker had reached this
        zoom_factor   = 3        # same 3× zoom
        global_shift  = LEFT     # whole graph nudged left once

        # (2)  REBUILD PLANE & GRAPH exactly where we left them
        plane = NumberPlane(
            x_range=(-4, 8),
            y_length=7,
            axis_config={"color": PRIMARY_COLOR},
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 0.5,
                "stroke_opacity": 0.2,
            },
        )

        zoom_point = plane.c2p(x0, self.polynomial(x0))
        

        function_graph = plane.plot(
            self.polynomial,
            x_range=[-1.05, 6.51],
            color=SPECIAL_FUNC_COLOR,
        )


        # (3)  MAIN POINT, SECANT & TANGENT (all in the shifted / scaled frame)
        p0 = plane.c2p(x0, self.polynomial(x0))
        pf = plane.c2p(x0 + delta_x_final, self.polynomial(x0 + delta_x_final))

        point_dot   = Dot(p0, color=PRIMARY_COLOR, radius=0.04)
        secant_line = Line(p0, pf, color=TANGENT_LINE_BLUE).set_length(4)

        tan_len   = 0.4
        tan_start = plane.c2p(x0 - tan_len, self.polynomial(x0) - self.derivative(x0) * tan_len)
        tan_end   = plane.c2p(x0 + tan_len, self.polynomial(x0) + self.derivative(x0) * tan_len)
        tangent_line = DashedLine(tan_start, tan_end, color=TANGENT_LINE_GREEN)

        # x_0 label (under the x‑axis at p0)
        x0_label = MathTex("x_0", font_size=20, color=PRIMARY_COLOR)
        x0_label.next_to(plane.c2p(x0, 0), DOWN, buff=0.1)

        # tiny label r_sec ≈ r_tan kept from previous scene
        sec_tan_lbl = (
            MathTex("r_{sec}", "\\approx", "r_{tan}", font_size=24, color=PRIMARY_COLOR)
            .next_to(secant_line, UR, buff=0.2)
        )

        # (4) TITLE & box (upper‑right)
        title = (
            Text("Definição de Derivada", font_size=36, color=PRIMARY_COLOR)
            .scale(0.5)
            .to_corner(UR, buff=0.5)
        )
        title_box = SurroundingRectangle(title, color=PRIMARY_COLOR, buff=0.1)
        title_box.set_stroke(opacity=0.5, width=1)

        # (5)  DERIVATIVE‑LIMIT FORMULA & box (lower‑right)
        derivative_eq = (
            MathTex(
                "f'(x_0)", "=", r"\lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}",
                font_size=24,
                color=PRIMARY_COLOR,
            )
            .scale(0.8)
            .to_corner(DR, buff=0.8)
        )
        deriv_box = SurroundingRectangle(derivative_eq, color=PRIMARY_COLOR, buff=0.1)
        deriv_box.set_stroke(opacity=0.5, width=1)

        # (6) GROUP graph‑space objects to keep future transforms in sync
        plane.scale(zoom_factor, about_point=zoom_point)
        function_graph.scale(zoom_factor, about_point=zoom_point)
        graph_group = VGroup(
            plane,
            function_graph,
            point_dot,
            secant_line,
            tangent_line,
            x0_label,
            sec_tan_lbl,
        ).shift(global_shift)

        # (7)  INSTANTLY add everything that was already visible
        self.add(graph_group, title, title_box, derivative_eq, deriv_box)

        # ────────────────────────────────────────────────────────────────
        #   CONTINUE THE STORY… (feel free to replace from here on)
        # ────────────────────────────────────────────────────────────────

        self.wait(1.2)
        self.play(Indicate(derivative_eq, scale_factor=1.2), run_time=1.6)
        self.wait(2)
