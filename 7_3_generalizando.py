from manim import *
import numpy as np
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


class generalizando_3(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = BG_COLOR

        generalize_label = Text("Generalizando").set_color(PRIMARY_COLOR)
        generalize_label.to_edge(UP).shift(DOWN * 1.5).scale(0.5).to_corner(UR, buff=0.5)

        title_box = SurroundingRectangle(generalize_label, color=PRIMARY_COLOR, buff=0.1)
        title_box.set_stroke(opacity=0.5, width=1)

        gn_eq = MathTex("g_n(x_0+n","u",")","=","\\sum_{k=0}^{n}\\frac{n!}{k!(n-k)!}","u^k","f^k(x_0)", font_size=30).set_color(PRIMARY_COLOR).to_corner(UL, buff=1.6)
        gn_eq_deltax = MathTex("g_n(x_0+n","\\frac{\\Delta x}{n}",")","=","\\sum_{k=0}^{n}\\frac{n!}{k!(n-k)!}","\\left(\\frac{\\Delta x}{n}\\right)^k","f^k(x_0)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25)
        gn_eq_deltax_simplified = MathTex("g_n(x_0+","\\Delta x",")","=","\\sum_{k=0}^{n}\\frac{n!}{k!(n-k)!}","\\left(\\frac{\\Delta x}{n}\\right)^k","f^k(x_0)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25).move_to(gn_eq_deltax, aligned_edge=LEFT)
        gn_eq_deltax_simplified_faux = MathTex("g_n(x_0+","\\Delta x",")","=","\\sum_{k=0}^{n}\\frac{n!}{k!(n-k)!}","\\left(\\frac{\\Delta x}{n}\\right)^k","f^k(x_0)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25).move_to(gn_eq_deltax, aligned_edge=LEFT)
        gn_eq_deltax_simplified_approx_fx0 = MathTex("g_n(x_0+","\\Delta x",")","=","\\sum_{k=0}^{n}\\frac{n!}{k!(n-k)!}","\\left(\\frac{\\Delta x}{n}\\right)^k","f^k(x_0)", "\\approx f(x_0+\\Delta x)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25)
        gn_eq_deltax_simplified_approx_fx0_faux = MathTex("g_{","n","}","(x_0+","\\Delta x",")","=","\\sum_{k=0}^{","n","}","\\frac{n!}{k!(","n","-k)!}","\\left(\\frac{\\Delta x}{","n","}","\\right)^k","f^k(x_0)", "\\approx f(x_0+\\Delta x)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25)
        g100_eq_deltax_simplified_approx_fx0 = MathTex("g_{","100","}","(x_0+","\\Delta x",")","=","\\sum_{k=0}^{","100","}","\\frac{n!}{k!(","100","-k)!}","\\left(\\frac{\\Delta x}{","100","}","\\right)^k","f^k(x_0)", "=2.23616533...", font_size=30).set_color(PRIMARY_COLOR).scale(1.25).align_to(gn_eq_deltax_simplified_approx_fx0_faux, LEFT)
    
        
        binomial_theorem = MathTex("(x+u)^","n","=","\\sum_{k=0}^{","n","}","\\frac{n!}{k!(n-k)!}u^kx^{n-k}", font_size=30).set_color(PRIMARY_COLOR).next_to(gn_eq, DOWN)
        x_u_3 = MathTex("(x+u)^","3","=","\\sum_{k=0}^{","3","}","\\frac{3!}{k!(3-k)!}u^kx^{3-k}", font_size=30).set_color(PRIMARY_COLOR).move_to(binomial_theorem, aligned_edge=LEFT)
        x_u_3_3 = MathTex("(x+u)^","3","=","\\frac{3!}{0!(3-0)!}u^0x^3", "+", "\\sum_{k=1}^{","3","}","\\frac{3!}{k!(3-k)!}u^kx^{3-k}", font_size=30).set_color(PRIMARY_COLOR).move_to(binomial_theorem, aligned_edge=LEFT)
        
        x_u_3_32 = MathTex("(x+u)^","3","=","\\frac{3!}{0!(3-0)!}u^0x^3", "+", "\\frac{3!}{1!(3-1)!}u^1x^2","+","\\sum_{k=2}^{","3","}","\\frac{3!}{k!(3-k)!}u^kx^{3-k}", font_size=30).set_color(PRIMARY_COLOR).move_to(binomial_theorem, aligned_edge=LEFT)
        x_u_3_321 = MathTex("(x+u)^","3","=","\\frac{3!}{0!(3-0)!}u^0x^3", "+", "\\frac{3!}{1!(3-1)!}u^1x^2","+", "\\frac{3!}{2!(3-2)!}u^0x^1","+", "\\sum_{k=3}^{","3","}","\\frac{3!}{k!(3-k)!}u^kx^{3-k}", font_size=30).set_color(PRIMARY_COLOR).move_to(binomial_theorem, aligned_edge=LEFT)
        x_u_3_full = MathTex("(x+u)^","3","=","\\frac{3!}{0!(3-0)!}u^0x^3", "+", "\\frac{3!}{1!(3-1)!}u^1x^2","+", "\\frac{3!}{2!(3-2)!}u^0x^1","+", "\\frac{3!}{3!(3-3)!}u^3x^0", font_size=30).set_color(PRIMARY_COLOR).move_to(binomial_theorem, aligned_edge=LEFT)
        x_u_3_full_faux = MathTex("(x+u)^","3","=","\\frac{3!}{0!(3-0)!}","u^0x^3", "+", "\\frac{3!}{1!(3-1)!}","u^1x^2","+", "\\frac{3!}{2!(3-2)!}","u^2x^1","+", "\\frac{3!}{3!(3-3)!}","u^3x^0", font_size=30).set_color(PRIMARY_COLOR).move_to(binomial_theorem, aligned_edge=LEFT)

        x_u_3_full_1 = MathTex("(x+u)^","3","=","\\frac{3!}{3!}","u^0x^3", "+", "\\frac{3!}{2!}","u^1x^2","+", "\\frac{3!}{2!}","u^0x^1","+", "\\frac{3!}{3!}","u^3x^0", font_size=30).set_color(PRIMARY_COLOR).move_to(binomial_theorem, aligned_edge=LEFT)
        x_u_3_full_2 = MathTex("(x+u)^","3","=","1","u^0x^3", "+", "3","u^1x^2","+", "3","u^0x^1","+", "1","u^3x^0", font_size=30).set_color(PRIMARY_COLOR).move_to(binomial_theorem, aligned_edge=LEFT)

        u_eq = MathTex("u = ","\\frac{\\Delta x}{n}", font_size=30).set_color(PRIMARY_COLOR).next_to(gn_eq_deltax, DOWN)
        # u_eq[0][0].set_color(SPECIAL_FUNC_COLOR)

        k_eq_0 = MathTex("k=0", font_size=24).set_color(SPECIAL_FUNC_COLOR).next_to(x_u_3_3[3], 1.5*DOWN)
        k_eq_1 = MathTex("k=1", font_size=24).set_color(SPECIAL_FUNC_COLOR).next_to(x_u_3_32[5], 1.5*DOWN)
        k_eq_2 = MathTex("k=2", font_size=24).set_color(SPECIAL_FUNC_COLOR).next_to(x_u_3_321[7], 1.5*DOWN)
        k_eq_3 = MathTex("k=3", font_size=24).set_color(SPECIAL_FUNC_COLOR).next_to(x_u_3_full[9], 1.5*DOWN)

        inside_summation = x_u_3[6].copy()
        inside_summation.set_opacity(0)
        inside_summation_1 = x_u_3_3[8].copy()
        inside_summation_1.set_opacity(0)
        inside_summation_2 = x_u_3_321[10].copy()
        inside_summation_2.set_opacity(0)

        if_bigger_better_label = Text("Quanto maior 'n', menor o erro.", font_size=30).set_color(PRIMARY_COLOR).next_to(gn_eq_deltax_simplified_approx_fx0,  2*DOWN)
        than_what_if_infinite = Text("E se 'n' fosse infinito?", font_size=30).set_color(PRIMARY_COLOR).next_to(if_bigger_better_label, DOWN)

        
        sqrt_calculator = MathTex("\\sqrt 5","=2.23606797...", font_size=24).next_to(gn_eq_deltax_simplified_approx_fx0, 2*UP, aligned_edge=LEFT).set_color(PRIMARY_COLOR)
        g100_ex = MathTex("g_{100}(5)","=2.23616533...","\\approx \\sqrt 5", font_size=24).next_to(sqrt_calculator, UP, aligned_edge=LEFT).set_color(PRIMARY_COLOR)
        g3_ex = MathTex("g_3(5)","=2.24001736","\\approx \\sqrt 5", font_size=24).next_to(g100_ex, UP, aligned_edge=LEFT).set_color(PRIMARY_COLOR)
        g1_ex = MathTex("g_1(5)","=2.25","\\approx \\sqrt 5", font_size=24).next_to(g3_ex, UP, aligned_edge=LEFT).set_color(PRIMARY_COLOR)

        g1_move = VGroup(g1_ex[1], g1_ex[2])
        g1_move.align_to(g100_ex[1], LEFT)
        g3_move = VGroup(g3_ex[1], g3_ex[2])
        g3_move.align_to(g100_ex[1], LEFT)
        sqrt_calculator[1].align_to(g100_ex[1], LEFT)

        gn_eq.move_to(ORIGIN)
        
        self.add(generalize_label, title_box)

        self.wait(1)
        self.play(Write(gn_eq))

        self.wait(6)

        self.play(HighlightWithRect(gn_eq))

        self.wait(4)

        self.play(gn_eq.animate.to_corner(UL, buff=1.6))

        self.play(FadeIn(binomial_theorem))

        self.wait(3)

        self.play(HighlightWithRect(binomial_theorem))

        self.wait(14)
        self.play(MathSubstitutionTransform(binomial_theorem, x_u_3, lag_ratio=0.2))

        self.wait(2)
        self.play(
            ReplacementTransform(x_u_3[0], x_u_3_3[0]),
            ReplacementTransform(x_u_3[1], x_u_3_3[1]),
            ReplacementTransform(x_u_3[2], x_u_3_3[2]),
            ReplacementTransform(inside_summation, x_u_3_3[3]),
            FadeIn(x_u_3_3[4], shift=RIGHT),
            ReplacementTransform(x_u_3[3], x_u_3_3[5]),
            ReplacementTransform(x_u_3[4], x_u_3_3[6]),
            ReplacementTransform(x_u_3[5], x_u_3_3[7]),
            ReplacementTransform(x_u_3[6], x_u_3_3[8]),
            FadeIn(k_eq_0, shift=LEFT)
        )

        self.wait(1)
        self.play(
            ReplacementTransform(x_u_3_3[0], x_u_3_32[0]),
            ReplacementTransform(x_u_3_3[1], x_u_3_32[1]),
            ReplacementTransform(x_u_3_3[2], x_u_3_32[2]),
            ReplacementTransform(x_u_3_3[3], x_u_3_32[3]),
            ReplacementTransform(x_u_3_3[4], x_u_3_32[4]),
            ReplacementTransform(inside_summation_1, x_u_3_32[5]),
            FadeIn(x_u_3_32[6], shift=RIGHT),
            ReplacementTransform(x_u_3_3[5], x_u_3_32[7]),
            ReplacementTransform(x_u_3_3[6], x_u_3_32[8]),
            ReplacementTransform(x_u_3_3[7], x_u_3_32[9]),
            ReplacementTransform(x_u_3_3[8], x_u_3_32[10]),
            FadeIn(k_eq_1, shift=LEFT)
        )
        self.wait(1)
        self.play(
            ReplacementTransform(x_u_3_32[0], x_u_3_321[0]),
            ReplacementTransform(x_u_3_32[1], x_u_3_321[1]),
            ReplacementTransform(x_u_3_32[2], x_u_3_321[2]),
            ReplacementTransform(x_u_3_32[3], x_u_3_321[3]),
            ReplacementTransform(x_u_3_32[4], x_u_3_321[4]),
            ReplacementTransform(x_u_3_32[5], x_u_3_321[5]),
            ReplacementTransform(x_u_3_32[6], x_u_3_321[6]),
            ReplacementTransform(inside_summation_2, x_u_3_321[7]),
            FadeIn(x_u_3_321[8], shift=RIGHT),
            ReplacementTransform(x_u_3_32[7], x_u_3_321[9]),
            ReplacementTransform(x_u_3_32[8], x_u_3_321[10]),
            ReplacementTransform(x_u_3_32[9], x_u_3_321[11]),
            ReplacementTransform(x_u_3_32[10], x_u_3_321[12]),
            FadeIn(k_eq_2, shift=LEFT)
        )
        self.wait(1)
        self.play(
            ReplacementTransform(x_u_3_321[0], x_u_3_full[0]),
            ReplacementTransform(x_u_3_321[1], x_u_3_full[1]),
            ReplacementTransform(x_u_3_321[2], x_u_3_full[2]),
            ReplacementTransform(x_u_3_321[3], x_u_3_full[3]),
            ReplacementTransform(x_u_3_321[4], x_u_3_full[4]),
            ReplacementTransform(x_u_3_321[5], x_u_3_full[5]),
            ReplacementTransform(x_u_3_321[6], x_u_3_full[6]),
            ReplacementTransform(x_u_3_321[7], x_u_3_full[7]),
            ReplacementTransform(x_u_3_321[8], x_u_3_full[8]),
            FadeOut(x_u_3_321[9], x_u_3_321[10],  x_u_3_321[11]),
            ReplacementTransform(x_u_3_321[12], x_u_3_full[9]),
            FadeIn(k_eq_3)
        )

        self.wait(1)        
        self.play(FadeTransform(x_u_3_full,x_u_3_full_faux, replace_mobject_with_target_in_scene =True))
        self.wait(1)

        self.play(
            MathSubstitutionTransform(x_u_3_full_faux, x_u_3_full_1),
            FadeOut(k_eq_1, k_eq_0, k_eq_2, k_eq_3)
        )
        self.wait(1)

        self.play(MathSubstitutionTransform(x_u_3_full_1, x_u_3_full_2))

        self.wait(3)
        self.play(
            FadeOut(x_u_3_full_2),
            gn_eq.animate.move_to(ORIGIN).scale(1.25)
        )

        self.wait(4)
        highlightrects = VGroup(CreateHighlightRect(gn_eq[1][0]), CreateHighlightRect(gn_eq[5][0]))

        self.play(FadeIn(highlightrects))
        self.wait(2)
        self.play(
            Write(u_eq)
        )
        self.play(HighlightWithRect(u_eq))
        self.wait(2)
        self.play(
            Indicate(u_eq[1][0], color=SPECIAL_FUNC_COLOR),
            Indicate(u_eq[1][1], color=SPECIAL_FUNC_COLOR)
        )
        self.wait(2)
        self.play(
            Indicate(u_eq[1][3], color=SPECIAL_FUNC_COLOR)
        )
        self.play(HighlightWithRect(u_eq))

        self.wait(6)
        self.play(LaggedStart(
            FadeOut(highlightrects),
            MathSubstitutionTransform(gn_eq,gn_eq_deltax),
            lag_ratio=0.3
        ))

        ns = VGroup(gn_eq_deltax[0][6], gn_eq_deltax[1][-1])
        slashes = VGroup(CreateSlash(gn_eq_deltax[0][6]), CreateSlash(gn_eq_deltax[1][-1]))
        self.wait(1)
        self.play(
            FadeIn(slashes),
        )
        self.play(
            FadeOut(slashes, ns, gn_eq_deltax[1][-2]),
            ReplacementTransform(gn_eq_deltax[1][:2], gn_eq_deltax_simplified[1]), 
            ReplacementTransform(gn_eq_deltax[2], gn_eq_deltax_simplified[2]),
            ReplacementTransform(gn_eq_deltax[3], gn_eq_deltax_simplified[3]),
            ReplacementTransform(gn_eq_deltax[4], gn_eq_deltax_simplified[4]),
            ReplacementTransform(gn_eq_deltax[5], gn_eq_deltax_simplified[5]),
            ReplacementTransform(gn_eq_deltax[6], gn_eq_deltax_simplified[6])
        )
        self.play(FadeOut(u_eq))
        self.wait(2)
        gn_eq_deltax[0].set_opacity(0)
        self.play(
            FadeTransform(gn_eq_deltax_simplified, gn_eq_deltax_simplified_faux, replace_mobject_with_target_in_scene=True),
            FadeOut(gn_eq_deltax[0])
        )

        self.wait(6)
        
        self.play(
            MathSubstitutionTransform(gn_eq_deltax_simplified_faux, gn_eq_deltax_simplified_approx_fx0),
            FadeIn(gn_eq_deltax_simplified_approx_fx0[7], shift=LEFT)
        )

        self.wait(8)
        self.play(Write(g1_ex))
        self.wait(2)
        self.play(LaggedStart(
            Write(g3_ex[0:2]),
            ReplacementTransform(g1_ex[2], g3_ex[2]),
            lag_ratio=0.3
        ))

        self.wait(5)
        self.play(FadeTransform(gn_eq_deltax_simplified_approx_fx0, gn_eq_deltax_simplified_approx_fx0_faux))
        self.play(MathSubstitutionTransform(gn_eq_deltax_simplified_approx_fx0_faux, g100_eq_deltax_simplified_approx_fx0, lag_ratio=0.1))

        self.wait(2)
        self.play(LaggedStart(
            Write(g100_ex[0:2]),
            ReplacementTransform(g3_ex[2], g100_ex[2]),
            lag_ratio=0.3
        ))

        self.wait(1)
        self.play(
            Write(sqrt_calculator)
        )
        gn_eq_deltax_simplified_approx_fx0_faux = MathTex("g_{","n","}","(x_0+","\\Delta x",")","=","\\sum_{k=0}^{","n","}","\\frac{n!}{k!(","n","-k)!}","\\left(\\frac{\\Delta x}{","n","}","\\right)^k","f^k(x_0)", "\\approx f(x_0+\\Delta x)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25)

        self.play(MathSubstitutionTransform(g100_eq_deltax_simplified_approx_fx0, gn_eq_deltax_simplified_approx_fx0_faux, lag_ratio=0.1))
        self.play(HighlightWithRect(gn_eq_deltax_simplified_approx_fx0_faux))

        self.wait(2)
        self.play(Write(if_bigger_better_label))
        self.wait(6)
        self.play(Write(than_what_if_infinite))

        self.wait(1)
        self.play(FadeOut(sqrt_calculator, g100_ex, g1_ex, g3_ex))

        gn_label_group = VGroup(gn_eq_deltax_simplified_approx_fx0_faux, if_bigger_better_label, than_what_if_infinite)
        self.wait(1)
        self.play(
            gn_label_group.animate.shift(UP)
        )
        
        n_lim = MathTex("n \\to \\infty", font_size=28).set_color(PRIMARY_COLOR).next_to(than_what_if_infinite, 3*DOWN)
        u_lim = MathTex("u \\to 0", font_size=28, color=PRIMARY_COLOR).next_to(n_lim, DOWN)
        error_lim = MathTex("erro(u) \\to 0", font_size=28, color=PRIMARY_COLOR).next_to(u_lim, DOWN)

        # Animate the new limit list
        self.play(Succession(
            Write(n_lim),
            Write(u_lim),
            Write(error_lim)
        ))

        label_group = VGroup(if_bigger_better_label, than_what_if_infinite)
        self.wait(4)
        self.play(LaggedStart(
            FadeOut(
            gn_eq_deltax_simplified_approx_fx0_faux,
            n_lim,
            u_lim,
            error_lim
            ),
            label_group.animate.move_to(ORIGIN).scale(1.25),
            lag_ratio=0.4
        ))
        levando_ao_limite_label = Text("Levando ao limite").set_color(PRIMARY_COLOR)

        self.play(
            FadeIn(levando_ao_limite_label),
            FadeOut(generalize_label, title_box),
            label_group.animate.scale(15).set_opacity(0),
            run_time=2
        )


        self.wait(2)