class Point:
    pass

p1 = Point()

p1.x = 5

print(p1)       # prints <__main__.Point object at 0x0000027BD0A98880>
print(p1.x)     # print 5




class Point2:
    def move(self, x, y):
        # takes 'self' argument first
        self.x = x
        self.y = y

    def reset(self):
        self.x = 0
        self.y = 0

p2 = Point2()

p2.move(1, 2)   # shorthand for Point.move(p2, 1, 2)
print(p2.x)
print(p2.y)

p2.reset()      # shorthand for Point.reset(p2)
print(p2.x)
print(p2.y)

# print directory of p2
print("========== dir(p2) ==========")
print(dir(p2))  # see a lot of dunder methods, along with what we defined