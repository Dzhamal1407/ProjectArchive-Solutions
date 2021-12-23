import random
from math import factorial
from exceptions import MismatchQuantityError, TooManyQuestionFiles

""" 
Вопросы, которые будут фигурировать в тесте и возможные варианты
ответов я определил в данном файле.
"""
question_war = "В каком году началась первая мировая война?"
question_battle = "В каком году произошла Куликовская битва?"
question_music = "В каком году был написан альбом Горгород?"

data = {question_war: ['1918', '1914', '1910'],
        question_battle: ['1380', '1392', '1480'],
        question_music: ['2020', '2015', '2017', '2018']}


class Question(object):
    """Класс, описывающий вопрос

    Поля:
        __theme: тематика вопроса
        __text: содержимое вопроса
        __answer_variants: варианты ответа

    Методы:
        choosing_answer_quantity: выбрать часть вариантов из всех
        Дандер-методы __init__ и __str__
    """

    def __init__(self, text: str, answers_list: list[str]) -> None:
        self.__theme: str = ""
        self.__text: str = text
        self.__answer_variants: list[str] = answers_list

    def choosing_answer_quantity(self, quantity: int) -> list[str]:
        """Выбор определенного количества вариантов из набора
        всевозможных вариантов"""
        self.__answer_variants = random.sample(self.__answer_variants, k=quantity)
        return self.__answer_variants

    def __str__(self) -> str:
        result_string = ""
        answer_string = ""
        for answer in self.__answer_variants:
            answer_string += answer + '\n'
        result_string += \
            "Текст вопроса:\n" \
            f"{self.__text}\n\n" \
            "Всевозможные варианты ответов:\n" \
            f"{answer_string}"
        return result_string


class TextFile(object):
    """Класс, описывающий выходной файл.

    Поля:
        __file_name: имя текстового файла (+ расширение)
        __path: путь файла
        __questions: список объектов-вопросов
        __number_of_questions: количество вопросов

    Методы:
        shuffle_questions: изменить порядок следования
            вопросов на произвольный
        write: запись файла по заданному пути с указанным
            именем, с переданными заголовком и вопросами
        """

    def __init__(self, questions: list[Question], file_name="test.txt",
                 path="") -> None:
        """
        !!! В качестве аргумента path вы передаете путь, по которому
        будут находиться сгенерированные текстовые файлы-тесты.
        """
        self.__file_name: str = file_name
        self.__path: str = path
        self.__questions: list = questions
        self.__number_of_questions: int = \
            len(self.__questions)

    @property
    def questions(self) -> list[Question]:
        return self.__questions

    def shuffle_questions(self) -> None:
        random.shuffle(self.__questions)

    def write(self, title="") -> None:
        """Запись одного файла по пути self.__path"""
        result_string: str = title + '\n\n' + str(self)
        with open(self.__path + self.__file_name, 'w') as file:
            file.write(result_string)

    @staticmethod
    def multiple_files(questions: list[Question], names: list[str],
                       path: str = "", quantity: int = 0) -> None:
        """
        Запись нескольких однотипных файлов, отличающихся
        лишь следованием вопросов, но не их количеством и
        содержимым.

        names: список имен файлов
        path: путь, по которому происходит запись множества
            файлов
        quantity: количество файлов
        """

        if factorial(len(questions)) < quantity:
            """
            если человек хочет слишком много файлов,
            то некоторые из них будут идентичными,
            в таком случае я вызываю исключение
            """
            raise TooManyQuestionFiles
        if len(names) != quantity and len(names) != 1:
            """
            если количество имен файлов не совпадает с
            количеством файлов, то я вызываю соответствующее
            исключение
            """
            raise MismatchQuantityError
        elif len(names) == 1 and quantity > 0:
            """
            если в списке имен только одно имя, то
            я его просто размножаю посредством добавления
            цифр в конец имени.
            """
            example = names[0]
            names = []
            for i in range(quantity):
                name_string = example[:-4] + f"({i + 1})" + ".txt"
                names.append(name_string)
        # print(names)
        for number in range(quantity):
            # генерация и запись текстовых файлов
            file = TextFile(questions, names[number], path)
            file.shuffle_questions()
            file.write()

    def __str__(self) -> str:
        result_string = ""
        for question in self.__questions:
            result_string += str(question) + '\n\n'
        return result_string

    def __repr__(self) -> str:
        result_string = ""
        result_string += \
            f"Количество вопросов: {self.__number_of_questions}\n\n"
        for question in self.__questions:
            result_string += str(question) + '\n\n'
        return result_string


if __name__ == "__main__":
    first_question = Question(question_war, data[question_war])
    second_question = Question(question_battle, data[question_battle])
    third_question = Question(question_music, data[question_music])

    TextFile.multiple_files([first_question, second_question, third_question],
                            [], quantity=0)
