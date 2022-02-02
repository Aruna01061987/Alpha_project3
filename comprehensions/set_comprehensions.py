"""to create a set of tuples of item and its index using set comprehension """

# list_ = ["java", "python", 10, True]

files = ("Amazon", "flipkart", "walmart", "gmail", "yahoo")

res = {(item, index) for item, index in enumerate(files)}

print(res)
print(type(res))


