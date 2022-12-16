saved_messages = [""]


def print_without_duplicates(message):
    if saved_messages[-1] != message:
        saved_messages.append(message)
        print(message)
