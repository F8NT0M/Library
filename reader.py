class Reader: #новый класс с именем Reader
    def __init__(self, first_name, last_name, card_number, borrowed_books=None): #Это метод инициализации (конструктор) класса Reader\
        #Он вызывается автоматически при создании нового объекта этого класса (borrowed_books: список книг, взятых на время (по умолчанию равен None))
        """Класс для представления читателя."""
        self.first_name = first_name
        #Эта строка присваивает значение параметра first_name атрибуту экземпляра self.first_name. self ссылается на текущий экземпляр класса, что позволяет каждому объекту иметь свои собственные значения атрибутов
        self.last_name = last_name
        self.card_number = card_number
        # borrowed_books хранит список кортежей: (название книги, дата выдачи)
        self.borrowed_books = borrowed_books or [] #Эта строка присваивает значение параметра borrowed_books атрибуту экземпляра self.borrowed_books.
        # Если borrowed_books равен None (или не передан), то используется пустой список ([]). Это позволяет избежать ошибок при попытке добавления книг в неинициализированный список
