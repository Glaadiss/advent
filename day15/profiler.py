import cProfile
from pstats import Stats, SortKey

from task import main


if __name__ == "__main__":
    do_profiling = True
    if do_profiling:
        with cProfile.Profile() as pr:
            main()

        with open("profiling_stats.txt", "w") as stream:
            stats = Stats(pr, stream=stream)
            stats.strip_dirs()
            stats.sort_stats("time")
            stats.dump_stats(".prof_stats")
            stats.print_stats()
