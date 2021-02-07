from datetime import datetime
print(datetime.now())

# Function to print date and time
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = 'Will'
print_time('Printed first name')

for i in range(10):
    print(i)

print_time('Loop completed')