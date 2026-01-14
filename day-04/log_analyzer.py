import json
def read_file(log_file):
    try:
        print("Reading log file")
        with open(log_file, "r") as file:
            content=file.read()
        return content

    except Exception as e:
        print("file not found")
        return ""

def calculate_count(log_content):
    info_count = 0
    error_count = 0
    warn_count = 0

    log_lines = log_content.splitlines()
    for single_line in log_lines:
        if "INFO" in single_line:
            info_count +=1
        elif "ERROR" in single_line:
            error_count +=1
        elif "WARNING" in single_line:
            warn_count +=1

    return info_count, error_count, warn_count

def write_file(new_file,info,error,warn):
    try:
        summary = {"INFO": info, "ERROR": error, "WARNING": warn}
        with open(new_file,"w") as f:
            json.dump(summary, f)
    except Exception as e:
        print("Unable to write to file:", e)
        

log_file_data = read_file("app.log")
info, error, warn = calculate_count(log_file_data)
print(f"INFO: {info}, ERROR: {error}, WARNING: {warn}")
write_file("log_summary.json",info,error,warn)
print("Log Summary added to log_summary.json")