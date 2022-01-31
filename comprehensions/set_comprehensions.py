"""to create a set of tuples of item and its index using set comprehension """

# list_ = ["java", "python", 10, True]

files = ("Amazon", "flipkart", "walmart", "gmail", "yahoo")

res = {(file,len(file)) for file in files}

print(res)
