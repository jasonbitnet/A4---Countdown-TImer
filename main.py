import time  # Import the time module


def countdown(t, message):
    # Countdown function
    while t >= 0:  # Whule Loop continues
        # Calculate hours, minutes, and seconds
        hours, remainder = divmod(t, 3600)  #divide t by 3600
        mins, secs = divmod(remainder, 60)

        # Format timer to time in hours mins and seconds
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)

        # Print the timer inside a box
        print(f"+---------------------+")
        print(f"| {timer} |")
        print(f"+---------------------+", end="\r", flush=True)


        time.sleep(1)
        t -= 1

    # print message at end of countdown
    print(f"\n{message}")


def main():
    try:
        # enter time in seconds and a message
        t = int(input("Enter time in seconds: "))  # Convert input to integer
        message = input("Enter a message to display when the timer finishes: ")

        # Check if the entered time is valid (non-negative)
        if t >= 0:
            countdown(t, message)  # Call countdown function
        else:
            print("Please enter a number.")  # Display an error message if time is negative

    except ValueError:
        # print an error message if input not an integer
        print("Invalid input. Please enter a valid integer.")


# Start program
if __name__ == "__main__":
    main()  # Call the main function
