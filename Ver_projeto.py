from tkinter import font
import pandas as pd
import plotly.graph_objects as go
from csv import writer 
from csv import DictWriter 


arquivo_filtrado = pd.read_csv('nos_2_filtro.csv',sep=',',encoding='utf-8')

#titulacao = ['Graduacao','Mestrado','Especializacao','Doutorado','PosDoc','Não Informado']
#grande_area = {'Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
#                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros'}
#uf = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']

#=======================Quantidade de titulação total======================

linhas_Grad = arquivo_filtrado[arquivo_filtrado['titulacao'] == 'Graduacao']
linhas_Esp = arquivo_filtrado[arquivo_filtrado['titulacao'] == 'Especializacao']
linhas_Mes = arquivo_filtrado[arquivo_filtrado['titulacao'] == 'Mestrado']
linhas_Doc = arquivo_filtrado[arquivo_filtrado['titulacao'] == 'Doutorado']
linhas_Pos_Doc = arquivo_filtrado[arquivo_filtrado['titulacao'] == 'PosDoc']
linhas_Naoinformado = arquivo_filtrado[arquivo_filtrado['titulacao'] == 'Não informado']


#=======================Contador da titulação total=======================

Cont_Grad = len(linhas_Grad)
Cont_Esp = len(linhas_Esp)
Cont_Mes = len(linhas_Mes)
Cont_Doc = len(linhas_Doc)
Cont_Pos_Doc = len(linhas_Pos_Doc)
Cont_Naoinformado = len(linhas_Naoinformado)


#========================Quantidade de cada grande área====================

linhas_naoinf = arquivo_filtrado[arquivo_filtrado['grande_area'] == 'Não informado']
linhas_eng = arquivo_filtrado[arquivo_filtrado['grande_area'] == 'Engenharias']
linhas_ter = arquivo_filtrado[arquivo_filtrado['grande_area'] == 'Ciencias Exatas e da Terra']
linhas_sau = arquivo_filtrado[arquivo_filtrado['grande_area'] == 'Ciencias da Saude']
linhas_soc = arquivo_filtrado[arquivo_filtrado['grande_area'] == 'Ciencias Sociais Aplicadas']
linhas_bio = arquivo_filtrado[arquivo_filtrado['grande_area'] == 'Ciencias Biologicas']
linhas_agr = arquivo_filtrado[arquivo_filtrado['grande_area'] == 'Ciencias Agrarias']
linhas_hum = arquivo_filtrado[arquivo_filtrado['grande_area'] == 'Ciencias Humanas']
linhas_ling = arquivo_filtrado[arquivo_filtrado['grande_area'] == 'Linguistica; Letras e Artes']
linhas_out = arquivo_filtrado[arquivo_filtrado['grande_area'] == 'Outros']

Cont_linhas_naoinf = len(linhas_naoinf)
Cont_linhas_eng = len(linhas_eng)
Cont_linhas_ter = len(linhas_ter)
Cont_linhas_sau = len(linhas_sau)
Cont_linhas_soc = len(linhas_soc)
Cont_linhas_bio = len(linhas_bio)
Cont_linhas_agr = len(linhas_agr)
Cont_linhas_hum = len(linhas_hum)
Cont_linhas_ling = len(linhas_ling)
Cont_linhas_out = len(linhas_out)


#===================Contador titulação por grande área=======================


#Não informado
Cont_NaoInf_Doc    = len(linhas_naoinf[linhas_naoinf['titulacao']=="Doutorado"])
Cont_NaoInf_PosDoc = len(linhas_naoinf[linhas_naoinf['titulacao']=="PosDoc"])
Cont_NaoInf_Mes    = len(linhas_naoinf[linhas_naoinf['titulacao']=="Mestrado"])
Cont_NaoInf_Grad   = len(linhas_naoinf[linhas_naoinf['titulacao']=="Graduacao"])
Cont_NaoInf_Esp    = len(linhas_naoinf[linhas_naoinf['titulacao']=="Especializacao"])
Cont_NaoInf_NaoInf = len(linhas_naoinf[linhas_naoinf['titulacao']=="Não informado"])

#Engenharia
Cont_Eng_Doc = len(linhas_eng[linhas_eng['titulacao']=="Doutorado"])
Cont_Eng_PosDoc = len(linhas_eng[linhas_eng['titulacao']=="PosDoc"])
Cont_Eng_Mes = len(linhas_eng[linhas_eng['titulacao']=="Mestrado"])
Cont_Eng_Gra = len(linhas_eng[linhas_eng['titulacao']=="Graduacao"])
Cont_Eng_Esp = len(linhas_eng[linhas_eng['titulacao']=="Especializacao"])
Cont_Eng_NaoInf = len(linhas_eng[linhas_eng['titulacao']=="Não informado"])

#Ciencias Exatas e da Terra
Cont_CienTer_Doc = len(linhas_ter[linhas_ter['titulacao']=="Doutorado"])
Cont_CienTer_PosDoc = len(linhas_ter[linhas_ter['titulacao']=="PosDoc"])
Cont_CienTer_Mes = len(linhas_ter[linhas_ter['titulacao']=="Mestrado"])
Cont_CienTer_Gra = len(linhas_ter[linhas_ter['titulacao']=="Graduacao"])
Cont_CienTer_Esp = len(linhas_ter[linhas_ter['titulacao']=="Especializacao"])
Cont_CienTer_NaoInf = len(linhas_ter[linhas_ter['titulacao']=="Não informado"])

#Ciencia da saude
Cont_CienSau_Doc = len(linhas_sau[linhas_sau['titulacao']=="Doutorado"])
Cont_CienSau_PosDoc = len(linhas_sau[linhas_sau['titulacao']=="PosDoc"])
Cont_CienSau_Mes = len(linhas_sau[linhas_sau['titulacao']=="Mestrado"])
Cont_CienSau_Gra = len(linhas_sau[linhas_sau['titulacao']=="Graduacao"])
Cont_CienSau_Esp = len(linhas_sau[linhas_sau['titulacao']=="Especializacao"])
Cont_CienSau_NaoInf = len(linhas_sau[linhas_sau['titulacao']=="Não informado"])

#Ciencias Sociais Aplicadas
Cont_CiencSoci_Doc = len(linhas_soc[linhas_soc['titulacao']=="Doutorado"])
Cont_CiencSoci_PosDoc = len(linhas_soc[linhas_soc['titulacao']=="PosDoc"])
Cont_CiencSoci_Mes = len(linhas_soc[linhas_soc['titulacao']=="Mestrado"])
Cont_CiencSoci_Gra = len(linhas_soc[linhas_soc['titulacao']=="Graduacao"])
Cont_CiencSoci_Esp = len(linhas_soc[linhas_soc['titulacao']=="Especializacao"])
Cont_CiencSoci_NaoInf = len(linhas_soc[linhas_soc['titulacao']=="Não informado"])


#CienciasBiologicas
Cont_CienBio_Doc = len(linhas_bio[linhas_bio['titulacao']=="Doutorado"])
Cont_CienBio_PosDoc = len(linhas_bio[linhas_bio['titulacao']=="PosDoc"])
Cont_CienBio_Mes = len(linhas_bio[linhas_bio['titulacao']=="Mestrado"])
Cont_CienBio_Gra = len(linhas_bio[linhas_bio['titulacao']=="Graduacao"])
Cont_CienBio_Esp = len(linhas_bio[linhas_bio['titulacao']=="Especializacao"])
Cont_CienBio_NaoInf = len(linhas_bio[linhas_bio['titulacao']=="Não informado"])

#Ciencias Agrarias
Cont_CienAgr_Doc = len(linhas_agr[linhas_agr['titulacao']=="Doutorado"])
Cont_CienAgr_PosDoc = len(linhas_agr[linhas_agr['titulacao']=="PosDoc"])
Cont_CienAgr_Mes = len(linhas_agr[linhas_agr['titulacao']=="Mestrado"])
Cont_CienAgr_Gra = len(linhas_agr[linhas_agr['titulacao']=="Graduacao"])
Cont_CienAgr_Esp = len(linhas_agr[linhas_agr['titulacao']=="Especializacao"])
Cont_CienAgr_NaoInf = len(linhas_agr[linhas_agr['titulacao']=="Não informado"])

#Ciencias Humanas
Cont_CienHu_Doc = len(linhas_hum[linhas_hum['titulacao']=="Doutorado"])
Cont_CienHu_PosDoc = len(linhas_hum[linhas_hum['titulacao']=="PosDoc"])
Cont_CienHu_Mes = len(linhas_hum[linhas_hum['titulacao']=="Mestrado"])
Cont_CienHu_Gra = len(linhas_hum[linhas_hum['titulacao']=="Graduacao"])
Cont_CienHu_Esp = len(linhas_hum[linhas_hum['titulacao']=="Especializacao"])
Cont_CienHu_NaoInf = len(linhas_hum[linhas_hum['titulacao']=="Não informado"])


