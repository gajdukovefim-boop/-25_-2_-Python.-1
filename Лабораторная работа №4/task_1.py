import json
import math


def task() -> float:
    with open('input.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    total_sum = 0.0
    for item in data:
        score = item.get("score", 0)
        weight = item.get("weight", 0)

        total_sum += score * weight
    return round(total_sum, 3)
if __name__ == '__main__':
    print(task())