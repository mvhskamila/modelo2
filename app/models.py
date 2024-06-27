from django.db import models

# Create your models here.
class tab_td(models.Model):
    data = models.DateField(auto_now_add=True,blank=True, null=True)
    placa = models.CharField(max_length=8, blank=True, null=True)
    motorista = models.CharField(max_length=30, blank=True, null=True)
    ajudante = models.CharField(max_length=30, blank=True, null=True)

    td = models.IntegerField(blank=True, null=True)
    km = models.IntegerField(default=0,blank=True, null=True) 
    cliente = models.CharField(max_length=30,blank=True, null=True)
    nota_1 = models.IntegerField(default=0,blank=True, null=True)  
    nota_2 = models.IntegerField(default=0,blank=True, null=True)  

    p2 = models.IntegerField(default=0,blank=True, null=True)  
    p5 = models.IntegerField(default=0,blank=True, null=True)  
    p8 = models.IntegerField(default=0,blank=True, null=True)  
    p13 = models.IntegerField(default=0,blank=True, null=True)  
    p20 = models.IntegerField(default=0,blank=True, null=True)  
    p45 = models.IntegerField(default=0,blank=True, null=True) 
     
    entrada = models.TimeField(blank=True, null=True)
    saida = models.TimeField(blank=True, null=True)
    OBS = models.CharField(max_length=254, blank=True, null=True)

    def __int__(self):
        
        return self.td


 


    


