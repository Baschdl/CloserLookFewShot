# Create train, val, test split
from generate_cross_domain_split import generate_cross_domain_split
base_classes = ["beaver", "dolphin", "otter", "seal", "whale", "aquarium_fish", "flatfish", "ray", "shark", "trout"]
val_classes = ["bicycle", "bus"]
novel_classes = ["motorcycle", "pickup_truck", "train"]
generate_cross_domain_split(base_classes, val_classes, novel_classes)
