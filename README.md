##Python 2: Cisco
### pacotes e módulos
- pacote é tipo um container de módulos

#### passo a passo
- arquivo module.py: vazio
- arquivo main.py: import module (na mesma pasta) → rodar
- nova subpasta __pycache__: arquivo module.cpython-xy (código semi compilado, roda só se alterar)
- colocar um print em module.py + print(__name__)
- roda module.py: imprime o print + “__main__”
- quando roda um arquivo a variável __name__ vira __main__
- roda main.py: imprime o print + “module”
- quando um arquivo é importado como módulo, sua variável __name__ vira o nome do arquivo sem .py
- usar __main__ para ver o contexto que o código foi ativado
counter = 0
```bash   
if __name__ == "__main__":
   print("I prefer to be a module.")
else:
   print("I like to be a module.")
```

`module.counter` – não é seguro, permite acessar variáveis privadas (não tem como esconder variáveis, como no java)
pode informar que os usuários não devem modificar usando __ antes do nome
 
`#!/usr/bin/env python3` – para SOs Unix (mac, linux) essa linha informa onde está o interpretador Python (como executar o conteúdo), em SOs Windows essa linha é ignorada 
doc-string: string posta antes de qualquer instrução de módulo, explica o conteúdo do módulo ""

#### resumo
- módulo: juntar entidades relacionadas (funções, variáveis, constantes)
   - em cada 1a importação de um módulo, Python traduz seu códgo-fonte em um formato semi compilado nos arquivos `.pyc` e implanta esses arquivos no diretório `__pycache__` (no diretório home do módulo)
- pacote: container que permite juntar módulos relacionados sob um nome ocmum
   - pode ser um lote de arquivos implantados (subárvore) ou um .zip
- para dizer ao usuário (que usa o módulo) que uma entidade deve ser privada (não usada fora do módulo): marcar o nome com prefixo `_` ou `__` (recomendação)
- os nomes shabang, shebang, hasbang, poundbang, hashpling descrevem os dígrafos no `#!` (instruem SOs Unix como carregar arquivos-fonte Python; não afeta Windows)
- para o Python "ver" um diretório não padrão: o nome do pacote deve ser inserido na lista de diretórios de importação (variável de ambiente `path` - módulo `sys`)
- arquivo `__init__.py`: executado quando um pacote é importado, para inicializá-lo (pode ser vazio)
- para impedir que o usuário execute o código do módulo como um script comum:
```bash
import sys

if __name__ == "__main__":
    print "Don't do that!"
    sys.exit()
```