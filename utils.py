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
    BG_COLOR = "#FCF2E0"
    PRIMARY_COLOR = BLACK
    ARROW_COLOR = GRAY_E
    ERROR_COLOR = RED
    SPECIAL_FUNC_COLOR = rgb_to_color(hex_to_rgb("#C00000"))
    TANGENT_LINE_GREEN = GREEN
    TANGENT_LINE_BLUE = BLUE


def MathSubstitutionTransform(math_tex_mob_a, math_tex_mob_b, lag_ratio=0, replace=True):
    if replace:
        return LaggedStart(*[ReplacementTransform(math_tex_mob_a[i], math_tex_mob_b[i]) for i in range(len(math_tex_mob_a.tex_strings))], lag_ratio=lag_ratio)
    else: 
        return LaggedStart(*[Transform(math_tex_mob_a[i], math_tex_mob_b[i]) for i in range(len(math_tex_mob_a.tex_strings))], lag_ratio=lag_ratio)

def MathRemoveTransform(math_tex_mob, remove, lag_ratio=0, replace=True):
    print(math_tex_mob.tex_strings)
    filtered_array = []
    for idx, term in enumerate(math_tex_mob.tex_strings):
        if idx not in remove:
            filtered_array.append(term)

    filtered_mob = MathTex(*filtered_array, font_size=math_tex_mob.get_fontsize()).set_color(math_tex_mob.get_color()).scale(math_tex_mob.get_scale())
    if replace:
        return LaggedStart(*[ReplacementTransform(math_tex_mob[i], filtered_mob[i]) for i in range(len(math_tex_mob.tex_strings))], lag_ratio=lag_ratio)
    else: 
        return LaggedStart(*[Transform(math_tex_mob[i], math_tex_mob[i]) for i in range(len(math_tex_mob.tex_strings))], lag_ratio=lag_ratio)


def CreateSlash(mob):
    width = mob.width
    height = mob.height
    bottom_left_corner = mob.get_corner(DL) + [width/5, -height/4, 0]
    top_right_corner = mob.get_corner(UR) + [-width/5, height/4, 0]
    return Line(bottom_left_corner, top_right_corner, color=SPECIAL_FUNC_COLOR, stroke_width = 1.5)

def SlashAndFadeOut(mob):
    width = mob.width
    height = mob.height
    bottom_left_corner = mob.get_corner(DL) + [width/5, -height/4, 0]
    top_right_corner = mob.get_corner(UR) + [-width/5, height/4, 0]
    line_across = Line(bottom_left_corner, top_right_corner, color=SPECIAL_FUNC_COLOR, stroke_width = 1.5)
    return Succession(FadeIn(line_across), FadeOut(line_across, mob))

def HighlightWithRect(mob, run_time=2, buff=0.1, color=SPECIAL_FUNC_COLOR):
    rect = SurroundingRectangle(mob, color=color, buff=buff).set_stroke(opacity=1, width=2)
    return Succession(FadeIn(rect, run_time=run_time/2, rate_func=rate_functions.ease_out_sine), FadeOut(rect, run_time=run_time/2, rate_func=rate_functions.ease_out_sine))

def CreateHighlightRect(mob, buff=0.1, color=SPECIAL_FUNC_COLOR):
    rect = SurroundingRectangle(mob, color=color, buff=buff).set_stroke(opacity=1, width=2)
    return rect


from manim import *
from PIL import Image, ImageSequence


class GifMobject(ImageMobject):
    """Mostra um GIF dentro do Manim sem converter para vídeo."""
    def __init__(self, path, fps=24, **kwargs):
        pil_gif = Image.open(path)

        # Todos os quadros convertidos para ndarray RGBA
        self.frames = [
            np.asarray(frame.convert("RGBA"))
            for frame in ImageSequence.Iterator(pil_gif)
        ]

        # Inicia com o primeiro quadro
        super().__init__(self.frames[0], **kwargs)

        # Controle de tempo
        self.fps = fps
        self._dt_per_frame = 1 / fps
        self._accum = 0
        self._idx = 0

        self.add_updater(self._update)

    def _update(self, mobj, dt):
        self._accum += dt
        print(self._idx)
        while self._accum >= self._dt_per_frame:
            self._accum -= self._dt_per_frame
            self._idx = (self._idx + 1) % len(self.frames)

            # replace the pixel array *and* flag the object for redraw
            mobj.set(pixel_array= self.frames[self._idx])