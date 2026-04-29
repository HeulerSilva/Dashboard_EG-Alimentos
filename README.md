# Título: Dashboard de Vendas Interativo - EG Alimentos.
# Descrição: Projeto de Engenharia de Dados focado em extração (SQL Server), transformação (Pandas) e visualização (Streamlit).
# Tecnologias: Python, SQL Server, Pandas, Streamlit e Plotly.
# Destaque Técnico: Este projeto foi desenvolvido aplicando boas práticas de Engenharia e Arquitetura de Dados, com foco em escalabilidade e segurança:
  #1 - Pipeline de ETL Robusto: Implementação de um fluxo completo de extração via SQLAlchemy conectando diretamente a uma instância de SQL Server, permitindo o processamento eficiente de uma base histórica REAL com mais de 45.000 registros.
  #2 - Data Wrangling & Normalização: Utilização intensiva da biblioteca Pandas para o tratamento de dados brutos, incluindo a resolução de conflitos de padrões de data (ISO vs. BR) e tipagem de dados para garantir a integridade das métricas de faturamento.
  #3 - Arquitetura de Segurança: Implementação de Variáveis de Ambiente (python-dotenv) para a gestão segura de credenciais sensíveis, garantindo que informações de conexão e segurança do banco de dados nunca sejam expostas em repositórios públicos.
  #4 - Visualização de Alta Performance: Desenvolvimento de uma interface interativa em Streamlit integrada a gráficos dinâmicos do Plotly, utilizando técnicas de caching de dados (@st.cache_data) para otimizar a performance e reduzir a carga de consultas ao banco de dados.
  #5 - Business Intelligence Aplicado: Criação de visões multidimensionais e análise temporal (Year-over-Year / Month-over-Month) para suporte direto à tomada de decisão estratégica na gestão da EG Alimentos.
