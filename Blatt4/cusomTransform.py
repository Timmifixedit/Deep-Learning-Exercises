import random


class MyTransform(object):
    def __init__(self, rotation_abs_range):
        self.abs_angle = rotation_abs_range

    def __call__(self, sample):
        # When called there seems to be a type mismatch, sample cannot be split up.
        # The error persists even if I do the transformation directly on the sample.
        image, label = sample
        angle = random.randint(-self.abs_angle, self.abs_angle)
        image.rotate(angle)
        return image, label
