# This is an example of stacking
# take an example of browser where it redirects you to previous URL when you press "back" button
# same way stacking is implemented LIFO, here in this example we are taking away one element from last in the list


browsing_sesion = []

browsing_sesion.append(1)
browsing_sesion.append(2)
browsing_sesion.append(3)

print(browsing_sesion)
last = browsing_sesion.pop()
print(last)
print(browsing_sesion)
print(browsing_sesion[-1])
