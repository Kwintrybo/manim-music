import manim as m


class HelloLaTeX(m.Scene):
    def construct(self):
        tex = m.Tex(r"\LaTeX", font_size=144)
        self.add(tex)


class MathTeXDemo(m.Scene):
    def construct(self):
        rtarrow0 = m.MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        rtarrow1 = m.Tex(r"$\xrightarrow{x^6y^8}$", font_size=96)

        self.add(m.VGroup(rtarrow0, rtarrow1).arrange(m.DOWN))


class LilyPondTest(m.Scene):
    def construct(self):
        template = m.TexTemplate(
            preamble=r"\usepackage{lyluatex}", tex_compiler="lualatex")
        music = m.Tex(r"""
\begin{lilypond}

music = {c' e' g'}
\score {
    \new Staff <<
        \clef bass
        \music
    >>
}

\end{lilypond}
""", tex_template=template)
        self.play(m.FadeIn(music))
