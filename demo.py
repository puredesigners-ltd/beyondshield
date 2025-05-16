# demo.py

from postprocess import clean

# Simulated Roboflow-style output (like from InferencePipeline)
sample_predictions = [
    {
        "class": "g - v1 2025-01-15 2-18pm",  # Should be mapped to "Gun"
        "confidence": 0.926,
        "x": 215.5,
        "y": 152.5,
        "width": 233,
        "height": 231
    },
    {
        "class": "climbing",  # Below threshold, should be filtered
        "confidence": 0.39,
        "x": 100,
        "y": 100,
        "width": 80,
        "height": 150
    }
]

# Run the cleanup function
cleaned_results = clean(sample_predictions)

# Print the final output
print("✅ Cleaned Predictions:\n")
for obj in cleaned_results:
    print(obj)
