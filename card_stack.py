from card import Card

class CenterStack:
    def __init__(self,card_vals = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen"], wilds = ["King","Joker"]):
        self.cards = []
        self.card_vals = card_vals
        self.wilds = wilds

    # add a card to the stack
    def add_card(self,new_card):
        if len(self.cards) == 0:
            if new_card.get_val() == self.card_vals[0]:
                self.cards.append(new_card)
                return True
            else:
                return False
        else:
            if new_card.get_val() in self.card_vals:
                if len(self.cards) + 1 == self.card_vals.index(new_card.get_val()):
                    self.cards.append(new_card)
                    return True
                else:
                    return False
            elif new_card.get_val() in self.wilds:
                self.cards.append(new_card)
                return True
            else:
                return False
    

    # checks the top card on the stack
    def check_top(self):
        if len(self.cards) > 0:
            return self.cards[-1]
        else:
            return None
    
    # gets the top card and removes it from the stack
    def get_top(self):
        return_card = self.check_top(self)
        self.cards.pop(-1)
        return return_card

    # returns the whole stack
    def check_stack(self):
        return self.cards.copy()

    # emptys the stack, returning the stack
    def empty_stack(self):
        return_stack = self.cards.copy()
        self.cards = []
        return return_stack
    

class SideStack:
    def __init__(self,card_vals = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen"]):
        self.cards = []
        self.card_vals = card_vals

    # add a card to the stack
    def add_card(self,new_card):
        if len(self.cards) == 0:
            self.cards.append(new_card)
            return True
        else:
            if new_card.get_val() in self.card_vals:
                if self.card_vals.index(self.cards[-1].get_val()) + 1 == self.card_vals.index(new_card.get_val()):
                    self.cards.append(new_card)
                    return True
                elif self.card_vals.index(self.cards[-1].get_val()) + 1 == self.card_vals.index(new_card.get_val()):
                    self.cards.append(new_card)
                    return True
                elif self.card_vals.index(self.cards[-1].get_val()) == self.card_vals.index(new_card.get_val()):
                    self.cards.append(new_card)
                    return True
                else:
                    return False
            else:
                return False

    # checks the top card on the stack
    def check_top(self):
        if len(self.cards) > 0:
            return self.cards[-1]
        else:
            return None
    
    # gets the top card and removes it from the stack
    def get_top(self):
        return_card = self.check_top(self)
        self.cards.pop(-1)
        return return_card

    # returns the whole stack
    def check_stack(self):
        return self.cards.copy()

    # emptys the stack, returning the stack
    def empty_stack(self):
        return_stack = self.cards.copy()
        self.cards = []
        return return_stack