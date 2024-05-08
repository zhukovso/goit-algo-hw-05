import sys
from pathlib import Path
from collections import defaultdict


# Function to parse log lines.
def parse_log_line(line: str) -> dict:
    try:
        data, time, level, message = line.strip().split(' ', 3)
        if not data or not time or not level:
            raise ValueError("some values are empty")
        return {"data": data, "time": time, "level": level, "message": message}
    except ValueError as e:
        print(f'{e} with line: {line}')


# Function to download logs from a file.
def load_logs(file_path: str) -> list:
    log_list = []
    try:
        with open(Path(__file__).parent / file_path, 'r', encoding='utf-8') as file:
            for line in file:
                log_list.append(parse_log_line(line))
    except FileNotFoundError as e:
        print(f'{e} with file path: {file_path}')
    return log_list.copy()


# Function to create a list with all logs filtered by level.
def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda elem: elem['level'] == level.upper(), logs))


# Function to count records by logging level.
def count_logs_by_level(logs: list) -> dict:
    count_dict = defaultdict(int)
    for elem in logs:
        count_dict[elem['level']] += 1
    return dict(count_dict.items())
    # return {i: len(filter_logs_by_level(logs, i)) for i in ['INFO', 'WARNING', 'ERROR', 'DEBUG']}


# Function that formats and displays the results.
def display_log_counts(counts: dict):
    print('Рівень логування | Кількість\n-----------------|----------')
    for level in counts.keys():
        print(f'{level:<16} | {counts.get(level):<10}')


# Function that formats and displays detailed results by level.
def display_logs_by_level(logs: list, level: str):
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for element in filter_logs_by_level(logs, level):
        # print(' '.join(element.values()))
        print(f"{element['data']} {element['time']} - {element['message']}")


def main(logfile: str, level=""):
    if logfile:
        logs = load_logs(logfile)
        if logs:
            display_log_counts(count_logs_by_level(logs))
            if level:
                display_logs_by_level(logs, level)


if __name__ == '__main__':
    main(
        sys.argv[1] if len(sys.argv) > 1 else "logfile.log",
        sys.argv[2] if len(sys.argv) > 2 else ""
    )
