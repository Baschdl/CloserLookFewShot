# Change to whatever split you like
import os
from CloserLookFewShot.filelists.CIFARFS.generate_cross_domain_split import generate_cross_domain_split
base_path = os.getcwd()
cifar_path = os.path.join(base_path, "CloserLookFewShot/filelists/CIFARFS/")

base_classes = ["poppy", "rose", "tulip", "palm_tree", "pine_tree", "oak_tree", "willow_tree"]
val_classes = ["orchid", "sunflower", "maple_tree"]
novel_classes = ["apple", "pear", "mushroom"]
generate_cross_domain_split(base_classes, val_classes, novel_classes)
