from app_interface_ui import *
from PyQt5 import QtWidgets
from subprocess import call, check_output, CalledProcessError
import re

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Ip Tables UI')

        self.restrict.clicked.connect(self.restrict_ip)
        self.enable.clicked.connect(self.enable_ip)

    def restrict_ip(self):
        drop_command = 'iptables -A INPUT -s ' + self.ip_address.text() + ' -j DROP'
        response = call('echo {} | sudo -S {}'.format(self.password.text(), drop_command), shell=True)
        if response != 0:
            self.output.setText('Error al Restringir')
        else:
            self.output.setText('Correctamente Bloqueado')

    def enable_ip(self):
        # CalledProcessError

        list_command = 'sudo iptables -L INPUT --line-numbers'
        try:
            # List all INPUT instructions
            list_command_out = check_output('echo {} | sudo -S {}'.format(self.password.text(), list_command),
                                            shell=True)\
                .decode('utf-8')

            # Split lines
            instruction_lines = list_command_out.split('\n')

            # Get index of lines we want to delete
            lines_index = [re.split(' +', line)[0]
                           for line in instruction_lines
                           if 'DROP' in line and self.ip_address.text() in line]

            for index in reversed(lines_index):
                delete_command = 'sudo iptables -D INPUT ' + index
                response = call('echo {} | sudo -S {}'.format(self.password.text(), delete_command), shell=True)
                if response != 0:
                    self.output.setText('Error al habilitar')
                else:
                    self.output.setText('Habilitado Correctamente')
        except CalledProcessError:
            self.output.setText('No se puede encontrar la dirección')

    #     # Logic
    #     self.boton.clicked.connect(self.square_button)
    #
    # def square_button(self):
    #     inp = self.entrada.text()
    #     if not inp == '':
    #         n = int(inp)
    #         self.salida.setText(str(square(n)))
    #     else:
    #         self.salida.setText('No se ingresó nada')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
