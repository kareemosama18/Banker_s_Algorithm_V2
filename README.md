
# Banker's Algorithm GUI

This is a Python program that implements the Banker's algorithm using a graphical user interface (GUI) created with Tkinter. The Banker's algorithm is a resource allocation and deadlock avoidance algorithm used in operating systems.

## Prerequisites

To run this program, you need to have Python installed on your system. Additionally, you need to have the Tkinter library, which is usually included in the standard library of Python installations.

## Running the Program

To run the program, follow these steps:

1.  Clone the repository or download the source code files.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where the files are located.
4.  Run the following command:

Copy code

`python banker_s_Algorithm_V2.py` 

5.  The GUI window will open, allowing you to input the necessary parameters for the Banker's algorithm.
6.  Enter the total resources, available resources, current allocation, maximum need, and request in the respective input fields.
7.  Click the "Check" button to execute the Banker's algorithm.
8.  The program will display the result (whether the request can be granted or not) in the GUI window.

## Understanding the Code

The code consists of two main parts: the Banker's algorithm implementation and the GUI creation using Tkinter.

### Banker's Algorithm Implementation

The Banker's algorithm implementation is contained in the `banker_algorithm()` function. Here's a brief overview of its functionality:

1.  It takes five parameters: `total_resources`, `available_resources`, `current_allocation`, `maximum_need`, and `request`.
2.  It initializes the `work`, `finish`, and `need` matrices based on the input parameters.
3.  It checks if the requested resources are within the need and available resources for the process.
4.  If the request is valid, it temporarily allocates the resources, finds a safe sequence of processes, and checks if a safe sequence was found.
5.  Finally, it rolls back the temporary allocation and returns the result (whether the request can be granted or not).

### GUI Creation using Tkinter

The code uses Tkinter to create a GUI for user interaction. Here's a summary of the GUI elements and their functionality:

1.  The main window is created using `Tk()` and titled "Banker's Algorithm".
2.  Labels, entry fields, and buttons are created and positioned within the main window to allow the user to input the necessary parameters for the Banker's algorithm.
3.  The `check_button_click()` function serves as the event handler for the "Check" button click event. It retrieves the input values, calls the `banker_algorithm()` function, and displays the result in the GUI.
4.  The result of the Banker's algorithm is displayed in the `result_label`.

## Limitations

-   The code assumes a fixed number of resources (3) and processes (3) for simplicity. However, you can modify the code to handle a different number of resources and processes by adjusting the appropriate sections.
-   Error handling for invalid inputs (e.g., non-integer values, negative values) is not implemented in the code. You may need to add additional validation logic to handle such cases.

That's it! You now have an understanding of the Banker's algorithm implementation using a GUI created with Tkinter. Feel free to modify and extend the code to suit your specific requirements.

# Developer 
This code is created By : Kareem Osama Ahmed Sobhy (ID : 19105457)

