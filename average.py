class Phone:

    line_type = 'проводной'

    def __init__(self):
        self.dial_type = 'дисковый'


# Создать объект rotary_phone.
rotary_phone = Phone()
# Создать объект rotary_phone_2.
rotary_phone_2 = Phone()

print(rotary_phone.line_type)
print(rotary_phone_2.dial_type)