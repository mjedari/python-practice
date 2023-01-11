from collections import Counter, namedtuple

# Counter from Collection
my_str = "this is a text that you should learn about the counter functionality through it"
counter_is_dictionary = Counter(my_str)

print(counter_is_dictionary)
print(counter_is_dictionary.most_common()[0])  # give you the most common elements in the list

# namedTuple is used whenever you want to have a tuple but like struct in golang
"""
type Point struct {
    Start   ini
    End     int
}
"""
Point = namedtuple("Point", "Start, End")

start_point = Point(1,2)
print(start_point.Start)
