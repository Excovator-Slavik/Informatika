# TODO решите задачу
import json
def task() -> float:
    # Исходные данные в формате  JSON
    json_data = """
    [
  {
    "score": 0.0009456152645028281,
    "weight": 1
  },
  {
    "score": 0.00020640167757499364,
    "weight": 1
  },
  {
    "score": 0,
    "weight": 1
  },
  {
    "score": 1.6557065217391307,
    "weight": 1
  },
  {
    "score": 0,
    "weight": 1
  },
  {
    "score": 0.6066065217391303,
    "weight": 1
  },
  {
    "score": 0.03126181644071977,
    "weight": 1
  },
  {
    "score": 0.001253973281817707,
    "weight": 1
  }
]
    """
    #декадируем json в python и считаем произведение
    items = json.loads(json_data)
    total = 0.0
    for d in items:
        product = d["score"] * d["weight"]
        total += product
    return round(total, 3)

print(task())
