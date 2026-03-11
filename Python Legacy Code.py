class ComputeStatistics:

    def compute_stats(self, file):
        total = 0
        sum_val = 0
        average = 0
        min_val = 0
        max_val = 0

        try:
            with open(file, 'r') as f:
                line = f.readline().strip()
                first_line = int(line)

                min_val = first_line
                max_val = first_line

                while line:
                    num = int(line)

                    total += 1
                    sum_val += num

                    if min_val > num:
                        min_val = num

                    if max_val < num:
                        max_val = num

                    line = f.readline().strip()

            print("total =", total)
            print("summation =", sum_val)
            print("average =", round(sum_val / total))
            print("Minimum =", min_val)
            print("Maximum =", max_val)

        except IOError as e:
            print(e)

if __name__ == "__main__":
    cs = ComputeStatistics()
    cs.compute_stats("random_nums.txt")