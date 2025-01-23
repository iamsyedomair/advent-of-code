inp = open('inp.txt').read().strip().split('\n')
inp = [list(map(int, i.split(' '))) for i in inp]

total = 0

for report in inp:
    # Check the differences and sequence rules
    differences = [abs(report[j] - report[j + 1]) for j in range(len(report) - 1)]
    increasing = all(report[j] <= report[j + 1] for j in range(len(report) - 1))
    decreasing = all(report[j] >= report[j + 1] for j in range(len(report) - 1))
    valid_differences = all(1 <= d <= 3 for d in differences)
    
    # If inherently safe, count it
    if (increasing or decreasing) and valid_differences:
        total += 1
        continue

    # Otherwise, apply the Problem Dampener
    for j in range(len(report)):
        # Remove one level and check again
        modified_report = report[:j] + report[j + 1:]
        differences = [abs(modified_report[k] - modified_report[k + 1]) for k in range(len(modified_report) - 1)]
        increasing = all(modified_report[k] <= modified_report[k + 1] for k in range(len(modified_report) - 1))
        decreasing = all(modified_report[k] >= modified_report[k + 1] for k in range(len(modified_report) - 1))
        valid_differences = all(1 <= d <= 3 for d in differences)
        
        if (increasing or decreasing) and valid_differences:
            total += 1
            break  # Stop checking further removals for this report

print("Total Safe Reports:", total)

