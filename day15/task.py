import numpy as np
import re

MAX = 4000000


def main():
    with open("./day15/input.txt") as input:
        lines = [line.replace("\n", "") for line in input.readlines()]
        sb_pairs = [re.findall("-?\d+\.?\d*", line) for line in lines]

        sb_pairs = [
            (int(s_x), int(s_y), int(b_x), int(b_y))
            for (s_x, s_y, b_x, b_y) in sb_pairs
        ]

        sb_pairs = [
            (s_x, s_y, b_x, b_y, abs(s_x - b_x) + abs(s_y - b_y))
            for (s_x, s_y, b_x, b_y) in sb_pairs
        ]

        ys = np.array(list(range(MAX)))

        d_ys = []
        for s_x, s_y, _, _, max_size in sb_pairs:
            dy = np.abs(s_y - ys)
            x_len = max_size - dy
            start_end = np.where(
                x_len > 0,
                (np.maximum(s_x - x_len, 0), np.minimum(s_x + x_len, MAX)),
                None,
            )
            d_ys.append(start_end)

        for y in range(MAX):
            ranges = []
            for i, (s_x, s_y, b_x, b_y, max_size) in enumerate(sb_pairs):
                min_max = d_ys[i]
                start_end = (min_max[0][y], min_max[1][y])
                if start_end != (None, None):
                    ranges.append(start_end)

            f, t = 0, 0
            for i, j in sorted(ranges):
                if i > t:
                    print(t + 1, y)
                    return
                f = max(f, i)
                t = max(t, j)


if __name__ == "__main__":
    main()
