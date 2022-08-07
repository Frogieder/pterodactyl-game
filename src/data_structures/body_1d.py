class Body1D:
    def __init__(self, position=0, mass=1, velocity=0, gravity=0):
        self.mass = mass
        self.position = position  # pixel
        self.velocity = velocity  # pixel / second
        self.gravity = gravity    # pixel / second^2

    def time_step(self, dt):
        self.position += 0.5*self.gravity*dt**2 + self.velocity*dt
        self.velocity += self.gravity*dt
        return self.position
