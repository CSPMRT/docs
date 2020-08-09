***********
Manim安装
***********

.. metadata::
    Chen Longhao
    2020,08,02

安装系统依赖库::

    # apt install ffmpeg

安装LaTeX(TeXLive)::

    # apt install texlive texlive-latex-extra texlive-fonts-extra texlive-latex-recommended texlive-science texlive-fonts-extra tipa

通过pypi安装manimlib::

    # pip3 install manimlib

解决中文无法输出问题：

将manimlib目录下的 ``constants.py`` 里面的其中的 ``TEX_USE_CTEX = False`` 改成 ``TEX_USE_CTEX = True`` ，
具体可参见: https://blog.csdn.net/yiqishangxuewu/article/details/105414057

至此，manim就安装完成了。

一个简单的示例::
    
    from manimlib.imports import *

    class SquareToCircle(Scene):
        def construct(self):
            circle = Circle()
            square = Square()
            square.flip(RIGHT)
            square.rotate(-3 * TAU / 8)
            circle.set_fill(PINK, opacity=0.5)
            clh = TextMobject("Made by Chen Longhao", tex_to_color_map={"text": YELLOW})
            py = TextMobject("Use python",  tex_to_color_map={"text": RED})
            self.play(ShowCreation(square))
            self.play(Transform(square, circle))
            self.play(FadeOut(square))
            self.play(Write(clh))
            self.wait(1)
            self.play(Transform(clh,py))
            self.wait()

编译::

    $ manim 文件名
