#Mapa, definir os registradores em formas binarias 
Mapa_De_Registradores = {
    "x0": "00000",
    "x1": "00001",
    "x2": "00010",
    "x3": "00011",
    "x4": "00100",
    "x5": "00101",
    "x6": "00110",
    "x7": "00111",
    "x8": "01000",
    "x9": "01001",
    "x10": "01010",
    "x11": "01011",
    "x12": "01100",
    "x13": "01101",
    "x14": "01110",
    "x15": "01111",
    "x16": "10000",
    "x17": "10001",
    "x18": "10010",
    "x19": "10011",
    "x20": "10100",
    "x21": "10101",
    "x22": "10110",
    "x23": "10111",
    "x24": "11000",
    "x25": "11001",
    "x26": "11010",
    "x27": "11011",
    "x28": "11100",
    "x29": "11101",
    "x30": "11110",
    "x31": "11111"
}
#Funções, que juntam as informações adiquiridas, e que montam a instrução em linguagem de maquina
#E printam no terminal
#Instruções Tipo (R)

#pseudo instruções
def SRL(arquivo):
    opcode = "0110011"
    funct7 = "0000000"
    funct3 = "101"
    print(f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}")
    return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

def SUB(arquivo):
    opcode = "0110011"
    funct7 = "0100000"
    funct3 = "000"
    print(f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}")
    return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

def AND(arquivo): #I-and pois ja existi uma função and em python
    opcode = "0110011"
    funct7 = "0000000"
    funct3 = "111"
    print(f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}")
    return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}" 

def ADD(arquivo):
    opcode = "0110011"
    funct7 = "0000000"
    funct3 = "000"
    print(f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}")
    return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

def SLL(arquivo):
    opcode = "0110011"
    funct7 = "0000000"
    funct3 = "001"
    print(f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}")
    return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

def SLT(arquivo):
    opcode = "0110011"
    funct7 = "0000000"
    funct3 = "010"
    print(f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}")
    return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

def SLTU(arquivo):
    opcode = "0110011"
    funct7 = "0000000"
    funct3 = "011"
    print(f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}")
    return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

def XOR(arquivo):
    opcode = "0110011"
    funct7 = "0000000"
    funct3 = "100"
    print(f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}")
    return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

def SRA(arquivo):
    opcode = "0110011"
    funct7 = "0100000"
    funct3 = "101"
    print(f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}")
    return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

def OR(arquivo):
    opcode = "0110011"
    funct7 = "0000000"
    funct3 = "110"
    print(f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}")
    return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"


#Instruções Tipo (I)

def ORI(arquivo):
    opcode = "0010011"
    funct3 = "110"
    print(f"{imediato}{rs1}{funct3}{rd}{opcode}")
    return f"{imediato}{rs1}{funct3}{rd}{opcode}"

def ADDI(arquivo):
    opcode = "0010011"
    funct3 = "000"
    print(f"{imediato}{rs1}{funct3}{rd}{opcode}")
    return f"{imediato}{rs1}{funct3}{rd}{opcode}"

def SLTI(arquivo):
    opcode = "0010011"
    funct3 = "010"
    print(f"{imediato}{rs1}{funct3}{rd}{opcode}")
    return f"{imediato}{rs1}{funct3}{rd}{opcode}"

def SLTIU(arquivo):
    opcode = "0010011"
    funct3 = "011"
    print(f"{imediato}{rs1}{funct3}{rd}{opcode}")
    return f"{imediato}{rs1}{funct3}{rd}{opcode}"

def XORI(arquivo):
    opcode = "0010011"
    funct3 = "100"
    print(f"{imediato}{rs1}{funct3}{rd}{opcode}")
    return f"{imediato}{rs1}{funct3}{rd}{opcode}"

def ANDI(arquivo):
    opcode = "0010011"
    funct3 = "111"
    print(f"{imediato}{rs1}{funct3}{rd}{opcode}")
    return f"{imediato}{rs1}{funct3}{rd}{opcode}"

#Tipo (I) - LOAD

def LB(arquivo): 
    opcode = "0000011"
    funct3 = "000"
    print(f"{imediato}{rs1}{funct3}{rd}{opcode}")
    return f"{imediato}{rs1}{funct3}{rd}{opcode}"

def LH(arquivo): 
    opcode = "0000011"
    funct3 = "001"
    print(f"{imediato}{rs1}{funct3}{rd}{opcode}")
    return f"{imediato}{rs1}{funct3}{rd}{opcode}"

def LW(arquivo): 
    opcode = "0000011"
    funct3 = "010"
    print(f"{imediato}{rs1}{funct3}{rd}{opcode}")
    return f"{imediato}{rs1}{funct3}{rd}{opcode}"

def LBU(arquivo): 
    opcode = "0000011"
    funct3 = "100"
    print(f"{imediato}{rs1}{funct3}{rd}{opcode}")
    return f"{imediato}{rs1}{funct3}{rd}{opcode}"

def LHU(arquivo): 
    opcode = "0000011"
    funct3 = "101"
    print(f"{imediato}{rs1}{funct3}{rd}{opcode}")
    return f"{imediato}{rs1}{funct3}{rd}{opcode}"


#Instruções Tipo(S)

def SB(arquivo):
    opcode = "0100011"
    funct3 = "000"
    print(f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}")
    return f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}"

def SH(arquivo):
    opcode = "0100011"
    funct3 = "001"
    print(f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}")
    return f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}"

def SW(arquivo):
    opcode = "0100011"
    funct3 = "010"
    print(f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}")
    return f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}"

#Instruções Tipo (B)

