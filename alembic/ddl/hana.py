from .impl import DefaultImpl


class HanaImpl(DefaultImpl):

    __dialect__ = 'hana'
    transactional_ddl = True
