# 📘 Atividade: Organizador Automático de Arquivos

## 🎯 Objetivo

Aprenda a automatizar uma tarefa comum do computador usando Python. Você irá percorrer uma pasta, identificar arquivos por extensão e organizá-los em subpastas com segurança usando apenas a biblioteca padrão.

## 📝 Tarefas

### 🛠️ Listar e Classificar Arquivos

#### Descrição

Complete o programa para receber uma pasta de origem e listar os arquivos que estão diretamente dentro dela. Para cada arquivo, identifique sua extensão e classifique arquivos sem extensão como `outros`.

#### Requisitos

O programa concluído deve:

- Usar `pathlib.Path` para trabalhar com caminhos.
- Ignorar subpastas durante a listagem inicial.
- Exibir o nome do arquivo e sua categoria, como `relatorio.pdf -> pdf`.
- Classificar arquivos sem extensão em uma categoria chamada `outros`.

### 🛠️ Organizar Arquivos por Extensão

#### Descrição

Expanda o programa para criar uma subpasta para cada categoria e mover os arquivos para o local correspondente. Por exemplo, arquivos `.txt` devem ir para `txt/` e arquivos `.jpg` para `jpg/`.

#### Requisitos

O programa concluído deve:

- Criar as subpastas de destino somente quando forem necessárias.
- Mover cada arquivo para a subpasta correspondente usando `shutil`.
- Manter arquivos sem extensão na pasta `outros/`.
- Exibir um resumo com a quantidade de arquivos processados por categoria.

### 🛠️ Adicionar Segurança e Opções de Execução

#### Descrição

Torne o organizador adequado para uso real. Adicione argumentos de linha de comando, valide a pasta de origem e evite substituir um arquivo que já exista no destino.

#### Requisitos

O programa concluído deve:

- Aceitar a pasta de origem e, opcionalmente, uma pasta de destino com `argparse`.
- Exibir uma mensagem clara e encerrar sem alterar arquivos quando a pasta de origem não existir ou não for uma pasta.
- Não sobrescrever arquivos existentes; arquivos com nomes conflitantes devem ser ignorados e informados ao usuário.
- Permitir executar o programa com um comando semelhante a:

```text
python starter-code.py ./arquivos-teste --destino ./arquivos-organizados
```

- Informar ao final quantos arquivos foram movidos e quantos foram ignorados.
