import os
import json

# Caminho para o arquivo de armazenamento em disco
STORAGE_FILE = "srvData.json"

# Classe do dicionário remoto
class Dicionario:
    def __init__(self):
        self.dictionary = {}

    def load_dictionary(self):
        if os.path.exists(STORAGE_FILE):
            with open(STORAGE_FILE, "r") as file:
                self.dictionary = json.load(file)

    def save_dictionary(self):
        with open(STORAGE_FILE, "w") as file:
            json.dump(self.dictionary, file)

    def query(self, key):
        self.load_dictionary()
        values = self.dictionary.get(key, [])
        return sorted(values)

    def write(self, key, value):
        if key not in self.dictionary:
            self.dictionary[key] = []
        self.dictionary[key].append(value)
        self.save_dictionary()
        return "Entrada inserida com sucesso."

    def remove(self, key):
        if key in self.dictionary:
            del self.dictionary[key]
            self.save_dictionary()
            return "Entrada removida com sucesso."
        else:
            return "A entrada não existe."
