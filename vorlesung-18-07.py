from manim import *

class LinearTransformationSceneExample(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )

    def construct(self):
        matrix = [[2, 1.5], [1, 1.5]]
        self.apply_matrix(matrix)
        self.wait()