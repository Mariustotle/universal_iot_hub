

from typing import Any, Dict
from common.environment import Env
from peripherals.contracts.pins.pin_position import PinPosition

class DisplayHelper:

    @staticmethod
    def print_pin_table(pins: Dict[PinPosition, Any], name:str):
        Env.clear_screan()
        Env.print_paragraph(
             '-------------------------------------------------------------',
            f'This is the pin layout for [{name}]',
             '------------------------------------------------------------',
             'Turn the board so that the majority of the pins are at the bottom side of the board.',
             '')

        # Determine min/max range for both axes
        all_h = [p.horizontal_position for p in pins.keys()]
        all_v = [p.vertical_position for p in pins.keys()]
        min_h, max_h = min(all_h), max(all_h)
        min_v, max_v = min(all_v), max(all_v)

        # Build a 2D matrix of cell values (as strings)
        grid = {}
        for v in range(min_v, max_v + 1):
            grid[v] = []
            for h in range(min_h, max_h + 1):
                pin = next((pins[pos] for pos in pins if pos.horizontal_position == h and pos.vertical_position == v), None)
                cell_value = getattr(pin, "label", str(pin)) if pin else "N/A"
                grid[v].append(str(cell_value))

        # Determine column widths dynamically
        num_cols = max_h - min_h + 1
        col_widths = []
        for col_idx in range(num_cols):
            col_cells = [grid[v][col_idx] for v in grid]  # values in this column
            header_label = str(min_h + col_idx)
            max_len = max(len(header_label), *(len(c) for c in col_cells))
            col_widths.append(max_len + 2)  # padding for spacing

        # Build header row
        header_cells = [f"{(min_h + i):^{col_widths[i]}}" for i in range(num_cols)]
        header = "     " + "".join(header_cells)
        Env.print(header)
        Env.print("   " + "-" * (len(header) - 3))

        # Print each row
        for v in range(min_v, max_v + 1):
            row_cells = [
                f"{grid[v][i]:^{col_widths[i]}}" for i in range(num_cols)
            ]
            Env.print(f"{v:<3} |" + "".join(row_cells))


        Env.print()
        