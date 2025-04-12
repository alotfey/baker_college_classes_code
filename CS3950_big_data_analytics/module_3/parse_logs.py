import re
import pandas as pd

log_file = "apache_logs.txt"

pattern_log = re.compile(
    r"(?P<ip>\S+) "  # IP address
    r"(?P<identity>\S+) "  # Remote identity
    r"(?P<user>\S+) "  # Authenticated user
    r"\[(?P<time>[^\]]+)\] "  # Timestamp
    r'"(?P<request>[^"]+)" '  # Request method and resource
    r"(?P<status>\d{3}) "  # HTTP status code
    r"(?P<size>\S+)"  # Size of response
)

log = []
with open(log_file, "r") as f:
    for line in f:
        match = re.match(pattern_log, line)
        if match:
            log.append(match.groupdict())

# Convert to DataFrame
df = pd.DataFrame(log)
# Convert time to datetime
df["time"] = pd.to_datetime(df["time"], format="%d/%b/%Y:%H:%M:%S %z")
# Convert size to int
df["size"] = df["size"].replace("-", 0).astype(int)
# Convert status to int
df["status"] = df["status"].astype(int)
print(df.head())
print(f"Before removeing duplicates: {len(df)}")
df.drop_duplicates(inplace=True)
print(f"After removeing duplicates: {len(df)}")

# Convert status to int
df["status"] = df["status"].astype(int)

# Filter essential status codes 304
df = df[df["status"] == 304]

# print the first 5 records
print(df.head())
