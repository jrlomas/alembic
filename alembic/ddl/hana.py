from sqlalchemy.ext.compiler import compiles

from .. import util
from .impl import DefaultImpl
from .base import alter_table, AddColumn, ColumnName, RenameTable,\
    format_table_name, format_column_name, ColumnNullable, alter_column,\
    format_server_default, ColumnDefault, format_type, ColumnType
from sqlalchemy.sql.expression import ClauseElement, Executable

class HanaImpl(DefaultImpl):

    __dialect__ = 'hana'
    transactional_ddl = True

@compiles(AddColumn, 'hana')
def visit_add_column(element, compiler, **kw):
    return "%s %s" % (
        alter_table(compiler, element.table_name, element.schema),
        hana_add_column(compiler, element.column, **kw)
    )

def hana_add_column(compiler, column, **kw):
    return "ADD (%s)" % compiler.get_column_specification(column, **kw)
