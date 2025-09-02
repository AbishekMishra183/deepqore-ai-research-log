# Function to check palindrome for numbers
def is_palindrome_number(num):
    original = str(num)      # convert number to string
    reversed_num = original[::-1]  # reverse the string
    return original == reversed_num

# Main program
def main():
    try:
        num = int(input("Enter a number: "))
        if is_palindrome_number(num):
            print(f"{num} is a palindrome!")
        else:
            print(f"{num} is not a palindrome.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
