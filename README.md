# Hospitais-Municipio
 Estudo para a coleta dos dados de Hospitais por municipio utilzando API com Python

A coleta dos dados é feita através da API aberda do CNES, que é o Cadastro Nacional de Estabelecimentos de Saúde. Encontrada [aqui](https://apidadosabertos.saude.gov.br/v1/#/CNES/).

A API é bem simples de ser utilizada, basta fazer um GET na URL https://api.saude.gov.br/cnes/v1/estabelecimentos/ e passar os parâmetros que deseja. No caso, para pegar os hospitais de um município, basta passar o código do município como parâmetro.

O código do estado é o código IBGE. Esse código pode ser encontrado no [site do IBGE](https://www.ibge.gov.br/explica/codigos-dos-municipios.php#RJ), e no caso dos códigos deste repositorio, estão estruturados como um dicionário, onde a chave é o nome do município e o valor é o código do IBGE.

Para obter os códigos dos municípios, foi feita uma relação do dado do CEP obtidos da API do CNES com os códigos de estado e a API do viaCEP, que retorna o endereço completo de um CEP. (A API do viaCEP é encontrada [aqui](https://viacep.com.br/) 
Assim, é feita uma relação do municipio com o código do municipio utilizado na API do CNES, vinda da lista original. Após isso, é feita uma nova busca, utilizando esse código, para obter os dados dos hospitais do municipio especifico.

O código foi feito em Python, e utiliza as bibliotecas requests.

Além do filtro pelo municipio, a função que faz a busca dos dados dos hospitais (*obter_hospitais_por_municipio()*), também pode ser filtrada por outro parâmetro, o tipo de estabelecimento.
Esse código no momento atual está configurado para buscar apenas os Postos de Saúde (*1*) e Pronto Atendimento (*73*), mas pode ser alterado para buscar qualquer tipo de estabelecimento, como hospitais, clinicas, etc. Basta adicionar na lista

Para saber qual código se relaciona a qual tipo de estabelecimento, basta fazer um GET na URL https://apidadosabertos.saude.gov.br/cnes/tipounidades


| codigo_tipo_unidade  | descricao_tipo_unidade |
| ------------- | ------------- |
| 80  | LABORATORIO DE SAUDE PUBLICA  |
| 81  | CENTRAL DE REGULACAO DO ACESSO  |
| 79  | OFICINA ORTOPEDICA  |
| 82  | CENTRAL DE NOTIFICACAO,CAPTACAO E DISTRIB DE ORGAOS ESTADUAL  |
| 78  | UNIDADE DE ATENCAO EM REGIME RESIDENCIAL  |
| 74  | POLO ACADEMIA DA SAUDE  |
| 75  | TELESSAUDE  |
| 77  | SERVICO DE ATENCAO DOMICILIAR ISOLADO(HOME CARE)  |
| 76  | CENTRAL DE REGULACAO MEDICA DAS URGENCIAS  |
| 69  | CENTRO DE ATENCAO HEMOTERAPIA E OU HEMATOLOGICA  |
| 70  | CENTRO DE ATENCAO PSICOSSOCIAL  |
| 71  | CENTRO DE APOIO A SAUDE DA FAMILIA  |
| 72  | UNIDADE DE ATENCAO A SAUDE INDIGENA  |
| 1  | POSTO DE SAUDE  |
| 2  | CENTRO DE SAUDE/UNIDADE BASICA  |
| 4  | POLICLINICA  |
| 22  | CONSULTORIO ISOLADO  |
| 40  | UNIDADE MOVEL TERRESTRE  |
| 42  | UNIDADE MOVEL DE NIVEL PRE-HOSPITALAR NA AREA DE URGENCIA  |
| 32  | UNIDADE MOVEL FLUVIAL  |
| 36  | CLINICA/CENTRO DE ESPECIALIDADE  |
| 64  | CENTRAL DE REGULACAO DE SERVICOS DE SAUDE  |
| 43  | FARMACIA  |
| 39  | UNIDADE DE APOIO DIAGNOSE E TERAPIA (SADT ISOLADO)  |
| 61  | CENTRO DE PARTO NORMAL - ISOLADO  |
| 62  | HOSPITAL/DIA - ISOLADO  |
| 15  | UNIDADE MISTA  |
| 20  | PRONTO SOCORRO GERAL  |
| 21  | PRONTO SOCORRO ESPECIALIZADO  |
| 5  | HOSPITAL GERAL  |
| 7  | HOSPITAL ESPECIALIZADO  |
| 50  | UNIDADE DE VIGILANCIA EM SAUDE  |
| 67  | LABORATORIO CENTRAL DE SAUDE PUBLICA LACEN  |
| 73  | PRONTO ATENDIMENTO  |
| 60  | COOPERATIVA OU EMPRESA DE CESSAO DE TRABALHADORES NA SAUDE  |
| 68  | CENTRAL DE GESTAO EM SAUDE  |
| 83  | POLO DE PREVENCAO DE DOENCAS E AGRAVOS E PROMOCAO DA SAUDE  |
| 84  | CENTRAL DE ABASTECIMENTO  |
| 85  | CENTRO DE IMUNIZACAO  |

Problema encontrado e opotunidades de melhoria: 
A API do CNES não retorna todos os dados de uma vez, ela retorna apenas 1000 registros por vez. Para obter todos os registros, é necessário fazer uma paginação, passando o parâmetro “pagina” na URL. Portanto é necessário fazer um loop para obter todos os registros, e caso o município indicado pelo usuário seja pouco conhecido, a API do viaCEP pode chegar ao limite de requisições. Campo dos Goytacazes é um exemplo estudado.

Idealizado por: Matheus Soares e [Andrews Costa](https://github.com/Andrewsrj)





