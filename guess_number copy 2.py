from datetime import datetime as dt
from random import randint

from access_control import access_control
from constants import ADMIN_USERNAME, UNKNOWN_COMMAND

class GuessGame:

    def __init__(self):
        self.start_time = dt.now()
        self.total_games = 0
        self.username = self.get_username()
        self.current_game_number = 0

    def get_username(self) -> str:
        self.username = input('Представьтесь, пожалуйста, как Вас зовут?\n').strip()
        if self.username == ADMIN_USERNAME:
            print(
                '\nДобро пожаловать, создатель! '
                'Во время игры вам доступны команды "stat", "answer"'
            )
        else:
            print(f'\n{self.username}, добро пожаловать в игру!')
        return self.username



    @access_control
    def get_statistics(self, *args, **kwargs) -> None:
        game_time = dt.now() - self.start_time
        print(f'Общее время игры: {game_time}, текущая игра - №{self.total_games}')


    @access_control
    def get_right_answer(self, number: int, *args, **kwargs) -> None:
        print(f'Правильный ответ: {number}')


    def check_number(self, guess: int, number: int) -> bool:
        # Если число угадано...
        if guess == number:
            print(f'Отличная интуиция, {self.username}! Вы угадали число :)')
            # ...возвращаем True
            return True
        
        if guess < number:
            print('Ваше число меньше того, что загадано.')
        else:
            print('Ваше число больше того, что загадано.')
        return False


    def game(self) -> None:
        # Получаем случайное число в диапазоне от 1 до 100.
        number = randint(1, 100)
        print(
            '\nУгадайте число от 1 до 100.\n'
            'Для выхода из текущей игры введите команду "stop"'
        )
        while True:
            # Получаем пользовательский ввод, 
            # отрезаем лишние пробелы и переводим в нижний регистр.
            user_input = input('Введите число или команду: ').strip().lower()

            if user_input == 'stop':
                break
            elif user_input == 'stat':
                self.get_statistics(total_games, username=self.username)
            elif user_input == 'answer':
                    self.get_right_answer(number, username=self.username)
            else:
                try: 
                    guess = int(user_input)                
                except ValueError:
                    print(UNKNOWN_COMMAND)
                    continue
                else:
                    if self.check_number(guess, number):
                        break          


    def guess_number(self) -> None:
        while True:
            self.total_games += 1
            self.game()
            play_again = input(f'\nХотите сыграть ещё? (yes/no) ')
            if play_again.strip().lower() not in ('y', 'yes'):
                break


if __name__ == '__main__':
    print(
        'Вас приветствует игра "Угадай число"!\n'
        'Для выхода нажмите Ctrl+C'
    )
    game = GuessGame()
    game.guess_number()
