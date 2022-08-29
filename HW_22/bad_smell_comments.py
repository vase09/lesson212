class Unit:
    def move_unit_on_field(self, field, field_1_param, field_2_param, direct, is_fly, is_creep, base_speed=1):
        """Функция реализует перемещение юнита по полю. В качестве параметров принимает текущие координаты юнита,
        направление его движения, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с
        которым двигается юнит
        :param field: поле по которому перемещается юнит
        :param field_1_param: x-координата юнита
        :param field_2_param: у- координата юнита
        :param direct: направление перемещения
        :param is_fly: летит ли юнит
        :param is_creep: крадется ли юнит
        :param base_speed: базовый параметр скорости
        """
        # Для начала проверим не установлены ли у нас два флага полета и подкрадывания в истину,
        # т.к. одновременно эти события не должны происходить

        if is_fly and is_creep:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            base_speed *= 1.2
            if direct == 'UP':
                new_y = field_2_param + base_speed
                new_x = field_1_param
            elif direct == 'DOWN':
                new_y = field_2_param - base_speed
                new_x = field_1_param
            elif direct == 'LEFT':
                new_y = field_2_param
                new_x = field_1_param - base_speed
            elif direct == 'RIGHT':
                new_y = field_2_param
                new_x = field_1_param + base_speed
        if is_creep:
            base_speed *= 0.5
            if direct == 'UP':
                new_y = field_2_param + base_speed
                new_x = field_1_param
            elif direct == 'DOWN':
                new_y = field_2_param - base_speed
                new_x = field_1_param
            elif direct == 'LEFT':
                new_y = field_2_param
                new_x = field_1_param - base_speed
            elif direct == 'RIGHT':
                new_y = field_2_param
                new_x = field_1_param + base_speed

            field.set_unit(x=new_x, y=new_y, unit=self)
