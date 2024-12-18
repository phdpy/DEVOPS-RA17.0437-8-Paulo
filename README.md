# DEVOPS-RA17.0437-8-Paulo Henrique
# DEVOPS-RA17.0283-6-Gulherme Neves
## Problema com Jenkins

Infelizmente, durante o processo de instalação do Jenkins, houve dificuldades em configurar corretamente o serviço no meu ambiente. Eu segui as etapas recomendadas, mas encontrei um erro ao tentar iniciar o Jenkins:

## Desafios Enfrentados

Durante a execução deste trabalho, encontrei dificuldades na instalação do Jenkins em minha máquina local, o que me impediu de concluir a configuração da pipeline de integração contínua (CI/CD). Apesar disso, consegui configurar todos os arquivos necessários para a automação, incluindo o `Jenkinsfile`, o `docker-compose.yml`, além das configurações para o Prometheus e Grafana, que são parte fundamental do trabalho.

Acredito que o projeto ainda está em andamento, e estou buscando soluções para resolver as questões do Jenkins, mas estou confiante de que a estrutura do projeto está corretamente configurada para que o Jenkins seja integrado quando o ambiente estiver funcional.

Agradeço pela compreensão e estou à disposição para discutir as dificuldades que enfrentei.

## Instalado o Docker
sudo apt update && sudo apt upgrade -y
sudo apt install docker.io -y

E adicionados  dois novos arquivos ao prj.
docker-compose.yml:

Configura dois serviços principais:

Prometheus: Coleta métricas e roda na porta 9090.
Grafana: Exibe dashboards e roda na porta 3000.
Também mapeia volumes para carregar as configurações do Prometheus.
prometheus.yml:
Define o intervalo de coleta de métricas e especifica os alvos a serem monitorados, como a aplicação Flask.

Esses arquivos garantem que Prometheus e Grafana sejam executados automaticamente com as configurações corretas.

# Monitoramento e Dashboards no Grafana
O projeto inclui um ambiente de monitoramento utilizando Prometheus e Grafana. O Prometheus coleta métricas da aplicação e do banco de dados, enquanto o Grafana exibe essas métricas em dashboards.

Configuração do Grafana:
Acesse o Grafana pelo link: http://localhost:3000.
Faça login com as credenciais padrão (admin / admin).
Adicione o Prometheus como fonte de dados em Configuration > Data Sources, utilizando a URL:
http://prometheus:9090

Número de requisições à aplicação.
Uso de CPU e memória.
Consultas ao banco de dados MariaDB.
Visualização de Métricas:
Os dashboards fornecem uma visão clara e detalhada do desempenho da aplicação e do banco de dados, facilitando o acompanhamento em tempo real.

