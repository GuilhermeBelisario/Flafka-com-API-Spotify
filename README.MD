## Descrição do Projeto
O projeto é uma extração de dados conforme um arquivo TXT com nome de bandas para consulta no Spotify. Na consulta, são obtidos o gênero, nome da banda, popularidade e os 10 sons mais populares da banda. Após isso, os dados são gravados em um arquivo, lidos com o Flume e publicados em tópicos do Kafka com filtro através do gênero.

## Objetivos
- Extrair dados de bandas a partir de um arquivo TXT.
- Consultar informações no Spotify.
- Gravar os dados em um arquivo JSON ou TXT.
- Ler o arquivo com o Flume.
- Enviar os dados em tópicos do Kafka com filtro por gênero.

## Funcionalidades
- Leitura de arquivo TXT com nomes de bandas.
- Consulta à API do Spotify para obter informações detalhadas das bandas.
- Salvamento dos dados.
- Integração com Apache Flume para leitura dos dados.
- Publicação dos dados filtrados por gênero no topico do Apache Kafka.

## Estrutura do Projeto
- `data/`: Contém o arquivo TXT com nomes de bandas.
- `scripts/`: Scripts para extração e consulta de dados.
- `output/`: Arquivos JSON gerados.
- `flume/`: Configurações e scripts do Apache Flume.
- `kafka/`: Configurações e scripts do Apache Kafka.

## Requisitos
- Sistema Operacional: Windows 10 (Uso a Versão Pro)
- Python 3.12.3 (Uso essa versão)
- Bibliotecas Python: `requests`, `json`, `os`,`spotipy`, etc.
- Conta de desenvolvedor no Spotify e credenciais da API.
- Apache Flume
- Apache Kafka_2.13-3.7.0

## Uso
1. Adicione nomes de bandas ao arquivo `data/bandas.txt` ou adaptar para usar INPUT ou outra forma de entrada dos nomes.

## Contribuições
Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request para melhorias, correções e sugestões!
