from django.db import models

# Create your models here.

class accessibility(models.Model):
    class Meta:
        verbose_name_plural = 'accessibility'
    year = models.IntegerField()
    Samuel_T = models.IntegerField()
    Mario_L = models.IntegerField()
    Jason_W = models.IntegerField()
    Kenny_H = models.IntegerField()
    Jean_Philippe_M = models.IntegerField()
    mattias = models.IntegerField()
    Halim_S = models.IntegerField()
    Cyril_B = models.IntegerField()
    Veli_Pekka_T = models.IntegerField()
    Sebastian_D = models.IntegerField()
    Frans_P = models.IntegerField()
    Andor_D = models.IntegerField()
    Sebastian_H = models.IntegerField()
    Jan_and_Bertil_Smark_N = models.IntegerField()
    Odd_Martin_B = models.IntegerField()
    Simon_B = models.IntegerField()
    Milan_Z = models.IntegerField()
    Nath = models.IntegerField()
    Daniel_D = models.IntegerField()
    Paul_G = models.IntegerField()
    Jude_D = models.IntegerField()
    Petra_R = models.IntegerField()
    Denis_B = models.IntegerField()
    Gaijin = models.IntegerField()
    Luke_Y = models.IntegerField()
    Boris_D = models.IntegerField()
    mike_cutie_and_m = models.IntegerField()
    Bill_C = models.IntegerField()
    Anthony_S = models.IntegerField()
    Christian_P = models.IntegerField()

    def __unicode__(self):
        return str(self.year)

    def getlist(self):
        return [self.year,self.Samuel_T,self.Mario_L,self.Jason_W,self.Kenny_H,self.Jean_Philippe_M,self.mattias,self.Halim_S,self.Cyril_B,self.Veli_Pekka_T,self.Sebastian_D,self.Frans_P,self.Andor_D,self.Sebastian_H,self.Jan_and_Bertil_Smark_N,self.Odd_Martin_B,self.Simon_B,self.Milan_Z,self.Nath,self.Daniel_D,self.Paul_G,self.Jude_D,self.Petra_R,self.Denis_B,self.Gaijin,self.Luke_Y,self.Boris_D,self.mike_cutie_and_m,self.Bill_C,self.Anthony_S,self.Christian_P]

    def getfields(self):
        return '"Samuel_T","Mario_L","Jason_W","Kenny_H","Jean_Philippe_M","mattias","Halim_S","Cyril_B","Veli_Pekka_T","Sebastian_D","Frans_P","Andor_D","Sebastian_H","Jan_and_Bertil_Smark_N","Odd_Martin_B","Simon_B","Milan_Z","Nath","Daniel_D","Paul_G","Jude_D","Petra_R","Denis_B","Gaijin","Luke_Y","Boris_D","mike_cutie_and_m","Bill_C","Anthony_S","Christian_P"'

class amd64(models.Model):
    class Meta:
        verbose_name_plural = 'amd64'
    year = models.IntegerField()
    Lennart_S = models.IntegerField()
    Goswin_von_B = models.IntegerField()
    Francesco_P = models.IntegerField()
    Kurt_R = models.IntegerField()
    Hans_J_U = models.IntegerField()
    Jo_S = models.IntegerField()
    Javier_K = models.IntegerField()
    Frederik_S = models.IntegerField()
    Harald_D = models.IntegerField()
    Hamish_M = models.IntegerField()
    Jean_Luc_C = models.IntegerField()
    Dean_H = models.IntegerField()
    Ron_J = models.IntegerField()
    Andreas_J = models.IntegerField()
    Jaime_Ochoa_M = models.IntegerField()
    Clive_M = models.IntegerField()
    Gudjon_I_G = models.IntegerField()
    Alex_S = models.IntegerField()
    John_G = models.IntegerField()
    hendrik_topoi_pooq_com = models.IntegerField()
    A_J_S = models.IntegerField()
    David_L = models.IntegerField()
    Giacomo_M = models.IntegerField()
    Bob_P = models.IntegerField()
    Stephen_F = models.IntegerField()
    Thomas_S = models.IntegerField()
    Jack_M = models.IntegerField()
    antongiulio05 = models.IntegerField()
    antonio_g = models.IntegerField()
    Paul_B = models.IntegerField()

    def __unicode__(self):
        return str(self.year)

    def getlist(self):
        return [self.year,self.Lennart_S,self.Goswin_von_B,self.Francesco_P,self.Kurt_R,self.Hans_J_U,self.Jo_S,self.Javier_K,self.Frederik_S,self.Harald_D,self.Hamish_M,self.Jean_Luc_C,self.Dean_H,self.Ron_J,self.Andreas_J,self.Jaime_Ochoa_M,self.Clive_M,self.Gudjon_I_G,self.Alex_S,self.John_G,self.hendrik_topoi_pooq_com,self.A_J_S,self.David_L,self.Giacomo_M,self.Bob_P,self.Stephen_F,self.Thomas_S,self.Jack_M,self.antongiulio05,self.antonio_g,self.Paul_B]

    def getfields(self):
        return '"Lennart_S","Goswin_von_B","Francesco_P","Kurt_R","Hans_J_U","Jo_S","Javier_K","Frederik_S","Harald_D","Hamish_M","Jean_Luc_C","Dean_H","Ron_J","Andreas_J","Jaime_Ochoa_M","Clive_M","Gudjon_I_G","Alex_S","John_G","hendrik_topoi_pooq_com","A_J_S","David_L","Giacomo_M","Bob_P","Stephen_F","Thomas_S","Jack_M","antongiulio05","antonio_g","Paul_B"'

class teammetrics_discuss(models.Model):
    class Meta:
        verbose_name_plural = 'teammetrics_discuss'
    year = models.IntegerField()
    Sukhbir_S = models.IntegerField()
    Andreas_T = models.IntegerField()
    Alexander_W = models.IntegerField()
    Scott_H = models.IntegerField()
    Christian_P = models.IntegerField()
    Tollef_Fog_H = models.IntegerField()
    Cord_B = models.IntegerField()
    Martin_Z = models.IntegerField()
    Stephen_G = models.IntegerField()
    David_B = models.IntegerField()
    Ana_G = models.IntegerField()
    Charles_P = models.IntegerField()

    def __unicode__(self):
        return str(self.year)

    def getlist(self):
        return [self.year,self.Sukhbir_S,self.Andreas_T,self.Alexander_W,self.Scott_H,self.Christian_P,self.Tollef_Fog_H,self.Cord_B,self.Martin_Z,self.Stephen_G,self.David_B,self.Ana_G,self.Charles_P]

    def getfields(self):
        return '"Sukhbir_S","Andreas_T","Alexander_W","Scott_H","Christian_P","Tollef_Fog_H","Cord_B","Martin_Z","Stephen_G","David_B","Ana_G","Charles_P"'
