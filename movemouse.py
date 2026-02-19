import pyautogui
import time
import threading
import customtkinter as ctk

#Função que move o mouse e faz o clique
def move_mouse_and_click():
    pyautogui.move(10, 10)
    pyautogui.move(-10, -10)
    pyautogui.click()

#Função que executa o loop de automação
def start_automation():
    global running
    running = True
    while running:
        start_time = time.time()  #Captura o tempo inicial
        while running and time.time() - start_time < 10:  #Contagem de 10 segundos
            time_remaining = 10 - (time.time() - start_time)
            #Atualiza o cronômetro na interface
            update_timer_label(time_remaining)
            time.sleep(0.1)  #Espera 100ms para evitar uso excessivo de CPU
        if running:  #Executa a ação apenas se a automação não foi interrompida
            move_mouse_and_click()

#Função para atualizar o tempo no rótulo da interface
def update_timer_label(time_remaining):
    timer_label.configure(text=f"Tempo restante: {int(time_remaining)}s")

#Função para parar a automação
def stop_automation():
    global running
    running = False
    timer_label.configure(text="Automação parada")

#Configurações da interface
app = ctk.CTk()
app.geometry("400x300")
app.title("Automação de Mouse")

timer_label = ctk.CTkLabel(app, text="Tempo restante: 10s", font=("Arial", 24))
timer_label.pack(pady=20)

#Botão Iniciar Automação - cor verde
start_button = ctk.CTkButton(app, text="Iniciar Automação", command=lambda: threading.Thread(target=start_automation).start(), fg_color="green")
start_button.pack(pady=10)

#Botão Parar Automação - cor vermelha
stop_button = ctk.CTkButton(app, text="Parar Automação", command=stop_automation, fg_color="red")
stop_button.pack(pady=10)

app.mainloop()
