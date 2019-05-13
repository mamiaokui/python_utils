
import Augmentor
p=Augmentor.Pipeline("/Users/mamk/ssd/flower_world/water/crop_no")
p.rotate(probability=0.5,max_left_rotation=25,max_right_rotation=10)
p.skew_tilt(probability=0.7,magnitude=1)
p.skew_corner(probability=0.7,magnitude=1)
p.random_distortion(probability=0.3,grid_height=5,grid_width=16,magnitude=8)
p.shear(probability=0.3,max_shear_left=15,max_shear_right=15)
p.random_erasing(probability=0.3,rectangle_area=0.5)
p.zoom_random(probability=0.5, percentage_area=0.5, randomise_percentage_area=True)
p.sample(10000)


p=Augmentor.Pipeline("/Users/mamk/ssd/flower_world/water/crop_yes")
p.rotate(probability=0.5,max_left_rotation=25,max_right_rotation=10)
p.skew_tilt(probability=0.7,magnitude=1)
p.skew_corner(probability=0.7,magnitude=1)
p.random_distortion(probability=0.3,grid_height=5,grid_width=16,magnitude=8)
p.shear(probability=0.3,max_shear_left=15,max_shear_right=15)
p.random_erasing(probability=0.3,rectangle_area=0.5)
p.zoom_random(probability=0.5, percentage_area=0.5, randomise_percentage_area=True)
p.sample(10000)