
import Augmentor

def aug(path):
    p=Augmentor.Pipeline(path)
    #p.rotate(probability=0.5,max_left_rotation=25,max_right_rotation=10)
    #p.skew_tilt(probability=0.1,magnitude=1)
    #p.skew_corner(probability=0.01,magnitude=1)
    #p.random_distortion(probability=0.01,grid_height=5,grid_width=16,magnitude=8)
    p.shear(probability=0.01,max_shear_left=15,max_shear_right=15)
    #p.random_erasing(probability=0.3,rectangle_area=0.5)
    p.zoom(probability=0.5, min_factor=1, max_factor=1.5)
    p.random_brightness(probability=0.2, min_factor=0.7, max_factor=1.2)
    p.random_color(probability=0.2, min_factor=0.7, max_factor=1.2)
    p.random_contrast(probability=0.2, min_factor=0.7, max_factor=1.2)
    p.greyscale(probability=0.4)
    p.sample(11700)

path = "/Users/mamk/Documents/tail/no/"
aug(path)
path = "/Users/mamk/Documents/tail/yes/"
aug(path)