# Change to whatever split you like
import os
from CloserLookFewShot.filelists.CIFARFS.generate_cross_domain_split import generate_cross_domain_split
base_path = os.getcwd()
cifar_path = os.path.join(base_path, "CloserLookFewShot/filelists/CIFARFS/")

base_classes = ["cloud", "forest", "mountain", "castle", "house", "road", "skyscraper"]
val_classes = ["plain", "sea", "bridge"]
novel_classes = ["bicycle", "bus", "tractor"]
generate_cross_domain_split(base_classes, val_classes, novel_classes)