#Linguistica, Letras e Artes
Cont_LinLetAr_Doc = len(linhas_ling[linhas_ling['titulacao']=="Doutorado"])
Cont_LinLetAr_PosDoc = len(linhas_ling[linhas_ling['titulacao']=="PosDoc"])
Cont_LinLetAr_Mes = len(linhas_ling[linhas_ling['titulacao']=="Mestrado"])
Cont_LinLetAr_Gra = len(linhas_ling[linhas_ling['titulacao']=="Graduacao"])
Cont_LinLetAr_Esp = len(linhas_ling[linhas_ling['titulacao']=="Especializacao"])
Cont_LinLetAr_NaoInf = len(linhas_ling[linhas_ling['titulacao']=="Não informado"])

#Outros
Cont_Out_Doc = len(linhas_out[linhas_out['titulacao']=="Doutorado"])
Cont_Out_PosDoc = len(linhas_out[linhas_out['titulacao']=="PosDoc"])
Cont_Out_Mes = len(linhas_out[linhas_out['titulacao']=="Mestrado"])
Cont_Out_Gra = len(linhas_out[linhas_out['titulacao']=="Graduacao"])
Cont_Out_Esp = len(linhas_out[linhas_out['titulacao']=="Especializacao"])
Cont_Out_NaoInf = len(linhas_out[linhas_out['titulacao']=="Não informado"])


#===================Contador grande área por UF======================

#AC

linhas_naoinf_AC = linhas_naoinf[linhas_naoinf['uf']=='AC']
linhas_eng_AC = linhas_eng[linhas_eng['uf']=='AC']
linhas_ter_AC = linhas_ter[linhas_ter['uf']=='AC']
linhas_sau_AC = linhas_sau[linhas_sau['uf']=='AC']
linhas_soc_AC = linhas_soc[linhas_soc['uf']=='AC']
linhas_bio_AC = linhas_bio[linhas_bio['uf']=='AC']
linhas_agr_AC = linhas_agr[linhas_agr['uf']=='AC']
linhas_hum_AC = linhas_hum[linhas_hum['uf']=='AC']
linhas_ling_AC = linhas_ling[linhas_ling['uf']=='AC']
linhas_out_AC = linhas_out[linhas_out['uf']=='AC']


Cont_naoinf_AC = len(linhas_naoinf_AC)
Cont_eng_AC = len(linhas_eng_AC)
Cont_ter_AC = len(linhas_ter_AC)
Cont_sau_AC = len(linhas_sau_AC)
Cont_soc_AC = len(linhas_soc_AC)
Cont_bio_AC = len(linhas_bio_AC)
Cont_agr_AC = len(linhas_agr_AC)
Cont_hum_AC = len(linhas_hum_AC)
Cont_ling_AC = len(linhas_ling_AC)
Cont_out_AC = len(linhas_out_AC)

#AL

linhas_naoinf_AL = linhas_naoinf[linhas_naoinf['uf']=='AL']
linhas_eng_AL = linhas_eng [linhas_eng ['uf']=='AL']
linhas_ter_AL = linhas_ter [linhas_ter ['uf']=='AL']
linhas_sau_AL = linhas_sau [linhas_sau ['uf']=='AL']
linhas_soc_AL = linhas_soc [linhas_soc ['uf']=='AL']
linhas_bio_AL = linhas_bio [linhas_bio ['uf']=='AL']
linhas_agr_AL = linhas_agr [linhas_agr ['uf']=='AL']
linhas_hum_AL = linhas_hum [linhas_hum ['uf']=='AL']
linhas_ling_AL = linhas_ling[linhas_ling['uf']=='AL']
linhas_out_AL = linhas_out [linhas_out ['uf']=='AL']


Cont_naoinf_AL = len(linhas_naoinf_AL)
Cont_eng_AL = len(linhas_eng_AL)
Cont_ter_AL = len(linhas_ter_AL)
Cont_sau_AL = len(linhas_sau_AL)
Cont_soc_AL = len(linhas_soc_AL)
Cont_bio_AL = len(linhas_bio_AL)
Cont_agr_AL = len(linhas_agr_AL)
Cont_hum_AL = len(linhas_hum_AL)
Cont_ling_AL = len(linhas_ling_AL)
Cont_out_AL = len(linhas_out_AL)

#AP

linhas_naoinf_AP = linhas_naoinf[linhas_naoinf['uf']=='AP']
linhas_eng_AP = linhas_eng[linhas_eng['uf']=='AP']
linhas_ter_AP = linhas_ter[linhas_ter['uf']=='AP']
linhas_sau_AP = linhas_sau[linhas_sau['uf']=='AP']
linhas_soc_AP = linhas_soc[linhas_soc['uf']=='AP']
linhas_bio_AP = linhas_bio[linhas_bio['uf']=='AP']
linhas_agr_AP = linhas_agr[linhas_agr['uf']=='AP']
linhas_hum_AP = linhas_hum[linhas_hum['uf']=='AP']
linhas_ling_AP = linhas_ling[linhas_ling['uf']=='AP']
linhas_out_AP = linhas_out[linhas_out['uf']=='AP']


Cont_naoinf_AP = len(linhas_naoinf_AP)
Cont_eng_AP = len(linhas_eng_AP)
Cont_ter_AP = len(linhas_ter_AP)
Cont_sau_AP = len(linhas_sau_AP)
Cont_soc_AP = len(linhas_soc_AP)
Cont_bio_AP = len(linhas_bio_AP)
Cont_agr_AP = len(linhas_agr_AP)
Cont_hum_AP = len(linhas_hum_AP)
Cont_ling_AP = len(linhas_ling_AP)
Cont_out_AP = len(linhas_out_AP)


#AM

linhas_naoinf_AM = linhas_naoinf[linhas_naoinf['uf']=='AM']
linhas_eng_AM = linhas_eng[linhas_eng['uf']=='AM']
linhas_ter_AM = linhas_ter[linhas_ter['uf']=='AM']
linhas_sau_AM = linhas_sau[linhas_sau['uf']=='AM']
linhas_soc_AM = linhas_soc[linhas_soc['uf']=='AM']
linhas_bio_AM = linhas_bio[linhas_bio['uf']=='AM']
linhas_agr_AM = linhas_agr[linhas_agr['uf']=='AM']
linhas_hum_AM = linhas_hum[linhas_hum['uf']=='AM']
linhas_ling_AM = linhas_ling[linhas_ling['uf']=='AM']
linhas_out_AM = linhas_out[linhas_out['uf']=='AM']


Cont_naoinf_AM = len(linhas_naoinf_AM)
Cont_eng_AM = len(linhas_eng_AM)
Cont_ter_AM = len(linhas_ter_AM)
Cont_sau_AM = len(linhas_sau_AM)
Cont_soc_AM = len(linhas_soc_AM)
Cont_bio_AM = len(linhas_bio_AM)
Cont_agr_AM = len(linhas_agr_AM)
Cont_hum_AM = len(linhas_hum_AM)
Cont_ling_AM = len(linhas_ling_AM)
Cont_out_AM = len(linhas_out_AM)


#BA

linhas_naoinf_BA = linhas_naoinf[linhas_naoinf['uf']=='BA']
linhas_eng_BA = linhas_eng[linhas_eng['uf']=='BA']
linhas_ter_BA = linhas_ter[linhas_ter['uf']=='BA']
linhas_sau_BA = linhas_sau[linhas_sau['uf']=='BA']
linhas_soc_BA = linhas_soc[linhas_soc['uf']=='BA']
linhas_bio_BA = linhas_bio[linhas_bio['uf']=='BA']
linhas_agr_BA = linhas_agr[linhas_agr['uf']=='BA']
linhas_hum_BA = linhas_hum[linhas_hum['uf']=='BA']
linhas_ling_BA = linhas_ling[linhas_ling['uf']=='BA']
linhas_out_BA = linhas_out[linhas_out['uf']=='BA']


Cont_naoinf_BA = len(linhas_naoinf_BA)
Cont_eng_BA = len(linhas_eng_BA)
Cont_ter_BA = len(linhas_ter_BA)
Cont_sau_BA = len(linhas_sau_BA)
Cont_soc_BA = len(linhas_soc_BA)
Cont_bio_BA = len(linhas_bio_BA)
Cont_agr_BA = len(linhas_agr_BA)
Cont_hum_BA = len(linhas_hum_BA)
Cont_ling_BA = len(linhas_ling_BA)
Cont_out_BA = len(linhas_out_BA)

#CE

