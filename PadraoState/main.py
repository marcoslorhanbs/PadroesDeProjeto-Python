from __future__ import annotations
from abc import ABC, abstractmethod

# A classe Elevator é o contexto. Ele deve ser iniciado com um estado padrão.
class Elevator:

    _state = None

    def __init__(self, state: State) -> None:
        self.setElevator(state)

    # método para alterar o estado do objeto
    def setElevator(self, state: State):

        self._state = state
        self._state.elevator = self

    def presentState(self):
        print(f"Elevador está no {type(self._state).__name__}")

    # os métodos para executar a funcionalidade do elevador. Isso depende do estado atual do objeto.

    def pushDownBtn(self):
        self._state.pushDownBtn()

    def pushUpBtn(self):
        self._state.pushUpBtn()

    # se ambos os botões forem pressionados ao mesmo tempo, nada deve acontecer
    def pushUpAndDownBtns(self) -> None:
        print("Você deve apertar um botão de cada vez")

    # se nenhum botão foi pressionado, ele deve apenas aguardar aberto para os convidados
    def noBtnPushed(self) -> None:
        print("Pressione qualquer botão. Para cima ou para baixo")


# A interface de estado comum para todos os estados
class State(ABC):
    @property
    def elevator(self) -> Elevator:
        return self._elevator

    @elevator.setter
    def elevator(self, elevator: Elevator) -> None:
        self._elevator = elevator

    @abstractmethod
    def pushDownBtn(self) -> None:
        pass

    @abstractmethod
    def pushUpBtn(self) -> None:
        pass


# Os estados concretos
# Temos dois estados do elevador: quando está no primeiro andar e no segundo andar
class firstFloor(State):

    # Se o botão para baixo for pressionado quando já estiver no primeiro andar, nada deve acontecer
    def pushDownBtn(self) -> None:
        print("Já está no andar de baixo")

    # se o botão para cima for pressionado, mova para cima e ele mudará seu estado para o segundo andar.
    def pushUpBtn(self) -> None:
        print("Elevador subindo um andar...")
        self.elevator.setElevator(secondFloor())


class secondFloor(State):

    # se o botão para baixo for pressionado, ele deve mover um andar para baixo e abrir a porta
    def pushDownBtn(self) -> None:
        print("Elevador descendo um andar...")
        self.elevator.setElevator(firstFloor())

    # se o botão para cima for pressionado, nada deve acontecer
    def pushUpBtn(self) -> None:
        print("Já no último andar")


if __name__ == "__main__":

    myElevator = Elevator(firstFloor())
    myElevator.presentState()

    # O botão para cima é pressionado
    myElevator.pushUpBtn()
    # Mostra o estado atual do Elevador
    myElevator.presentState()
    # O botão para baixo é pressionado
    myElevator.pushDownBtn()

    myElevator.presentState()