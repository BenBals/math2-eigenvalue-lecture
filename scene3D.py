from manim import *

class ExampleArrow3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        arrow = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([2, 2, 2]),
            resolution=8
        )
        arrow2 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([2, 4, 4]),
            resolution=8
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, arrow, arrow2)

class AnimateArrow3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=(- 10, 10, 1), y_range=(- 10, 10, 1), z_range=(- 10, 10, 1),x_length=10, y_length=10, z_length=10)
        arrow = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([2, 2, 2]),
            resolution=8,
            color = BLUE
        )
        arrow2 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([2, 4, 4]),
            resolution=8,
            color = BLUE
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES, zoom = 0.5)
        self.add(axes,arrow)
        self.play(Create(arrow))
        self.play(ReplacementTransform(arrow, arrow2))

class AnimatePrism3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=(- 10, 10, 1), y_range=(- 10, 10, 1), z_range=(- 10, 10, 1),x_length=10, y_length=10, z_length=10)
        arrow = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([0, 0, 1]),
            resolution=8,
            color = BLUE
        )
        arrow2 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([0, 1, 0]),
            resolution=8,
            color = BLUE
        )
        arrow3 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([1, 0, 0]),
            resolution=8,
            color = BLUE
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES, zoom = 0.5)
        self.add(axes,arrow, arrow2, arrow3)
        # self.play(Create(arrow))
        # self.play(ReplacementTransform(arrow, arrow2))
        self.move_camera(theta=30*DEGREES,run_time=4)
        self.wait()

class VectorExample(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        self.set_camera_orientation(phi=75 * DEGREES, theta=-80 * DEGREES)

        b1_raw = [1,0,2]
        b2_raw = [1,2,0]
        b3_raw = [2,-1,0]

        b1 = Vector(b1_raw, color=YELLOW)
        b2 = Vector(b2_raw, color=YELLOW)
        b3 = Vector(b3_raw, color=YELLOW)
        self.add(axes)

        T_b1 = Vector(b1_raw, color=YELLOW)
        T_b2 = Vector(b2_raw, color=YELLOW)
        T_b3 = Vector(b3_raw, color=YELLOW)


        self.play(Create(b1), Create(b2))
        #self.play(Transform(b1, T_b1))

class Vectors(VectorScene):
    def construct(self):
        plane = self.add_plane(animate=True).add_coordinates()
        vector = self.add_vector([-3,-2], color=YELLOW)
        basis = self.get_basis_vectors()

        self.add(basis)
        self.vector_to_coords(vector = vector)

        vector2 = self.add_vector([2,2])
        self.write_vector_coordinates(vector = vector2)
        self.wait()

