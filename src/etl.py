import pandera as pa
from pandera.typing import Series

class MetricasFinanceirasBase(pa.DataFrameModel):
    setor_da_empresa: Series[str]
    receita_operacional: Series[float] = pa.Field(ge=0)
    data: Series[pa.DateTime] 
    percentual_de_imposto: Series[float] = pa.Field(in_range= {"min_value": 0, "max_value": 1})
    custo_operacionais: Series[float] = pa.Field(ge=0)