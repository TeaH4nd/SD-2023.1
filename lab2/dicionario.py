import json
from pathlib import Path

class Dicionario:
    
    def __init__(self, nomeArq):
        self.nomeArq = nomeArq
        Path(self.nomeArq).touch(exist_ok=True)
        try:
            with open(self.nomeArq, 'r') as f:
                self.dicionario = json.load(f)
        except:
            self.dicionario = {}

    def fechar(self):
        with open(self.nomeArq, 'w') as f:
            json.dump(self.dicionario, f)

    def add(self, chave, valor):
        if chave in self.dicionario:
            self.dicionario[chave].append(valor)
            print(f"Valor [{valor}] adicionado ao dicionario!")
        else:
            self.dicionario[chave] = [valor]
            print(f"Chave adicionada ao dicionario!")
        self.fechar()
        return self.dicionario[chave]

    def rem(self, chave):
        if chave in self.dicionario:
            del self.dicionario[chave]
            self.fechar()
            print("Chave removida com sucesso.")
        else:
            print("Error: Chave não encontrada.")

    def con(self, chave):
        if chave in self.dicionario:
            return self.dicionario[chave]
        else:
            return ['Chave não encontrada no dicionario!']