def BEQ(Arquivo):
    opcode = "1100011"
    funct3 = "000"
    print(f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}")
    return f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}"

def BNE(Arquivo):
    opcode = "1100011"
    funct3 = "001"
    print(f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}")
    return f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}"

def BLT(Arquivo):
    opcode = "1100011"
    funct3 = "100"
    print(f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}")
    return f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}"

def BGE(Arquivo):
    opcode = "1100011"
    funct3 = "101"
    print(f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}")
    return f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}"

def BLTU(Arquivo):
    opcode = "1100011"
    funct3 = "110"
    print(f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}")
    return f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}"

def BGEU(Arquivo):
    opcode = "1100011"
    funct3 = "111"
    print(f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}")
    return f"{(imediato[:7])}{rs1}{rd}{funct3}{imediato[7:]}{opcode}"

#Input para pegar o nome do endereço de Entrada
Nome_Arquivo = str(input("Nome do Arquivo:\n"))

#Abre tanto o Arquivo de Entrada(Para ler), quanto o de Saida (Para Escrever)
with open(Nome_Arquivo, 'r') as Entrada: #Entrada
    with open('Saida', 'w') as Saida: #Saida
        linhas = Entrada.readlines()

        for line in linhas:
            words = line.split()

            if words: #Pega as palavras
                Instrucao = words[0] #Pega a Instrucao
                rd = words[1].strip(',') #Retira a virgula
                Contador = 0
                for i in Mapa_De_Registradores:
                    if rd == i:
                        rd = format(Contador, '05b') #Completa/transforma para um numero binario de 5 bits
                        Contador = 0
                        break
                    Contador += 1

                rs1 = words[2].strip(',')
                if rs1[0] == 'x': #transforma o registrador, em um formato binario
                    for i in Mapa_De_Registradores:
                        if rs1 == i:
                            rs1 = format(Contador, '05b')
                            Contador = 0
                            break
                        Contador += 1

                rs2 = words[3]
                if rs2[0] == 'x':
                    for i in Mapa_De_Registradores:
                        if rs2 == i:
                            rs2 = format(Contador, '05b')
                            Contador = 0
                            break
                        Contador += 1
                
                else :
                    imediato = format(int(words[3]), '012b') #Pega um numero inteiro e transforma em um binario de 12 bits
                    imediato = str(imediato) #Transforma o binario em string
                
                #Verifica a Instrucao da linha do arquivo em especifico
                #Chama a função e armazena o codigo em Aux
                if Instrucao == 'lb':
                    Aux = LB(Nome_Arquivo)

                elif Instrucao == 'sb':
                    Aux = SB(Nome_Arquivo)
                
                elif Instrucao == 'sub':
                    Aux = SUB(Nome_Arquivo)
                    
                elif Instrucao == 'and':
                    Aux = AND(Nome_Arquivo)
                
                elif Instrucao == 'ori':
                    Aux = ORI(Nome_Arquivo)
                
                elif Instrucao == 'srl':
                    Aux = SRL(Nome_Arquivo)
                elif Instrucao == 'beq':
                    Aux = BEQ(Nome_Arquivo)
                #Instruções a mais, que não foram designadas ao meu grupo
                #Tipo R
                elif Instrucao == 'add':
                    Aux = ADD(Nome_Arquivo)
                elif Instrucao == 'sll':
                    Aux = SLL(Nome_Arquivo)
                elif Instrucao == 'slt':
                    Aux = SLT(Nome_Arquivo)
                elif Instrucao == 'sltu':
                    Aux = SLTU(Nome_Arquivo)
                elif Instrucao == 'xor':
                    Aux = XOR(Nome_Arquivo)
                elif Instrucao == 'sra':
                    Aux = SRA(Nome_Arquivo)
                elif Instrucao == 'or':
                    Aux = OR(Nome_Arquivo)
                
                #Tipo I
                elif Instrucao == 'addi':
                    Aux = ADDI(Nome_Arquivo)
                elif Instrucao == 'slti':
                    Aux = SLTI(Nome_Arquivo)
                elif Instrucao == 'sltiu':
                    Aux = SLTIU(Nome_Arquivo)
                elif Instrucao == 'xori':
                    Aux = XORI(Nome_Arquivo)
                elif Instrucao == 'andi':
                    Aux = ANDI(Nome_Arquivo)
                
                #Tipo I - Load
                elif Instrucao == 'lh':
                    Aux = LH(Nome_Arquivo)
                elif Instrucao == 'lw':
                    Aux = LW(Nome_Arquivo)
                elif Instrucao == 'lbu':
                    Aux = LBU(Nome_Arquivo)
                elif Instrucao == 'lhu':
                    Aux = LHU(Nome_Arquivo)

                #Tipo S
                elif Instrucao == 'sw':
                    Aux = SW(Nome_Arquivo)
                elif Instrucao == 'sh':
                    Aux = SH(Nome_Arquivo)

                #Tipo B
                elif Instrucao == 'bne':
                    Aux = BNE(Nome_Arquivo)
                elif Instrucao == 'blt':
                    Aux = BLT(Nome_Arquivo)
                elif Instrucao == 'bge':
                    Aux = BGE(Nome_Arquivo)
                elif Instrucao == 'bltu':
                    Aux = BLTU(Nome_Arquivo)
                elif Instrucao == 'bgeu':
                    Aux = BGEU(Nome_Arquivo)

                else:
                    print("Instrução Invalida")

                #Escreve no Arquivo de saida a instrução em linguagem de Maquina
                Saida.write(Aux)
                Saida.write("\n")
