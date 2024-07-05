import sys

# Check if an input string is provided as a command line argument
if len(sys.argv) < 2:
    print("Usage: python -c 'import sys; input_string=sys.argv[1]; output_string=input_string[::-1]; print(\"Inverse sequence of characters:\", output_string)' <input_string>")
    sys.exit(1)

# Get the input string from command line argument
input_string = sys.argv[1]

# Reverse the input string
output_string = input_string[::-1]

# Print the reversed string
print("Inverse sequence of characters:", output_string)
