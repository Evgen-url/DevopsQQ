Ответы на вопросы:
1)Kernel
Kernel - Ядро в ОС Linux. Это основная часть в данной операционной системе
которая обмеспечивает взаимодейсвтие между апаратной частью компьютера и 
програмным обеспечением. Управляет ресурсами системы, такими как 
процессоры, памятью, устройствами ввода и вывода а также сетями.
Из плюсов можно выделить то что ядро Linux имеет открытый исходный код
что позволяет изменять его исходный код. Имеет модульность, что позволяет
добавлять необходимый функционал без перезагрузки самой системы. 
Также управляет созданием процессов, а также их распределением 
по их важности и приоритетам(какой процес должен быть выполнен 
в первую очередь, а который другорядный.)
При необходимости может обеспечивать для выполнения процеса или использования 
приложения виртуальную память.
2)Libraries 
Libraries(библиотеки) - Это набор функций и програмного кода, который может бить использован 
различными программами. Предназначены для упрощения работы и кодинга тем что 
помогает переиспользовать код без его повторения. Библиотеки есть двух видов:
- Динамичесие -- программы используют данные библиотеки при выполнении какой-то
программы, а не копирует её в исполняемый файл
- Статические -- Встраивается в исполняемый файл на этапе компеляции что делает
программу более автономной, но увеличивает её размер. 
Из плюсов следует выделить то что:
- Убирает потребность использовать код дважды
- Динамические библиотеки можно загрузить один раз, а использовать их могут несколько 
программ одновременно.
- Позволяет экономить время, так как в стандартных библиотеках уже есть 
базовый функционал.
3)System utulities
System utilities(системные утилиты) - Это инструменты, программы и команды которые
используються для управления , настройки и мониторинга ОС Linux. Помогают эффективно 
управлять системой.
Системные утилиты нужны для:
- Мониторинга системы -- отслеживать состояние ОС, включая мониторинг ЦП, ОЗУ, HDD(SSD), сети.
- Оптимизация системы -- настройка параметров ОС для её большей производительности
- Администрирование системы - Позволяет добавлять новых юзеров, настраивать права доступа, 
А также служит для управления файлами, процессами и ресурсами системы.

Kernel, system utilities, libraries Связаны между собой и работают вместе для обеспечения
работы самой ОС.
1)Ядро и библиотеки - Библиотеки используют системные вызовы которые предоставляються ядром,
чтоб связыватся с апаратным обеспечением и выполнять задачи
2)Ядро и системные утилиты - Через библиотеки утилиты обращаются к ядру для выполнения
задач, таких как чтения файлов, управления процессами и отправка сетевых запросов 
3) Библиотеки и системные утилиты - Системные утилиты используют библиотеки для выполнения задач.
