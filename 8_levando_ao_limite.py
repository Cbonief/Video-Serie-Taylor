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


class levando_ao_limite(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = BG_COLOR
        
        levando_ao_limite_label = Text("Levando ao limite").set_color(PRIMARY_COLOR)
        self.add(levando_ao_limite_label)

        levando_ao_limite_label_copy = levando_ao_limite_label.copy()
        levando_ao_limite_label_copy.to_edge(UP).shift(DOWN * 1.5).scale(0.5).to_corner(UR, buff=0.5)

        title_box = SurroundingRectangle(levando_ao_limite_label_copy, color=PRIMARY_COLOR, buff=0.1)
        title_box.set_stroke(opacity=0.5, width=1)

        gn_eq_deltax = MathTex("f(x_0+\\Delta x)","\\approx"," g_n(x_0+\\Delta x)","=","\\sum_{k=0}^{n}\\frac{n!}{k!(n-k)!}\\left(\\frac{\\Delta x}{n}\\right)^kf^k(x_0)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25)
        gn_eq_deltax_lim = MathTex("f(x_0+\\Delta x)","\\approx"," \\lim_{n \\to \\infty}","g_n(x_0+\\Delta x)","=","\\lim_{n \\to \\infty}","\\sum_{k=0}^{n}\\frac{n!}{k!(n-k)!} \\left(\\frac{\\Delta x}{n}\\right)^kf^k(x_0)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25)
        gn_eq_deltax_lim_aux = MathTex("f(x_0+\\Delta x)","="," \\lim_{n \\to \\infty}","g_n(x_0+\\Delta x)","=","\\lim_{n \\to \\infty}","\\sum_{k=0}^{n}\\frac{n!}{k!(n-k)!} \\left(\\frac{\\Delta x}{n}\\right)^kf^k(x_0)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25).align_to(gn_eq_deltax_lim, LEFT)
        fx_lim = MathTex("f(x_0+\\Delta x)","=","\\lim_{n \\to \\infty}","\\sum_{k=0}^{n}\\frac{n!}{k!(n-k)!} \\left(\\frac{\\Delta x}{n}\\right)^kf^k(x_0)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25)
        fx_lim_1 = MathTex("f(x_0+\\Delta x)","=","\\lim_{n \\to \\infty}","\\sum_{k=0}^{\\infty}","\\frac{n!}{k!(n-k)!}","\\left(\\frac{\\Delta x}{n}\\right)^k","f^k(x_0)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25)
        fx_lim_2 = MathTex("f(x_0+\\Delta x)","=","\\sum_{k=0}^{\\infty}","\\lim_{n \\to \\infty}","\\frac{n!}{k!(n-k)!}","\\left(\\frac{\\Delta x}{n}\\right)^k","f^k(x_0)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25)
        fx_lim_3 = MathTex("f(x_0+\\Delta x)","=","\\sum_{k=0}^{\\infty}","\\lim_{n \\to \\infty}","\\frac{n!}{k!(n-k)!}","\\frac{\\Delta x^k}{n^k}","f^k(x_0)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25)
        fx_lim_4 = MathTex("f(x_0+\\Delta x)","=","\\sum_{k=0}^{\\infty}","\\lim_{n \\to \\infty}","\\frac{n!}{n^k(n-k)!}","\\frac{\\Delta x^k}{k!}","f^k(x_0)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25)
        fx_lim_5 = MathTex("f(x_0+\\Delta x)","=","\\sum_{k=0}^{\\infty}","\\frac{\\Delta x^k}{k!}","f^k(x_0)", "\\lim_{n \\to \\infty}","\\frac{n!}{n^k(n-k)!}", font_size=30).set_color(PRIMARY_COLOR).scale(1.25).align_to(fx_lim_4, LEFT)



        self.play(
            Transform(levando_ao_limite_label, levando_ao_limite_label_copy),
            FadeIn(title_box)
        )
        self.wait(1)
        self.play(
            FadeIn(gn_eq_deltax)
        )

        self.wait(6)
        self.play(HighlightWithRect(gn_eq_deltax[0]))

        self.wait(2)
        self.play(HighlightWithRect(gn_eq_deltax[2]))

        self.wait(2)
        self.play(HighlightWithRect(gn_eq_deltax[4]))

        self.wait(1)
        self.play(
            ReplacementTransform(gn_eq_deltax[0], gn_eq_deltax_lim[0]),
            ReplacementTransform(gn_eq_deltax[1], gn_eq_deltax_lim[1]),
            ReplacementTransform(gn_eq_deltax[2], gn_eq_deltax_lim[3]),
            ReplacementTransform(gn_eq_deltax[3], gn_eq_deltax_lim[4]),
            ReplacementTransform(gn_eq_deltax[4], gn_eq_deltax_lim[6]),
            FadeIn(gn_eq_deltax_lim[2], gn_eq_deltax_lim[5], shift=DOWN)
        )

        self.wait(3)
        self.play(
            HighlightWithRect(VGroup(gn_eq_deltax_lim[2], gn_eq_deltax_lim[3]), buff=0.2)
        )

        self.wait(1)
        self.play(
            HighlightWithRect(gn_eq_deltax_lim[0], buff=0.2)
        )

        self.wait(1)
        self.play(MathSubstitutionTransform(gn_eq_deltax_lim, gn_eq_deltax_lim_aux, replace=False))

        self.wait(2)
        keep = [gn_eq_deltax_lim[0], gn_eq_deltax_lim[1], gn_eq_deltax_lim[5], gn_eq_deltax_lim[6]]
        remove_gn_animation = [ReplacementTransform(keep[i], fx_lim[i]) for i in range(len(keep))]
        
        remove = VGroup(gn_eq_deltax_lim[2], gn_eq_deltax_lim[3], gn_eq_deltax_lim[4])
        self.play(LaggedStart(
            FadeOut(remove, shift=UP),
            AnimationGroup(*remove_gn_animation, rate_func=rate_functions.ease_out_sine, run_time=2),
            lag_ratio = 0.3
        ))

        self.wait(11)
        self.play(HighlightWithRect(fx_lim[3][0], run_time=1.5, buff=0.05))
        
        copy = fx_lim[2][5].copy()
        self.wait(2)
        self.play(LaggedStart(
            copy.animate(rate_func=rate_functions.ease_out_sine).move_to(fx_lim[3][0]),
            Transform(fx_lim[3][0], fx_lim_1[3][0]),
            lag_ratio=0.3
        ))

        self.play(FadeOut(copy), FadeTransform(fx_lim, fx_lim_1, replace_mobject_with_target_in_scene=True))
        self.wait(1)
        self.play(TransformMatchingTex(fx_lim_1, fx_lim_2, rate_func=rate_functions.ease_out_sine))
        self.wait(3)

        k1 = VGroup(fx_lim_2[4][4], fx_lim_2[4][4])
        nk = VGroup(fx_lim_2[4][4], fx_lim_2[4][4])
        # self.play(HighlightWithRect(k1))

        # self.wait(2)

        self.play(MathSubstitutionTransform(fx_lim_2, fx_lim_3, replace=True))
        self.wait(2)

        self.play(
            HighlightWithRect(VGroup((fx_lim_3[4][0]),fx_lim_3[4][1])),
            HighlightWithRect(fx_lim_3[4][6]),
            HighlightWithRect(VGroup((fx_lim_3[5][4]), fx_lim_3[5][5]))
        )

        self.wait(1)
        k_factorial = VGroup(fx_lim_3[4][3], fx_lim_3[4][4])
        n_to_the_k = VGroup(fx_lim_3[5][4], fx_lim_3[5][5])
        k_target = VGroup(fx_lim_4[5][4], fx_lim_4[5][5])
        n_target  = VGroup(fx_lim_4[4][3], fx_lim_4[4][4])

        self.play(LaggedStart(
            ReplacementTransform(k_factorial, k_target, path_arc=90*DEGREES),
            ReplacementTransform(n_to_the_k, n_target, path_arc=-90*DEGREES),
            lag_ratio=0.1,
            run_time=2,
            rate_func=rate_functions.ease_out_sine
        ))
        self.play(FadeTransform(fx_lim_3, fx_lim_4, run_time=0.1))

        lim_4 = VGroup(fx_lim_4[3], fx_lim_4[4])
        terms_4 = VGroup(fx_lim_4[5], fx_lim_4[6])
        lim_5 = VGroup(fx_lim_5[5], fx_lim_5[6])
        terms_5 = VGroup(fx_lim_5[3], fx_lim_5[4])
        self.wait(2)
        self.play(
            lim_4.animate.move_to(lim_5),
            terms_4.animate.move_to(terms_5)
        )
        self.wait(2)
        limit = lim_4.copy()
        
        limit_highlight_rect = CreateHighlightRect(limit)
        eq_sign = MathTex("=", font_size=32).set_color(PRIMARY_COLOR).scale(1.25).rotate(np.pi/2)
        eq_sign.next_to(limit_highlight_rect, UP)
        L_eq = MathTex("L", font_size=30).set_color(PRIMARY_COLOR).scale(1.25)
        L_eq.next_to(eq_sign, UP)
        self.play(Create(limit_highlight_rect))
        self.play(Succession(FadeIn(eq_sign), Write(L_eq)))

        fx_lim_4_copy = fx_lim_4.copy()
        fx_lim_4_copy.scale(0.6).to_corner(DL, buff=0.5)
        

        fx0_L = MathTex("f(x_0+\\Delta x)","=","\\sum_{k=0}^{\\infty}","\\frac{\\Delta x^k}{k!}","f^k(x_0)", "L", font_size=30).set_color(PRIMARY_COLOR).scale(1.25).scale(0.6).to_corner(DL, buff=0.5)
        eq_box = SurroundingRectangle(fx0_L, color=PRIMARY_COLOR, buff=0.1)
        eq_box.set_stroke(opacity=0.5, width=1)

        self.play(LaggedStart(
            FadeIn(limit),
            fx_lim_4.animate.scale(0.6).to_corner(DL, buff=0.5),
            lag_ratio = 0.3,  
        ))

        self.play(
            Transform(lim_4, fx0_L[5]),
            FadeIn(eq_box)
        )

        l_lim_eq = MathTex("L","=","\\lim_{n \\to \\infty}","\\frac{n!}{n^k(n-k)!}", font_size=30).set_color(PRIMARY_COLOR).scale(1.25)
        l_lim_eq_expanded = MathTex("L","=","\\lim_{n \\to \\infty}","\\frac{n\\cdot (n-1)!}{n^k(n-k)!}", font_size=30).set_color(PRIMARY_COLOR).scale(1.25).move_to(l_lim_eq, aligned_edge=LEFT)
        l_lim_eq_expanded_1 = MathTex("L","=","\\lim_{n \\to \\infty}","\\frac{n\\cdot (n-1)\\cdot (n-2)!}{n^k(n-k)!}", font_size=30).set_color(PRIMARY_COLOR).scale(1.25).move_to(l_lim_eq, aligned_edge=LEFT)
        l_lim_eq_expanded_2 = MathTex("L","=","\\lim_{n \\to \\infty}","\\frac{n\\cdot (n-1)\\cdot (n-2) \\dots (n-k+1) \\cdot (n-k)!}{n^k(n-k)!}", font_size=30).set_color(PRIMARY_COLOR).scale(1.25)
        l_lim_eq_expanded_3 = MathTex("L","=","\\lim_{n \\to \\infty}","\\frac{n\\cdot (n-1)\\cdot (n-2) \\dots (n-k+1)}{n^k}", font_size=30).set_color(PRIMARY_COLOR).scale(1.25).move_to(l_lim_eq_expanded_2, aligned_edge=UL)



        _n = l_lim_eq[3][0]
        _factorial = l_lim_eq[3][1]
        _n_target = l_lim_eq_expanded[3][0]
        _factorial_target = l_lim_eq_expanded[3][7]
        _dot = l_lim_eq_expanded[3][1]
        _n_1_factorial = VGroup(
            l_lim_eq_expanded[3][2], l_lim_eq_expanded[3][3], l_lim_eq_expanded[3][4], 
            l_lim_eq_expanded[3][5], l_lim_eq_expanded[3][6]
        )

        _factorial_1 = l_lim_eq_expanded[3][7]
        _denominator = VGroup(*l_lim_eq_expanded[3][9:])
        _fraction_bar = l_lim_eq_expanded[3][8]
        _dot_1 = l_lim_eq_expanded_1[3][7]
        _n_2_factorial = VGroup(
            l_lim_eq_expanded_1[3][8], l_lim_eq_expanded_1[3][9], l_lim_eq_expanded_1[3][10], 
            l_lim_eq_expanded_1[3][11], l_lim_eq_expanded_1[3][12]
        )
        _factorial_1_target = l_lim_eq_expanded_1[3][13]
        _denominator_target = VGroup(*l_lim_eq_expanded_1[3][15:])
        _fraction_bar_target = l_lim_eq_expanded_1[3][14]


        _cdots = VGroup(l_lim_eq_expanded_2[3][13], l_lim_eq_expanded_2[3][14], l_lim_eq_expanded_2[3][15])
        _n_k_1 = VGroup(
            l_lim_eq_expanded_2[3][16], l_lim_eq_expanded_2[3][17], l_lim_eq_expanded_2[3][18],
            l_lim_eq_expanded_2[3][19], l_lim_eq_expanded_2[3][20], l_lim_eq_expanded_2[3][21],
            l_lim_eq_expanded_2[3][22]
        )
        _dot_2 = l_lim_eq_expanded_2[3][23]
        _n_k_factorial = VGroup(
            l_lim_eq_expanded_2[3][24], l_lim_eq_expanded_2[3][25], l_lim_eq_expanded_2[3][26], 
            l_lim_eq_expanded_2[3][27], l_lim_eq_expanded_2[3][28]
        )
        _factorial_2_target = l_lim_eq_expanded_2[3][29]
        _fraction_bar_target_1 = l_lim_eq_expanded_2[3][30]
        _denominator_target_1 = VGroup(*l_lim_eq_expanded_2[3][31:])
        _nk_factorial_denominator = VGroup(*l_lim_eq_expanded_2[3][33:])
        _nk_factorial_numerator = VGroup(*l_lim_eq_expanded_2[3][24:30])

        _fraction_bar_target_2 = l_lim_eq_expanded_3[3][23]

        limit_part = VGroup(l_lim_eq[2], l_lim_eq[3])

        _nk = VGroup(l_lim_eq_expanded_2[3][31:33])
        _nk_target = VGroup(l_lim_eq_expanded_3[3][24:26])
        _numerator_remaining = VGroup(l_lim_eq_expanded_2[3][:23])
        _numerator = VGroup(l_lim_eq_expanded_3[3][:23])

        self.wait(1)
        self.play(LaggedStart(
            FadeOut(limit_highlight_rect),
            AnimationGroup(
                ReplacementTransform(L_eq, l_lim_eq[0], path_arc=90*DEGREES),
                ReplacementTransform(eq_sign, l_lim_eq[1], path_arc=90*DEGREES),
                ReplacementTransform(limit, limit_part)
            ),
            lag_ratio=0.3
        ))

        self.wait(3)
        # self.play(FadeIn(l_lim_eq_expanded))

        self.play(LaggedStart(
            _n.animate.move_to(_n_target),
            _factorial.animate.move_to(_factorial_target),
            LaggedStart(FadeIn(_dot, shift=DOWN), FadeIn(_n_1_factorial, shift=DOWN), lag_ratio=0.3),
            lag_ratio = 0.3 
        ))

        self.play(FadeTransform(l_lim_eq, l_lim_eq_expanded))

        self.wait(1)

        self.play(LaggedStart(
            AnimationGroup(
                Transform(_fraction_bar, _fraction_bar_target),
                _factorial_1.animate.move_to(_factorial_1_target),
                _denominator.animate.move_to(_denominator_target)
            ),
            LaggedStart(
                FadeIn(_dot_1, shift=DOWN),
                FadeIn(_n_2_factorial, shift=DOWN),
                lag_ratio=0.3
            ),
            lag_ratio=0.3
        ))
        self.play(FadeTransform(l_lim_eq_expanded, l_lim_eq_expanded_1))
        self.play(l_lim_eq_expanded_1.animate.move_to(ORIGIN).align_to(l_lim_eq_expanded_2, LEFT))

        self.wait(1)
        self.play(LaggedStart(
            AnimationGroup(
                Transform(_fraction_bar_target, _fraction_bar_target_1),
                _factorial_1_target.animate.move_to(_factorial_2_target),
                _denominator_target.animate.move_to(_denominator_target_1)
            ),
            LaggedStart(
                FadeIn(_cdots, shift=DOWN),
                FadeIn(_n_k_1, shift=DOWN),
                FadeIn(_dot_2, shift=DOWN),
                FadeIn(_n_k_factorial, shift=DOWN),
                lag_ratio = 0.3
            ),
            lag_ratio=0.3
        ))

        self.play(FadeTransform(l_lim_eq_expanded_1, l_lim_eq_expanded_2))

        self.wait(1)
        self.play(LaggedStart(
            AnimationGroup(
                SlashAndFadeOut(_nk_factorial_denominator), 
                SlashAndFadeOut(_nk_factorial_numerator),
                ReplacementTransform(l_lim_eq_expanded_2[0], l_lim_eq_expanded_3[0]),
                ReplacementTransform(l_lim_eq_expanded_2[1], l_lim_eq_expanded_3[1]),
                ReplacementTransform(l_lim_eq_expanded_2[2], l_lim_eq_expanded_3[2]),
                ReplacementTransform(_numerator_remaining,_numerator),
                ReplacementTransform(_nk, _nk_target)
            ),
            FadeOut(_dot_2),
            ReplacementTransform(_fraction_bar_target_1,_fraction_bar_target_2),
            lag_ratio=0.4
        ))
        self.wait(1)
        self.play(l_lim_eq_expanded_3.animate.move_to(ORIGIN))
        self.wait(1)

        k_terms_brace = Brace(l_lim_eq_expanded_3[3], UP, buff=0.2, color=PRIMARY_COLOR)
        brace_text_1 = MathTex("n-(n-k+1)+1", font_size=26).set_color(PRIMARY_COLOR)
        brace_text_11 = MathTex("n-n+k-1+1", font_size=26).set_color(PRIMARY_COLOR)
        brace_text_12 = MathTex("k", font_size=26).set_color(PRIMARY_COLOR)
        brace_text_2 = MathTex("termos", font_size=26).set_color(PRIMARY_COLOR).next_to(brace_text_1, RIGHT, buff=0.2)

        brace_text = VGroup(brace_text_1, brace_text_2).next_to(k_terms_brace, UP)
        brace_text_11.move_to(brace_text_1, aligned_edge=RIGHT)
        brace_text_12.move_to(brace_text_1, aligned_edge=RIGHT)

        self.play(FadeIn(k_terms_brace), Write(brace_text_1), Write(brace_text_2))
        self.wait(2)
        self.play(LaggedStart(
            AnimationGroup(
                FadeOut(brace_text_1[0][2], shift=UP),
                FadeOut(brace_text_1[0][8], shift=UP)
            ),
            AnimationGroup(
                ReplacementTransform(brace_text_1[0][0], brace_text_11[0][0]),
                ReplacementTransform(brace_text_1[0][1], brace_text_11[0][1]),
                ReplacementTransform(brace_text_1[0][3], brace_text_11[0][2]),
                ReplacementTransform(brace_text_1[0][4], brace_text_11[0][3]),
                ReplacementTransform(brace_text_1[0][5], brace_text_11[0][4]),
                ReplacementTransform(brace_text_1[0][6], brace_text_11[0][5]),
                ReplacementTransform(brace_text_1[0][7], brace_text_11[0][6]),
                ReplacementTransform(brace_text_1[0][9], brace_text_11[0][7]),
                ReplacementTransform(brace_text_1[0][10], brace_text_11[0][8])
            ),
            lag_ratio=0.3
        ))

        brace_text = VGroup(brace_text_12, brace_text_2.copy()).next_to(k_terms_brace, UP)
        self.wait(2)
        self.play(LaggedStart(
            AnimationGroup(
                SlashAndFadeOut(brace_text_11[0][0]),                
                SlashAndFadeOut(brace_text_11[0][2]),
                SlashAndFadeOut(brace_text_11[0][6]),
                SlashAndFadeOut(brace_text_11[0][8]),
            ),
            AnimationGroup(
                FadeOut(brace_text_11[0][1]),
                FadeOut(brace_text_11[0][3]),
                FadeOut(brace_text_11[0][5]),
                FadeOut(brace_text_11[0][7]),
            ),
            AnimationGroup(
                ReplacementTransform(brace_text_11[0][4], brace_text_12),
                ReplacementTransform(brace_text_2, brace_text[1])
            ),
            lag_ratio=0.5
        ))

        l_lim_eq_expanded_4 = MathTex("L","=","\\lim_{n \\to \\infty}","\\frac{n}{n}\\cdot \\frac{(n-1)}{n}\\cdot \\frac{(n-2)}{n} \\dots \\frac{(n-k+1)}{n}", font_size=30).set_color(PRIMARY_COLOR).scale(1.25).move_to(l_lim_eq_expanded_3, aligned_edge=UL)
        fraction_bar_copy_1 = _fraction_bar_target_2
        fraction_bar_copy_2 = _fraction_bar_target_2.copy()
        fraction_bar_copy_3 = _fraction_bar_target_2.copy()
        fraction_bar_copy_4 = _fraction_bar_target_2.copy()
        _dot_1 = l_lim_eq_expanded_3[3][1]
        _dot_2 = l_lim_eq_expanded_3[3][7]
        _dots = l_lim_eq_expanded_3[3][13:16]
        _n_ = l_lim_eq_expanded_3[3][0]
        _n_1 = l_lim_eq_expanded_3[3][2:7]
        _n_2 = l_lim_eq_expanded_3[3][8:13]
        _n_k_1_ = l_lim_eq_expanded_3[3][16:23]
        _n_copy_1 = l_lim_eq_expanded_3[3][-2]
        _n_copy_2 = l_lim_eq_expanded_3[3][-2].copy()
        _n_copy_3 = l_lim_eq_expanded_3[3][-2].copy()
        _n_copy_4 = l_lim_eq_expanded_3[3][-2].copy()
        

        self.wait(4)
        self.play(HighlightWithRect(_nk_target))
        self.wait(5)

        self.play(LaggedStart(
            AnimationGroup(
                ReplacementTransform(l_lim_eq_expanded_3[0], l_lim_eq_expanded_4[0]),
                ReplacementTransform(l_lim_eq_expanded_3[1], l_lim_eq_expanded_4[1]),
                ReplacementTransform(l_lim_eq_expanded_3[2], l_lim_eq_expanded_4[2]),
                ReplacementTransform(fraction_bar_copy_1, l_lim_eq_expanded_4[3][1]),
                ReplacementTransform(fraction_bar_copy_2, l_lim_eq_expanded_4[3][9]),
                ReplacementTransform(fraction_bar_copy_3, l_lim_eq_expanded_4[3][17]),
                ReplacementTransform(fraction_bar_copy_4, l_lim_eq_expanded_4[3][29])
            ),
            FadeOut(l_lim_eq_expanded_3[3][-1]),
            AnimationGroup(
                ReplacementTransform(_n_, l_lim_eq_expanded_4[3][0]),
                ReplacementTransform(_dot_1, l_lim_eq_expanded_4[3][3]),
                ReplacementTransform(_dot_2, l_lim_eq_expanded_4[3][11]),
                ReplacementTransform(_dots, l_lim_eq_expanded_4[3][19:22]),
                ReplacementTransform(_n_1, l_lim_eq_expanded_4[3][4:9]),
                ReplacementTransform(_n_2, l_lim_eq_expanded_4[3][12:17]),
                ReplacementTransform(_n_k_1_, l_lim_eq_expanded_4[3][22:29]),
                ReplacementTransform(_n_copy_1, l_lim_eq_expanded_4[3][2]),
                ReplacementTransform(_n_copy_2, l_lim_eq_expanded_4[3][10]),
                ReplacementTransform(_n_copy_3, l_lim_eq_expanded_4[3][18]),
                ReplacementTransform(_n_copy_4, l_lim_eq_expanded_4[3][30]),
            ),
            lag_ratio=0.3
        ))
        
        l_lim_eq_expanded_41 = MathTex("L","=","\\lim_{n \\to \\infty}","\\frac{n}{n}","\\cdot","\\frac{(n-1)}{n}","\\cdot","\\frac{(n-2)}{n}","\\dots","\\frac{(n-k+1)}{n}", font_size=30).set_color(PRIMARY_COLOR).scale(1.25).move_to(l_lim_eq_expanded_4)
        self.play(FadeTransform(l_lim_eq_expanded_4, l_lim_eq_expanded_41))
        l_lim_eq_expanded_5 = MathTex("L","=","\\lim_{n \\to \\infty}","1","\\cdot","\\left(1-\\frac{1}{n}\\right)","\\cdot","\\left(1-\\frac{2}{n}\\right)","\\dots","\\left(1+\\frac{1-k}{n}\\right)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25).move_to(l_lim_eq_expanded_41, aligned_edge=UL)
        l_lim_eq_expanded_51 = MathTex("L","=","\\lim_{n \\to \\infty}","1","\\cdot","\\left(1-","\\frac{1}{n}","\\right)","\\cdot","\\left(1-","\\frac{2}{n}","\\right)","\\dots","\\left(1+","\\frac{1-k}{n}","\\right)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25).move_to(l_lim_eq_expanded_5, aligned_edge=UL)
        l_lim_eq_expanded_6 = MathTex("L","=","\\lim_{n \\to \\infty}","1","\\cdot","\\left(1-","0","\\right)","\\cdot","\\left(1-","0","\\right)","\\dots","\\left(1+","0","\\right)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25).move_to(l_lim_eq_expanded_5, aligned_edge=UL)
        l_lim_eq_expanded_6[2].set_opacity(0)
        aux = VGroup(*l_lim_eq_expanded_6[3:])

        self.wait(5)
        

        self.play(MathSubstitutionTransform(l_lim_eq_expanded_41, l_lim_eq_expanded_5))
        self.play(
            FadeTransform(l_lim_eq_expanded_5, l_lim_eq_expanded_51)
        )
        self.wait(1)
        self.play(HighlightWithRect(l_lim_eq_expanded_5[5][3:6]))
        self.wait(1)
        self.play(HighlightWithRect(l_lim_eq_expanded_5[7][3:6]))
        self.wait(1)
        self.play(HighlightWithRect(l_lim_eq_expanded_5[9][3:6]))
        

        self.wait(8)

        self.play(
            MathSubstitutionTransform(l_lim_eq_expanded_51, l_lim_eq_expanded_6),
        )
        aux_copy = aux.copy()
        aux_copy.align_to(l_lim_eq_expanded_51[2], LEFT)
        k_terms_brace_1 = Brace(aux_copy, UP, buff=0.2, color=PRIMARY_COLOR)
        brace_text_copy = brace_text.copy().next_to(k_terms_brace_1, UP)
        self.wait(6)
        self.play(
            aux.animate.align_to(l_lim_eq_expanded_51[2], LEFT),
            Transform(k_terms_brace, k_terms_brace_1),
            Transform(brace_text, brace_text_copy)
        )
        # eq_group = VGroup(k_terms_brace, brace_text, l_lim_eq_expanded_6)
        # self.play(
        #     eq_group.animate.move_to(ORIGIN)
        # )


        l_lim_eq_expanded_61 = MathTex("L","=","1","\\cdot","\\left(1-","0","\\right)","\\cdot","\\left(1-","0","\\right)","\\dots","\\left(1+","0","\\right)", font_size=30).set_color(PRIMARY_COLOR).scale(1.25).move_to(l_lim_eq_expanded_6, aligned_edge=UL)
        self.play(
            FadeTransform(l_lim_eq_expanded_6, l_lim_eq_expanded_61)
        )
        l_lim_eq_expanded_7 = MathTex("L","=","1","\\cdot","1","\\cdot","1","\\dots","1", font_size=30).set_color(PRIMARY_COLOR).scale(1.25).move_to(l_lim_eq_expanded_61, aligned_edge=UL)

        aux_2 = l_lim_eq_expanded_7[2:]
        k_terms_brace_2 = Brace(aux_2, UP, buff=0.2, color=PRIMARY_COLOR)
        brace_text_copy_1 = brace_text.copy().next_to(k_terms_brace_2, UP)
        self.play(
            TransformMatchingTex(l_lim_eq_expanded_61, l_lim_eq_expanded_7),
            Transform(k_terms_brace, k_terms_brace_2),
            Transform(brace_text, brace_text_copy_1)
        )
        self.wait(2)
        eq_group = VGroup(k_terms_brace, brace_text, l_lim_eq_expanded_7)
        self.play(
            eq_group.animate.move_to(ORIGIN)
        )
        l_eq_1 = MathTex("L","=","1", font_size=30).set_color(PRIMARY_COLOR).scale(1.25).move_to(l_lim_eq_expanded_7)
        l_eq_1_copy = l_eq_1.copy()
        l_eq_1_copy.shift(3*RIGHT)
        fx_lim_4_copy = fx0_L.copy()
        fx_lim_4_copy.scale(5/3).next_to(l_eq_1_copy, 3*LEFT)
        l_eq_1_copy.align_to(fx_lim_4_copy[-1], UP)
        self.play(
            FadeOut(k_terms_brace, brace_text),
            FadeOut(*l_lim_eq_expanded_7[3:]),
            ReplacementTransform(l_lim_eq_expanded_7[0], l_eq_1[0]),
            ReplacementTransform(l_lim_eq_expanded_7[1], l_eq_1[1]),
            ReplacementTransform(l_lim_eq_expanded_7[2], l_eq_1[2])
        )
        self.wait(1)
        self.play(HighlightWithRect(l_eq_1))
        self.wait(2)
        self.play(LaggedStart(
            FadeOut(eq_box),
            fx_lim_4.animate.scale(5/3).move_to(fx_lim_4_copy),
            l_eq_1.animate.move_to(l_eq_1_copy)
        ))

        self.wait(1)
        self.play(HighlightWithRect(l_eq_1), HighlightWithRect(fx_lim_4_copy[-1]))
        self.play(
            l_eq_1[0].animate.move_to(fx_lim_4_copy[-1]).set_opacity(0),
            l_eq_1[1].animate.move_to(fx_lim_4_copy[-1]).set_opacity(0),
            l_eq_1[2].animate.move_to(fx_lim_4_copy[-1]),
            FadeOut(lim_4)
        )
        lim_4.set_opacity(0)

        self.wait(0.5)
        self.play(
            SlashAndFadeOut(l_eq_1[2]),
        )
        self.play(
            fx_lim_4.animate.move_to(ORIGIN)
        )

        serie_de_taylor_label = Text("Série de Taylor", font_size=30, color=PRIMARY_COLOR).next_to(fx_lim_4, 3*UP)
        highligh_rect = CreateHighlightRect(fx_lim_4)
        self.play(LaggedStart(
            Create(highligh_rect),
            Write(serie_de_taylor_label),
            lag_ratio=0.3
        ))

        self.wait(6)