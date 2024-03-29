from bootiful_sanic.model import DATABASE


class User(DATABASE.Model):
    __tablename__ = "users"

    id = DATABASE.Column(DATABASE.BigInteger(), primary_key=True)
    name = DATABASE.Column(DATABASE.Unicode())

    def __str__(self):
        return "{}<{}>".format(self.name, self.id)

    def __repr__(self):
        return self.__str__()
