from manim import *
import numpy as np
from utils import *

# Toggle Dark Mode here
DARK_MODE = False

# -----------------------------------------------------------------------------
# Colour palette (same logic as previous scenes so the look remains consistent)
# -----------------------------------------------------------------------------
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


class conclusao(Scene):
    """Scene 9 – Conclusão

    Minimal starting layout that preserves exactly the three persistent visual
    elements that remained at the very end of *levando_ao_limite*:

    1. **Title** ("Levando ao limite") tucked into the upper-right corner with a
       subtle outline.
    2. **General Taylor-series formula** centred on screen and boxed using the
       project-specific `CreateHighlightRect` helper rather than a raw
       `SurroundingRectangle`.
    3. A small **section label** ("Série de Taylor") sitting just above the
       equation.
    """

    def construct(self):
        # ------------------------------------------------------------------
        # Background --------------------------------------------------------
        self.camera.background_color = BG_COLOR

        # ------------------------------------------------------------------
        # 1) Title (upper-right) --------------------------------------------
        title = Text("Levando ao limite").set_color(PRIMARY_COLOR)
        title.scale(0.5).to_corner(UR, buff=0.5)

        title_box = SurroundingRectangle(
            title,
            color=PRIMARY_COLOR,
            buff=0.1,
        )
        title_box.set_stroke(opacity=0.5, width=1)

        # ------------------------------------------------------------------
        # 2) Taylor-series equation (centre) --------------------------------
        taylor_eq = MathTex(
            "f(x_0+\\Delta x)", "=", "\\sum_{k=0}^{\\infty}", "\\frac{\\Delta x^{k}}{k!}", "f^{k}(x_0)",
            font_size=30,
        ).set_color(PRIMARY_COLOR).scale(1.25).scale(0.6).scale(5/3).move_to(ORIGIN)

        # Use the custom helper so styling matches the rest of the project
        taylor_box = CreateHighlightRect(taylor_eq)

        # ------------------------------------------------------------------
        # 3) Label above the equation --------------------------------------
        taylor_label = Text("Série de Taylor", font_size=30).set_color(PRIMARY_COLOR)
        taylor_label.next_to(taylor_eq, 3*UP)
        conclusao_label = Text(" - Conclusão", font_size=30).set_color(PRIMARY_COLOR)

        # ------------------------------------------------------------------
        # Static placement (no animations here) -----------------------------
        self.add(
            title_box,
            title,
            taylor_box,
            taylor_eq,
            taylor_label,
        )

        self.wait(2)
        
        taylor_group = VGroup(taylor_box, taylor_eq, taylor_label)
        self.play(LaggedStart(
            FadeOut(title_box, title),
            taylor_group.animate.to_edge(UP, buff=1),
            lag_ratio=0.5
        ))
        taylor_label_copy = taylor_label.copy()
        conclusao_label.next_to(taylor_label_copy, RIGHT, aligned_edge=UP, buff=0.1)
        aux_group = VGroup(taylor_label_copy, conclusao_label)
        aux_group.move_to(taylor_label)
        self.play(LaggedStart(
            taylor_label.animate.move_to(taylor_label_copy),
            Write(conclusao_label),
            lag_ratio=0.5
        ))

        derivada_label = Tex("Derivada", font_size=26)
        aproximacao_linear_label = Tex("Aproximação Linear", font_size=26)
        aproximar_ponto_medio_label = Tex("Aproximar ponto médio", font_size=26)
        generalizar_label = Tex("Generalizar", font_size=26)
        limite_label = Tex("Limite", font_size=26)
        derivada_rect = Rectangle(color=PRIMARY_COLOR, width=derivada_label.width+0.5, height=aproximacao_linear_label.height+0.5, fill_opacity=1).move_to(derivada_label)
        aproximacao_linear_rect = Rectangle(color=PRIMARY_COLOR, width=aproximacao_linear_label.width+0.5, height=aproximacao_linear_label.height+0.5, fill_opacity=1).move_to(aproximacao_linear_label)
        aproximar_ponto_medio_rect = Rectangle(color=PRIMARY_COLOR, width=aproximar_ponto_medio_label.width+0.5, height=aproximacao_linear_label.height+0.5, fill_opacity=1).move_to(aproximar_ponto_medio_label)
        generalizar_rect = Rectangle(color=PRIMARY_COLOR, width=generalizar_label.width+0.5, height=aproximacao_linear_label.height+0.5, fill_opacity=1).move_to(generalizar_label)
        limite_rect = Rectangle(color=PRIMARY_COLOR, width=limite_label.width+0.5, height=aproximacao_linear_label.height+0.5, fill_opacity=1).move_to(limite_label)
        derivada = VGroup(derivada_rect, derivada_label)
        aproximacao_linear = VGroup(aproximacao_linear_rect, aproximacao_linear_label)
        aproximar_ponto_medio = VGroup(aproximar_ponto_medio_rect, aproximar_ponto_medio_label)
        generalizar = VGroup(generalizar_rect, generalizar_label)
        limite = VGroup(limite_rect, limite_label)

                # --- (everything you already had that defines the labels & rectangles) ---

        subtitles = VGroup(
            derivada,
            aproximacao_linear,
            aproximar_ponto_medio,
            generalizar,
            limite
        ).arrange(buff=0.5).next_to(taylor_group, DOWN, buff=1)

        # Pre-create the arrows so we can reference them in the loop
        arrows = [
            Arrow(
                start=left.get_right(),
                end=right.get_left(),
                buff=0.1,
                color=PRIMARY_COLOR,
                stroke_width=2
            )
            for left, right in zip(subtitles[:-1], subtitles[1:])
        ]

        sub_arrow = VGroup(subtitles, *arrows)

        self.wait(41)
        # -----------  SEQUENTIAL ANIMATION    ------------
        for i, subtitle in enumerate(subtitles):
            rect, label = subtitle  # unpack the VGroup

            # 1) draw the rectangle
            if i < len(arrows):
                self.play(LaggedStart(
                    FadeIn(rect),
                    Write(label),
                    Create(arrows[i]),
                    lag_ratio=0.8
                ))
            else:
                self.play(LaggedStart(
                    FadeIn(rect),
                    Write(label),
                    lag_ratio=0.8
                ))

                # ------------------------------------------------------------
        # 1)  Build vertical copies of every subtitle (rect + label)
        # ------------------------------------------------------------
        # 1) build vertical copies
        vertical_subs = VGroup(*[sub.copy() for sub in subtitles])

        # ⬇︎ arrange DOWN with the default (centers lined up) …
        vertical_subs.arrange(DOWN, buff=0.3)

        # … then park the whole column in the upper-left corner of the frame
        vertical_subs.to_corner(UL)

        # ------------------------------------------------------------
        # 2)  Create vertical arrows that go top→bottom
        # ------------------------------------------------------------
        vertical_arrows = VGroup()
        for top_sub, bottom_sub in zip(vertical_subs[:-1], vertical_subs[1:]):
            arrow = Arrow(
                start=top_sub.get_bottom(),
                end=bottom_sub.get_top(),
                buff=0.1,
                color=PRIMARY_COLOR,
                stroke_width=2
            )
            vertical_arrows.add(arrow)

                # ═════════════════  TARGET LAYOUT (invisible helpers)  ═════════════════
        # Build invisible copies laid out vertically – just to steal their positions.
        targets = VGroup(*[sub.copy() for sub in subtitles])
        targets.arrange(DOWN, buff=0.3).to_corner(UL)   # centered & in upper-left

        # # Arrow targets (also kept off-screen)
        # arrow_targets = [
        #     Arrow(
        #         start=upper.get_bottom(),
        #         end=lower.get_top(),
        #         buff=0.1,
        #         color=PRIMARY_COLOR,
        #         stroke_width=2
        #     )
        #     for upper, lower in zip(targets[:-1], targets[1:])
        # ]

        # # ═════════════════  TRANSFORM SEQUENTIALLY  ═════════════════
        # for i, subtitle in enumerate(subtitles):
        #     # 1) move *this* rectangle+label to its target spot
        #     self.play(subtitle.animate.move_to(targets[i]))

        #     # 2) then reshape the corresponding arrow (if there is one)
        #     if i < len(arrows):
        #         new_start = arrow_targets[i].get_start()
        #         new_end   = arrow_targets[i].get_end()
        #         self.play(
        #             arrows[i].animate.put_start_and_end_on(new_start, new_end)
        #         )

        self.play(
            sub_arrow.animate.to_edge(DOWN, buff=1)
        )

        # f(x_0+\\Delta x)", "=", "\\sum_{k=0}^{\\infty}", "\\frac{\\Delta x^{k}}{k!}", "f^{k}(x_0)",

        infinite_series = MathTex(
            "f(x_0+\\Delta x)", "=", "\\sum_{k=0}^{\\infty}", "a_k", "\\Delta x^k",
            font_size=32,
        ).set_color(PRIMARY_COLOR).move_to(taylor_eq, aligned_edge=LEFT)

        self.wait(5)
        self.play(FadeOut(taylor_box))

        self.wait(2)
        self.play(
            MathSubstitutionTransform(taylor_eq, infinite_series)
        )
        self.wait(2)
        self.play(HighlightWithRect(infinite_series[3]))


        # a = {a₀, a₁, a₂, …} = ???
        a_coeffs = MathTex(
            r"a_k \in \{\,a_0,\, a_1,\, a_2,\, \ldots\} = ???",
            font_size=32
        ).set_color(PRIMARY_COLOR).next_to(infinite_series, DOWN, buff=0.5)

        self.wait(1)
        self.play(Write(a_coeffs))

        taylor_eq = MathTex(
            "f(x_0+\\Delta x)", "=", "\\sum_{k=0}^{\\infty}", "\\frac{\\Delta x^{k}}{k!}", "f^{k}(x_0)",
            font_size=32,
        ).set_color(PRIMARY_COLOR).move_to(infinite_series, aligned_edge=LEFT)

        self.wait(2)
        self.play(LaggedStart(
            FadeOut(a_coeffs),
            FadeOut(sub_arrow),
            MathSubstitutionTransform(infinite_series, taylor_eq),
            lag_ratio=0.2
        ))

        self.wait(8)

        # 1) create the GIF (no position yet)
        gif = GifMobject("rotating_house_2.gif", fps=24)
        gif.scale(2)                         # or match to whatever size you like

        # 2) load the blueprint image
        blueprint = ImageMobject("blueprints.jpg")
        blueprint.match_height(gif)          # keep both the same height

        # 3) put them in a single VGroup and arrange horizontally
        media_pair = Group(gif, blueprint).arrange(RIGHT, buff=0.5)

        # 4) position the whole pair relative to the Taylor box
        media_pair.next_to(taylor_box, DOWN, buff=0.5)

        # 5) add (or animate) them on screen
        self.add(media_pair) 

        self.wait(38, frozen_frame=False)

        

