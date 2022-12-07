from .properties import Properties


class Hopfield(Properties):
    """
    Hopfield is neural network.
    """

    name: str = 'hopfield'
    type: str = 'Hopfield'
    description: str = 'description'

    def __init__(self, reader=name, **kwargs):
        super().__init__(reader, **kwargs)

    def __repr__(self):
        return '<%s.%s: %r>' % (self.__class__.__name__, self.name, self.description)

    def __str__(self):
        return '%s.%s' % (self.__class__.__name__, self.name)

    def __dir__(self):
        """
        Returns all members and all public methods.
        """
        return ['__class__', '__doc__', '__module__'] + \
               [
                   m
                   for cls in self.__class__.mro()
                   for m in cls.__dict__
                   if m[0] != '_'
               ] + [m for m in self.__dict__ if m[0] != '_']
