import pyautogui
import time
import keyboard
import random

def autoclick(interval=0.1):

    print("Autoclicker iniciado. Pressione 'q' para parar.")
    
    try:
        while True:
            if keyboard.is_pressed('q'):
                print("Autoclicker interrompido.")
                break
            pyautogui.click()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Autoclicker interrompido manualmente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def autoclick_with_movement(interval=0.1):

    print("Autoclicker com movimento iniciado. Pressione 'q' para parar.")
    
    try:
        while True:
            if keyboard.is_pressed('q'):
                print("Autoclicker interrompido.")
                break
            x = random.randint(0, pyautogui.size().width - 1)
            y = random.randint(0, pyautogui.size().height - 1)
            pyautogui.moveTo(x, y, duration=0.1)
            pyautogui.click()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Autoclicker interrompido manualmente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():

    print("Escolha o tipo de autoclicker:")
    print("1: Simples")
    print("2: Com Movimento")
    
    choice = input("Digite a opção desejada (1 ou 2): ").strip()
    
    if choice == '1':
        try:
            interval = float(input("Insira o intervalo entre cliques (em segundos): ").strip())
            autoclick(interval=interval)
        except ValueError:
            print("Valor inválido para o intervalo. Por favor, insira um número.")
    elif choice == '2':
        try:
            interval = float(input("Insira o intervalo entre cliques (em segundos): ").strip())
            autoclick_with_movement(interval=interval)
        except ValueError:
            print("Valor inválido para o intervalo. Por favor, insira um número.")
    else:
        print("Escolha inválida. Por favor, digite 1 ou 2.")

if __name__ == "__main__":
    main()
