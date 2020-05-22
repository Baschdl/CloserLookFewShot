# Create train, val, test split
from generate_cross_domain_split import generate_cross_domain_split
base_classes = ["beaver", "dolphin", "otter", "seal", "whale"]
val_classes = ["aquarium_fish", "flatfish"]
novel_classes = ["ray", "shark", "trout"]
generate_cross_domain_split(base_classes, val_classes, novel_classes)
