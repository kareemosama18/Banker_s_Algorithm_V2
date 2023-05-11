from tkinter import *

# Banker's Algorithm function
def banker_algorithm(total_resources, available_resources, current_allocation, maximum_need, request):
    num_processes = len(current_allocation)
    num_resources = len(total_resources)

    # Initialize work, finish, and need matrices
    work = available_resources.copy()
    finish = [False] * num_processes
    need = [[maximum_need[i][j] - current_allocation[i][j] for j in range(num_resources)] for i in range(num_processes)]

    # Check if the request is within the need and available resources
    process_id = request[0]
    requested_resources = request[1:]
    if all(requested_resources[j] <= need[process_id][j] and requested_resources[j] <= work[j] for j in range(num_resources)):
        # Temporarily allocate the resources
        for j in range(num_resources):
            work[j] -= requested_resources[j]
            current_allocation[process_id][j] += requested_resources[j]
            need[process_id][j] -= requested_resources[j]

        # Find a safe sequence
        safe_sequence = []
        while True:
            # Find an index i such that finish[i] is False and need[i] <= work
            found = False
            for i in range(num_processes):
                if not finish[i] and all(need[i][j] <= work[j] for j in range(num_resources)):
                    found = True
                    break

            if not found:
                break

            # Add process i to the safe sequence, update work, and mark process i as finished
            safe_sequence.append(i)
            for j in range(num_resources):
                work[j] += current_allocation[i][j]
            finish[i] = True

        # Rollback the temporary allocation
        for j in range(num_resources):
            work[j] += requested_resources[j]
            current_allocation[process_id][j] -= requested_resources[j]
            need[process_id][j] += requested_resources[j]

        # Check if a safe sequence was found
        if len(safe_sequence) == num_processes:
            return True
        else:
            return False
    else:
        return False

# Function to handle the 'Check' button click event
def check_button_click():
    # Retrieve input values
    total_resources_values = [int(entry.get()) for entry in total_resources_entries]
    available_resources_values = [int(entry.get()) for entry in available_resources_entries]

    num_processes = len(current_allocation_entries)
    num_resources = len(total_resources_values)

    current_allocation_values = []
    maximum_need_values = []
    for i in range(num_processes):
        current_allocation_values.append([int(entry.get()) for entry in current_allocation_entries[i]])
        maximum_need_values.append([int(entry.get()) for entry in maximum_need_entries[i]])

    # Retrieve the request
    process_id = int(request_process_entry.get())
    request_values = [int(entry.get()) for entry in request_entries]

    # Call Banker's Algorithm
    request = [process_id] + request_values
    safe = banker_algorithm(total_resources_values, available_resources_values, current_allocation_values, maximum_need_values, request)

    # Display the result
    if safe:
        result_label.config(text="Request can be granted! System is still in a safe state.")
    else:
        result_label.config(text="Request cannot be granted! System may enter an unsafe state.")

# Create the main window
window = Tk()
window.title("Banker's Algorithm")

# Total Resources
# Total Resources
total_resources_label = Label(window, text="Total Resources:")
total_resources_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

total_resources_entries = []
for i in range(3):  # Assuming 3 resources
    entry = Entry(window, width=5)
    entry.grid(row=0, column=i+1, padx=5, pady=5)
    total_resources_entries.append(entry)

# Available Resources
available_resources_label = Label(window, text="Available Resources:")
available_resources_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

available_resources_entries = []
for i in range(3):  # Assuming 3 resources
    entry = Entry(window, width=5)
    entry.grid(row=1, column=i+1, padx=5, pady=5)
    available_resources_entries.append(entry)

# Current Allocation
current_allocation_label = Label(window, text="Current Allocation:")
current_allocation_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

current_allocation_entries = []
for i in range(3):  # Assuming 3 processes
    current_allocation_row = []
    for j in range(3):  # Assuming 3 resources
        entry = Entry(window, width=5)
        entry.grid(row=i+2, column=j+1, padx=5, pady=5)
        current_allocation_row.append(entry)
    current_allocation_entries.append(current_allocation_row)

# Maximum Need
maximum_need_label = Label(window, text="Maximum Need:")
maximum_need_label.grid(row=5, column=0, padx=5, pady=5, sticky=W)

maximum_need_entries = []
for i in range(3):  # Assuming 3 processes
    maximum_need_row = []
    for j in range(3):  # Assuming 3 resources
        entry = Entry(window, width=5)
        entry.grid(row=i+5, column=j+1, padx=5, pady=5)
        maximum_need_row.append(entry)
    maximum_need_entries.append(maximum_need_row)

# Request Process
request_process_label = Label(window, text="Request Process:")
request_process_label.grid(row=8, column=0, padx=5, pady=5, sticky=W)

request_process_entry = Entry(window, width=5)
request_process_entry.grid(row=8, column=1, padx=5, pady=5)

# Request Resources
request_resources_label = Label(window, text="Request Resources:")
request_resources_label.grid(row=8, column=2, padx=5, pady=5, sticky=W)

request_entries = []
for i in range(3):  # Assuming 3 resources
    entry = Entry(window, width=5)
    entry.grid(row=8, column=i+3, padx=5, pady=5)
    request_entries.append(entry)

# Check Button
check_button = Button(window, text="Check", command=check_button_click)
check_button.grid(row=9, column=0, columnspan=4, padx=5, pady=10)

# Result Label
result_label = Label(window, text="")
result_label.grid(row=10, column=0, columnspan=4, padx=5, pady=5)

# Run the main window loop
window.mainloop()

