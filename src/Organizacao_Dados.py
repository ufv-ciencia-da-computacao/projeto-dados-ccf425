# -*- coding: utf-8 -*-
"""Organizacao_Dados_Trabalho_Prático.ipynb


Original file is located at
    https://colab.research.google.com/drive/14m_P0sv04jieV5AXqoQ32_DiqijnOeoy
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""# Organizando e entendendo dados de Horas-Aula
## 2016 - 2020
"""

ha16 = pd.read_excel("/content/horas_aula_2016.xlsX", index_col=False, header=None, squeeze=True)
ha16

ha16New = ha16
ha16New.columns = ha16.iloc[8]
ha16New = ha16.drop(labels=[0,1,2,3,4,5,6,7,8,65821,65822,65823], axis=0)
ha16New = ha16New.replace("--", np.nan, regex=True)
ha16New.reset_index(drop=True, inplace=True)
ha16New

ha16New.dtypes

ha17 = pd.read_excel("/content/horas_aula_2017.xlsX", index_col=False, header=None, squeeze=True)
ha17

ha17New = ha17
ha17New.columns = ha16.iloc[8]
ha17New = ha17.drop(labels=[0,1,2,3,4,5,6,7,8,65855,65856,65857], axis=0)
ha17New = ha17New.replace("--", np.nan, regex=True)
ha17New.reset_index(drop=True, inplace=True)
ha17New

ha17New.dtypes

ha18 = pd.read_excel("/content/horas_aula_2018.xlsx", index_col=False, header=None, squeeze=True)
ha18

ha18New = ha18
ha18New.columns = ha17.iloc[8]
ha18New = ha18.drop(labels=[0,1,2,3,4,5,6,7,8,65781,65782,65783], axis=0)
ha18New = ha18New.replace("--", np.nan, regex=True)
ha18New.reset_index(drop=True, inplace=True)
ha18New

ha18New.dtypes

ha19 = pd.read_excel("/content/horas_aula_2019.xlsx", index_col=False, header=None, squeeze=True)
ha19

ha19New = ha19
ha19New.columns = ha17.iloc[8]
ha19New = ha19.drop(labels=[0,1,2,3,4,5,6,7,8,65696,65697,65698], axis=0)
ha19New = ha19New.replace("--", np.nan, regex=True)
ha19New.reset_index(drop=True, inplace=True)
ha19New

ha19New.dtypes

ha20 = pd.read_excel("/content/horas_aula_2020.xlsx", index_col=False, header=None, squeeze=True)
ha20

ha20New = ha20
ha20New.columns = ha17.iloc[8]
ha20New = ha20.drop(labels=[0,1,2,3,4,5,6,7,8,65640,65641,65642], axis=0)
ha20New = ha20New.replace("--", np.nan, regex=True)
ha20New.reset_index(drop=True, inplace=True)
ha20New

ha20New.dtypes

haTot = pd.concat([ha16New,ha17New,ha18New,ha19New,ha20New])
haTot

compression_opts = dict(method='zip',
                        archive_name='horas_aula_completo.csv')  
haTot.to_csv('out.zip', index=True,
          compression=compression_opts)

haTot.to_excel('out.xlsx', index=True)

"""# Organizando e entendendo Dados de Alunos por Turma
## 2016 - 2020
"""

at16 = pd.read_excel("/content/alunos_turma_2016.xlsx", index_col=False, header=None, squeeze=True)
at16

at16New = at16
at16New.columns = at16.iloc[8]
at16New = at16.drop(labels=[0,1,2,3,4,5,6,7,8,66632,66633,66634], axis=0)
at16New = at16New.replace("--", np.nan, regex=True)
at16New.reset_index(drop=True, inplace=True)
at16New

at16New.dtypes

at17 = pd.read_excel("/content/alunos_turma_2017.xlsx", index_col=False, header=None, squeeze=True)
at17

at17New = at17
at17New.columns = at17.iloc[8]
at17New = at17.drop(labels=[0,1,2,3,4,5,6,7,8,66606,66607,66608], axis=0)
at17New = at17New.replace("--", np.nan, regex=True)
at17New.reset_index(drop=True, inplace=True)
at17New

at17New.dtypes

at18 = pd.read_excel("/content/alunos_turma_2018.xlsx", index_col=False, header=None, squeeze=True)
at18

