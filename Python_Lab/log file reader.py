
# Log File Reader Program

file = open("system.log", "r")

info_count = 0
warning_count = 0
error_count = 0

print("===== LOG FILE CONTENTS =====")

for line in file:

    print(line.strip())

    if "INFO" in line:
        info_count += 1

    elif "WARNING" in line:
        warning_count += 1

    elif "ERROR" in line:
        error_count += 1

file.close()

print("\n===== LOG SUMMARY =====")
print("INFO messages:", info_count)
print("WARNING messages:", warning_count)
print("ERROR messages:", error_count)
