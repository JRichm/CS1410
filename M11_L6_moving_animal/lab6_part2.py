import pygame as pg

img_path = "./capybara.png"


class AnimalMover:
    def __init__(self):

        # open image and scale to size
        self.sprite_size = 100
        self.sprite = pg.image.load(img_path)
        self.sprite = pg.transform.scale(self.sprite, (self.sprite_size, self.sprite_size))

        # initialize window
        self.screen_width = 800
        self.screen_height = 600
        self.window = pg.display.set_mode((self.screen_width, self.screen_height))
        pg.display.set_caption("Capybara (using rect)")

        # start position in the middle of the screen
        self.position = (
            self.screen_width / 2 - self.sprite_size / 2,
            self.screen_height / 2 - self.sprite_size / 2
        )

        # move direction (1 for right, -1 for left)
        self.direction = 1

        # amount of pixels to move per frame
        self.speed = 2

        # start main loop
        self.running = True
        self.clock = pg.time.Clock()
        self.main()


    def main(self):

        # main loop
        while self.running:

            # fill window with black
            self.window.fill("black")

            # hanle pygame events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    return
            
            # update animal position
            self.move()

            # draw animal
            self.window.blit(self.sprite, self.position)

            # flip display
            pg.display.flip()

            # wait for next frame
            self.clock.tick(30)


    def move(self):
        
        # get rect and make sure both left and right are within bounds of the window
        rect = self.sprite.get_rect(topleft=self.position)
        if rect.left <= 0 or rect.right > self.screen_width:
            self.direction *= -1

        # calculate new x position
        new_x = self.position[0] + self.speed * self.direction
        
        # set position attribute
        self.position = (
            new_x,
            self.position[1]
        )



if __name__ == "__main__":
    AnimalMover()