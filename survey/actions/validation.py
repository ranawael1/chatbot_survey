def agree_status(data):
    if data.isnumeric():
        data = int(data)
        if data >= 1 and data <= 5:
            return data
        else:
            return None
    else:
        return None


