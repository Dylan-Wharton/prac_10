import wikipedia

# print(wikipedia.search("Ford", results=3))
# print(wikipedia.summary("GitHub"))
# ny = wikipedia.page("New York")
# print(ny.title)
# print(ny.url)
# print(ny.content)
# print(ny.images[1])
# print(ny.links[1])


user_search = input("what do you want to search for?")
while user_search != "":
    print(wikipedia.search(user_search))
    current_page = wikipedia.page(user_search)
    print(current_page.title, "\n" ,wikipedia.summary(current_page), "\n" ,current_page.url)
    user_search = input("what do you want to search for?")
print("bye")
