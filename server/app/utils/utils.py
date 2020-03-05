class Utils():
    @staticmethod
    def arrayKeysExists(data, keys):
        keys_exists = True
        
        for key in keys:
            if key in data.keys():
                keys_exists = True
            else:
                keys_exists = False
                break

        return keys_exists