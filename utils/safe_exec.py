import io
import contextlib
import traceback
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np	
import plotly.express as px

def executar_codigo(codigo: str, df):
    """
    Executa o código gerado pelo modelo com acesso controlado ao DataFrame.
    """

    ambiente_local = {
        "df": df,
        "plt": plt,
        "pd": pd,
        "pandas": pd,
        "np": np,
        "numpy": np,
        "px": px,
        "fig": None
    }
        
    saida_capturada = io.StringIO()

    try:
        exec(codigo, {"__builtins__": {}}, ambiente_local)
        return ambiente_local.get("fig"), None

    except Exception:
        erro = traceback.format_exc()
        return None, erro