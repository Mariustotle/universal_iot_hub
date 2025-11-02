from typing import List
from common.environment import Env
from peripherals.contracts.pins.pin_display import PinDisplay


class DisplayHelper:

    @staticmethod
    def print_pin_table(pin_matrix: List[List['PinDisplay']], name: str, color:str):
        Env.clear_screan()
        Env.print_paragraph(
            '-------------------------------------------------------------',
            f'This is the pin layout for [{name}]',
            '-------------------------------------------------------------',
            'Turn the board so that the majority of the pins are at the bottom side of the board.',
            ''
        )

        if not pin_matrix or not any(pin_matrix):
            Env.print("No pins available to display.")
            return

        # Determine matrix dimensions
        num_rows = len(pin_matrix)
        num_cols = max(len(row) for row in pin_matrix)

        # Determine column widths dynamically
        col_widths = []
        for col_idx in range(num_cols):
            max_length:int = None
            for row in pin_matrix:
                item = row[col_idx]
                item_text = str(item) if item else "N/A"
                item_length = len(item_text)

                if (max_length is None or item_length > max_length):
                    max_length = item_length

            col_widths.append(max_length + 2)

        # Header row
        header_cells = [f"{i+1:^{col_widths[i]}}" for i in range(num_cols)]
        header = "     " + "".join(header_cells)
        Env.print(header)
        Env.print("   " + "-" * (len(header) - 3))

        # Print each row
        for row_idx in range(num_rows):
            Env.print(f"{row_idx+1:<3} ", keep_same_line=True)

            for col_idx in range(num_cols):

                item = pin_matrix[row_idx][col_idx]
                item_text = str(item) if item else "N/A"
            
                if (not item.in_use):
                    Env.print(f"{item_text:^{col_widths[col_idx]}}", keep_same_line=True)
                else:
                    Env.print(f"{item_text:^{col_widths[col_idx]}}", keep_same_line=True, color=color)

            Env.print()


        Env.print()
