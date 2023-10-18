# In Python, the match statement is introduced in Python 3.10 as a way to perform pattern matching, 
# allowing you to match patterns within data structures. Here's an example of how to use the match statement to match patterns within a list:

def process_data(data):
    match data:
        case []:  # Match an empty list
            print("The list is empty.")
        case [1, 2, 3]:  # Match a specific list pattern
            print("The list is [1, 2, 3].")
        case [1, _rest...]:  # Match a list starting with 1
            print("The list starts with 1.")
        case [_, *rest, 5]:  # Match a list ending with 5
            print("The list ends with 5.")
        case [_, 2, 3]:  # Match any list with the second and third elements as 2 and 3
            print("The list has [_, 2, 3] as the second and third elements.")
        case _ as default:  # Catch-all case
            print("Default case: The list does not match any specific pattern.")

data1 = []
data2 = [1, 2, 3]
data3 = [1, 4, 5]
data4 = [6, 7, 8, 5]

process_data(data1)
process_data(data2)
process_data(data3)
process_data(data4)