linhas_naoinf_CE = linhas_naoinf[linhas_naoinf['uf']=='CE']
linhas_eng_CE = linhas_eng[linhas_eng['uf']=='CE']
linhas_ter_CE = linhas_ter[linhas_ter['uf']=='CE']
linhas_sau_CE = linhas_sau[linhas_sau['uf']=='CE']
linhas_soc_CE = linhas_soc[linhas_soc['uf']=='CE']
linhas_bio_CE = linhas_bio[linhas_bio['uf']=='CE']
linhas_agr_CE = linhas_agr[linhas_agr['uf']=='CE']
linhas_hum_CE = linhas_hum[linhas_hum['uf']=='CE']
linhas_ling_CE = linhas_ling[linhas_ling['uf']=='CE']
linhas_out_CE = linhas_out[linhas_out['uf']=='CE']


Cont_naoinf_CE = len(linhas_naoinf_CE)
Cont_eng_CE = len(linhas_eng_CE)
Cont_ter_CE = len(linhas_ter_CE)
Cont_sau_CE = len(linhas_sau_CE)
Cont_soc_CE = len(linhas_soc_CE)
Cont_bio_CE = len(linhas_bio_CE)
Cont_agr_CE = len(linhas_agr_CE)
Cont_hum_CE = len(linhas_hum_CE)
Cont_ling_CE = len(linhas_ling_CE)
Cont_out_CE = len(linhas_out_CE)

#ES

linhas_naoinf_ES = linhas_naoinf[linhas_naoinf['uf']=='ES']
linhas_eng_ES = linhas_eng[linhas_eng['uf']=='ES']
linhas_ter_ES = linhas_ter[linhas_ter['uf']=='ES']
linhas_sau_ES = linhas_sau[linhas_sau['uf']=='ES']
linhas_soc_ES = linhas_soc[linhas_soc['uf']=='ES']
linhas_bio_ES = linhas_bio[linhas_bio['uf']=='ES']
linhas_agr_ES = linhas_agr[linhas_agr['uf']=='ES']
linhas_hum_ES = linhas_hum[linhas_hum['uf']=='ES']
linhas_ling_ES = linhas_ling[linhas_ling['uf']=='ES']
linhas_out_ES = linhas_out[linhas_out['uf']=='ES']


Cont_naoinf_ES = len(linhas_naoinf_ES)
Cont_eng_ES = len(linhas_eng_ES)
Cont_ter_ES = len(linhas_ter_ES)
Cont_sau_ES = len(linhas_sau_ES)
Cont_soc_ES = len(linhas_soc_ES)
Cont_bio_ES = len(linhas_bio_ES)
Cont_agr_ES = len(linhas_agr_ES)
Cont_hum_ES = len(linhas_hum_ES)
Cont_ling_ES = len(linhas_ling_ES)
Cont_out_ES = len(linhas_out_ES)

#GO

linhas_naoinf_GO = linhas_naoinf[linhas_naoinf['uf']=='GO']
linhas_eng_GO = linhas_eng[linhas_eng['uf']=='GO']
linhas_ter_GO = linhas_ter[linhas_ter['uf']=='GO']
linhas_sau_GO = linhas_sau[linhas_sau['uf']=='GO']
linhas_soc_GO = linhas_soc[linhas_soc['uf']=='GO']
linhas_bio_GO = linhas_bio[linhas_bio['uf']=='GO']
linhas_agr_GO = linhas_agr[linhas_agr['uf']=='GO']
linhas_hum_GO = linhas_hum[linhas_hum['uf']=='GO']
linhas_ling_GO = linhas_ling[linhas_ling['uf']=='GO']
linhas_out_GO = linhas_out[linhas_out['uf']=='GO']


Cont_naoinf_GO = len(linhas_naoinf_GO)
Cont_eng_GO = len(linhas_eng_GO)
Cont_ter_GO = len(linhas_ter_GO)
Cont_sau_GO = len(linhas_sau_GO)
Cont_soc_GO = len(linhas_soc_GO)
Cont_bio_GO = len(linhas_bio_GO)
Cont_agr_GO = len(linhas_agr_GO)
Cont_hum_GO = len(linhas_hum_GO)
Cont_ling_GO = len(linhas_ling_GO)
Cont_out_GO = len(linhas_out_GO)

#MA

linhas_naoinf_MA = linhas_naoinf[linhas_naoinf['uf']=='MA']
linhas_eng_MA = linhas_eng[linhas_eng['uf']=='MA']
linhas_ter_MA = linhas_ter[linhas_ter['uf']=='MA']
linhas_sau_MA = linhas_sau[linhas_sau['uf']=='MA']
linhas_soc_MA = linhas_soc[linhas_soc['uf']=='MA']
linhas_bio_MA = linhas_bio[linhas_bio['uf']=='MA']
linhas_agr_MA = linhas_agr[linhas_agr['uf']=='MA']
linhas_hum_MA = linhas_hum[linhas_hum['uf']=='MA']
linhas_ling_MA = linhas_ling[linhas_ling['uf']=='MA']
linhas_out_MA = linhas_out[linhas_out['uf']=='MA']


Cont_naoinf_MA = len(linhas_naoinf_MA)
Cont_eng_MA = len(linhas_eng_MA)
Cont_ter_MA = len(linhas_ter_MA)
Cont_sau_MA = len(linhas_sau_MA)
Cont_soc_MA = len(linhas_soc_MA)
Cont_bio_MA = len(linhas_bio_MA)
Cont_agr_MA = len(linhas_agr_MA)
Cont_hum_MA = len(linhas_hum_MA)
Cont_ling_MA = len(linhas_ling_MA)
Cont_out_MA = len(linhas_out_MA)

#MT

linhas_naoinf_MT = linhas_naoinf[linhas_naoinf['uf']=='MT']
linhas_eng_MT = linhas_eng[linhas_eng['uf']=='MT']
linhas_ter_MT = linhas_ter[linhas_ter['uf']=='MT']
linhas_sau_MT = linhas_sau[linhas_sau['uf']=='MT']
linhas_soc_MT = linhas_soc[linhas_soc['uf']=='MT']
linhas_bio_MT = linhas_bio[linhas_bio['uf']=='MT']
linhas_agr_MT = linhas_agr[linhas_agr['uf']=='MT']
linhas_hum_MT = linhas_hum[linhas_hum['uf']=='MT']
linhas_ling_MT = linhas_ling[linhas_ling['uf']=='MT']
linhas_out_MT = linhas_out[linhas_out['uf']=='MT']


Cont_naoinf_MT = len(linhas_naoinf_MT)
Cont_eng_MT = len(linhas_eng_MT)
Cont_ter_MT = len(linhas_ter_MT)
Cont_sau_MT = len(linhas_sau_MT)
Cont_soc_MT = len(linhas_soc_MT)
Cont_bio_MT = len(linhas_bio_MT)
Cont_agr_MT = len(linhas_agr_MT)
Cont_hum_MT = len(linhas_hum_MT)
Cont_ling_MT = len(linhas_ling_MT)
Cont_out_MT = len(linhas_out_MT)

#MS

linhas_naoinf_MS = linhas_naoinf[linhas_naoinf['uf']=='MS']
linhas_eng_MS = linhas_eng[linhas_eng['uf']=='MS']
linhas_ter_MS = linhas_ter[linhas_ter['uf']=='MS']
linhas_sau_MS = linhas_sau[linhas_sau['uf']=='MS']
linhas_soc_MS = linhas_soc[linhas_soc['uf']=='MS']
linhas_bio_MS = linhas_bio[linhas_bio['uf']=='MS']
linhas_agr_MS = linhas_agr[linhas_agr['uf']=='MS']
linhas_hum_MS = linhas_hum[linhas_hum['uf']=='MS']
linhas_ling_MS = linhas_ling[linhas_ling['uf']=='MS']
linhas_out_MS = linhas_out[linhas_out['uf']=='MS']


Cont_naoinf_MS = len(linhas_naoinf_MS)
Cont_eng_MS = len(linhas_eng_MS)
Cont_ter_MS = len(linhas_ter_MS)
Cont_sau_MS = len(linhas_sau_MS)
Cont_soc_MS = len(linhas_soc_MS)
Cont_bio_MS = len(linhas_bio_MS)
Cont_agr_MS = len(linhas_agr_MS)
Cont_hum_MS = len(linhas_hum_MS)
Cont_ling_MS = len(linhas_ling_MS)
Cont_out_MS = len(linhas_out_MS)

#MG

