class Song:
    def __init__(self, song_id, title, artist, duration):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.duration = duration

    def display(self):
        print(f"ID: {self.song_id} | Title: {self.title} | Artist: {self.artist} | Duration: {self.duration}")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_first(self, song):
        new_node = Node(song)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        print("Song added at the beginning.")

    def insert_last(self, song):
        new_node = Node(song)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

        self.size += 1
        print("Song added at the end.")

    def insert_at(self, position, song):
        if position < 1 or position > self.size + 1:
            print("Invalid position.")
            return

        if position == 1:
            self.insert_first(song)
            return

        new_node = Node(song)
        current = self.head

        for _ in range(1, position - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.size += 1

        print(f"Song inserted at position {position}.")

    def display_playlist(self):
        if self.head is None:
            print("Playlist is empty.")
            return

        current = self.head

        print("Playlist: ", end="")

        while current is not None:
            print(f"[{current.data.title}] -> ", end="")
            current = current.next

        print("NULL")
        print(f"Total songs: {self.size}")

    def search_song(self, song_id):
        current = self.head

        while current is not None:
            if current.data.song_id == song_id:
                print("Song Found:")
                current.data.display()
                return

            current = current.next

        print("Song ID not found.")

    def delete(self, song_id):
        if self.head is None:
            print("Playlist is empty.")
            return

        if self.head.data.song_id == song_id:
            self.head = self.head.next
            self.size -= 1
            print("Song removed successfully.")
            return

        current = self.head

        while current.next is not None and current.next.data.song_id != song_id:
            current = current.next

        if current.next is None:
            print("Song ID not found.")
        else:
            current.next = current.next.next
            self.size -= 1
            print("Song removed successfully.")

    def display_size(self):
        print(f"Total number of songs: {self.size}")


def main_part2():
    playlist = LinkedList()

    while True:
        print("\n--- MUSIC PLAYLIST MANAGER ---")
        print("1. Add Song at Beginning")
        print("2. Add Song at End")
        print("3. Insert Song at Position")
        print("4. Display Playlist")
        print("5. Search Song")
        print("6. Remove Song")
        print("7. Display Playlist Size")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 1 <= choice <= 3:
            s_id = input("Enter Song ID: ")
            title = input("Enter Title: ")
            artist = input("Enter Artist: ")
            duration = input("Enter Duration (e.g. 4:23): ")

            new_song = Song(s_id, title, artist, duration)

            if choice == 1:
                playlist.insert_first(new_song)

            elif choice == 2:
                playlist.insert_last(new_song)

            else:
                try:
                    pos = int(input("Enter Position to insert: "))
                    playlist.insert_at(pos, new_song)
                except ValueError:
                    print("Invalid position format.")

        elif choice == 4:
            playlist.display_playlist()

        elif choice == 5:
            s_id = input("Enter Song ID to search: ")
            playlist.search_song(s_id)

        elif choice == 6:
            s_id = input("Enter Song ID to remove: ")
            playlist.delete(s_id)

        elif choice == 7:
            playlist.display_size()

        elif choice == 8:
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_part2()
