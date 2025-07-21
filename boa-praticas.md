            3-  boas praticas para usar Git e Github
Git:

1-Use 3. Use branches para organizar o trabalho
Nunca trabalhe diretamente na main.

Crie branches por feature, bug ou refatoração:

feat/login

fix/form-validation

refactor/user-service

2- Commits atomicos

Cada commit deve conter uma unica mudança logica
(ex:corrigir um bug, adicionar uma funçao)

3- Atualize sua branch com frequencia

Use o git pull ou git fetch + merge/rebase para manter sua branch sincronizada com a main

GitHub: 

1-Pull Requests (PRs)
Crie PRs pequenos e com descrição clara
Explique o que foi feito, por quê e o impacto.

Solicite revisões de código (code reviews)
Mesmo em times pequenos, isso melhora a qualidade.

Não faça merge direto na main
Sempre via PR.

2- 4. Issues (Controle de tarefas e bugs)
Use Issues para rastrear bugs e funcionalidades
Evite usar anotações fora do GitHub.

Adicione labels às Issues
Ex: bug, feature, help wanted, documentação.

Relacione PRs com Issues
Exemplo no corpo da PR:

3-  6. Colaboração
Use projetos (Projects)
Tipo um quadro Kanban para organizar tarefas.

Adicione colaboradores com permissões corretas
Não dê acesso de admin a quem não precisa.

Use Wikis ou /docs para documentar processos mais longos
