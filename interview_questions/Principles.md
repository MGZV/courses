Зачем нужны принципы

- позволяют разговаривать на одном языке
- разрабатывать поддерживаемые, масштабируемые приложения

Кодовая база 
- легко вносить изменения
- новым людям легко вникнуть в проект
- код должен быть простым

# SOLID
## The Single-Responsibility Principle (SRP)
Принцип единственной ответственности
- 1 класс должен решать 1 задачу
- 1 сущность - 1 задача
- 1 класс инкапсулирует решение одной задачи

если не применять сущность разрастается:
- получаем много связанного кода
- ломается одно, ломается и другое
- ухудшается читабельность кода
- вносить изменения в такой класс долго и дорого

## The Open-Closed Principle (OCP)
Принцип открытости/закрытости

программные сущности (классы, функции, модули и др.) открыты для расширения, но закрыты для изменения

- существующий код протестирован и работает если внести в него изменения нужно производить регрессионное тестирование
- меньше вероятность ошибок

## The Liskov Substitution Principle (LSP)
Принцип подстановки Барбары Лисков

Функции и классы которые используют родительский тип 
должны также работать и с дочерними классами при этом ничего не должно ломаться в логике программы
(Наследуемый класс должен дополнять, а не замечать наследуемые классы)

## The Interface Segregation Principle (ISP)
Принцип разделения интерфейса.

Программные методы не должны зависеть от методов которые они не используют
(нужно разбивать толстые интерфейсы на более маленькие узкоспециализированные решающие одну задачу)
(нельзя заставлять клиента реализовывать интерфейс, которым он не пользуется)
- избавляем программные сущности от методов, которые они не используют
- получаем более предсказуемую работу 
- код становится менее связанным

## The Dependency inversion Principle (DIP)
Принцип инверсии зависимости
Модули высокого уровня не должны зависит от модулей более низкого уровня
Все они должны зависеть от абстракций, абстракции не должны зависеть от деталей
А детали должны зависеть от абстракций


Ссылки:

[SOLID ПРИНЦИПЫ простым языком (много примеров)](https://www.youtube.com/watch?v=TxZwqVTaCmA)
