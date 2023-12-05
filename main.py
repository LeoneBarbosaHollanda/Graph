import subprocess
import os

# Definir o caminho para o emulador e o jogo
emulador_executavel = "Mesen.exe"
rom_caminho = "mario.nes" # Substitua pelo caminho correto do jogo

# Verificar se o arquivo ROM existe
if not os.path.exists(rom_caminho):
    raise FileNotFoundError(f"O arquivo ROM não foi encontrado: {rom_caminho}")

# Iniciar o emulador com o jogo
subprocess.run([emulador_executavel, rom_caminho])
