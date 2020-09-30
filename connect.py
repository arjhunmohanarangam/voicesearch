from googlesearch import search
cars = search("what is a Car", num_results=4)
for i in cars:
    print(i)
