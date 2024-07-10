# 전체 애플리케이션의 진입점을 제공
# GUI, 게임 로직, 통신 모듈을 초기화하고 실행

import gui.main_window as MainWindow
import communication.client as BingoClient
import game.bingo_logic as BingoGame

def main():
    MainWindow.do_something()
    BingoClient.do_something()
    BingoGame.do_something()

if __name__ == "__main__":
    main()