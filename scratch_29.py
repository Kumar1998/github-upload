#importing pandas as pd
import pandas as pd
data={"country":["Brazil","India","China"],"capital":["Brasillia","Newdelhi","Bejing"],"area":[8.516,17.10,9.597],
      "population":[200,1252,357]}
data_table=pd.DataFrame(data)
print(data_table)
