class ProgrammingLanguage:
    
    def __init__(self, name, typing, reflection, year):
        """ Use parameters passed in and constrcyt them """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """ return True if the typing is dynamic """
        return self.typing == "Dynamic"

    def __str__(self):
        """ return strings about a programming language """
        return "{}, {} Typing,Reflection = {}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                            self.year)
