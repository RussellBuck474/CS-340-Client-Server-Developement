from pymongo import MongoClient

class AnimalShelter:
    """
    CRUD operations for the AAC MongoDB animals collection.
    This version aligns with SNHU CS-340 requirements while
    preserving strong error handling and clean structure.
    """

    def __init__(self, user, password):
        """
        Initialize MongoDB connection using authenticated user.
        """
        try:
            connection_string = (
                f"mongodb://{user}:{password}@localhost:27017/?authSource=aac"
            )
            self.client = MongoClient(connection_string)
            self.database = self.client["aac"]
            self.collection = self.database["animals"]
            print("Connected to MongoDB successfully.")

        except Exception as e:
            print(f"Connection error: {e}")
            self.client = None
            self.database = None
            self.collection = None

    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------
    def create(self, data):
        """
        Insert a document into the animals collection.
        Returns True if successful, False otherwise.
        """
        try:
            if data is None:
                raise ValueError("No data provided for insert.")

            result = self.collection.insert_one(data)
            return result.acknowledged

        except Exception as e:
            print(f"Error inserting document: {e}")
            return False

    # ---------------------------------------------------------
    # READ
    # ---------------------------------------------------------
    def read(self, query):
        """
        Read documents from the animals collection.
        Returns a list of matching documents.
        """
        try:
            cursor = self.collection.find(query)
            return list(cursor)

        except Exception as e:
            print(f"Error reading documents: {e}")
            return []

    # ---------------------------------------------------------
    # UPDATE
    # ---------------------------------------------------------
    def update(self, query, new_values):
        """
        Update documents in the animals collection.
        Returns the number of modified documents.
        """
        try:
            if not new_values:
                raise ValueError("No update values provided.")

            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count

        except Exception as e:
            print(f"Error updating documents: {e}")
            return 0

    # ---------------------------------------------------------
    # DELETE
    # ---------------------------------------------------------
    def delete(self, query):
        """
        Delete documents from the animals collection.
        Returns the number of deleted documents.
        """
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count

        except Exception as e:
            print(f"Error deleting documents: {e}")
            return 0
