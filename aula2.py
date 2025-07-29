class Employee: #Employee é um tipo
    def __init__(self,name,salary): #Aqui há dois campos na classe: "name" e "salary", este metodo inicia um elemento da classe.
        self.name = name
        self.salary = salary
    def __str__(self): #Metodo que vai retornar uma determinada cadeia de caracteres.
        return self.name + ' recebe ' + str(self.salary)
    def proportional(self, days): #Função da classe que retorna o proporcional do salário aplicado aos dias trabalhados.
        return self.salary/30 * days


joao = Employee('Joao Grilo', 7500)

print(joao.name) #Agora é possível retornar os valores dos parâmetros do elemento pertencente à classe.
print(type(joao)) #O tipo de "joao" é a classe criada, "Employee".
print(str(joao))
print(joao.proportional(10))