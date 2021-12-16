import csv

fieldnames = ['input_1', 'input_2', 'operation', 'result']


class Write:
    @staticmethod
    def ToCSV(filename, data: dict):
        f = open(filename, 'a', newline='')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(data)
        f.close()
