import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")



pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=763, y=381)
pyautogui.write("testeteste@teste.com")
pyautogui.press("tab")
pyautogui.write("testeteste@teste.com")
pyautogui.press("tab")
pyautogui.press("enter")



tabela = pandas.read_csv("produtos.csv")
print(tabela)

time.sleep(15)
for linha in tabela.index:

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.click(x=802, y=263)testeteste@teste.com
    pyautogui.write(codigo)
    pyautogui.press("tab")

    codigo = str(tabela.loc[linha, "marca"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    codigo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    codigo = str(tabela.loc[linha, "categoria"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    codigo = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    codigo = str(tabela.loc[linha, "custo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(500000)
    