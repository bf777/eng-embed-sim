#!/usr/bin/env python


class PhysicsBody1D:
    """ A simple 1 dimensional physics object """
    
    # Note: All units are SI

    def __init__(self):
                
        # Note: mass can change during simulation, but usually doesn't
        self.mass = 0.0            # kg
        
        # Volatile
        self.acceleration = 0.0    # m/s^2
        self.velocity = 0.0        # m/s
        self.position = 0.0        # m
        
        self.net_force = 0.0       # Newtons, in the x direction. Note that this is cleared after each step.
        
        
    def step(self, dt_usec):
        """ Take a single step (called during simulation) """
        # @todo: update acceleration, velocity, and position based on self.net_force applied over dt_usec
        
        t_sec = dt_usec / 1000000
        
        # F = ma, a = F/m
        self.acceleration = self.net_force / self.mass
        
        # v*t + 1/2*a*t^2
        # @todo: update position before velocity? 
        self.position += self.velocity * t_sec + 0.5 * self.acceleration * t_sec * t_sec
        
        # vf = v0 + at
        self.velocity = self.velocity + self.acceleration * t_sec
        
            

if __name__ == "__main__":
    body = PhysicsBody1D()
    body.mass = 250
    
    fixed_timestep_usec = 1000000
    body.net_force = 30  # Continuously apply 30 newtons of force
    for i in xrange(1001):
        t = fixed_timestep_usec * i
        row = [t, body.acceleration, body.position, body.velocity]
        print ",".join([str(x) for x in row])
        body.step(fixed_timestep_usec)  # We take an extra step at the end, but don't print it. Keeps the printing code simple.
        
