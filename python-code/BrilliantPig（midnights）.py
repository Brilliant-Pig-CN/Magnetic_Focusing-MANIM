from manim import *

class CMZ(Scene):
    def construct(self):
        text = Text ("Brilliant_Pig", font_size= 50)
        midnigyts_color1 = "#526087"
        midnigyts_color2 = "#6998AB"
        text.set_color_by_gradient(midnigyts_color1, midnigyts_color2)
        self.play(Write(text, run_time=0.5))
        self.wait(1)