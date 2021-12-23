class MismatchQuantityError(Exception):
    """Исключение вызывается, когда количества не совпадают."""
    def __init__(self, message="Количество файлов не совпадает"
                               "с количеством переданных имен"):
        self.message = message
        super().__init__(self.message)


class TooManyQuestionFiles(Exception):
    """Исключение вызывается, когда пользователь хочет слишком
     много текстовых файлов."""
    def __init__(self, message="Вы хотите очень много файлов,"
                               " возможны повторения"):
        self.message = message
        super().__init__(self.message)
