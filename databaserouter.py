class GeodataRouter:
    """
    A router to control all database operations on models in the geodata application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read geodata models go to `geodata` database.
        """
        if model._meta.app_label == 'geodata':
            return 'geodata'
        return None

    # def db_for_write(self, model, **hints):
    #    """
    #    Attempts to write into `geodata` database.
    #    """
    #    if model._meta.app_label == 'geodata':
    #        return 'geodata'
    #    return None

    # def allow_relation(self, obj1, obj2, **hints):
    #    """
    #    Allow relations if a model in the `geodata` app is involved.
    #    """
    #    if obj1._meta.app_label == 'user_data' or \
    #       obj2._meta.app_label == 'user_data':
    #        return True
    #    return None

    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #    """
    #    Make sure the auth app only appears in the 'geodata' database.
    #    """
    #    if app_label == 'geodata':
    #        return db == 'geodata'
    #    return None