linhas_naoinf_MG = linhas_naoinf[linhas_naoinf['uf']=='MG']
linhas_eng_MG = linhas_eng[linhas_eng['uf']=='MG']
linhas_ter_MG = linhas_ter[linhas_ter['uf']=='MG']
linhas_sau_MG = linhas_sau[linhas_sau['uf']=='MG']
linhas_soc_MG = linhas_soc[linhas_soc['uf']=='MG']
linhas_bio_MG = linhas_bio[linhas_bio['uf']=='MG']
linhas_agr_MG = linhas_agr[linhas_agr['uf']=='MG']
linhas_hum_MG = linhas_hum[linhas_hum['uf']=='MG']
linhas_ling_MG = linhas_ling[linhas_ling['uf']=='MG']
linhas_out_MG = linhas_out[linhas_out['uf']=='MG']


Cont_naoinf_MG = len(linhas_naoinf_MG)
Cont_eng_MG = len(linhas_eng_MG)
Cont_ter_MG = len(linhas_ter_MG)
Cont_sau_MG = len(linhas_sau_MG)
Cont_soc_MG = len(linhas_soc_MG)
Cont_bio_MG = len(linhas_bio_MG)
Cont_agr_MG = len(linhas_agr_MG)
Cont_hum_MG = len(linhas_hum_MG)
Cont_ling_MG = len(linhas_ling_MG)
Cont_out_MG = len(linhas_out_MG)

#PA

linhas_naoinf_PA = linhas_naoinf[linhas_naoinf['uf']=='PA']
linhas_eng_PA = linhas_eng[linhas_eng['uf']=='PA']
linhas_ter_PA = linhas_ter[linhas_ter['uf']=='PA']
linhas_sau_PA = linhas_sau[linhas_sau['uf']=='PA']
linhas_soc_PA = linhas_soc[linhas_soc['uf']=='PA']
linhas_bio_PA = linhas_bio[linhas_bio['uf']=='PA']
linhas_agr_PA = linhas_agr[linhas_agr['uf']=='PA']
linhas_hum_PA = linhas_hum[linhas_hum['uf']=='PA']
linhas_ling_PA = linhas_ling[linhas_ling['uf']=='PA']
linhas_out_PA = linhas_out[linhas_out['uf']=='PA']


Cont_naoinf_PA = len(linhas_naoinf_PA)
Cont_eng_PA = len(linhas_eng_PA)
Cont_ter_PA = len(linhas_ter_PA)
Cont_sau_PA = len(linhas_sau_PA)
Cont_soc_PA = len(linhas_soc_PA)
Cont_bio_PA = len(linhas_bio_PA)
Cont_agr_PA = len(linhas_agr_PA)
Cont_hum_PA = len(linhas_hum_PA)
Cont_ling_PA = len(linhas_ling_PA)
Cont_out_PA = len(linhas_out_PA)

#PB

linhas_naoinf_PB = linhas_naoinf[linhas_naoinf['uf']=='PB']
linhas_eng_PB = linhas_eng[linhas_eng['uf']=='PB']
linhas_ter_PB = linhas_ter[linhas_ter['uf']=='PB']
linhas_sau_PB = linhas_sau[linhas_sau['uf']=='PB']
linhas_soc_PB = linhas_soc[linhas_soc['uf']=='PB']
linhas_bio_PB = linhas_bio[linhas_bio['uf']=='PB']
linhas_agr_PB = linhas_agr[linhas_agr['uf']=='PB']
linhas_hum_PB = linhas_hum[linhas_hum['uf']=='PB']
linhas_ling_PB = linhas_ling[linhas_ling['uf']=='PB']
linhas_out_PB = linhas_out[linhas_out['uf']=='PB']


Cont_naoinf_PB = len(linhas_naoinf_PB)
Cont_eng_PB = len(linhas_eng_PB)
Cont_ter_PB = len(linhas_ter_PB)
Cont_sau_PB = len(linhas_sau_PB)
Cont_soc_PB = len(linhas_soc_PB)
Cont_bio_PB = len(linhas_bio_PB)
Cont_agr_PB = len(linhas_agr_PB)
Cont_hum_PB = len(linhas_hum_PB)
Cont_ling_PB = len(linhas_ling_PB)
Cont_out_PB = len(linhas_out_PB)

#PR

linhas_naoinf_PR = linhas_naoinf[linhas_naoinf['uf']=='PR']
linhas_eng_PR = linhas_eng[linhas_eng['uf']=='PR']
linhas_ter_PR = linhas_ter[linhas_ter['uf']=='PR']
linhas_sau_PR = linhas_sau[linhas_sau['uf']=='PR']
linhas_soc_PR = linhas_soc[linhas_soc['uf']=='PR']
linhas_bio_PR = linhas_bio[linhas_bio['uf']=='PR']
linhas_agr_PR = linhas_agr[linhas_agr['uf']=='PR']
linhas_hum_PR = linhas_hum[linhas_hum['uf']=='PR']
linhas_ling_PR = linhas_ling[linhas_ling['uf']=='PR']
linhas_out_PR = linhas_out[linhas_out['uf']=='PR']


Cont_naoinf_PR = len(linhas_naoinf_PR)
Cont_eng_PR = len(linhas_eng_PR)
Cont_ter_PR = len(linhas_ter_PR)
Cont_sau_PR = len(linhas_sau_PR)
Cont_soc_PR = len(linhas_soc_PR)
Cont_bio_PR = len(linhas_bio_PR)
Cont_agr_PR = len(linhas_agr_PR)
Cont_hum_PR = len(linhas_hum_PR)
Cont_ling_PR = len(linhas_ling_PR)
Cont_out_PR = len(linhas_out_PR)

#PE

linhas_naoinf_PE = linhas_naoinf[linhas_naoinf['uf']=='PE']
linhas_eng_PE = linhas_eng[linhas_eng['uf']=='PE']
linhas_ter_PE = linhas_ter[linhas_ter['uf']=='PE']
linhas_sau_PE = linhas_sau[linhas_sau['uf']=='PE']
linhas_soc_PE = linhas_soc[linhas_soc['uf']=='PE']
linhas_bio_PE = linhas_bio[linhas_bio['uf']=='PE']
linhas_agr_PE = linhas_agr[linhas_agr['uf']=='PE']
linhas_hum_PE = linhas_hum[linhas_hum['uf']=='PE']
linhas_ling_PE = linhas_ling[linhas_ling['uf']=='PE']
linhas_out_PE = linhas_out[linhas_out['uf']=='PE']


Cont_naoinf_PE = len(linhas_naoinf_PE)
Cont_eng_PE = len(linhas_eng_PE)
Cont_ter_PE = len(linhas_ter_PE)
Cont_sau_PE = len(linhas_sau_PE)
Cont_soc_PE = len(linhas_soc_PE)
Cont_bio_PE = len(linhas_bio_PE)
Cont_agr_PE = len(linhas_agr_PE)
Cont_hum_PE = len(linhas_hum_PE)
Cont_ling_PE = len(linhas_ling_PE)
Cont_out_PE = len(linhas_out_PE)

#PI

linhas_naoinf_PI = linhas_naoinf[linhas_naoinf['uf']=='PI']
linhas_eng_PI = linhas_eng[linhas_eng['uf']=='PI']
linhas_ter_PI = linhas_ter[linhas_ter['uf']=='PI']
linhas_sau_PI = linhas_sau[linhas_sau['uf']=='PI']
linhas_soc_PI = linhas_soc[linhas_soc['uf']=='PI']
linhas_bio_PI = linhas_bio[linhas_bio['uf']=='PI']
linhas_agr_PI = linhas_agr[linhas_agr['uf']=='PI']
linhas_hum_PI = linhas_hum[linhas_hum['uf']=='PI']
linhas_ling_PI = linhas_ling[linhas_ling['uf']=='PI']
linhas_out_PI = linhas_out[linhas_out['uf']=='API']


Cont_naoinf_PI = len(linhas_naoinf_PI)
Cont_eng_PI = len(linhas_eng_PI)
Cont_ter_PI = len(linhas_ter_PI)
Cont_sau_PI = len(linhas_sau_PI)
Cont_soc_PI = len(linhas_soc_PI)
Cont_bio_PI = len(linhas_bio_PI)
Cont_agr_PI = len(linhas_agr_PI)
Cont_hum_PI = len(linhas_hum_PI)
Cont_ling_PI = len(linhas_ling_PI)
Cont_out_PI = len(linhas_out_PI)

#RJ

linhas_naoinf_RJ = linhas_naoinf[linhas_naoinf['uf']=='RJ']
linhas_eng_RJ = linhas_eng[linhas_eng['uf']=='RJ']
linhas_ter_RJ = linhas_ter[linhas_ter['uf']=='RJ']
linhas_sau_RJ = linhas_sau[linhas_sau['uf']=='RJ']
linhas_soc_RJ = linhas_soc[linhas_soc['uf']=='RJ']
linhas_bio_RJ = linhas_bio[linhas_bio['uf']=='RJ']
linhas_agr_RJ = linhas_agr[linhas_agr['uf']=='RJ']
linhas_hum_RJ = linhas_hum[linhas_hum['uf']=='RJ']
linhas_ling_RJ = linhas_ling[linhas_ling['uf']=='RJ']
linhas_out_RJ = linhas_out[linhas_out['uf']=='RJ']


