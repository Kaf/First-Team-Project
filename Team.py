class Team:

    def __init__(self):
        """ Asks for the user input for a noun and stores the noun in
        the instance variable self.word.  Remember a noun is a person,
        place, or thing. """
        # TODO by person 3
        self.word = raw_input('Enter a Noun: ')

        

    def reverse_input(self):
        """ Changes self.word to its reverse.  For example if
        self.word is 'apples', then it becomes 'selppa'."""
        # TODO by person 1
        reverse =self.word[::-1]
        print reverse

    
    def print_in_sentence(self):
        """ Insert self.word in the sentence 'Today I dreamt of
        <self.word> while walking on the beach.' replacing <self.word>
        for the noun that was chosen during class construction. """
	  # TODO by person 2
	print 'Today I dreamt of ',self.word,' while walking on the beach'

t = Team()
t.reverse_input()
t.print_in_sentence()
