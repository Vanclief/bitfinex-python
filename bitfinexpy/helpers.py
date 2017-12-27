class Helper(object):

    def dict_to_float(self, d):
        """
        Converts all strings to floats from a dict
        """
        if type(d) is dict:
            for key, value in d.items():
                if type(value) is str:
                    try:
                        d[key] = float(value)
                    except ValueError:
                        d[key] = value

        return d

    def list_dict_to_float(self, l):
        """
        Applies dict_to_float to all elements from a list
        """

        for d in l:
            d = self.dict_to_float(d)

        return l
