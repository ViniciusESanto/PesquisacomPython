# Ferramenta de pesquisa com Python (Google)

from googlesearch import search

conteudo = 'crimson san' # Conteudo a ser pesquisado

pesquisa = list(
    search(
        conteudo,
        lang='pt-br', # Em qual linguagem fazer a pesquisa
        num_results=5 # Quantidade de resultados que buscara para a pesquisa
    )
)

print(pesquisa)