at18New = at18
at18New.columns = at18.iloc[8]
at18New = at18.drop(labels=[0,1,2,3,4,5,6,7,8,66756,66757,66758], axis=0)
at18New = at18New.replace("--", np.nan, regex=True)
at18New.reset_index(drop=True, inplace=True)
at18New

at18New.dtypes

at19 = pd.read_excel("/content/alunos_turma_2019.xlsx", index_col=False, header=None, squeeze=True)
at19

at19New = at19
at19New.columns = at18.iloc[8]
at19New = at19.drop(labels=[0,1,2,3,4,5,6,7,8,66690,66691,66692], axis=0)
at19New = at19New.replace("--", np.nan, regex=True)
at19New.reset_index(drop=True, inplace=True)
at19New

at19New.dtypes

at20 = pd.read_excel("/content/alunos_turma_2020.xlsx", index_col=False, header=None, squeeze=True)
at20

at20New = at20
at20New.columns = at18.iloc[8]
at20New = at20.drop(labels=[0,1,2,3,4,5,6,7,8,66643,66644,66645], axis=0)
at20New = at20New.replace("--", np.nan, regex=True)
at20New.reset_index(drop=True, inplace=True)
at20New

at20New.dtypes

atTot = pd.concat([at16New,at17New,at18New,at19New,at20New])
atTot

compression_opts = dict(method='zip',
                        archive_name='alunos_turma_completo.csv')  
atTot.to_csv('out.zip', index=True,
          compression=compression_opts)

atTot.to_excel('out.xlsx', index=True)

"""# Organizando e entendendo Formação dos Docentes
## 2016 - 2020
"""

ds16 = pd.read_excel("/content/docentes_superior_2016.xlsx", index_col=False, header=None, squeeze=True)
ds16

ds16New = ds16
ds16New.columns = ds16.iloc[9]
ds16New = ds16New.drop(labels=[0,1,2,3,4,5,6,7,8,9], axis=0)
ds16New = ds16New[ds16New.index < 67828]
ds16New = ds16New.replace("--", np.nan, regex=True)
ds16New.reset_index(drop=True, inplace=True)
ds16New

ds16New.dtypes

ds17 = pd.read_excel("/content/docentes_superior_2017.xlsx", index_col=False, header=None, squeeze=True)
ds17

ds17New = ds17
ds17New.columns = ds17.iloc[9]
ds17New = ds17New.drop(labels=[0,1,2,3,4,5,6,7,8,9], axis=0)
ds17New = ds17New[ds17New.index < 67695]
ds17New = ds17New.replace("--", np.nan, regex=True)
ds17New.reset_index(drop=True, inplace=True)
ds17New

ds17New.dtypes

ds18 = pd.read_excel("/content/docentes_superior_2018.xlsx", index_col=False, header=None, squeeze=True)
ds18

ds18New = ds18
ds18New.columns = ds17.iloc[9]
ds18New = ds18New.drop(labels=[0,1,2,3,4,5,6,7,8,9], axis=0)
ds18New = ds18New[ds18New.index < 67662]
ds18New = ds18New.replace("--", np.nan, regex=True)
ds18New.reset_index(drop=True, inplace=True)
ds18New

ds18New.dtypes

ds19 = pd.read_excel("/content/docentes_superior_2019.xlsx", index_col=False, header=None, squeeze=True)
ds19

ds19New = ds19
ds19New.columns = ds17.iloc[9]
ds19New = ds19New.drop(labels=[0,1,2,3,4,5,6,7,8,9], axis=0)
ds19New = ds19New[ds19New.index < 67519]
ds19New = ds19New.replace("--", np.nan, regex=True)
ds19New.reset_index(drop=True, inplace=True)
ds19New

ds19New.dtypes

ds20 = pd.read_excel("/content/docentes_superior_2020.xlsx", index_col=False, header=None, squeeze=True)
ds20

ds20New = ds20
ds20New.columns = ds17.iloc[9]
ds20New = ds20New.drop(labels=[0,1,2,3,4,5,6,7,8,9], axis=0)
ds20New = ds20New[ds20New.index < 67457]
ds20New = ds20New.replace("--", np.nan, regex=True)
ds20New.reset_index(drop=True, inplace=True)
ds20New

ds20New.dtypes

dsTot = pd.concat([ds16New,ds17New,ds18New,ds19New,ds20New])
dsTot

compression_opts = dict(method='zip',
                        archive_name='docentes_superior_completo.csv')  
dsTot.to_csv('out.zip', index=True,
          compression=compression_opts)

dsTot.to_excel('out.xlsx', index=True)
