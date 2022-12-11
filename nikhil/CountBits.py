import  re
class UserMaincode(object):
    @classmethod
    def historyDocuments(cls,input1):
        '''

        :param input1: string
        :return: int
        '''
        match = re.findall(r'\d{2}-\d{2}-\d{4}', input1)
        match = [int(i[-4:]) for i in match]
        return len(set(match))

