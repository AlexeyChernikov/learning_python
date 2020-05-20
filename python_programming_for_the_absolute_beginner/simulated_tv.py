import os
import sys


class TV:
    """ Imitates the operation of the TV """
    __MIN_VOLUME = 0
    __MAX_VOLUME = 100
    __channels = (
        'Информационный', 'Первый канал', 'Россия 1', 'Рен ТВ', 'СТС',
        'Домашний', 'ТНТ', 'Муз ТВ', 'Звезда', 'СПАС', 'Пятница',
        'Моя планета', 'МИР', 'Мульт ТВ', 'Союз', 'Бокс ТВ',
        'НТВ', 'Радио Шансон', 'ТВТУР', 'Супер', 'Время'
        )

    def status(self):
        """ Displays information about the current channel and volume level """
        print(f'Current channel: {TV.__channels[self.__cur_channel_num]}')
        print(f'Current volume: {self.__cur_volume}')

    @staticmethod
    def show_channel_list():
        print('Channel list:')
        channel_counter = 0
        for channel in TV.__channels:
            print(f'{channel_counter}: {channel}')
            channel_counter += 1

    def switch_the_channel(self):
        """ To switch the channel """
        print('Enter the channel number:')
        try:
            channel_number = int(input('>>> '))
            if channel_number > len(TV.__channels) - 1:
                self.__cur_channel_num += channel_number % len(TV.__channels)
            else:
                self.__cur_channel_num = channel_number
        except ValueError:
            print('Unidentified channel!')
        finally:
            print(f'Current channel: {TV.__channels[self.__cur_channel_num]}')
        
    def increase_volume(self):
        """ To increase the volume """
        if self.__cur_volume < TV.__MAX_VOLUME:
            self.__cur_volume += 1
        print(f'Current volume: {self.__cur_volume}')

    def decrease_volume(self):
        """ To decrease the volume """
        if self.__cur_volume > TV.__MIN_VOLUME:
            self.__cur_volume -= 1
        print(f'Current volume: {self.__cur_volume}')

    def __init__(self):
        """ Default constructor """
        self.__cur_channel_num = 0
        self.__cur_volume = 50


def info():
    print("""List of possible actions:
off\tTurn off the TV
stc\tSwitch between channels
+\tIncrease volume
-\tDecrease volume
st\tView current channel and volume
scl\tView a list of available channels
info\tShow list of commands""")

def actions(action, tv_obj):
    if action == 'off':
        print('Goodbye...')
        sys.exit(0)
    elif action == 'stc':
        tv_obj.switch_the_channel()
    elif action == '+':
        tv_obj.increase_volume()
    elif action == '-':
        tv_obj.decrease_volume()
    elif action == 'st':
        tv_obj.status()
    elif action == 'scl':
        TV.show_channel_list()
    elif action == 'info':
        info()
    else:
        print('Command not found!')

def main():
    sony = TV()

    os.system('cls')
    info()

    while True:
        action = input('\n>>> ')
        print()
        actions(action, sony)


main()