import sys
import json


def read_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def insert_test(index: int, value, data):
    if isinstance(data, dict):
        for key, value_d in data.items():
            if key == "id" and value_d == index:
                data["value"] = value
                return
            elif key == "values":
                insert_test(index, value, value_d)
    elif isinstance(data, list):
        for item in data:
            insert_test(index, value, item)


def create_report(values_data: dict, report_data: dict):
    for item in values_data["values"]:
        insert_test(item["id"], item["value"], report_data["tests"])


def main():
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]
    values_data = read_json(values_file)
    report_data = read_json(tests_file)
    create_report(values_data, report_data)
    with open(report_file, "w") as f:
        json.dump(report_data, f)


if __name__ == "__main__":
    main()
