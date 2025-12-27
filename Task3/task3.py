import sys
import json

def fill_values(node, values_map):
    if "id" in node and node["id"] in values_map:
        node["value"] = values_map[node["id"]]

    if "values" in node:
        for child in node["values"]:
            fill_values(child, values_map)

def main():
    if len(sys.argv) < 4:
        print("Нужно передать три файла: tests.json values.json report.json")
        return

    tests_file = sys.argv[1]
    values_file = sys.argv[2]
    report_file = sys.argv[3]

    # читаем values.json
    with open(values_file) as f:
        values_data = json.load(f)
    values_map = {item["id"]: item["value"] for item in values_data["values"]}

    # читаем tests.json
    with open(tests_file) as f:
        tests_data = json.load(f)

    # заполняем значения
    for test in tests_data["tests"]:
        fill_values(test, values_map)

    # записываем результат
    with open(report_file, "w") as f:
        json.dump(tests_data, f, indent=2)

if __name__ == "__main__":
    main()
