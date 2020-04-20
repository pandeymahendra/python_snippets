# This is an example of stacking
# take an example of browser where it redirects you to previous URL when you press "back" button
# same way stacking is implemented LIFO, here in this example we are taking away one element from last in the list


browsing_sesion = []

browsing_sesion.append(1)
browsing_sesion.append(2)
browsing_sesion.append(3)

print(browsing_sesion)
last = browsing_sesion.pop()
print("Popped (removed) element from the list: ", last)
print(browsing_sesion)
print(browsing_sesion[-1])

# next we need to disable back button if the list is empty
browsing_sesion.pop()  # 2nd Value
browsing_sesion.pop()  # 3rd Value gone
if not browsing_sesion:
    print("Disable")
