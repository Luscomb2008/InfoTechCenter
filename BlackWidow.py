# Import necessary libraries
import sys  # Provides access to system-specific parameters and functions
import time  # Provides time-related functions

# Print the welcome message and developer info
print("Welcome Branch - Developer: Lucas Luscomb")

# Print a greeting message for InfoTechCenter
print("\n\tWelcome To InfoTechCenter!\n")

# Initialize variables
x = 0  # Counter to track the number of iterations
ellipsis = 0  # Variable to control the number of dots in the loading message

# Start a loop that runs 20 times
while x != 20:
    x += 1  # Increment counter
    # Create a message with a varying number of dots
    message = ("InfoTech Center System Booting" + "." * ellipsis)
    ellipsis += 1  # Increase the number of dots
    # Overwrite the previous output on the same line with the new message
    sys.stdout.write("\r" + message)
    # Pause for half a second before updating the message
    time.sleep(.5)
    
    # Reset the number of dots after reaching 4
    if ellipsis == 4:
        ellipsis = 0
    
    # Once the loop reaches 20 iterations, print a final success message
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted")
