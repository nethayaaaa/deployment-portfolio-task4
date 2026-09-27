import sys
import os
from datetime import datetime

if len(sys.argv) < 2:
    print("Usage: provide marks as command-line arguments.")
    print("Example: 75 82 69 91 88")
    sys.exit(1)

try:
    marks = [float(mark) for mark in sys.argv[1:]]
except ValueError:
    print("Error: all marks must be numbers.")
    sys.exit(1)

average = sum(marks) / len(marks)
minimum = min(marks)
maximum = max(marks)

result = f"""
Student Marks Statistics
------------------------
Number of marks: {len(marks)}
Average: {average:.2f}
Minimum: {minimum:.2f}
Maximum: {maximum:.2f}
Processed at: {datetime.now()}
"""

print(result)

os.makedirs("/data", exist_ok=True)

with open("/data/results.txt", "w") as file:
    file.write(result)

print("Results successfully saved to /data/results.txt")