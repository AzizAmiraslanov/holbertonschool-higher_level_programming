#!/usr/bin/python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current object instance to a file using pickle.
        Returns None if an error occurs.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (FileNotFoundError, PermissionError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes a CustomObject instance from a pickle file.
        Returns None if file does not exist or is malformed.
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                return obj
        except (FileNotFoundError, PermissionError, pickle.UnpicklingError, EOFError):
            return None
