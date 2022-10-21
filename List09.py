def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    b=0
    while b<len(list1):
        if list1[0]!=list[b]:
            return False
        b+=1
    return True
print(main(["x","y","x","y","y"]))