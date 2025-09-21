# find the  formula to get the output of minutes saved /
#driving 80mph instead of 60mph
result = 100/60 - (100/80)*60

print("Equation used: 100/60 - (100/80)*60")
print(f"Result: {result}")

# Variables used 
distance = 100  # miles
speed_lmt = 60  # mph
average_lmt = 80  # mph

# Calculate time for both speeds in hours
speed_hours = distance / speed_lmt
average_hours = distance / average_lmt

# Convert to hours into minutes
speed_lmt_minutes = speed_hours * 60
average_lmt_minutes = average_hours * 60

# Calculate time saved and using the fvaule
time_saved_minutes = speed_lmt_minutes - average_lmt_minutes

print(f"speed hours: {speed_hours:.2f} hours = {speed_lmt_minutes:.2f} minutes")
print(f"average hours: {average_hours:.2f} hours = {average_lmt_minutes:.2f} minutes")
print(f"Time saved: {time_saved_minutes:.2f} minutes")
