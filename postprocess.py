"""
Beyond Shield post-processing helper:
- Maps raw class names from Roboflow
- Filters low-confidence predictions
- Converts to normalized YOLO-style output
"""

LABEL_MAP = {
    "g - v1 2025-01-15 2-18pm": "Gun",
    "knives": "Knife",
    "person": "Person",
    "car": "Vehicle",
    "climbing": "Climbing"
}

CONF_THRESHOLD = 0.40

def clean(predictions):
    out = []
    for p in predictions:
        if p["confidence"] < CONF_THRESHOLD:
            continue
        p["class"] = LABEL_MAP.get(p["class"], p["class"])
        p["x_center"] = p.pop("x")
        p["y_center"] = p.pop("y")
        p["w"] = p.pop("width")
        p["h"] = p.pop("height")
        out.append(p)
    return out
