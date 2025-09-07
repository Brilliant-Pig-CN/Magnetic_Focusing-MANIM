from manim import *
import numpy as np

r = 2

# 交点的 x 坐标
def cross(x):
    return np.sqrt(r**2 - x**2)

# 画圆弧的参数方程
def arc_parametric(t, c):
    x = c[0] + r * np.cos(t)
    y = c[1] + r * np.sin(t)
    return np.array([x, y, 0])

# 圆弧角度的末尾值
def end_angle(pe, c):
    return np.arccos((c[1] - pe[1])/r)


class MF(Scene):
    def construct(self):
        # color
        dot_color = "#E0EDFD"
        plane_color = "#526087"
        circle_color = "#6998AB"
        lr_color = "#D75689"    # lover
        text_t_color = "#BBD4B7"    # taylor swift
        text_color = "#FECED7"  # lover
        text_r_color = "#FBB3D1"    # lover 
        text_v_color = "#E0C9AF"    # evermore
        # 坐标系
        plane = NumberPlane(x_range=[-10, 10, 1], y_range=[-10, 10, 1],
                            background_line_style={
                "stroke_color": plane_color,  # 网格线颜色
                })
        # 磁聚焦的圆圈磁场区
        c0 = Circle(radius=r, color=circle_color, stroke_width=4)
        # all 粒子的聚焦点
        pend = Dot([0, -r, 0])

        # 第一个发射的粒子
        y1 = 1.2
        p10 = Dot([10, y1, 0], color=dot_color)
        # p1 与圆的交点
        p11 = Dot([cross(y1), y1, 0])
        # 沿直线的轨迹
        l1 = Line(p10.get_center(), p11.get_center())
        # 1 粒子圆周运动的圆心
        c1 = Dot([cross(y1), y1 - r, 0])

        # 粒子做圆周运动的圆弧
        arc1 = ParametricFunction(lambda t: arc_parametric(t, c1.get_center()),
                                  t_range=(np.pi/2, np.pi*3/2 - end_angle(pe=pend.get_center(), c=c1.get_center())),
                                  use_smoothing=True)
        # 记录轨迹
        path1 = TracedPath(p10.get_center, stroke_color=dot_color, stroke_width=3)

        # 组合第一个粒子的路径
        combined_path1 = VMobject()
        combined_path1.set_points_as_corners([*l1.get_points(), *arc1.get_points()])

        # 第二个发射的粒子 y2 = 1.5
        y2 = 1.5
        p20 = Dot([10, y2, 0], color=dot_color)
        # p2 与圆的交点
        p21 = Dot([cross(y2), y2, 0])
        # 沿直线的轨迹
        l2 = Line(p20.get_center(), p21.get_center())
        # 2 粒子圆周运动的圆心
        c2 = Dot([cross(y2), y2 - r, 0])

        # 粒子做圆周运动的圆弧
        arc2 = ParametricFunction(lambda t: arc_parametric(t, c2.get_center()),
                                  t_range=(np.pi/2, np.pi*3/2 - end_angle(pe=pend.get_center(), c=c2.get_center())),
                                  use_smoothing=True)
        # 记录轨迹
        path2 = TracedPath(p20.get_center, stroke_color=dot_color, stroke_width=3)

        # 组合第二个粒子的路径
        combined_path2 = VMobject()
        combined_path2.set_points_as_corners([*l2.get_points(), *arc2.get_points()])

        # 第三个发射的粒子 y3 = 0.7
        y3 = 0.7
        p30 = Dot([10, y3, 0], color=dot_color)
        # p3 与圆的交点
        p31 = Dot([cross(y3), y3, 0])
        # 沿直线的轨迹
        l3 = Line(p30.get_center(), p31.get_center())
        # 3 粒子圆周运动的圆心
        c3 = Dot([cross(y3), y3 - r, 0])

        # 粒子做圆周运动的圆弧
        arc3 = ParametricFunction(lambda t: arc_parametric(t, c3.get_center()),
                                  t_range=(np.pi/2, np.pi*3/2 - end_angle(pe=pend.get_center(), c=c3.get_center())),
                                  use_smoothing=True)
        # 记录轨迹
        path3 = TracedPath(p30.get_center, stroke_color=dot_color, stroke_width=3)

        # 组合第三个粒子的路径
        combined_path3 = VMobject()
        combined_path3.set_points_as_corners([*l3.get_points(), *arc3.get_points()])

        # 第四个发射的粒子 y4 = 0.3
        y4 = 0.3
        p40 = Dot([10, y4, 0], color=dot_color)
        # p4 与圆的交点
        p41 = Dot([cross(y4), y4, 0])
        # 沿直线的轨迹
        l4 = Line(p40.get_center(), p41.get_center())
        # 4 粒子圆周运动的圆心
        c4 = Dot([cross(y4), y4 - r, 0])

        # 粒子做圆周运动的圆弧
        arc4 = ParametricFunction(lambda t: arc_parametric(t, c4.get_center()),
                                  t_range=(np.pi/2, np.pi*3/2 - end_angle(pe=pend.get_center(), c=c4.get_center())),
                                  use_smoothing=True)
        # 记录轨迹
        path4 = TracedPath(p40.get_center, stroke_color=dot_color, stroke_width=3)

        # 组合第四个粒子的路径
        combined_path4 = VMobject()
        combined_path4.set_points_as_corners([*l4.get_points(), *arc4.get_points()])

        # 第五个发射的粒子 y5 = -0.7
        y5 = -0.7
        p50 = Dot([10, y5, 0], color=dot_color)
        # p5 与圆的交点
        p51 = Dot([cross(y5), y5, 0])
        # 沿直线的轨迹
        l5 = Line(p50.get_center(), p51.get_center())
        # 5 粒子圆周运动的圆心
        c5 = Dot([cross(y5), y5 - r, 0])

        # 粒子做圆周运动的圆弧
        arc5 = ParametricFunction(lambda t: arc_parametric(t, c5.get_center()),
                                  t_range=(np.pi/2, np.pi*3/2 - end_angle(pe=pend.get_center(), c=c5.get_center())),
                                  use_smoothing=True)
        # 记录轨迹
        path5 = TracedPath(p50.get_center, stroke_color=dot_color, stroke_width=3)

        # 组合第五个粒子的路径
        combined_path5 = VMobject()
        combined_path5.set_points_as_corners([*l5.get_points(), *arc5.get_points()])

        # 第六个发射的粒子 y6 = - 1.0
        y6 = -1.0
        p60 = Dot([10, y6, 0], color=dot_color)
        # p6 与圆的交点
        p61 = Dot([cross(y6), y6, 0])
        # 沿直线的轨迹
        l6 = Line(p60.get_center(), p61.get_center())
        # 6 粒子圆周运动的圆心
        c6 = Dot([cross(y6), y6 - r, 0])

        # 粒子做圆周运动的圆弧
        arc6 = ParametricFunction(lambda t: arc_parametric(t, c6.get_center()),
                                  t_range=(np.pi/2, np.pi*3/2 - end_angle(pe=pend.get_center(), c=c6.get_center())),
                                  use_smoothing=True)
        # 记录轨迹
        path6 = TracedPath(p60.get_center, stroke_color=dot_color, stroke_width=3)

        # 组合第六个粒子的路径
        combined_path6 = VMobject()
        combined_path6.set_points_as_corners([*l6.get_points(), *arc6.get_points()])

        # 第七个发射的粒子 y7 = - 1.6
        y7 = -1.6
        p70 = Dot([10, y7, 0], color=dot_color)
        # p7 与圆的交点
        p71 = Dot([cross(y7), y7, 0])
        # 沿直线的轨迹
        l7 = Line(p70.get_center(), p71.get_center())
        # 7 粒子圆周运动的圆心
        c7 = Dot([cross(y7), y7 - r, 0])

        # 粒子做圆周运动的圆弧
        arc7 = ParametricFunction(lambda t: arc_parametric(t, c7.get_center()),
                                  t_range=(np.pi / 2, np.pi * 3 / 2 - end_angle(pe=pend.get_center(), c=c7.get_center())),
                                  use_smoothing=True)
        # 记录轨迹
        path7 = TracedPath(p70.get_center, stroke_color=dot_color, stroke_width=3)

        # 组合第七个粒子的路径
        combined_path7 = VMobject()
        combined_path7.set_points_as_corners([*l7.get_points(), *arc7.get_points()])

        # 创建圆点表示磁场
        spacing = 0.5  # 圆点的间距
        dot_radius = 0.02  # 圆点的半径
        dots = VGroup()
        for x in np.arange(-r, r, spacing):
            for y in np.arange(-np.sqrt(r**2 - x**2), np.sqrt(r**2 - x**2), spacing):
                pos = np.array([x, y, 0])
                dot = Dot(point=pos, radius=dot_radius)
                dots.add(dot)


        # 表示出 v
        v = Arrow(start=p11, end=[cross(y1) - 2, y1, 0], color = text_v_color)
        # # 创建数学公式
        # vf = MathTex(r"v = \frac{qBR}{m}")
        # # 将公式放置在箭头的中间位置
        # vf.next_to(v.get_center(), UP, buff=0.2)
        #表示出F
        F = Arrow(start=p11, end=[cross(y1), y1 - 2, 0], color = text_color)
        #写出F的公式
        Ff1 = MathTex(r"F = qvB ", font_size = 48, color = text_color)
        Ff2 = MathTex(r" = m\frac{v^2}{r}", font_size = 48, color = text_color)
        Ff1.next_to(F.get_center(), RIGHT)
        Ff2.next_to(Ff1, RIGHT)
        # 写出 r 的公式
        rf = MathTex(r"r = \frac{mv}{qB}", font_size = 48, color = text_r_color).next_to(Ff1, DOWN)
        rf2 = MathTex(r" = R", font_size = 72, color = text_r_color)
        # 入射点 p11 ———— 粒子圆心 c1 （右竖向下）
        lr1 = Line(
            start = p11.get_center(),
            end = c1.get_center(),
            color = lr_color
        )
        # 圆心 c0 ———— 入射点 p11 （上横向右）
        lr2 = Line(
            start = c0.get_center(),
            end = p11.get_center(),
            color = lr_color
        )
        # 最低点 pend ———— 圆心 c0 （左竖向上）
        lr3 = Line(
            start = pend.get_center(),
            end = c0.get_center(),
            color = lr_color
        )
        # 粒子圆心 c1 ———— 最低点 pend （下横向左）
        lr4 = Line(
            start = c1.get_center(),
            end = pend.get_center(),
            color = lr_color
        )
        
        R1 = Text("R", font_size=56, color=lr_color).next_to(lr1, RIGHT)
        R2 = Text("R", font_size=56, color=lr_color).next_to(lr2, UP)
        R3 = Text("R", font_size=56, color=lr_color).next_to(lr3, LEFT)
        R4 = Text("R", font_size=56, color=lr_color).next_to(lr4, DOWN)
        B = Text("B", font_size=56, color=text_t_color).next_to(c0, UP + LEFT)
        vt = MathTex("v", font_size= 56, color = text_v_color).next_to(v, UP)
        explain = Text("菱形", font_size= 48, color=text_t_color).next_to(lr4, DOWN + RIGHT)
        explain1 = Text("匀速直线运动", font_size=56, color=text_t_color).next_to(v.get_center(), UP + RIGHT + RIGHT)
        explain2 = Text("圆心", font_size=36, color=text_t_color).next_to(c1, RIGHT)

        # # MF1
        self.add(plane)
        self.play(Create(path1), Create(path2), Create(path3),Create(path4),Create(path5),Create(path6),Create(path7))
        # 创建圆
        self.play(Create(c0), Create(dots), run_time = 3)
        # 一群粒子
        self.play(
            LaggedStart(
                MoveAlongPath(p10, combined_path1, rate_func=linear),
                MoveAlongPath(p20, combined_path2, rate_func=linear),
                MoveAlongPath(p30, combined_path3, rate_func=linear),
                MoveAlongPath(p40, combined_path4, rate_func=linear),
                MoveAlongPath(p50, combined_path5, rate_func=linear),
                MoveAlongPath(p60, combined_path6, rate_func=linear),
                MoveAlongPath(p70, combined_path7, rate_func=linear),
                lag_ratio= 0.5
            ),
            run_time = 8
        )
        self.wait(5)
        self.play(FadeOut(c0, dots, path1, path2, path3, path4, path5, path6, path7, pend), run_time = 2)
        self.wait(2)
        self.play(Create(c0), Create(dots), run_time = 3)
        self.wait(2)
        self.play(Create(lr2), run_time = 1)
        self.play(Create(R2),  run_time = 2)
        self.play(Create(B), run_time = 2)
        self.wait(2)

        # MF2
        # # 第一个粒子
        self.add(plane, path1, c0, dots)
        self.wait(2)
        self.play(MoveAlongPath(p10, l1, rate_func = linear), run_time = 1)
        self.wait(2)
        self.add(l1)
        self.play(Create(v), Write(vt), run_time = 1)
        self.wait(2)
        self.play(Write(explain1), run_time = 2)
        self.wait(2)
        self.play(Create(F), Write(Ff1), run_time = 2)
        self.wait(3)
        self.play(ScaleInPlace(v, 2), ScaleInPlace(vt, 2))
        self.play(ScaleInPlace(v, 0.5), ScaleInPlace(vt, 0.5))
        self.wait(1)
        self.play(Write(Ff2), run_time = 3)
        self.wait(3)
        self.play(Write(rf), run_time = 2)
        self.wait(2)
        self.play(ScaleInPlace(rf, 1.5))
        self.play(rf.animate.to_corner(UL), run_time = 3)
        self.play(Write(rf2.next_to(rf, RIGHT)), run_time = 2)
        self.wait(3)
        self.play(FadeOut(v, explain1, F, Ff1, Ff2, vt))
        self.wait(2)

        # MF3
        self.play(Create(lr1), Write(R1), run_time = 4)
        self.play(FadeIn(c1))
        self.play(ScaleInPlace(c1, 2))
        self.play(ScaleInPlace(c1, 0.5))
        self.play(Write(explain2))
        self.wait(1)
        self.play(Create(lr2), Create(lr3), Create(lr4))
        self.play(Write(R3))
        self.play(lr1.animate.shift(RIGHT * 0.5), lr3.animate.shift(RIGHT * 0.5), ScaleInPlace(R1, 1.5), ScaleInPlace(R3, 1.5))
        self.play(lr1.animate.shift(LEFT * 0.5), lr3.animate.shift(LEFT * 0.5), ScaleInPlace(R1, 1 / 1.5), ScaleInPlace(R3, 1 /1.5))
        self.wait(2)
        self.play(Write(R2), Write(R4))
        self.play(ScaleInPlace(R2, 1.5), ScaleInPlace(R4, 1.5))
        self.play(ScaleInPlace(R2, 1 / 1.5), ScaleInPlace(R4, 1/ 1.5))
        self.play(Write(explain))
        self.wait(2)
        self.add(pend)
        self.play(ScaleInPlace(R4, 2), ScaleInPlace(pend, 2))
        self.play(ScaleInPlace(R4, 0.5), ScaleInPlace(pend, 0.5))
        self.wait(3)
        self.play(FadeOut(lr1, lr2, lr3, lr4, R1, R2, R3, R4, explain, explain2, c1))
        self.wait(2)
        self.play(MoveAlongPath(p10, arc1, rate_func = linear))
        self.wait(6)

        # MF4
        # 让多个粒子依次沿着组合路径运动
        self.add(path2, path3, path4, path5, path6, path7)
        self.play(
            LaggedStart(
                MoveAlongPath(p20, combined_path2, run_time=3, rate_func=linear),
                MoveAlongPath(p30, combined_path3, run_time=3, rate_func=linear),
                MoveAlongPath(p40, combined_path4, run_time=3, rate_func=linear),
                MoveAlongPath(p50, combined_path5, run_time=3, rate_func=linear),
                MoveAlongPath(p60, combined_path6, run_time=3, rate_func=linear),
                MoveAlongPath(p70, combined_path7, run_time=3, rate_func=linear),
                lag_ratio= 0.5 / 3
            )
        )

        self.wait(2)

        