import numpy as np
from src.gender_model import GenderModel
from csv import reader, writer

gm = GenderModel()

with open("input.csv") as csvfile:
    csv_reader = reader(csvfile)
    next(csv_reader)
    rows = list(csv_reader)

count_accurate = 0
count_total = 0

with open("results.csv", "w", newline="") as f:
    csv_writer = writer(f)
    csv_writer.writerow(["", "img_path", "gender", "prediction", "confidence"])

    for row in rows:
        count_total += 1
        prediction = gm.predict(row[1])
        index_prediction = np.argmax(prediction)
        if (index_prediction == 0 and row[2] == "female") or (index_prediction == 1 and row[2] == "male"):
            count_accurate += 1
        csv_writer.writerow(
            [row[0], row[1], row[2], prediction, max(prediction)]
        )


def calculate_accuracy():
    accuracy = count_accurate / count_total
    print(f"The model was {np.round(accuracy, 4) * 100}% accurate.")


calculate_accuracy()
