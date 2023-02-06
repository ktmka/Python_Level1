from os import system
class Menu:
    def __init__(self, elements=[]):
        self.elements = elements

    def print(self):
        for (mark, text, _) in self.elements:
            print('{} - {}'.format(mark, text))
        
    def run(self, prompt='выберите команду: '):
        def clrscr(): return system('cls')
        while(True):
            clrscr()
            self.print()
            user_choice = input(prompt)
            for (mark, _, runmethod) in self.elements:
                if user_choice == mark:
                    if runmethod == -1:
                        return True
                    clrscr()
                    runmethod()
                    break
                
def __len__(self):  #размер меню
    return len(self.elements)
