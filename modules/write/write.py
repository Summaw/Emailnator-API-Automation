import sys
import colorama
import time

def write(text: str, case: str) -> None:
    current_time = time.strftime("%H:%M:%S", time.localtime())
    switcher = {
        'info': _write_info,
        'success': _write_success,
        'error': _write_error
    }
    func = switcher.get(case.lower(), lambda x, y: None)
    func(current_time, text)

def _write_info(current_time, text):
    sys.stdout.write(f"[{colorama.Fore.BLUE}{current_time}{colorama.Style.RESET_ALL}] {colorama.Fore.YELLOW}[INFO]{colorama.Style.RESET_ALL} {colorama.Fore.WHITE}{text}{colorama.Style.RESET_ALL}\n")
    sys.stdout.flush()

def _write_success(current_time, text):
    sys.stdout.write(f"[{colorama.Fore.BLUE}{current_time}{colorama.Style.RESET_ALL}] {colorama.Fore.GREEN}[SUCCESS]{colorama.Style.RESET_ALL} {colorama.Fore.WHITE}{text}{colorama.Style.RESET_ALL}\n")
    sys.stdout.flush()

def _write_error(current_time, text):
    sys.stdout.write(f"[{colorama.Fore.BLUE}{current_time}{colorama.Style.RESET_ALL}] {colorama.Fore.RED}[ERROR]{colorama.Style.RESET_ALL} {colorama.Fore.WHITE}{text}{colorama.Style.RESET_ALL}\n")
    sys.stdout.flush()