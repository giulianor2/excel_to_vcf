import pandas as pd

# Função para criar uma entrada VCF
def criar_entrada_vcf(nome, numero, titulo):
    vcf_entry = (
        "BEGIN:VCARD\n"
        "VERSION:3.0\n"
        f"N:{nome}\n"
        f"TEL;TYPE=CELL:{numero}\n"
        f"TITLE:{titulo}\n"
        "END:VCARD\n"
    )
    return vcf_entry

# Função principal para ler a planilha e gerar o arquivo VCF
def gerar_vcf_de_planilha(caminho_planilha, caminho_vcf):
    df = pd.read_excel(caminho_planilha)

    with open(caminho_vcf, 'w') as arquivo_vcf:
        for index, row in df.iterrows():
            nome = row['nome do contato']
            numero = row['número do celular']
            titulo = row['title'] 
            vcf_entry = criar_entrada_vcf(nome, numero, titulo)
            arquivo_vcf.write(vcf_entry)

    print(f"Arquivo VCF salvo em {caminho_vcf}")


caminho_planilha = 'contatos.xlsx'  # Caminho para o arquivo da planilha
caminho_vcf = 'contatos.vcf'        # Caminho para o arquivo VCF de saída
gerar_vcf_de_planilha(caminho_planilha, caminho_vcf)
