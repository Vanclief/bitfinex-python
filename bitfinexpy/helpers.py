class Helper(object):
    def to_float(d):
        """
        Strings to Float from response
        """
        if type(d) is dict:
            for key, value in d.items():
                if type(value) is str:
                    d[key] = float(value)

        return d
