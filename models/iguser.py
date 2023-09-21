# Represents an instagram user that is followed by or is following you
class IGUser:
    def __init__(self, name, interaction_date):
        self.name = name
        self.interaction_date = interaction_date

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if not isinstance(other, IGUser):
            return False
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name)