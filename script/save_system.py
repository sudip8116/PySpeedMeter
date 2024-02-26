import os
import pickle


class SaveSystem:

    ALPHA_PATH = "app/src/save/alpha.data"
    POS_PATH = "app/src/save/pos.data"

    @staticmethod
    def loadData(path, default):
        if not os.path.exists(path):
            with open(path, "wb") as f:
                f.write(pickle.dumps(default))
            return default
        with open(path, "rb") as f:
            return pickle.loads(f.read())

    @staticmethod
    def saveData(path, value):
        with open(path, "wb") as f:
            f.write(pickle.dumps(value))
