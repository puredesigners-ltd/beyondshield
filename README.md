# Beyond Shield Utils

🛡️ Helper scripts for Beyond Shield — Pakistan's first AI surveillance system by [Beyond Tahir](https://beyondtahir.com) under [Pure Designers Ltd.](https://puredesigners.com)

---

## 🔧 Files

- `postprocess.py` – Cleans Roboflow-style predictions (label mapping + confidence filtering)
- `demo.py` – Runs the postprocess module on fake JSON
- Future: live inference + draw bounding box overlays

---

## 📦 Example Usage

```python
from postprocess import clean

sample = [{"class": "g - v1 2025-01-15 2-18pm", "confidence": 0.92, "x": 215.5, "y": 152.5, "width": 233, "height": 231}]
print(clean(sample))
