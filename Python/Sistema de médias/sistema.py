#Importar a biblioteca PysimpleGUI as sg
from PySimpleGUI import PySimpleGUI as sg

#Selecionar tema do layout
sg.theme=('black')
#determinar layout
layout = [
    [sg.Text('Coloque suas notas para ver se está aprovado', font=('Helvetica', 12))],
    [sg.Text('1ª Nota:'), sg.Input(key='num1', size=(5,1))],
    [sg.Text('2ª Nota:'), sg.Input(key='num2', size=(5,1))],
    [sg.Text('3ª Nota:'), sg.Input(key='num3', size=(5,1))],
    [sg.Text('4ª Nota:'), sg.Input(key='num4', size=(5,1))],
    [sg.Button('média', size=(30,1), pad=((50,0),0))]
]

#determinar a janela
janela = sg.Window('Média', layout, size=(360, 200))
#fazer as condições
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'média':
        num1 = float(valores['num1'])
        num2 = float(valores['num2'])
        num3 = float(valores['num3'])
        num4 = float(valores['num4'])
#calcular a media das notas
        média = (num1 + num2 + num3 + num4)
#verificar se a média é maior ou igual a 28
    if média >= 28:
        #sg.popup serve para exibir uma nova janela com uma mensagem
        sg.popup('Parabéns, você está aprovado!')
    else:
        sg.popup('Infelizmente você está reprovado...')
#fechar a janela 
        
janela.close()
