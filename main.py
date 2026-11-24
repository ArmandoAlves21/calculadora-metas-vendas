def calcular_comissao(vendas, meta, percentual_base=0.03, bonus_meta=0.02):
    comissao = vendas * percentual_base
    if vendas >= meta:
        comissao += vendas * bonus_meta
        status = "Meta atingida!"
    else:
        status = "Meta não atingida."
    return comissao, status

if __name__ == "__main__":
    print("=== Calculadora de Metas e Comissões ===")
    vendas = float(input("Total de vendas no mês (R$): "))
    meta = float(input("Meta mensal (R$): "))
    
    valor, status = calcular_comissao(vendas, meta)
    print(f"\nStatus: {status}")
    print(f"Comissão a receber: R$ {valor:.2f}")
