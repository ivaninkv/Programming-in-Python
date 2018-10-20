class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []
        
    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
    
    def set_lights(self, lights):
        self.lights = lights
        self.generate_lights()
    
    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.generate_lights()
        
    def generate_lights(self):
        return self.grid.copy()


class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1 # Источники света
        self.map[5][2] = -1 # Стены
    
    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)


class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        self.adaptee.set_dim((len(grid[0]), len(grid)))
        light = [(i2, i1) for i1, e1 in enumerate(grid) for i2, e2 in enumerate(e1) if e2 == 1]
        obstacles = [(i2, i1) for i1, e1 in enumerate(grid) for i2, e2 in enumerate(e1) if e2 == -1]
        print(light)
        print(obstacles)
        self.adaptee.set_lights(light)
        self.adaptee.set_obstacles(obstacles)
        
        return self.adaptee.generate_lights()


def main():
    system = System()        
    light = Light((30, 20))
    adapter = MappingAdapter(light)
    system.get_lightening(adapter)
    # print(system.lightmap)

if __name__ == '__main__':
    main()