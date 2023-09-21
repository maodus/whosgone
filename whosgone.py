from utils.extractor import IGExtractor
import os

if __name__ == "__main__":
    zip_path = input("Please enter the file path for your instagram data file: ")

    while not os.path.exists(zip_path) or not zip_path.endswith(".zip"):
        zip_path = input("Input was invalid, please try again: ")

    igextract = IGExtractor(zip_path)

    followers = igextract.get_followers()
    following = igextract.get_following()

    non_followers = following - followers # People that don't follow us back
    non_following = followers - following # People that we don't follow back

    print(f"Users that don't follow you back ({len(non_followers)}/{len(following)}): ")

    for user in (following - followers):
        print(user)

    print(f"\nUsers that you dont follow back ({len(non_following)}/{len(followers)}): ")

    for user in (followers - following):
        print(user)

