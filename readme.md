# Integração com a API Discogs

Este projeto realiza requisições à API Discogs para buscar dados relacionados a artistas e álbuns e os salva em um arquivo JSON. 

## API Discogs
A [API Discogs](https://www.discogs.com/developers) pode ser usada para acessar informações de artistas, álbuns e lançamentos.

# Overview
O projeto realiza requisições à API Discogs para buscar informações sobre artistas e seus respectivos álbuns. Os dados são formatados e salvos num arquivo `.json`, seguindo esssa estrutura:

```python
{
    "id": "",
    "name": "",
    "genre": "",
    "members": [],
    "websites": [],
    "albums": [
        {
            "name": "",
            "year": "",
            "label": "",
            "styles": [],
            "tracks": [
                {
                    "number": 0,
                    "title": "",
                    "duration": ""
                }
            ]
        }
    ]
}
```

# Estrutura do Projeto

O código foi estruturado utilizando a arquitetura hexagonal para garantir separação de responsabilidades.

- apps/ - Contém o código-fonte, organizado de acordo com a arquitetura hexagonal.
- adapterss/ - Implementação das interfaces externas (requisições à API).
- domain/ - Lógica de negócio e entidades do sistema.
    - entities: define as classes que representam as entidades principais do domínio, organiza os dados relacionados aos artistas, álbuns e faixas (tracks) de maneira estruturada.
    - service: Orquestra as interações entre os adaptadores DiscogsAPI (para buscar dados) e    FileStorage (para salvar os dados).
- config/ - inclui arquivos de configuração e código relacionado à inicialização e gestão de parâmetros globais.
- main.py - Ponto de entrada do programa, responsável por orquestrar a execução.

# Requisitos
- [Python 3.x](https://www.python.org/doc/)


# Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/projeto-discogs.git
```

2. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

3. Execute o script na raiz do projeto para buscar dados da API e salvar em um arquivo JSON:
```bash
python main.py
```

> O arquivo `dados.json` será gerado na pasta onde o script foi executado.
