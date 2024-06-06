import requests

# Dicionário de códigos IBGE para estados
estados_codigos_ibge = {
    "AC": 12,
    "AL": 27,
    "AP": 16,
    "AM": 13,
    "BA": 29,
    "CE": 23,
    "DF": 53,
    "ES": 32,
    "GO": 52,
    "MA": 21,
    "MT": 51,
    "MS": 50,
    "MG": 31,
    "PA": 15,
    "PB": 25,
    "PR": 41,
    "PE": 26,
    "PI": 22,
    "RJ": 33,
    "RN": 24,
    "RS": 43,
    "RO": 11,
    "RR": 14,
    "SC": 42,
    "SP": 35,
    "SE": 28,
    "TO": 17
}

#Acessa a API do CNES para obter hospitais pelo código do estado
def obter_hospitais_por_estado(codigo_estado, pags):
    url = f"https://apidadosabertos.saude.gov.br/cnes/estabelecimentos?codigo_uf={codigo_estado}&status=1&limit=20&offset={pags}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return (response.json().get('estabelecimentos', []), pags)
    except requests.RequestException as e:
        print(f"Erro ao acessar a API do CNES: {e}")
        return ([], pags)

#Acessa a API do CNES para obter hospitais pelo código do município e tipo de unidade
def obter_hospitais_por_municipio(codigo_municipio):

    tipo_unid = [1, 73]
    lista = []

    for tipo in tipo_unid:
        url = f"https://apidadosabertos.saude.gov.br/cnes/estabelecimentos?codigo_tipo_unidade={tipo}&codigo_municipio={codigo_municipio}&status=1&limit=20&offset=1"
        try:
            response = requests.get(url)
            response.raise_for_status()
            resposta = response.json().get('estabelecimentos', [])
            lista.append(resposta)
        except requests.RequestException as e:
            print(f"Erro ao acessar a API do CNES: {e}")
            break 

    return lista

# Acessa a API do ViaCEP para obter o município a partir do CEP
def obter_municipio_por_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    return response.json()

# Filtra hospitais por município -> após obter o código de município
def filtrar_hospitais_por_municipio(hospitais, municipio_desejado, pags):
    hospitais_no_municipio = []
    for hospital in hospitais:
        cep = hospital.get('codigo_cep_estabelecimento', '')
        print(cep)
        if cep:
            endereco = obter_municipio_por_cep(cep)
            print(endereco)
            if municipio_desejado.lower() in endereco.get('localidade', '').lower():
                codigo_municipio = hospital.get('codigo_municipio', '')

                return obter_hospitais_por_municipio(codigo_municipio)

                #print(hospitais_no_municipio)

    if len(hospitais) == 0:
        return hospitais
    codigo_estado = hospitais[0].get('codigo_uf', '')
    hospitais, _ = obter_hospitais_por_estado(codigo_estado, pags + 1) 
    return filtrar_hospitais_por_municipio(hospitais, municipio_desejado, pags+1)

def main():
    estado = input("Selecione o estado (sigla): ").strip().upper()
    if estado not in estados_codigos_ibge:
        print("Estado inválido")
        return
    municipio = input("Digite o nome do município: ").strip()
    
    print(estados_codigos_ibge[estado])
    codigo_estado = estados_codigos_ibge[estado]
    hospitais, pags = obter_hospitais_por_estado(codigo_estado, 1)
    hospitais_no_municipio = filtrar_hospitais_por_municipio(hospitais, municipio, pags)
    
    
    print(f"Hospitais em {municipio}, {estado}:")
    for hospitais in hospitais_no_municipio:
        for hospital in hospitais:
            print(hospital.get('nome_fantasia', ''))

if __name__ == "__main__":
    main()
