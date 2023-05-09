import json
from pathlib import Path
import threading

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
        '''Salva o dicionário em um arquivo'''
        with open(self.nomeArq, 'w') as f:
            json.dump(self.dicionario, f)

    def add(self, chave, valor):
        '''Adiciona um valor a uma chave do dicionário'''
        if chave in self.dicionario:
            self.dicionario[chave].append(valor)
        else:
          self.dicionario[chave] = [valor]
        self.fechar()
        print(f"Valor '{valor}' adicionado à chave '{chave}' com sucesso.")
        return self.dicionario[chave]

    def rem(self, chave):
        '''Remove uma chave do dicionário'''
        if chave in self.dicionario:
            del self.dicionario[chave]
            self.fechar()
            print("Chave removida com sucesso.")
        else:
            print("ERRO: Chave não encontrada.")

    def con(self, chave):
        '''Busca uma chave no dicionário'''
        print(f"Buscando chave '{chave}'...")
        if chave in self.dicionario:
            return self.dicionario[chave]
        else:
            return ['Chave não encontrada no dicionario!']