class Calculator:
    def init_calc_values(self):
        self.prev_value = None
        self.current_value = None
        self.first_value = None
        self.prev_msg_id = None
        self.keys = ['+', '-', '*', '/', '.', '=']
        self.current_operation = ''

    def set_value(self, value):
        if(value == '='):
            try:
                result = eval(self.current_value)
            except Exception:
                self.current_value = None
                return "Incorrect input"
            self.current_value = None
            return result
        elif (self.current_value):
            self.current_value += value
        else:
            self.current_value = value
        return self.current_value
