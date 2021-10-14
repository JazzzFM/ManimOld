class MoveCamera2(ThreeDScene):
    def get_axis(self, min_val, max_val, axis_config):
        new_config = merge_config([
            axis_config,
            {"x_min": min_val, "x_max": max_val},
            self.number_line_config,
        ])
        return NumberLine(**new_config)
    ThreeDAxes(
    x_min.
    x_max,
    y_min,
    y_max,
    z_min,
    z_max
    )
    def construct(self):
        image = ImageMobject("/home/jazzzfm/ManimOld/Fondos/stars.jpg")
        image.scale(6)
        self.add(image)
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=80 * DEGREES)           
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.begin_ambient_camera_rotation(rate=0.1)            #Start move camera
        self.wait(5)
        self.stop_ambient_camera_rotation()                     #Stop move camera
        self.move_camera(phi=80*DEGREES,theta=-PI/2)            #Return the position of the camera
        self.wait()