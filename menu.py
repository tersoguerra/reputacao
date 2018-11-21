from gerenciador import Gerenciador


class Menu(object):

    def __init__(self):
        self.gerenciador_obj = Gerenciador()
        self.start_interface()

    def start_interface(self):
        self.welcome_msg()
        self.select_option()

    def welcome_msg(self):
        print('Bem vindo à Aplicação de Análise de Reputação em Mídias Sociáis!')

    def select_option(self):
        option = None
        option_text = ('Digite o número para selecionar a funcionalidade à ser executada:\n'
                       '1: Coleta de tweets referentes à uma entidade alvo (Coleta de análise)\n'
                       '2: Gerar gráficos para dados (json) já coletados e validados (Validação de análise)\n')
        error_text = 'Não foi possível identificar uma opção válida. Por favor, tente novamente.'
        while option is None:
            option = input(option_text)
            if option == '1':
                self.quick_exec()
            elif option == '2':
                self.import_json()
            else:
                print(error_text)
                option = None

    def quick_exec(self):
        query = input(
            'Por favor, insira abaixo o termo que identifica a entidade alvo da análise, para coleta no Twitter:\n')
        self.gerenciador_obj.quick_execution(query)

    def import_json(self):
        query = input(
            'Por favor, insira abaixo o nome ou endereço do arquivo .json com os dados validados\n')
        self.gerenciador_obj.import_json(query)


if __name__ == '__main__':
    obj = Menu()
