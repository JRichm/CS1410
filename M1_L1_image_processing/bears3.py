from PIL import Image

path_bear = './starr_bears.jpg'
path_balloon = './red_balloon.png'
path_out = './bears3.jpg'

# open images
bear_image = Image.open(path_bear)
balloon_image = Image.open(path_balloon)

# get bear image details
bear_pixel_map = bear_image.load()
bear_w, bear_h = bear_image.size
bear_mode = bear_image.mode

# get balloon image details
balloon_pixel_map = balloon_image.load()
balloon_w, balloon_h = balloon_image.size

# define balloon position and scale
balloon_pos = (1100, 150)
balloon_scale = 0.05

# initialize new image
new_image = bear_image.copy()
new_pixel_map = new_image.load()

# loop through balloon pixels
for x in range(balloon_w):
    for y in range(balloon_h):

        # find position on the bear image
        bear_x = balloon_pos[0] + int(x * balloon_scale)
        bear_y = balloon_pos[1] + int(y * balloon_scale)

        # skip pixels that are outide the bounds of the bear image
        if any([bear_x < 0, bear_x >= bear_w, bear_y < 0, bear_y >= bear_h]):
            continue

        # get color of balloon pixel
        pixel = balloon_pixel_map[x, y]
        
        # skip transparent pixels
        if pixel[3] < 10:
            continue

        # blit to pixel map
        new_pixel_map[bear_x, bear_y] = pixel

# save image
new_image.save(path_out)





