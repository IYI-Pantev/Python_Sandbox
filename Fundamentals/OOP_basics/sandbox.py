# class Person:
#     def __init__(self, name, age, kg):
#         self.name = name
#         self.age = age
#         self.kg = kg
#
# person = Person("Test", 12, 30)
# p2 = Person("Nick", 27, 95)
#
# a = 5


class SlidoComment:
    def __init__(self, author_name,  likes=0, dislikes=0, content="never give up", date="now", author_picture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDFFnFeI5Gg6ngxXKgqnDKwvZUK3HFB0eLOg&usqp=CAU"):
        self.author_name = author_name
        self.likes = likes
        self.dislikes =dislikes
        self.content = content
        self.date = date
        self.author_picture = author_picture

    def present_comment(self):
            return f"{self.author_name}\nLikes:{self.likes}\nDislikes:{self.dislikes}\n{self.author_picture}"


comment = SlidoComment("No name")
comment.likes += 1
print(comment.present_comment())