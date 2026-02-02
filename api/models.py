from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=120)
    telefone = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return f"Nome: {self.nome} -- Email: {self.email} -- Telefone: {self.telefone}"
    
class Imovel(models.Model):
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    valor_aluguel = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(max_length=20)
    locador_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Imóvel: {self.titulo} -- Status: {self.status}"
    
class Contrato(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    imovel_id = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    locador_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="contratos_locador")
    locatario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="contratos_locatario")

    def __str__(self):
        return f"Data Início: {self.data_inicio} -- Imóvel: {self.imovel_id} -- Locador: {self.locador_id} -- Locatário: {self.locatario_id}"
    
class Pagamento(models.Model):
    data_pagamento = models.DateField()
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(max_length=20)
    contrato_id = models.ForeignKey(Contrato, on_delete=models.CASCADE)

    def __str__(self):
        return f"Data do Pagamento: {self.data_pagamento} -- Valor: R${self.valor}"


