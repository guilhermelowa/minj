versão em português abaixo

# Minimalist journaling 
This is a minimalist CLI journal. It is intended to log daily activities and evaluations of all kinds of sorts - well-being, physical, mental, energy levels and so on.

## Installing
`pip install minj`

## Usage
To get help: `minj -h`

`minj sleep 22:30 6:30` to log your sleep and wake up time, respectively.

`minj metrics` to log the metrics that you're tracking.

### Autorun metrics
You can add minj to your `crontab` so you have your're prompted periodically to check your metrics. 

To do so, open a terminal and type `$DISPLAY`, save this number (usually :0).

Next, know how-to launch your terminal from CLI. On Gnome systems it is usually `gnome-terminal`. Get the location of the command using `which gnome-terminal`. You will also need to know the path to _minj_: `which minj`.

Now think about how often do you want to run the metrics checker. I want it at 9:00, 12, 15, 18 and 21:00.

Finally, add a job to _cron_ using `crontab -e`. Add the following line to your crontab file:

`0 <hours> * * * DISPLAY=:0 /path/to/terminal -- /path/to/minj`

In my case:

`0 9,12,15,18,21 * * * DISPLAY=:1 /usr/bin/gnome-terminal -- /home/<usr>/.local/bin/minj metrics`

## References:
- [Peter Lyons on career advice](https://peterlyons.com/leveling-up/#pillar3)
- [Jeff Atwood (StackOverflow co-founder) on writing](https://blog.codinghorror.com/how-to-write-without-writing/)
- [jrnl - Python Journal](https://github.com/jrnl-org/jrnl)
- [pdiary](https://github.com/manipuladordedados/pdiary)

# Diário minimalista
Este é um diário minimalista para linha de comando (CLI).

Vou escrever depois melhor a motivação. O objetivo é criar um log das atividades diárias realizadas e como você se sente, pra quem sabe extrair alguma relação destes dados. Extraindo ou não, o fato de você registrar esses logs já dá uma clareada na mente sobre você mesmo. Leia mais em Journal Smarter.

Vou começar registrando só coisas relacionadas ao sono e a qualidade do sono no dia seguinte, que é sobre o que tô lendo agora - o maravilhoso livro Why We Sleep de Matthew Walker. A ideia é ir incrementando pra registrar todas as atividades: exercício, alimentação, meditação, estudos, etc.

# Instalação
`pip install minj`

## Uso
Você pode ler as opções utilizando `minj -h` 

`minj sleep 22:30 6:30` registra o horário que você dormiu (22:30) e que acordou (6:30), respectivamente.

`minj metrics` registra as métricas que você está medindo atualmente.

### Rodando automaticamente
Você pode adicionar minj no `crontab` para rodar automaticamente e te perguntar sobre as métricas que estão sendo monitoradas.

Para fazer isso, abra um terminal e digite `$DISPLAY`. Salve esse número (normalmente :0)

Depois, descubra como rodar um terminal pela linha de comando. Em sistemas Gnome geralmente é `gnome-terminal`. Adquira a localização do comando utilizando `which gnome-terminal`. Você também vai precisar do caminho para o _minj_: `which minj`

Agora pense nos horários que você quer que seja perguntado sobre as métricas. Eu coloquei 9h, 12, 15, 18 e 21h.

Finalmente, adicione este job no _cron_ com `crontab -e`. Adicione a seguinte linha ao arquivo:

`0 <hours> * * * DISPLAY=:0 /path/to/terminal -- /path/to/minj`

No meu caso:

`0 9,12,15,18,21 * * * DISPLAY=:1 /usr/bin/gnome-terminal -- /home/<usr>/.local/bin/minj metrics`


## Referências
- [Peter Lyons on career advice](https://peterlyons.com/leveling-up/#pillar3)
- [Jeff Atwood (StackOverflow co-founder) on writing](https://blog.codinghorror.com/how-to-write-without-writing/)
- [jrnl - Python Journal](https://github.com/jrnl-org/jrnl)
