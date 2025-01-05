from peewee import Model

from python_boilerplate.configuration.peewee_configuration import DATABASE

# Database https://docs.peewee-orm.com/en/latest/peewee/database.html
# Recommended Settings https://docs.peewee-orm.com/en/latest/peewee/database.html#recommended-settings
# Logging queries https://docs.peewee-orm.com/en/latest/peewee/database.html#logging-queries


class BaseModel(Model):
    """
    Base model for persistence.

    Models and Fields https://docs.peewee-orm.com/en/latest/peewee/models.html#model-inheritance
    Field types table https://docs.peewee-orm.com/en/latest/peewee/models.html#field-types-table
    """

    class Meta:
        """
        Model configuration is kept namespaced in a special class called Meta. This convention is borrowed from Django.
        Meta configuration is passed on to subclasses, so our project's models will all subclass BaseModel.
        There are many different attributes you can configure using Model.Meta.

        Model options and table metadata
        https://docs.peewee-orm.com/en/latest/peewee/models.html#model-options-and-table-metadata
        Primary Keys, Composite Keys and other Tricks
        https://docs.peewee-orm.com/en/latest/peewee/models.html#primary-keys-composite-keys-and-other-tricks
        """

        database = DATABASE
        legacy_table_names = False
