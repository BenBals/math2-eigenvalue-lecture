from manim import *


class Eigenvalues(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors = False,
        )

    def construct(self):
        matrix = Matrix([[2, 1.5], [1, 1.5]])
        matrix.to_corner(UP + LEFT)
        self.play(FadeIn(matrix, shift=UP))
        m = [[2, 1.5], [1, 1.5]]
        vec1 = Vector([1,0],color=GREEN)
        vec2 = Vector([-1,1],color=RED)
        self.play(GrowArrow(vec1),GrowArrow(vec2))
        shadow1 = Vector([1,0],color=GRAY)
        shadow2 = Vector([-1,1],color=GRAY)
        self.wait()
        self.add(shadow1,shadow2)
        # hacky dont touch
        self.moving_mobjects = [vec1,vec2]
        self.moving_vectors = [vec1,vec2]
        self.apply_matrix(m)
        # end hacky
        self.wait()

class Dimension(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors = False,
        )

    def construct(self):
        matrix = Matrix([[2, 1.5], [1, 1.5]])
        matrix.to_corner(UP + LEFT)
        self.play(FadeIn(matrix, shift=UP))
        m = [[2, 1.5], [1, 1.5]]
        vec1 = Vector([1,0],color=GREEN)
        vec2 = Vector([0,1],color=RED)
        self.play(GrowArrow(vec1),GrowArrow(vec2))
        shadow1 = Vector([1,0],color=GRAY)
        shadow2 = Vector([0,1],color=GRAY)
        self.wait()
        self.add(shadow1,shadow2)
        # hacky dont touch
        self.moving_mobjects = [vec1,vec2]
        self.moving_vectors = [vec1,vec2]
        self.apply_matrix(m)
        # end hacky
        self.wait()