Cont_naoinf_RJ = len(linhas_naoinf_RJ)
Cont_eng_RJ = len(linhas_eng_RJ)
Cont_ter_RJ = len(linhas_ter_RJ)
Cont_sau_RJ = len(linhas_sau_RJ)
Cont_soc_RJ = len(linhas_soc_RJ)
Cont_bio_RJ = len(linhas_bio_RJ)
Cont_agr_RJ = len(linhas_agr_RJ)
Cont_hum_RJ = len(linhas_hum_RJ)
Cont_ling_RJ = len(linhas_ling_RJ)
Cont_out_RJ = len(linhas_out_RJ)

#RN

linhas_naoinf_RN = linhas_naoinf[linhas_naoinf['uf']=='RN']
linhas_eng_RN = linhas_eng[linhas_eng['uf']=='RN']
linhas_ter_RN = linhas_ter[linhas_ter['uf']=='RN']
linhas_sau_RN = linhas_sau[linhas_sau['uf']=='RN']
linhas_soc_RN = linhas_soc[linhas_soc['uf']=='RN']
linhas_bio_RN = linhas_bio[linhas_bio['uf']=='RN']
linhas_agr_RN = linhas_agr[linhas_agr['uf']=='RN']
linhas_hum_RN = linhas_hum[linhas_hum['uf']=='RN']
linhas_ling_RN = linhas_ling[linhas_ling['uf']=='RN']
linhas_out_RN = linhas_out[linhas_out['uf']=='RN']


Cont_naoinf_RN = len(linhas_naoinf_RN)
Cont_eng_RN = len(linhas_eng_RN)
Cont_ter_RN = len(linhas_ter_RN)
Cont_sau_RN = len(linhas_sau_RN)
Cont_soc_RN = len(linhas_soc_RN)
Cont_bio_RN = len(linhas_bio_RN)
Cont_agr_RN = len(linhas_agr_RN)
Cont_hum_RN = len(linhas_hum_RN)
Cont_ling_RN = len(linhas_ling_RN)
Cont_out_RN = len(linhas_out_RN)

#RS

linhas_naoinf_RS = linhas_naoinf[linhas_naoinf['uf']=='RS']
linhas_eng_RS = linhas_eng[linhas_eng['uf']=='RS']
linhas_ter_RS = linhas_ter[linhas_ter['uf']=='RS']
linhas_sau_RS = linhas_sau[linhas_sau['uf']=='RS']
linhas_soc_RS = linhas_soc[linhas_soc['uf']=='RS']
linhas_bio_RS = linhas_bio[linhas_bio['uf']=='RS']
linhas_agr_RS = linhas_agr[linhas_agr['uf']=='RS']
linhas_hum_RS = linhas_hum[linhas_hum['uf']=='RS']
linhas_ling_RS = linhas_ling[linhas_ling['uf']=='RS']
linhas_out_RS = linhas_out[linhas_out['uf']=='RS']


Cont_naoinf_RS = len(linhas_naoinf_RS)
Cont_eng_RS = len(linhas_eng_RS)
Cont_ter_RS = len(linhas_ter_RS)
Cont_sau_RS = len(linhas_sau_RS)
Cont_soc_RS = len(linhas_soc_RS)
Cont_bio_RS = len(linhas_bio_RS)
Cont_agr_RS = len(linhas_agr_RS)
Cont_hum_RS = len(linhas_hum_RS)
Cont_ling_RS = len(linhas_ling_RS)
Cont_out_RS = len(linhas_out_RS)

#RO

linhas_naoinf_RO = linhas_naoinf[linhas_naoinf['uf']=='RO']
linhas_eng_RO = linhas_eng[linhas_eng['uf']=='RO']
linhas_ter_RO = linhas_ter[linhas_ter['uf']=='RO']
linhas_sau_RO = linhas_sau[linhas_sau['uf']=='RO']
linhas_soc_RO = linhas_soc[linhas_soc['uf']=='RO']
linhas_bio_RO = linhas_bio[linhas_bio['uf']=='RO']
linhas_agr_RO = linhas_agr[linhas_agr['uf']=='RO']
linhas_hum_RO = linhas_hum[linhas_hum['uf']=='RO']
linhas_ling_RO = linhas_ling[linhas_ling['uf']=='RO']
linhas_out_RO = linhas_out[linhas_out['uf']=='RO']


Cont_naoinf_RO = len(linhas_naoinf_RO)
Cont_eng_RO = len(linhas_eng_RO)
Cont_ter_RO = len(linhas_ter_RO)
Cont_sau_RO = len(linhas_sau_RO)
Cont_soc_RO = len(linhas_soc_RO)
Cont_bio_RO = len(linhas_bio_RO)
Cont_agr_RO = len(linhas_agr_RO)
Cont_hum_RO = len(linhas_hum_RO)
Cont_ling_RO = len(linhas_ling_RO)
Cont_out_RO = len(linhas_out_RO)

#RR

linhas_naoinf_RR = linhas_naoinf[linhas_naoinf['uf']=='RR']
linhas_eng_RR = linhas_eng[linhas_eng['uf']=='RR']
linhas_ter_RR = linhas_ter[linhas_ter['uf']=='RR']
linhas_sau_RR = linhas_sau[linhas_sau['uf']=='RR']
linhas_soc_RR = linhas_soc[linhas_soc['uf']=='RR']
linhas_bio_RR = linhas_bio[linhas_bio['uf']=='RR']
linhas_agr_RR = linhas_agr[linhas_agr['uf']=='RR']
linhas_hum_RR = linhas_hum[linhas_hum['uf']=='RR']
linhas_ling_RR = linhas_ling[linhas_ling['uf']=='RR']
linhas_out_RR = linhas_out[linhas_out['uf']=='RR']


Cont_naoinf_RR = len(linhas_naoinf_RR)
Cont_eng_RR = len(linhas_eng_RR)
Cont_ter_RR = len(linhas_ter_RR)
Cont_sau_RR = len(linhas_sau_RR)
Cont_soc_RR = len(linhas_soc_RR)
Cont_bio_RR = len(linhas_bio_RR)
Cont_agr_RR = len(linhas_agr_RR)
Cont_hum_RR = len(linhas_hum_RR)
Cont_ling_RR = len(linhas_ling_RR)
Cont_out_RR = len(linhas_out_RR)

#SC

linhas_naoinf_SC = linhas_naoinf[linhas_naoinf['uf']=='SC']
linhas_eng_SC = linhas_eng[linhas_eng['uf']=='SC']
linhas_ter_SC = linhas_ter[linhas_ter['uf']=='SC']
linhas_sau_SC = linhas_sau[linhas_sau['uf']=='SC']
linhas_soc_SC = linhas_soc[linhas_soc['uf']=='SC']
linhas_bio_SC = linhas_bio[linhas_bio['uf']=='SC']
linhas_agr_SC = linhas_agr[linhas_agr['uf']=='SC']
linhas_hum_SC = linhas_hum[linhas_hum['uf']=='SC']
linhas_ling_SC = linhas_ling[linhas_ling['uf']=='SC']
linhas_out_SC = linhas_out[linhas_out['uf']=='SC']


Cont_naoinf_SC = len(linhas_naoinf_SC)
Cont_eng_SC = len(linhas_eng_SC)
Cont_ter_SC = len(linhas_ter_SC)
Cont_sau_SC = len(linhas_sau_SC)
Cont_soc_SC = len(linhas_soc_SC)
Cont_bio_SC = len(linhas_bio_SC)
Cont_agr_SC = len(linhas_agr_SC)
Cont_hum_SC = len(linhas_hum_SC)
Cont_ling_SC = len(linhas_ling_SC)
Cont_out_SC = len(linhas_out_SC)

#SP

linhas_naoinf_SP = linhas_naoinf[linhas_naoinf['uf']=='SP']
linhas_eng_SP = linhas_eng[linhas_eng['uf']=='SP']
linhas_ter_SP = linhas_ter[linhas_ter['uf']=='SP']
linhas_sau_SP = linhas_sau[linhas_sau['uf']=='SP']
linhas_soc_SP = linhas_soc[linhas_soc['uf']=='SP']
linhas_bio_SP = linhas_bio[linhas_bio['uf']=='SP']
linhas_agr_SP = linhas_agr[linhas_agr['uf']=='SP']
linhas_hum_SP = linhas_hum[linhas_hum['uf']=='SP']
linhas_ling_SP = linhas_ling[linhas_ling['uf']=='SP']
linhas_out_SP = linhas_out[linhas_out['uf']=='SP']


