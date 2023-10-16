from collections import defaultdict

# manage the collection of game state info
class StateSet:
    def __init__(self):
        self.cache = defaultdict(dict)

    #  check whether a given state(item:(boxes, new_square_location)) is contained within the StateSet
    def __contains__(self, item):
        boxes, player = item
        if boxes in self.cache:
            state_info = self.cache[boxes]
            for norm_pos in state_info:
                if player in state_info[norm_pos]:
                    return True
        return False

    # update the state info cache with new info
    def update(self, boxes, norm_pos, accessible):
        self.cache[boxes][norm_pos] = accessible

    # retrieve normalized player coordinates associated with a state
    def find(self, item):
        boxes, player = item
        if boxes in self.cache:
            state_info = self.cache[boxes]
            for norm_pos in state_info:
                if player in state_info[norm_pos]:
                    return norm_pos
        return None
