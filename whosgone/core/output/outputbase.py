from abc import ABC, abstractmethod

class OutputBase(ABC):
    def __init__(self, followers, following):
        self.follower_len = len(followers)
        self.following_len = len(following)

        self.non_followers = following - followers
        self.non_following = followers - following

    @abstractmethod
    def create_output(self):
        pass
