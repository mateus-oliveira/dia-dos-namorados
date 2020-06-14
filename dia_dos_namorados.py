from turtle import Pen, Screen
from random import randint


class Coracao:
    def __init__(self):
        self._desenho = Pen()
        self._desenho.hideturtle()
        self._desenho.speed('fastest')
    
    def desenhar_coracao(self, cor:str):
        x = randint(-150, 150)
        y = randint(-250, 250)
        self._desenho.color(cor)
        self._desenho.up()
        self._desenho.goto(x, y)
        self._desenho.down()
        self._desenho.begin_fill()
        self._desenho.setheading(45)
        self._desenho.forward(50)
        self._desenho.circle(25, 180)
        self._desenho.setheading(135)
        self._desenho.circle(25, 180)
        self._desenho.forward(50)
        self._desenho.end_fill()
    
    def esconder_coracao(self):
        self._desenho.clear()


class Imagem:
    def __init__(self):
        self._desenho = Pen()
        self._desenho.shape('img.gif')


def main():
    try: 
        tela = Screen()
        tela.title('Casa comigo?')
        tela.setup(500, 600)
        tela.register_shape('img.gif')

        imagem = Imagem()
        
        coracao = Coracao()

        cores = ('red', 'blue', 'green', 'gold', 'pink', 'purple')
        
        while True:
            tela.onkey(tela.bye, 'space')
            tela.listen()
            for i in range(6):
                coracao.desenhar_coracao(cores[i])
            
            coracao.esconder_coracao()

    except: pass

if __name__ == '__main__':
    main()