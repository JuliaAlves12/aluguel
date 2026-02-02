from django.db import models

class Usuario(models.Model):
    TIPO_CHOICES = [
        ('LOCADOR', 'Locador'),
        ('LOCATARIO', 'Locatário')
   ]
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    tipo = models.CharField(choices=TIPO_CHOICES)

    def __str__(self):
        return f"Nome: {self.nome}"
    
class Imovel(models.Model):
    STATUS_CHOICES = [
        ('DISPONIVEL', 'Disponivel'),
        ('ALUGADO', 'Alugado')
    ]
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    valor_aluguel = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    locador_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='imoveis')

    def __str__(self):
        return f"Imóvel: {self.titulo} -- Status: {self.status}"
    
class Contrato(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    imovel_id = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name="contratos")
    locador_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="contratos_locador")
    locatario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="contratos_locatario")

    def __str__(self):
        return f"Data Início: {self.data_inicio} -- Imóvel: {self.imovel_id} -- Locador: {self.locador_id} -- Locatário: {self.locatario_id}"
    
class Pagamento(models.Model):
    data_pagamento = models.DateField()
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.BooleanField()
    contrato_id = models.ForeignKey(Contrato, on_delete=models.CASCADE, related_name='pagamento')

    def __str__(self):
        return f"Data do Pagamento: {self.data_pagamento} -- Valor: R${self.valor}"


