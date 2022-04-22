import os

class MaxHeap:
    def __init__(self):
        self.heap = [0]

    def put(self, item):
        self.heap.append(item)
        self.__floatUp(len(self.heap) - 1)

    def get(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        return False

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1: 
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        maior = index
        if len(self.heap) > left and self.heap[maior] < self.heap[left]:
            maior = left
        if len(self.heap) > right and self.heap[maior] < self.heap[right]:
            maior = right

        if maior != index:
            self.__swap(index, maior)
            self.__bubbleDown(maior)

class Paciente:
    def __init__(self):
        os.system("cls")
        self.patients = []
        self.prioridade = ()
        self.dados_paciente = ()
        self.contador = 999
        self.max_heap = MaxHeap()
        self.lista = []
        self.pacientes_chamados = []
   
    def _add_paciente(self, prioridade, nome_completo, tipo_sanguineo, data_nascimento):
        self.prioridade = prioridade
        self.dados_paciente = self.prioridade, self.contador, nome_completo, tipo_sanguineo, data_nascimento
        self.patients.append(self.dados_paciente)
        self.max_heap.put(self.prioridade)
        self.contador -= 1
        print("\nPaciente Adicionado!\n\n")

    def _mostrar_proximo_paciente(self):
        if not self.patients:
            print("Não há um próximo Paciente!")
        else:
            i = 0
            self.elemento = self.max_heap.get()
            self.lista.append(self.elemento)
            while len(self.lista) > 0:    
                if self.patients[i][0] == self.lista[0]:
                    print(f"Próximo Paciente: {self.patients[i]}")
                    break  
                elif len(self.patients) == 1:
                    print(self.patients[0])
                    break
                else:
                    i += 1

    def _chamar_proximo_paciente(self):
        if not self.patients:
            print("Não há nenhum Paciente para chamar!")
        else:
            i = 0
            self.elemento = self.max_heap.get()
            self.lista.append(self.elemento)
            while len(self.lista) > 0:    
                if self.patients[i][0] == self.lista[0]:
                    print(f"Paciente Chamado: {self.patients[i]}")
                    self.pacientes_chamados.append(self.patients[i])
                    self.lista.pop(0)
                    self.patients[i], self.patients[0] = self.patients[0], self.patients[i]
                    self.patients.pop(0)
                    break
                else:
                    i += 1
        
    def _mostrar_5_ultimos_pacientes(self):
        if len(self.patients) < 5:
            print(f"Último(s) Paciente(s) Chamado(s): {self.pacientes_chamados}")
        else:
            print(f"Últimos 5 Pacientes Chamados: {self.pacientes_chamados[-5]}")

patient = Paciente()

while True:    
    try:
        insertion = int(input('\n[1] Adicionar novo paciente\n[2] Chamar próximo paciente\n[3] Mostrar próximo paciente\n[4] Listar os 5 últimos chamados\nDIGITE O NUMERO DA OPÇÃO: '))
        os.system("cls")

        if insertion == 1:
            nome_completo = str(input("\nInforme o nome completo do paciente: "))

            print('Informe a grau da prioridade: 1 a 10')

            prioridade = int(input("Informe a prioridade: ")) 

            while prioridade < 1 or prioridade > 10:
                print("Prioridade Inválida!\n")
                prioridade = int(input("Informe a prioridade: "))
            
            tipo_sanguineo = str(input("Informe o tipo sanguíneo do paciente: ")) 
            data_nascimento = str(input("Informe a data de nascimento do paciente: "))
            patient._add_paciente(prioridade, nome_completo, tipo_sanguineo, data_nascimento)
        elif insertion == 2:
            patient._chamar_proximo_paciente()
        elif insertion == 3:
            patient._mostrar_proximo_paciente()
        elif insertion == 4:
            patient._mostrar_5_ultimos_pacientes()
        elif insertion == 5:
            break
        else:
            print("Opção inválida!")
    except ValueError:
        os.system("cls")
        print("O valor deve ser um número inteiro")