# Change to whatever split you like
import os
from CloserLookFewShot.filelists.CIFARFS.generate_cross_domain_split import generate_cross_domain_split
base_path = os.getcwd()
cifar_path = os.path.join(base_path, "CloserLookFewShot/filelists/CIFARFS/")

base_classes = ["bear", "leopard", "lion", "tiger",  "cattle", "chimpanzee", "elephant"]
val_classes = ["wolf", "kangaroo", "camel",]
novel_classes = ["trout", "aquarium_fish", "flatfish"]
generate_cross_domain_split(base_classes, val_classes, novel_classes)