Cont_naoinf_SP = len(linhas_naoinf_SP)
Cont_eng_SP = len(linhas_eng_SP)
Cont_ter_SP = len(linhas_ter_SP)
Cont_sau_SP = len(linhas_sau_SP)
Cont_soc_SP = len(linhas_soc_SP)
Cont_bio_SP = len(linhas_bio_SP)
Cont_agr_SP = len(linhas_agr_SP)
Cont_hum_SP = len(linhas_hum_SP)
Cont_ling_SP = len(linhas_ling_SP)
Cont_out_SP = len(linhas_out_SP)

#SE

linhas_naoinf_SE = linhas_naoinf[linhas_naoinf['uf']=='SE']
linhas_eng_SE = linhas_eng[linhas_eng['uf']=='SE']
linhas_ter_SE = linhas_ter[linhas_ter['uf']=='SE']
linhas_sau_SE = linhas_sau[linhas_sau['uf']=='SE']
linhas_soc_SE = linhas_soc[linhas_soc['uf']=='SE']
linhas_bio_SE = linhas_bio[linhas_bio['uf']=='SE']
linhas_agr_SE = linhas_agr[linhas_agr['uf']=='SE']
linhas_hum_SE = linhas_hum[linhas_hum['uf']=='SE']
linhas_ling_SE = linhas_ling[linhas_ling['uf']=='SE']
linhas_out_SE = linhas_out[linhas_out['uf']=='SE']


Cont_naoinf_SE = len(linhas_naoinf_SE)
Cont_eng_SE = len(linhas_eng_SE)
Cont_ter_SE = len(linhas_ter_SE)
Cont_sau_SE = len(linhas_sau_SE)
Cont_soc_SE = len(linhas_soc_SE)
Cont_bio_SE = len(linhas_bio_SE)
Cont_agr_SE = len(linhas_agr_SE)
Cont_hum_SE = len(linhas_hum_SE)
Cont_ling_SE = len(linhas_ling_SE)
Cont_out_SE = len(linhas_out_SE)


#TO

linhas_naoinf_TO = linhas_naoinf[linhas_naoinf['uf']=='TO']
linhas_eng_TO = linhas_eng[linhas_eng['uf']=='TO']
linhas_ter_TO = linhas_ter[linhas_ter['uf']=='TO']
linhas_sau_TO = linhas_sau[linhas_sau['uf']=='TO']
linhas_soc_TO = linhas_soc[linhas_soc['uf']=='TO']
linhas_bio_TO = linhas_bio[linhas_bio['uf']=='TO']
linhas_agr_TO = linhas_agr[linhas_agr['uf']=='TO']
linhas_hum_TO = linhas_hum[linhas_hum['uf']=='TO']
linhas_ling_TO = linhas_ling[linhas_ling['uf']=='TO']
linhas_out_TO = linhas_out[linhas_out['uf']=='TO']


Cont_naoinf_TO = len(linhas_naoinf_TO)
Cont_eng_TO = len(linhas_eng_TO)
Cont_ter_TO = len(linhas_ter_TO)
Cont_sau_TO = len(linhas_sau_TO)
Cont_soc_TO = len(linhas_soc_TO)
Cont_bio_TO = len(linhas_bio_TO)
Cont_agr_TO = len(linhas_agr_TO)
Cont_hum_TO = len(linhas_hum_TO)
Cont_ling_TO = len(linhas_ling_TO)
Cont_out_TO = len(linhas_out_TO)

#DF

linhas_naoinf_DF = linhas_naoinf[linhas_naoinf['uf']=='DF']
linhas_eng_DF = linhas_eng[linhas_eng['uf']=='DF']
linhas_ter_DF = linhas_ter[linhas_ter['uf']=='DF']
linhas_sau_DF = linhas_sau[linhas_sau['uf']=='DF']
linhas_soc_DF = linhas_soc[linhas_soc['uf']=='DF']
linhas_bio_DF = linhas_bio[linhas_bio['uf']=='DF']
linhas_agr_DF = linhas_agr[linhas_agr['uf']=='DF']
linhas_hum_DF = linhas_hum[linhas_hum['uf']=='DF']
linhas_ling_DF = linhas_ling[linhas_ling['uf']=='DF']
linhas_out_DF = linhas_out[linhas_out['uf']=='DF']


Cont_naoinf_DF = len(linhas_naoinf_DF)
Cont_eng_DF = len(linhas_eng_DF)
Cont_ter_DF = len(linhas_ter_DF)
Cont_sau_DF = len(linhas_sau_DF)
Cont_soc_DF = len(linhas_soc_DF)
Cont_bio_DF = len(linhas_bio_DF)
Cont_agr_DF = len(linhas_agr_DF)
Cont_hum_DF = len(linhas_hum_DF)
Cont_ling_DF = len(linhas_ling_DF)
Cont_out_DF = len(linhas_out_DF)





#abrir =  open('grande_area_uf.csv', 'a+', encoding='utf-8')
#
#linhas_uf_arquico = {'uf' : ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']}
#
#
#arquivo_linhas_uf = pd.DataFrame(linhas_uf_arquico)
#
#arquivo_linhas_uf.to_csv('grande_Area_uf.csv')
#
#
#===================Criar arquivo da Grande Área por UF=====================

linha_cabecalho =  ['UF','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']

with open('grande_area_uf.csv', 'a', encoding='utf-8') as f_object: 

    writer_object = writer(f_object) 

    writer_object.writerow(linha_cabecalho) 

    f_object.close()


field_names = ['UF','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']

dict={'UF':'AC','Não informado' : Cont_naoinf_AC,
        'Engenharias' : Cont_eng_AC,
        'Ciencias Exatas e da Terra' : Cont_ter_AC,
        'Ciencias da Saude' :Cont_sau_AC,
        'Ciencias Sociais Aplicadas' : Cont_soc_AC,
        'Ciencias Biologicas' : Cont_bio_AC,
        'Ciencias Agrarias' : Cont_agr_AC,
        'Ciencias Humanas' : Cont_hum_AC,
        'Linguistica, Letras e Artes' : Cont_ling_AC,
        'Outros' : Cont_out_AC} 



with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()


field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']

#AL
dict={'uf':'AL','Não informado' : Cont_naoinf_AL,
                'Engenharias' : Cont_eng_AL,
                'Ciencias Exatas e da Terra' : Cont_ter_AL,
                'Ciencias da Saude' :Cont_sau_AL,
                'Ciencias Sociais Aplicadas' : Cont_soc_AL,
                'Ciencias Biologicas' : Cont_bio_AL,
                'Ciencias Agrarias' : Cont_agr_AL,
                'Ciencias Humanas' : Cont_hum_AL,
                'Linguistica, Letras e Artes' : Cont_ling_AL,
                'Outros' : Cont_out_AL} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']



#AP
dict={'uf':'AP','Não informado' : Cont_naoinf_AP,
                'Engenharias' : Cont_eng_AP,
                'Ciencias Exatas e da Terra' : Cont_ter_AP ,
                'Ciencias da Saude' :Cont_sau_AP,
                'Ciencias Sociais Aplicadas' : Cont_soc_AP,
                'Ciencias Biologicas' : Cont_bio_AP,
                'Ciencias Agrarias' : Cont_agr_AP,
                'Ciencias Humanas' : Cont_hum_AP,
                'Linguistica, Letras e Artes' : Cont_ling_PA,
                'Outros' : Cont_out_AP} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']



#BA
dict={'uf':'BA','Não informado' : Cont_naoinf_BA,
                'Engenharias' : Cont_eng_BA,
                'Ciencias Exatas e da Terra' : Cont_ter_BA,
                'Ciencias da Saude' :Cont_sau_BA,
                'Ciencias Sociais Aplicadas' : Cont_soc_BA,
                'Ciencias Biologicas' : Cont_bio_BA,
                'Ciencias Agrarias' : Cont_agr_BA,
                'Ciencias Humanas' : Cont_hum_BA,
                'Linguistica, Letras e Artes' : Cont_ling_BA,
                'Outros' : Cont_out_BA} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']



#CE
dict={'uf':'CE','Não informado' : Cont_naoinf_CE,
                'Engenharias' : Cont_eng_CE,
                'Ciencias Exatas e da Terra' : Cont_ter_CE,
                'Ciencias da Saude' :Cont_sau_CE,
                'Ciencias Sociais Aplicadas' : Cont_soc_CE,
                'Ciencias Biologicas' : Cont_bio_CE,
                'Ciencias Agrarias' : Cont_agr_CE,
                'Ciencias Humanas' : Cont_hum_CE,
                'Linguistica, Letras e Artes' : Cont_ling_CE,
                'Outros' : Cont_out_CE} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']



