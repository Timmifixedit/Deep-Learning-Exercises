import random


class MyTransform(object):
    def __init__(self, rotation_abs_range):
        self.abs_angle = rotation_abs_range

    def __call__(self, sample):
        print(type(sample))
        image, label = sample
        angle = random.randint(-self.abs_angle, self.abs_angle)
        image.rotate(angle)
        return image, label
