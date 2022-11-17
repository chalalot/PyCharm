def game(h, a):
    '''
    a simple game:
    there are 3 environments: fire, water and air
    in air: h + 3 and a + 2
    in fire: h - 20 and a + 5
    in water: h - 5 and a - 10
    if h or a = 0 => you die
    :param h:
    :param a:
    :return:
    '''
    h = h + 3
    a = a + 2
