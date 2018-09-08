# python-2year
Домашние задания по курсу "Программирование и компьютерные инструменты лингвистического исследования" студентки II курса 4 группы Алины Смирновой
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Python Installation\n",
    "\n",
    "Установочный файл можно скачать [вот отсюда](https://www.python.org/downloads/), выбрав версию 3.6.4 для своей операционной системы.\n",
    "\n",
    "### Проверка связи\n",
    "\n",
    "Открываем терминал и пишем там `python`: если там появляется версия питона + еще некоторый служебный текст -- значит, все хорошо. Если же вам говорят, что \"python не является внутренней или внешней командой, исполняемой программой или пакетным файлом\" -- значит, надо настроить окружение.\n",
    "\n",
    "### Настройка окружения \n",
    "\n",
    "Если при вводе python в командную строку появляется ошибка, нужно прописать путь к питону в переменной среды (окружения) PATH. Эта переменная содержит список директорий, в которых операционная система должна искать исполняемые файлы. В качестве разделителя используется точка с запятой (;) в операционной системе Windows и двоеточие (:) в операционных системах Linux и MacOS. Очень хорошее краткое объяснение переменных среды в целом и PATH в частности можно почитать [вот тут](http://barancev.github.io/what-is-path-env-var/). На Windows добавить новую строку в PATH можно через `Изменение системных переменных среды > Переменные среды > PATH > Изменить`. В разных версиях и локализациях Windows это может называться \"переменными окружения\" или \"environment variables\". Например, если у вас Anaconda (подробнее о ней см. дальше), то в PATH должны быть строки следующего типа:\n",
    "\n",
    "`C:\\Users\\ancatmara\\Anaconda3\n",
    "C:\\Users\\ancatmara\\Anaconda3\\Lib\\bin\n",
    "C:\\Users\\ancatmara\\Anaconda3\\Scripts`\n",
    "\n",
    "А если обычный питон - то что-то вот такое.\n",
    "\n",
    "`C:\\ProgramFiles\\Python3\n",
    "C:\\ProgramFiles\\Python3\\Lib\n",
    "C:\\ProgramFiles\\Python3\\Scripts`\n",
    "\n",
    "\n",
    "## Package Installation\n",
    "\n",
    "В стандартной сборке питона есть только самые базовые функции -- для всего остального нужно устанавливать сторонние библиотеки. Все-все проверенные пакеты есть на [PyPI](https://pypi.python.org/pypi) (Python Package Index).\n",
    "\n",
    "### Как проверить версию питона и список установленных пакетов?\n",
    "\n",
    "* Чтобы посмотреть версию питона, нужно открыть терминал (на Windows он называется cmd, можно найти через поиск) и написать там `python --version`. В ответ вы должны получить что-то вроде `Python 3.6.0 :: Anaconda custom (64-bit)`.\n",
    "* Стандартный терминал на Windows очень неудобный. Альтернативу можно выбрать, прочитав [вот эту статью](https://habrahabr.ru/post/164687/).\n",
    "* Чтобы увидеть список установленных пакетов, нужно набрать в терминале `pip freeze`. На выходе вы увидите что-то такое:\n",
    "\n",
    "`\n",
    "regex==2017.9.23\n",
    "requests==2.14.2\n",
    "rope-py3k==0.9.4.post1\n",
    "scikit-image==0.13.0\n",
    "scikit-learn==0.19.0\n",
    "scipy==0.19.1\n",
    "seaborn==0.7.1\n",
    "simplegeneric==0.8.1\n",
    "singledispatch==3.4.0.3\n",
    "six==1.10.0\n",
    "snowballstemmer==1.2.1\n",
    "sockjs-tornado==1.0.3\n",
    "spacy==1.9.0`\n",
    "\n",
    "### pip\n",
    "\n",
    "**pip** -- это специальный питоновский скрипт, который позволяет устанавливать новые пакеты простой командой `pip install package-name`. Чтобы делать такие тетрадки, как эта, нам понадобятся пакеты ipython и jupyter -- и например, чтобы установить jupyter, мы напишем в командной строке `pip install jupyter`.\n",
    "\n",
    "**NB!** Если вы видите ошибку, что pip не является командой или программой, вернитесь к настройке окружения. \n",
    "\n",
    "Подробнее о работе с pip можно почитать на [официальном сайте с документацией](https://pip.pypa.io/en/stable/).\n",
    "\n",
    "### Anaconda\n",
    "\n",
    "Если не хочется установить набор часто использующихся пакетов сразу, чтобы не устанавливать их по одному в процессе работы, можно поставить **Anaconda** -- это дистрибутив питона, который включает в себя помимо интерпретатора и базовых функций некоторый набор популярных сторонних библиотек. Скачать ее можно [отсюда](https://www.anaconda.com/download/). У анаконды есть собственный менеджер пакетов, `conda`: так, чтобы установить пакет при наличии анаконды, можно написать в командной строке как `pip install package-name`, так и `conda install package-name`.  Конечно же, для conda есть [шпаргалка с командами](https://conda.io/docs/_downloads/conda-cheatsheet.pdf) и [сайт с документацией](https://conda.io/docs/index.html). Чтобы сэкомить место на компьютере, можно установить `Miniconda`, оторая включает только самые необходимые пакеты, и дальше устанавливать нужные самостоятельно. Стандартная же `Anaconda` включает в себя почти всё, что только помыслить -- с ней доустанавливать придется разве что `pymystem3` и `pymorphy2`.\n",
    "\n",
    "## Python и командная строка\n",
    "\n",
    "### Основные команды, которые вам понадобятся\n",
    "\n",
    "|Команда| Значение|\n",
    "|-------| -------:|\n",
    "|python| Запустить питон в терминале |\n",
    "|python --version| Посмотреть версию питона|\n",
    "|jupyter notebook| Запустить jupyter|\n",
    "|pip freeze| Посмотреть список установленных пакетов|\n",
    "|pip install| Установить пакет|\n",
    "|pip uninstall| Удалить пакет|\n",
    "|pip show| Показать информацию о конкретном пакете|\n",
    "|pip search| Найти пакет (если вы хотите установить что-то новое, но точно не помните название)|\n",
    "\n",
    "\n",
    "## IDE\n",
    "\n",
    "**IDE** (Integrated Development Environment) -- среда разработки, которая включает в себя\n",
    "* текстовый редактор, где вы пишете код;\n",
    "* компилятор/интерпретатор (то, с помощью чего исполняется ваш код)\n",
    "* отладчик (дебаггер), который помогает найти ошибки в коде\n",
    "\n",
    "### Компилятор?? Интерпретатор????\n",
    "\n",
    "Все языки программирования делятся на \n",
    "* компилируемые (Pascal, Visual Basic, C++, C#, Haskell...)\n",
    "* интерпретируемые (Java, Python, Ruby)\n",
    "\n",
    "Интерпретатор питона -- это специальная программа, в нашем случае файл `python.exe`.\n",
    "\n",
    "![](https://cdn.tproger.ru/wp-content/uploads/2016/12/concepts2mini.png)\n",
    "\n",
    "А еще среди языков программирования выделяют\n",
    "* низкоуровневые (близкие к машинному коду)\n",
    "* высокоуровневые (наиболее человекочитаемые)\n",
    "\n",
    "### Python IDEs\n",
    "\n",
    "Существует не одна IDE для питона. В стандартной сборке уже есть простенькая IDLE; если она вас не устраивает, то можно установить что-то с более широкими возмононостями вроде [PyCharm](https://www.jetbrains.com/pycharm/). Но на самом деле, чтобы писать код достаточно будет командной строки и любого текстового редактора -- Notepad++, Atom, Sublime и т.д. Многие из них включают в себя подсветку синтаксиса, автозаполнение и прочие нужные вещи. **NB!** Чтобы файл исполнялся, у него должно быть расширение `.py` В различных IDE тоже можно выбирать интерпретатор питона в настройках. Например, в PyCharm это делается с помощью `File > Settings > Project > Project Interpreter`. \n",
    "\n",
    "### Jupyter Notebooks\n",
    "\n",
    "Мы будем работать не только с запуском скриптов (= файлов с кодом) из командной строки, но и с `jupyter notebooks`. Это очень удобный формат, в котором код можно запускать не целиком, а по ячейкам. Кроме того, ячейки бывают текстовыми -- их можно форматировать с помощью markdown. Конспект, который вы сейчас читаете, написан как раз в таком формате. Файлы jupyter notebook имеют расширение `.ipynb` и автоматически рендерятся гитхабом (т.е. просто открываете такой файл и видите красоту).\n",
    "\n",
    "### Запуск Jupyter\n",
    "\n",
    "Для работы с тетрадкой нужно проделать следующие шаги:\n",
    "* Перейти в папку, из которой вы хотите запустить сервер\n",
    "* Открыть командную строку и запустить сервер командой `jupyter notebook`\n",
    "* Далее вы увидите сообщение с адресом сервера, что-то вроде `The Jupyter Notebook is running at: http://localhost:8888/...`. Если вкладка с этой страницей не открылась в браузере автоматически, то нужно скопировать появившуюся в командной строке ссылку *целиком* в адресную строку браузера.\n",
    "* Создать новую тетрадку в нужной папке / открыть уже существующую тетрадку\n",
    "\n",
    "\n",
    "### Чего делать не надо?\n",
    "\n",
    "1. Самое главное - не называть рабочий файл так же, как модуль. Если вы назовете файл flask.py, то получите ошибку импорта имени Flask, потому что ваш файл будет импортировать сам себя.\n",
    "2. Кроме того, не надо называть свои переменные и функции так же, как называются встроенные функции в питоне, т.е. переменные с именами dict и list - плохая идея.\n",
    "\n",
    "\n",
    "### А что надо?\n",
    "\n",
    "Писать четкий красивый код с комментариями по стандартам PEP8. :)\n",
    "\n",
    "**PEP** (Python Enhancement Proposal) -- техническая спецификация и правила хорошего тона, а PEP8 -- их последняя версия.\n",
    "\n",
    "[Style Guide for Python Code](http://legacy.python.org/dev/peps/pep-0008/)\n",
    "\n",
    "[То же самое, но попроще и в сокращении](http://docs.python-guide.org/en/latest/writing/style/)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## The Zen of Python\n",
    "\n",
    "<s>95</s> 20 тезисов Тима Питерса"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Zen of Python, by Tim Peters\n",
      "\n",
      "Beautiful is better than ugly.\n",
      "Explicit is better than implicit.\n",
      "Simple is better than complex.\n",
      "Complex is better than complicated.\n",
      "Flat is better than nested.\n",
      "Sparse is better than dense.\n",
      "Readability counts.\n",
      "Special cases aren't special enough to break the rules.\n",
      "Although practicality beats purity.\n",
      "Errors should never pass silently.\n",
      "Unless explicitly silenced.\n",
      "In the face of ambiguity, refuse the temptation to guess.\n",
      "There should be one-- and preferably only one --obvious way to do it.\n",
      "Although that way may not be obvious at first unless you're Dutch.\n",
      "Now is better than never.\n",
      "Although never is often better than *right* now.\n",
      "If the implementation is hard to explain, it's a bad idea.\n",
      "If the implementation is easy to explain, it may be a good idea.\n",
      "Namespaces are one honking great idea -- let's do more of those!\n"
     ]
    }
   ],
   "source": [
    "import this"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Полезные ссылки\n",
    "\n",
    "### Где читать документацию?\n",
    "\n",
    "[Keep this under your pillow :)](https://docs.python.org/3/)\n",
    "\n",
    "\n",
    "### Где искать ответы на вопросы?\n",
    "\n",
    "\"Google Driven Development\":\n",
    "\n",
    "* Загугли проблему\n",
    "* В топе выдачи будет её решение на [stackoverflow](https://stackoverflow.com/)\n",
    "* Не нашлось? Задай вопрос на stackoverflow сам!\n",
    "\n",
    "![](http://memesmix.net/media/created/v0h0oj.jpg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>\n",
       "  table {margin-left: 0 !important;}\n",
       "</style>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "%%html\n",
    "<style>\n",
    "  table {margin-left: 0 !important;}\n",
    "</style>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Задание №1\n",
    "\n",
    "1. Создать **новый репозиторий** для домашек по этому курсу с понятным названием -- например, python-2-year, python-hw-2 и т.п. -- и инициализировать его файлом README, не забыв также добавить .gitignore для питона.\n",
    "2. В README должно быть краткое описание содержимого репозитория -- например, такое. \n",
    "\n",
    "    * `Домашние задания по курсу \"Программирование и компьютерные инструменты лингвистического исследования\" студента/ки II курса ... группы Васи Пупкина`.\n",
    "\n",
    "    * Далее должна быть ссылка на репозиторий с домашками прошлого года, что-то типа:\n",
    "      `Домашние задания за I курс лежат вот тут`, \n",
    "      где слова \"вот тут\" -- это гиперссылка на ваш прошлогодний репозиторий.\n",
    "\n",
    "    * После этого делаем таблицу со списком домашек и ссылкой на каждую из них вот такого вида (обратите внимание на жирный жрифт и курсив! выравнивание внутри таблицы можно выбрать любое):\n",
    "    \n",
    "\n",
    "|  №      | Описание    | Ссылка на работу |\n",
    "| :------------- |:-------------| :-----|\n",
    "| **1**    | Игра \"Виселица\"| [*Код*](https://www.github.com) |\n",
    "| **2**    | Краулер для газеты \"Светлый путь\"| [*Код*](https://www.github.com) |\n",
    "| **3**    | Типологическая анкета об употреблении феминитивов| [*Код*](https://www.github.com) |\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "И, наконец, разбавляем это какой-нибудь картиночкой.\n",
    "\n",
    "<img src=\"./deadline.jpg\" style=\"width: 500px;\" align=\"left\" >"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Задание №2\n",
    "\n",
    "3. Выбрать любимое произведение (неважно, проза или поэзия) и сохранить его в текстовый файл с названием, соотвтествующим содержимому. \n",
    "4. Написать код, который \n",
    "    * открывает файл с текстом\n",
    "    * делает частотный список слов и отрезает все, у которых частотность < 3\n",
    "    * по запросу выдает пользователю случайное слово заданной длины на заданную букву\n",
    "5. Код должен быть оформлен по PEP8 в виде нескольких функций и записан в jupyter-тетрадке с названием, соотвтетсвующим содержимому. \n",
    "6. Все это загружаем в репозиторий в папку \"S1\" внутри репозитория для работ этого года с помощью консольного гита с информативным сообщением коммита. \n",
    "\n",
    "*Папку семинара можно назвать как угодно -- главное, чтобы было понятно, что в ней лежит код с первого семинара и остальные папки называть единообразно.*\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
