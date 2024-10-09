import os


# Count number of files in the ./data/raw directory
def count_files():
    raw_data_dir = "./data/raw"
    files = os.listdir(raw_data_dir)
    count = len(files)
    print(f"There are {count} files in the {raw_data_dir} directory.")


# Count how many files have a .abc extension
def count_abc_files():
    raw_data_dir = "./data/raw"
    files = os.listdir(raw_data_dir)
    count = 0
    for file in files:
        if file.endswith(".abc"):
            count += 1
    print(f"There are {count} .abc files in the {raw_data_dir} directory.")


def count_headers():
    raw_data_dir = "./data/raw"
    files = os.listdir(raw_data_dir)
    headers = {}
    for file in files:
        with open(
            os.path.join(raw_data_dir, file), "r", encoding="utf-8", errors="ignore"
        ) as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("A:"):
                    headers["A"] = headers.get("A", 0) + 1
                elif line.startswith("B:"):
                    headers["B"] = headers.get("B", 0) + 1
                elif line.startswith("C:"):
                    headers["C"] = headers.get("C", 0) + 1
                elif line.startswith("D:"):
                    headers["D"] = headers.get("D", 0) + 1
                elif line.startswith("F:"):
                    headers["F"] = headers.get("F", 0) + 1
                elif line.startswith("G:"):
                    headers["G"] = headers.get("G", 0) + 1
                elif line.startswith("H:"):
                    headers["H"] = headers.get("H", 0) + 1
                elif line.startswith("I:"):
                    headers["I"] = headers.get("I", 0) + 1
                elif line.startswith("K:"):
                    headers["K"] = headers.get("K", 0) + 1
                elif line.startswith("L:"):
                    headers["L"] = headers.get("L", 0) + 1
                elif line.startswith("M:"):
                    headers["M"] = headers.get("M", 0) + 1
                elif line.startswith("N:"):
                    headers["N"] = headers.get("N", 0) + 1
                elif line.startswith("O:"):
                    headers["O"] = headers.get("O", 0) + 1
                elif line.startswith("P:"):
                    headers["P"] = headers.get("P", 0) + 1
                elif line.startswith("Q:"):
                    headers["Q"] = headers.get("Q", 0) + 1
                elif line.startswith("R:"):
                    headers["R"] = headers.get("R", 0) + 1
                elif line.startswith("S:"):
                    headers["S"] = headers.get("S", 0) + 1
                elif line.startswith("T:"):
                    headers["T"] = headers.get("T", 0) + 1
                elif line.startswith("U:"):
                    headers["U"] = headers.get("U", 0) + 1
                elif line.startswith("W:"):
                    headers["W"] = headers.get("W", 0) + 1
                elif line.startswith("w:"):
                    headers["w"] = headers.get("w", 0) + 1
                elif line.startswith("X:"):
                    headers["X"] = headers.get("X", 0) + 1
                elif line.startswith("Z:"):
                    headers["Z"] = headers.get("Z", 0) + 1
    print(headers)


# Combine contents and divide by X: header
def get_tune_parts():
    raw_data_dir = "./data/raw"
    files = os.listdir(raw_data_dir)
    tunes = []
    for file in files:
        with open(
            os.path.join(raw_data_dir, file), "r", encoding="utf-8", errors="ignore"
        ) as f:
            lines = f.readlines()
            tune = []
            for line in lines:
                if line.startswith("X:"):
                    tunes.append(tune)
                    tune = []
                tune.append(line)
    return tunes


def get_line_stats(tunes):
    line_lengths = []
    for tune in tunes:
        line_lengths.append(len(tune))
    # Mean, median, mode, and range, etc
    mean = sum(line_lengths) / len(line_lengths)
    print(f"Mean: {mean}")
    # Median
    sorted_lengths = sorted(line_lengths)
    mid = len(sorted_lengths) // 2
    median = sorted_lengths[mid]
    print(f"Median: {median}")
    # Mode
    counts = {}
    for length in sorted_lengths:
        counts[length] = counts.get(length, 0) + 1
    mode = max(counts, key=counts.get)
    print(f"Mode: {mode}")
    # Range
    range = max(line_lengths) - min(line_lengths)
    print(f"Range: {range}")
    # Variance
    variance = sum([(length - mean) ** 2 for length in line_lengths]) / len(
        line_lengths
    )
    print(f"Variance: {variance}")
    # Standard deviation
    std_dev = variance**0.5
    print(f"Standard deviation: {std_dev}")
    # Min and max
    min_length = min(line_lengths)
    max_length = max(line_lengths)
    print(f"Min: {min_length}")
    print(f"Max: {max_length}")


def get_char_stats(tunes):
    char_lengths = []
    for tune in tunes:
        char_lengths.append(sum([len(line) for line in tune]))
    # Mean, median, mode, and range, etc
    mean = sum(char_lengths) / len(char_lengths)
    print(f"Mean: {mean}")
    # Median
    sorted_lengths = sorted(char_lengths)
    mid = len(sorted_lengths) // 2
    median = sorted_lengths[mid]
    print(f"Median: {median}")
    # Mode
    counts = {}
    for length in sorted_lengths:
        counts[length] = counts.get(length, 0) + 1
    mode = max(counts, key=counts.get)
    print(f"Mode: {mode}")
    # Range
    range = max(char_lengths) - min(char_lengths)
    print(f"Range: {range}")
    # Variance
    variance = sum([(length - mean) ** 2 for length in char_lengths]) / len(
        char_lengths
    )
    print(f"Variance: {variance}")
    # Standard deviation
    std_dev = variance**0.5
    print(f"Standard deviation: {std_dev}")
    # Min and max
    min_length = min(char_lengths)
    max_length = max(char_lengths)
    print(f"Min: {min_length}")
    print(f"Max: {max_length}")


if __name__ == "__main__":
    count_files()
    count_abc_files()
    count_headers()
    tunes = get_tune_parts()
    get_line_stats(tunes)
    get_char_stats(tunes)

    print(f"Found {len(tunes)} tunes.")
