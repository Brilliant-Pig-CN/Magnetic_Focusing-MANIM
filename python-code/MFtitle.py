from manim import *

class MFT(Scene):
    def construct(self):

        background_image = ImageMobject("E:\ManimProject\MFTBG.png")

        # 调整图片大小以适应屏幕
        background_image.scale_to_fit_height(config.frame_height)
        background_image.scale_to_fit_width(config.frame_width)

        # 将图片移动到中心
        background_image.move_to(ORIGIN)

        # 添加图片到场景作为背景（z_index设为-1确保在底层）
        self.add(background_image)

        # 可选：添加半透明覆盖层以提高文字可读性
        overlay = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=BLACK,
            fill_opacity=0.5,
            stroke_width=0
        )
        self.add(overlay)

        midnights_color1 = "#526087"
        midnights_color2 = "#6998AB"
        title = Text("磁聚焦", font_size=72, fill_opacity=1)

        box = SurroundingRectangle(
            title,
            color="#E0EDFD",           # 边框颜色
            fill_color="#E0EDFD",    # 填充颜色
            fill_opacity= 1,     # 填充透明度
            buff=0.3,             # 文字与边框的间距
            stroke_width=2        # 边框宽度
        )

        title.set_color_by_gradient(midnights_color1, midnights_color2)
        # self.play(Create(box, run_time=2), Write(title, run_time=2))
        self.add(box, title)
        # self.wait(2)