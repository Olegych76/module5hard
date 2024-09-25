from time import sleep


class User:
    """
    Атрибуты объектов класса User:
    nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return other.nickname == self.nickname


class Video:
    """
    Атрибуты объектов класса Video: title(заголовок, строка), duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return str(self.title)

    def __repr__(self):
        return str(self.title)


class UrTube:
    """
    Атрибуты объектов класса UrTube:
    users(список объектов User), videos(список объектов Video), current_user(текущий пользователь)
    """
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        """
        Функция проверяет, есть ли пользователь с таким логином и паролем в списке users.
        Если есть, то устанавливает его как текущего пользователя.
        """
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user

    def log_out(self):
        """
        Функция устанавливает текущего пользователя как None.
        """
        self.current_user = None

    def register(self, nickname, password, age):
        """
        Функция регистрирует нового пользователя с указанным логином, паролем и возрастом.
        """
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f'Пользователь {nickname} уже существует')

    def add(self, *videos: Video):
        """
        Функция добавляет новый видеоролик в список видеороликов.
        """
        for video in videos:
            if video.title not in self.videos:
                self.videos.append(video)

    def get_videos(self, word):
        """
        Функция возвращает список видеороликов, заголовок которых содержит указанное слово.
        """
        titles = []
        for video in self.videos:
            if word.lower() in str(video).lower():
                titles.append(video)
        return titles

    def watch_video(self, title):
        """
        Функция проверяет, залогинен ли текущий пользователь,
        есть ли видеоролик с указанным заголовком в списке видеороликов и есть ли у него ограничение 18+.
        """
        if self.current_user is None:
            print('Необходимо войти в аккаунт, чтобы смотреть видео.')
            return
        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age >= 18:
                    while video.time_now < video.duration:
                        video.time_now += 1
                        print(video.time_now, end=' ')
                        sleep(1)
                    video.time_now = 0
                    print('Конец видео')
                else:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                break


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
