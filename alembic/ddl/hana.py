from .impl import DefaultImpl


class HanaImpl(DefaultImpl):

    __dialect__ = 'hana'
    transactional_ddl = True

@compiles(AddColumn, 'mssql')
def visit_add_column(element, compiler, **kw):
    return "%s %s" % (
        alter_table(compiler, element.table_name, element.schema),
        hana_add_column(compiler, element.column, **kw)
    )

def mssql_add_column(compiler, column, **kw):
    return "ADD (%s)" % compiler.get_column_specification(column, **kw)
