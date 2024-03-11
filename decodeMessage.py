def decode():
  """
  Decodes the hidden message from the file "D:/coding_qual_input.txt".

  Returns:
      The decoded message as a string.
  """

  message_file = "D:/coding_qual_input.txt"

  message_lines = []
  with open(message_file, 'r') as file:
    for line in file:
      message_lines.append(line.strip().split())  # Split into number-word pairs

  pyramid_size = len(message_lines)
  message_words = []

  # Select words from the right side of the pyramid in ascending order
  for i in range(pyramid_size):
    message_words.append(message_lines[pyramid_size - i - 1][1])  # Get word from first element

  return " ".join(message_words)

# Call the function to decode the message
decoded_message = decode()
print(decoded_message)  # Output: The decoded message




# def decode():
#   """
#   Decodes the hidden message from the file "D:/coding_qual_input.txt".

#   Returns:
#       The decoded message as a string.
#   """

#   message_file = "D:/coding_qual_input.txt"

#   message_lines = []
#   with open(message_file, 'r') as file:
#     for line in file:
#       message_lines.append(line.strip().split())  # Split into number-word pairs

#   pyramid_size = len(message_lines)
#   pyramid_numbers = []

#   for i in range(pyramid_size):
#     start_index = pyramid_size - i - 1
#     end_index = start_index + i + 1
#     pyramid_numbers.append(int(message_lines[start_index][0]))  # Get number from first element

#   # Select numbers on the right side of the pyramid in ascending order
#   selected_numbers = sorted(pyramid_numbers)

#   return " ".join(str(number) for number in selected_numbers)  # Join numbers as a string

# # Call the function to select and print the numbers
# selected_numbers_string = decode()
# print(selected_numbers_string)  # Output: 1 3 6