#DF
dict={'uf':'DF','Não informado' : Cont_naoinf_DF,
                'Engenharias' : Cont_eng_DF ,
                'Ciencias Exatas e da Terra' : Cont_ter_DF ,
                'Ciencias da Saude' :Cont_sau_DF ,
                'Ciencias Sociais Aplicadas' : Cont_soc_DF,
                'Ciencias Biologicas' : Cont_bio_DF,
                'Ciencias Agrarias' : Cont_agr_DF,
                'Ciencias Humanas' : Cont_hum_DF,
                'Linguistica, Letras e Artes' : Cont_ling_DF,
                'Outros' : Cont_out_DF} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']



#ES
dict={'uf':'ES','Não informado' : Cont_naoinf_DF,
                'Engenharias' : Cont_eng_DF ,
                'Ciencias Exatas e da Terra' : Cont_ter_ES,
                'Ciencias da Saude' :Cont_sau_ES,
                'Ciencias Sociais Aplicadas' : Cont_soc_ES,
                'Ciencias Biologicas' : Cont_bio_ES,
                'Ciencias Agrarias' : Cont_agr_ES,
                'Ciencias Humanas' : Cont_hum_ES,
                'Linguistica, Letras e Artes' : Cont_ling_ES,
                'Outros' : Cont_out_ES} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']


#GO
dict={'uf':'GO','Não informado' : Cont_naoinf_GO,
                'Engenharias' : Cont_eng_GO,
                'Ciencias Exatas e da Terra' : Cont_ter_GO,
                'Ciencias da Saude' :Cont_sau_GO,
                'Ciencias Sociais Aplicadas' : Cont_soc_GO,
                'Ciencias Biologicas' : Cont_bio_GO,
                'Ciencias Agrarias' : Cont_agr_GO,
                'Ciencias Humanas' : Cont_hum_GO,
                'Linguistica, Letras e Artes' : Cont_ling_GO,
                'Outros' : Cont_out_GO} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']



#MA
dict={'uf':'MA','Não informado' : Cont_naoinf_MA,
                'Engenharias' : Cont_eng_MA,
                'Ciencias Exatas e da Terra' : Cont_ter_MA,
                'Ciencias da Saude' :Cont_sau_MA,
                'Ciencias Sociais Aplicadas' : Cont_soc_MA,
                'Ciencias Biologicas' : Cont_bio_MA,
                'Ciencias Agrarias' : Cont_agr_MA,
                'Ciencias Humanas' : Cont_hum_MA,
                'Linguistica, Letras e Artes' : Cont_ling_MA,
                'Outros' : Cont_out_MA} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']



#MT
dict={'uf':'MT','Não informado' : Cont_naoinf_MT,
                'Engenharias' : Cont_eng_MT,
                'Ciencias Exatas e da Terra' : Cont_ter_MT,
                'Ciencias da Saude' :Cont_sau_MT,
                'Ciencias Sociais Aplicadas' : Cont_soc_MT,
                'Ciencias Biologicas' : Cont_bio_MT,
                'Ciencias Agrarias' : Cont_agr_MT,
                'Ciencias Humanas' : Cont_hum_MT,
                'Linguistica, Letras e Artes' : Cont_ling_MT,
                'Outros' : Cont_out_MT} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']



#MS
dict={'uf':'MS','Não informado' : Cont_naoinf_MS,
                'Engenharias' : Cont_eng_MS,
                'Ciencias Exatas e da Terra' : Cont_ter_MS,
                'Ciencias da Saude' :Cont_sau_MS,
                'Ciencias Sociais Aplicadas' : Cont_soc_MS,
                'Ciencias Biologicas' : Cont_bio_MS,
                'Ciencias Agrarias' : Cont_agr_MS,
                'Ciencias Humanas' : Cont_hum_MS,
                'Linguistica, Letras e Artes' : Cont_ling_MS,
                'Outros' : Cont_out_MS} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']



#MG
dict={'uf':'MG','Não informado' : Cont_naoinf_MG,
                'Engenharias' : Cont_eng_MG,
                'Ciencias Exatas e da Terra' : Cont_ter_MG,
                'Ciencias da Saude' :Cont_sau_MG,
                'Ciencias Sociais Aplicadas' : Cont_soc_MG,
                'Ciencias Biologicas' : Cont_bio_MG,
                'Ciencias Agrarias' : Cont_agr_MG,
                'Ciencias Humanas' : Cont_hum_MG,
                'Linguistica, Letras e Artes' : Cont_ling_MG,
                'Outros' : Cont_out_MG} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']



#PA
dict={'uf':'PA','Não informado' : Cont_naoinf_PA,
                'Engenharias' : Cont_eng_PA,
                'Ciencias Exatas e da Terra' : Cont_ter_PA,
                'Ciencias da Saude' :Cont_sau_PA,
                'Ciencias Sociais Aplicadas' : Cont_soc_PA,
                'Ciencias Biologicas' : Cont_bio_PA,
                'Ciencias Agrarias' : Cont_agr_PA,
                'Ciencias Humanas' : Cont_hum_PA,
                'Linguistica, Letras e Artes' : Cont_ling_PA,
                'Outros' : Cont_out_PA} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']



#PB
dict={'uf':'PB','Não informado' : Cont_naoinf_PB,
                'Engenharias' : Cont_eng_PB,
                'Ciencias Exatas e da Terra' : Cont_ter_PB,
                'Ciencias da Saude' :Cont_sau_PB,
                'Ciencias Sociais Aplicadas' : Cont_soc_PB,
                'Ciencias Biologicas' : Cont_bio_PB,
                'Ciencias Agrarias' : Cont_agr_PB,
                'Ciencias Humanas' : Cont_hum_PB,
                'Linguistica, Letras e Artes' : Cont_ling_PB,
                'Outros' : Cont_out_PB} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']



#PR
dict={'uf':'PR','Não informado' : Cont_naoinf_PR,
                'Engenharias' : Cont_eng_PR,
                'Ciencias Exatas e da Terra' : Cont_ter_PR,
                'Ciencias da Saude' :Cont_sau_PR,
                'Ciencias Sociais Aplicadas' : Cont_soc_PR,
                'Ciencias Biologicas' : Cont_bio_PR,
                'Ciencias Agrarias' : Cont_agr_PR,
                'Ciencias Humanas' : Cont_hum_PR,
                'Linguistica, Letras e Artes' : Cont_ling_PR,
                'Outros' : Cont_out_PR} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']


#PE
dict={'uf':'PE','Não informado' : Cont_naoinf_PE,
                'Engenharias' : Cont_eng_PE,
                'Ciencias Exatas e da Terra' : Cont_ter_PE,
                'Ciencias da Saude' :Cont_sau_PE,
                'Ciencias Sociais Aplicadas' : Cont_soc_PE,
                'Ciencias Biologicas' : Cont_bio_PE,
                'Ciencias Agrarias' : Cont_agr_PE,
                'Ciencias Humanas' : Cont_hum_PE,
                'Linguistica, Letras e Artes' : Cont_ling_PE,
                'Outros' : Cont_out_PE} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']



#PI
dict={'uf':'PI','Não informado' : Cont_naoinf_PI,
                'Engenharias' : Cont_eng_PI,
                'Ciencias Exatas e da Terra' : Cont_ter_PI,
                'Ciencias da Saude' :Cont_sau_PI,
                'Ciencias Sociais Aplicadas' : Cont_soc_PI,
                'Ciencias Biologicas' : Cont_bio_PI,
                'Ciencias Agrarias' : Cont_agr_PI,
                'Ciencias Humanas' : Cont_hum_PI,
                'Linguistica, Letras e Artes' : Cont_ling_PI,
                'Outros' : Cont_out_PI} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']


#RJ
dict={'uf':'RJ','Não informado' : Cont_naoinf_RJ,
                'Engenharias' : Cont_eng_RJ,
                'Ciencias Exatas e da Terra' : Cont_ter_RJ,
                'Ciencias da Saude' :Cont_sau_RJ,
                'Ciencias Sociais Aplicadas' : Cont_soc_RJ,
                'Ciencias Biologicas' : Cont_bio_RJ,
                'Ciencias Agrarias' : Cont_agr_RJ,
                'Ciencias Humanas' : Cont_hum_RJ,
                'Linguistica, Letras e Artes' : Cont_ling_RJ,
                'Outros' : Cont_out_RJ} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']


