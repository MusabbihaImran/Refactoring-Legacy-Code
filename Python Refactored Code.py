"""
This is a sample Python program.
It demonstrates refactored code.
"""

class ComputeStatistics:
    """
    Class to compute statistics from a file containing integers.
    """

    def __init__(self, file):
        """
        Constructor to store file path.

        :param file: path of file containing numbers
        """
        self.file = file

    def read_int(self):
        """
        Read integer values from file and return a list.

        :return: list of integers
        """
        data = []

        try:
            with open(self.file, 'r') as f:
                for line in f:
                    num = int(line.strip())
                    data.append(num)

        except IOError as e:
            print(e)

        return data

    def count(self):
        """
        Return total numbers in file.
        """
        data = self.read_int()
        return len(data)

    def summation(self):
        """
        Return sum of all integers.
        """
        data = self.read_int()
        total = 0

        for x in data:
            total += x

        return total

    def average(self):
        """
        Return average value.
        """
        total = self.summation()
        count = self.count()

        return total / count

    def minimum(self):
        """
        Return minimum value.
        """
        data = self.read_int()
        return min(data)

    def maximum(self):
        """
        Return maximum value.
        """
        data = self.read_int()
        return max(data)


if __name__ == "__main__":

    file = "random_nums.txt"

    cs = ComputeStatistics(file)

    print("The values are:", cs.read_int())
    print("Total values in file are:", cs.count())
    print("Summation of data is:", cs.summation())
    print("Average of data is:", cs.average())
    print("Minimum value from data is:", cs.minimum())
    print("Maximum value from data is:", cs.maximum())