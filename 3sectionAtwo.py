import threading
import uuid
import random

class SessionIDGenerator:
    def __init__(self, storage_file="session_ids.txt"):
        self.next_id = 0
        self.session_ids = set()
        self.lock = threading.Lock()
        self.storage_file = storage_file

    def load_existing_ids(self):
        try:
            with open(self.storage_file, "r") as file:
                existing_ids = file.read().splitlines()
                self.session_ids = set(map(int, existing_ids))
                if self.session_ids:
                    self.next_id = max(self.session_ids) + 1
        except FileNotFoundError:
            pass

    def save_session_id(self, session_id):
        with open(self.storage_file, "a") as file:
            file.write(str(session_id) + "\n")

    def generate_section_id(self):
        uuid_str = str(uuid.uuid4()).replace("-", "")
        return int(uuid_str, 16)

    def generate_session_id(self):
        while True:
            session_id = self.generate_section_id()
            with self.lock:
                if session_id not in self.session_ids:
                    break
        self.session_ids.add(session_id)
        self.save_session_id(session_id)
        self.next_id = session_id + 1
        return session_id

    def is_session_id_available(self, session_id):
        with self.lock:
            return session_id not in self.session_ids

    def reset(self):
        with self.lock:
            self.session_ids = set()
            self.next_id = 0


# Create the SessionIDGenerator instance and load existing IDs from the file.
session_id_generator = SessionIDGenerator()
session_id_generator.load_existing_ids()

# Generate a new session ID and print it.
session_id = session_id_generator.generate_session_id()
print(session_id)
"""
200692614302068195578443797139247897662
330654026859482803296081705182550680794
100263661458156528839655456349091481698
200338684873865776431734624439039179750

"""


"""The provided code defines a SessionIDGenerator class, which is responsible for generating unique session IDs and managing them in a thread-safe manner. Below is a short explanation of the class and its methods:

    __init__(self, storage_file="session_ids.txt"): The constructor initializes the SessionIDGenerator object with a default storage_file parameter, which is the file to store the generated session IDs. It also initializes attributes like next_id (the next available ID to be generated), session_ids (a set to store existing session IDs), and lock (a threading lock to ensure thread safety).

    load_existing_ids(self): This method loads existing session IDs from the storage file, populating the session_ids set and updating the next_id attribute to be used for generating new session IDs.

    save_session_id(self, session_id): This method saves the given session_id to the storage file.

    generate_section_id(self): This method generates a new section ID by using the uuid library to create a random UUID string and converting it to an integer in base 16.

    generate_session_id(self): This method generates a new unique session ID by repeatedly calling generate_section_id() until a unique ID is found (i.e., not present in the session_ids set). Once a unique ID is generated, it is added to the set, saved to the storage file, and returned as the result.

    is_session_id_available(self, session_id): This method checks if a given session_id is available (not present in the session_ids set).

    reset(self): This method resets the session_ids set and sets the next_id back to 0.

In the provided code, an instance of SessionIDGenerator is created, and any existing session IDs from the file are loaded. Then, a new session ID is generated using the generate_session_id() method, and it is printed as the output."""