#RN
dict={'uf':'RN','Não informado' : Cont_naoinf_RN,
                'Engenharias' : Cont_eng_RN,
                'Ciencias Exatas e da Terra' : Cont_ter_RN,
                'Ciencias da Saude' :Cont_sau_RN,
                'Ciencias Sociais Aplicadas' : Cont_soc_RN,
                'Ciencias Biologicas' : Cont_bio_RN,
                'Ciencias Agrarias' : Cont_agr_RN,
                'Ciencias Humanas' : Cont_hum_RN,
                'Linguistica, Letras e Artes' : Cont_ling_RN,
                'Outros' : Cont_out_RN} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']



#RS
dict={'uf':'RS','Não informado' : Cont_naoinf_RS,
                'Engenharias' : Cont_eng_RS,
                'Ciencias Exatas e da Terra' : Cont_ter_RS,
                'Ciencias da Saude' :Cont_sau_RS,
                'Ciencias Sociais Aplicadas' : Cont_soc_RS,
                'Ciencias Biologicas' : Cont_bio_RS,
                'Ciencias Agrarias' : Cont_agr_RS,
                'Ciencias Humanas' : Cont_hum_RS,
                'Linguistica, Letras e Artes' : Cont_ling_RS,
                'Outros' : Cont_out_RS} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']


#RO
dict={'uf':'RO','Não informado' : Cont_naoinf_RO,
                'Engenharias' : Cont_eng_RO,
                'Ciencias Exatas e da Terra' : Cont_ter_RO,
                'Ciencias da Saude' :Cont_sau_RO,
                'Ciencias Sociais Aplicadas' : Cont_soc_RO,
                'Ciencias Biologicas' : Cont_bio_RO,
                'Ciencias Agrarias' : Cont_agr_RO,
                'Ciencias Humanas' : Cont_hum_RO,
                'Linguistica, Letras e Artes' : Cont_ling_RO,
                'Outros' : Cont_out_RO} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']


#RR
dict={'uf':'RR','Não informado' : Cont_naoinf_RR,
                'Engenharias' : Cont_eng_RR,
                'Ciencias Exatas e da Terra' : Cont_ter_RR,
                'Ciencias da Saude' :Cont_sau_RR,
                'Ciencias Sociais Aplicadas' : Cont_soc_RR,
                'Ciencias Biologicas' : Cont_bio_RR,
                'Ciencias Agrarias' : Cont_agr_RR,
                'Ciencias Humanas' : Cont_hum_RR,
                'Linguistica, Letras e Artes' : Cont_ling_RR,
                'Outros' : Cont_out_RR} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']


#SC
dict={'uf':'SC','Não informado' : Cont_naoinf_SC,
                'Engenharias' : Cont_eng_SC,
                'Ciencias Exatas e da Terra' : Cont_ter_SC,
                'Ciencias da Saude' :Cont_sau_SC,
                'Ciencias Sociais Aplicadas' : Cont_soc_SC,
                'Ciencias Biologicas' : Cont_bio_SC,
                'Ciencias Agrarias' : Cont_agr_SC,
                'Ciencias Humanas' : Cont_hum_SC,
                'Linguistica, Letras e Artes' : Cont_ling_SC,
                'Outros' : Cont_out_SC} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']


#SP
dict={'uf':'SP','Não informado' : Cont_naoinf_SP,
                'Engenharias' : Cont_eng_SP,
                'Ciencias Exatas e da Terra' : Cont_ter_SP,
                'Ciencias da Saude' :Cont_sau_SP,
                'Ciencias Sociais Aplicadas' : Cont_soc_SP,
                'Ciencias Biologicas' : Cont_bio_SP,
                'Ciencias Agrarias' : Cont_agr_SP,
                'Ciencias Humanas' : Cont_hum_SP,
                'Linguistica, Letras e Artes' : Cont_ling_SP,
                'Outros' : Cont_out_SP} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']



#SE
dict={'uf':'SE','Não informado' : Cont_naoinf_SE,
                'Engenharias' : Cont_eng_SE,
                'Ciencias Exatas e da Terra' : Cont_ter_SE,
                'Ciencias da Saude' :Cont_sau_SE,
                'Ciencias Sociais Aplicadas' : Cont_soc_SE,
                'Ciencias Biologicas' : Cont_bio_SE,
                'Ciencias Agrarias' : Cont_agr_SE,
                'Ciencias Humanas' : Cont_hum_SE,
                'Linguistica, Letras e Artes' : Cont_ling_SE,
                'Outros' : Cont_out_SE} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']


#TO
dict={'uf':'TO','Não informado' : Cont_naoinf_TO,
                'Engenharias' : Cont_eng_TO ,
                'Ciencias Exatas e da Terra' : Cont_ter_TO ,
                'Ciencias da Saude' :Cont_sau_TO ,
                'Ciencias Sociais Aplicadas' : Cont_soc_TO,
                'Ciencias Biologicas' : Cont_bio_TO,
                'Ciencias Agrarias' : Cont_agr_TO,
                'Ciencias Humanas' : Cont_hum_TO,
                'Linguistica, Letras e Artes' : Cont_ling_TO,
                'Outros' : Cont_out_TO} 

with open('grande_area_uf.csv', 'a') as f_object: 
    
    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
    dictwriter_object.writerow(dict)
    
    f_object.close()
    field_names = ['uf','Não informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude','Ciencias Sociais Aplicadas',
                'Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas','Linguistica, Letras e Artes','Outros']


arquivo_grande_area = pd.read_csv("grande_area_uf.csv", sep=',', encoding='utf-8')

#tirar linhas vazias
for i in range(len(arquivo_grande_area)):
    if " " in arquivo_grande_area['UF'][i]:
        arquivo_grande_area = arquivo_grande_area.drop([i])

arquivo_grande_area.to_csv('grande_area_uf.csv', sep=',', encoding='utf-8',index=False)


'''
#=================Plot da Distribuição da Titulação=====================
labels_titulacao = ['Não Informado','Graduação','Especialização','Mestrado','Doutorado','Pós Doutorado']
values_titulacao = [Cont_Naoinformado,Cont_Grad,Cont_Esp,Cont_Mes,Cont_Doc,Cont_Pos_Doc]

figura_titulacao = go.Figure(data=[go.Pie(labels=labels_titulacao, values=values_titulacao)])
figura_titulacao.update_layout(title='Distribuição das Titulações no Brasil')
figura_titulacao.show()

#=================Plot da Distribuição das Grandes Áreas=====================
labels_grandes_areas = ['Não Informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude',
                'Ciencias Sociais Aplicadas','Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas',
                'Linguistica; Letras e Artes','Outros']
values_grandes_areas = [Cont_linhas_naoinf, Cont_linhas_eng, Cont_linhas_ter, Cont_linhas_sau, Cont_linhas_soc,
                Cont_linhas_bio, Cont_linhas_agr, Cont_linhas_hum, Cont_linhas_ling, Cont_linhas_out]

figura_grande_areas = go.Figure(data=[go.Pie(labels=labels_grandes_areas, values=values_grandes_areas)])
figura_grande_areas.update_layout(title='Distribuição das Grandes Áreas no Brasil')
figura_grande_areas.show()
'''

#=================Plot da Distribuição das Grandes Áreas por UF=====================
#labels_titulacao_grande_area = ['Não Informado','Engenharias','Ciencias Exatas e da Terra','Ciencias da Saude',
#                'Ciencias Sociais Aplicadas','Ciencias Biologicas','Ciencias Agrarias','Ciencias Humanas',
#                'Linguistica; Letras e Artes','Outros']
#values_titulacao_grande_area = []
#
#figura_titulacao_grande_area = go.Figure(data=[go.Pie(labels=labels_titulacao_grande_area, values=values_titulacao_grande_area)])
#figura_titulacao_grande_area.update_layout(title='Distribuição das Titulações por Grande Área')
#figura_titulacao_grande_area.show()
#
#
#x = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
#fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='Montreal'))
#fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Ottawa'))
#fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Toronto'))
#
#fig.update_layout(barmode='stack')
#fig.update_xaxes(categoryorder='category ascending')
#fig.show()




#========================Plot das Grandes Áreas por UF===============================
#labels_graduacao = ['Não Informado','Graduação','Especialização','Mestrado','Doutorado','Pós Doutorado']
#values_graduacao = []
#
#figura_graduacao = go.Figure(data=[go.Pie(labels=labels_graduacao, values=values_graduacao)])
#figura_graduacao.update_layout(title='Distribuição das Grandes Áreas no Brasil')
#figura_graduacao.show()





#fig = go.Figure(data=[go.Bar(
#    x = arquivo_grande_area['uf'],
#    y = arquivo_grande_area['Engenharias'],
#    width=[0.8, 0.8]
#)])
#
#fig.update_layout(title_text='Distribuição da Grande Área da Engenharia no Brasil')
#fig.show()