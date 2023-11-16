# Atividade 2 - Módulo 8

### Pacote Demiurge:

O pacote Demiurge contempla os scripts necessários para realizar o mapeamento pelo robô em ambiente simulado e se encontra no diretório: `ativ2-m8/src/demiurge`. 

Para executá-lo, juntamente com as suas dependências, é preciso seguir as seguintes instruções:

- Na pasta raíz desse projeto rode o seguinte comando:

```
sudo chmod +x ./mapping_zsh.sh
```

> [!IMPORTANT]
> Verifique qual a versão do seu shell com o seguinte comando: ```echo $SHELL```, caso ela difira do tipo zsh rode o comando acima com o sufixo bash: ```sudo chmod +x ./mapping_bash.sh```.

- Em seguida, no mesmo diretório rode o comando:
```
./mapping_zsh.sh
```

O script acima instalará na sua máquina todas as dependências necessárias para executar os nós ROS necessárias para a etapa de mapeamento.

> [!IMPORTANT]
> Mais uma vez verifique qual a versão do seu shell com o seguinte comando: ```echo $SHELL```, caso ela difira do tipo zsh rode o comando acima com o sufixo bash: ```./mapping_bash.sh```.

- Após isso, em outro terminal, é preciso rodar o comando abaixo para salvar o mapa gerado pela varredura no mapa:
  
```
ros2 run nav2_map_server map_saver_cli -f ./assets/map
```

Depois de obter sucesso com os comandos acima, você cumpriu a rotina de mapeamento. Agora basta clicar em CTRL+C para encerrar todos os processos criados pelo script `.sh`

#### Video do mapeamentodo sistema de mapeamento que é lançado por um "launch file".
Neste [link](https://youtu.be/Jo1Fm9NkEkQ) é possível ver o funcionamento do pacote.

### Pacote Intelligible:

O pacote de intelligible se encontra no diretório `ativ2-m8/src/intelligible`. 

Para executa-lo é preciso seguir as seguintes instruções:

- Na pasta raíz desse projeto rode o seguinte comando:

```
sudo chmod +x ./navigation_zsh.sh
```

> [!IMPORTANT]
> Verifique qual a versão do seu shell com o seguinte comando: ```echo $SHELL```, caso ela difira do tipo zsh rode o comando acima com o sufixo bash: ```sudo chmod +x ./navigation_bash.sh```.

- Em seguida, no mesmo diretório rode o comando:
```
./navigation_zsh.sh
```

> [!IMPORTANT]
> Mais uma vez verifique qual a versão do seu shell com o seguinte comando: ```echo $SHELL```, caso ela difira do tipo zsh rode o comando acima com o sufixo bash: ```./navigation_bash.sh```.

- Em seguida, na janela do X-Term criada, indique as cordenadas x e y que você deseja que o robô se mova.

Depois de obter sucesso com os comandos acima, você cumpriu a rotina de mapeamento. Agora basta clicar em CTRL+C para encerrar todos os processos criados pelo script `.sh`. 

#### Video da navegação utilizando o pacote intelligible
Neste [link](https://youtu.be/XA6lfy7YLa0) é possível ver o funcionamento do pacote.
