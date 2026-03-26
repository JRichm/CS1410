import random as rd

import pygame as pg


img_map = {
    0: "./capybara.png",
    1: "./baby_capybara.png"
}



class Animal(pg.sprite.Sprite):
    next_y: int = 0


    def __init__(
        self, 
        image_id: int = 0,
        size: int = 100,
    ):

        super().__init__()

        # open image and scale to size
        self._sprite_size = size
        self._sprite = pg.image.load(img_map.get(image_id))
        self._sprite = pg.transform.scale(self.sprite, (self.sprite_size, self.sprite_size))

        # movement/position variables
        self._position = (400, Animal.next_y)
        self._speed = rd.randint(1, 5)
        self._direction = 1

        Animal.next_y += 100


    @property
    def sprite(self) -> pg.Surface:
        return self._sprite


    @property
    def sprite_size(self) -> int:
        return self._sprite_size


    @property
    def position(self) -> tuple:
        return self._position
    
    
    @property
    def speed(self) -> int:
        return self._speed
    

    @property
    def direction(self) -> int:
        return self._direction


    def change_direction(self):
        self._sprite = pg.transform.flip(self.sprite, True, False)
        self._direction *= -1


    def move(self):
        new_x = self._position[0] + self._speed * self.direction
        self._position = (
            new_x,
            self._position[1]
        )



class Display:
    def __init__(
        self,
        width: int = 800,
        height: int = 600,
    ):

        self._width = width
        self._height = height

        self._window = pg.display.set_mode((self._width, self._height))
        pg.display.set_caption("Capybara")

        self._animal_group: pg.sprite.Group = pg.sprite.Group()

        self._clock = pg.time.Clock()
        self._running = True


    def main(self):
        while self._running:
            self._window.fill("black")

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self._running = False
                    return

            for animal in self._animal_group:
                animal.move()
                self.check_bounds(animal)
                self.draw(animal)

            pg.display.flip()
            self._clock.tick(60)


    def add_animal(self, animal: Animal):
        self._animal_group.add(animal)


    def check_bounds(self, animal: Animal):
        x, y = animal.position
        if x < 0 or x > self._width - animal.sprite_size:
            animal.change_direction()


    def draw(self, animal: Animal):
        self._window.blit(animal.sprite, animal.position)



if __name__ == "__main__":
    pg.init()

    display = Display()

    display.add_animal(Animal(1, 100))
    display.add_animal(Animal(1, 100))
    display.add_animal(Animal(0, 100))
    display.add_animal(Animal(0, 100))
    display.add_animal(Animal(1, 100))
    display.add_animal(Animal(1, 100))

    display.main()




