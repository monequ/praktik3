В игре-стратегии есть солдаты и герои. У всех есть свойство,
содержащее уникальный номер объекта, и свойство, в котором хранится
принадлежность команде. У солдат есть метод "иду за героем", который в
качестве аргумента принимает объект типа "герой". У героев есть метод
увеличения собственного уровня.
В основной ветке программы создается по одному герою для каждой
команды. В цикле генерируются объекты-солдаты. Их принадлежность
команде определяется случайно. Солдаты разных команд добавляются в
разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится
на экран. У героя, принадлежащего команде с более длинным списком,
поднимается уровень.
