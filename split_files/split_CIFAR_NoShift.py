# Change to whatever split you like
import os
from CloserLookFewShot.filelists.CIFARFS.generate_cross_domain_split import generate_cross_domain_split
base_path = os.getcwd()
cifar_path = os.path.join(base_path, "CloserLookFewShot/filelists/CIFARFS/")

base_classes = ["poppy", "rose", "tulip", "apple", "sweet_pepper", "maple_tree", "oak_tree"]
val_classes = ["sunflower", "orange", "palm_tree"]
novel_classes = ["orchid", "pear", "pine_tree"]
generate_cross_domain_split(base_classes, val_classes, novel_classes)
