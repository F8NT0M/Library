class Book: #новый класс с именем Book
    def __init__(self, title, author, year, genre, copies): #Это метод инициализации (конструктор) класса Book. Он вызывается автоматически при создании нового объекта этого класса
        """Класс для представления книги."""
        self.title = title
        #Эта строка присваивает значение параметра title атрибуту экземпляра self.title. self ссылается на текущий экземпляр класса, что позволяет каждому объекту иметь свои собственные значения атрибутов
        self.author = author
        self.year = year
        self.genre = genre
        self.copies = copies
