from operations import add, sub

def math_result(a, b):
    return {"addition":add.add(a, b), "subtraction":sub.sub(a, b)}

if __name__ == "__main__":
    print(math_result(1, 2))