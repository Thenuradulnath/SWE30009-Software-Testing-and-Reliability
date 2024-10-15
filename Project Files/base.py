import os

# Specify the range for file creation
start_num = 4
end_num = 14

# Create and rename the files
for i in range(start_num, end_num + 1):
    filename = f'm{i}.py'  # Generate the filename
    with open(filename, 'w') as f:  # Create the file
        f.write(f'# This is {filename}\n')  # Optionally write a comment in the file
    print(f'Created: {filename}')  # Print confirmation
