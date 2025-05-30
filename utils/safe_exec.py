import io
import contextlib
import traceback
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np	

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
    }
        
    saida_capturada = io.StringIO()

    try:
        with contextlib.redirect_stdout(saida_capturada):
            exec(codigo, {"__builtins__": {}}, ambiente_local)

        return saida_capturada.getvalue(), None
    except Exception:
        erro = traceback.format_exc()
        return None, erro