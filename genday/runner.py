from curses import wrapper


def run_evolution(population):

    def main(stdscr):
        stdscr.clear()

        while True:
            stdscr.addstr(0, 0, str(population))
            stdscr.refresh()
            population.cycle()

        stdscr.getkey()

    wrapper(main)
