class person:
    def __init__(self):
        print(" this is instructor")
    def __del__(self):
        print("this is destructor")

if __name__ == "__main__":
    p = person()
    del p