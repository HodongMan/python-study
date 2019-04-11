
def reverse(word):

    return word[::-1]


if __name__ == "__main__":

    fruits = ['apple', 'banana', 'cherry', 'strawberry', 'raspberry']
    print( sorted(fruits, key=len) )

    print( sorted(fruits, key=reverse) )