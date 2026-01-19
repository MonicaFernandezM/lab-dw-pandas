import pandas as pd
import numpy as np
from IPython.display import display
'''
def quick_eda(df, head_rows=5):
    print("Head:" )
    display(df.head(head_rows))

    print("\n SHAPE: ")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[2]}")

    print("\n INFO: ")
    df.info()

    print("\n Describe (numerical): ")
    display(df.describe().T)

    print("\n Data Types: ")
    display(df.dtypes)
'''
    
def quick_eda1(df, head_rows=5):
    from IPython.display import display

    # Guardar resultados en un diccionario para devolverlos
    eda_results = {}

    print("Head:")
    eda_results['head'] = df.head(head_rows)
    display(eda_results['head'])

    print("\nShape:")
    eda_results['shape'] = df.shape
    print(f"Rows: {eda_results['shape'][0]}, Columns: {eda_results['shape'][1]}")

    print("\nInfo:")
    from io import StringIO
    import sys
        # Capturar la salida de df.info() para poder devolverla
    buffer = StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()
    eda_results['info'] = info_str
    print(info_str)

    print("\nDescribe (numerical):")
    eda_results['describe'] = df.describe().T
    display(eda_results['describe'])

    print("\nData Types:")
    eda_results['dtypes'] = df.dtypes
    display(eda_results['dtypes'])

    return eda_results