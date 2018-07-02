from curses import wrapper, echo
from memo_number import MemoNumber

def refresh(stdscr):
    stdscr.clear()
    stdscr.refresh()

def print_to_curse(stdscr, string):
    stdscr.addstr(string)
    stdscr.refresh()
    stdscr.getkey()

def main(stdscr):
    MEMO = 0
    REMEMO = 1
    END = 0

    memo = MemoNumber(10, 10)
    refresh(stdscr)
    # Memorisation
    while(memo.get_mode() == MEMO):
        stdscr.addstr(memo.get_number())
        stdscr.getkey()
        refresh(stdscr)

    # Verif memo
    echo()
    while memo.get_mode() == REMEMO:
        stdscr.addstr("answer:")
        stdscr.refresh()
        number = stdscr.getstr().decode(encoding="utf-8")
        l.append(number)
        rep = memo.check_number(number)
        refresh(stdscr)
        print_to_curse(stdscr, str(rep))
        if not rep:
            print_to_curse(stdscr, f"Bonne reponse: {memo.file_number[memo.counter_answer - 1]}")
            stdscr.clear()
    stdscr.addstr(f"nonbre de bonne reponse: {str(memo.nb_good_answer)}")
    stdscr.getkey()
    refresh(stdscr)

wrapper(main)
