pessoas = ["Fabio","Carlos","Regina","Vanuza"]

print(type(pessoas))

print(pessoas)

pessoas[1] = "Sergio"

#Adicionando elementos.

pessoas.append("Sarah")# Adiciona no final
pessoas.insert(2,"Flavio")# Adiciona em qualquer luga

for chave, valor in enumerate(pessoas):
    print(f"{chave:.<5}{valor}")

#Removendo elementos.

pessoas.pop()# Remove o último elemento.
pessoas.pop(1)
pessoas.remove("Flavio")


print(pessoas)

# copiando listas
pessoasBkp = pessoas[:]
pessoasBkp.append("Jerônimo")
print("\n\n",pessoas)
print(pessoasBkp,"\n\n") 

pessoas.clear()#limpa a lista
# del(pessoas) - Excluir a variável lista
print(pessoas,"\n\n")