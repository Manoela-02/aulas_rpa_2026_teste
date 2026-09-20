# Avaliação de Viabilidade de RPA

---

### 1. Nome do Processo
**Conciliação Bancária Diária** (Cenário A)

---

### 2. É viável para RPA? (Sim / Não)
**Sim**

---

### 3. Justificativa baseada nos 4 critérios essenciais

- **Repetitividade:** O processo segue uma rotina fixa e diária de download, leitura e comparação de arquivos, sendo executado de forma padronizada sem alterações no fluxo.
- **Regras de Negócio:** As regras de conciliação são 100% determinísticas e objetivas, baseadas na comparação direta de chaves de cruzamento (CNPJ e Valor Exato). Não há dependência de julgamento humano ou interpretação subjetiva.
- **Tipo de Dados:** Os dados de entrada são totalmente estruturados, compostos por arquivos no formato `.csv` (extrato bancário) e tabelas exportadas do sistema ERP.
- **Volume:** O processo envolve um volume elevado e recorrente de lançamentos bancários diários, tornando o trabalho manual lento, repetitivo e propenso a erros de digitação.

---

### 4. Mapeamento Passo a Passo das Ações do Robô

1. **Acesso e Download:** O robô acessa o portal do banco (ou diretório de rede) e baixa o arquivo do extrato bancário do dia em formato `.csv`.
2. **Leitura e Extração de Dados:** O robô lê o arquivo `.csv`, parseia os dados e armazena os registros em memória (identificando colunas como CNPJ do pagador, valor, data e número da transação).
3. **Consulta ao Sistema ERP:** O robô conecta-se ao sistema ERP (via API, banco de dados ou interface de usuário) e extrai a lista de contas a receber/baixas pendentes da data correspondente.
4. **Execução do Cruzamento (Conciliação):** 
   - Para cada registro do `.csv`, o robô busca um registro correspondente no ERP onde **CNPJ** e **Valor** sejam idênticos.
   - Se houver correspondência exata: O robô marca o lançamento como **"Conciliado"** no ERP.
5. **Tratamento de Exceções:** 
   - Se o CNPJ não for encontrado ou se o valor divergir, o robô registra o item em um relatório de divergências (exceção de negócio).
6. **Notificação e Finalização:** O robô gera um log final de execução e envia um e-mail para a equipe financeira com o resumo do processamento e a lista de itens não conciliados para análise humana.