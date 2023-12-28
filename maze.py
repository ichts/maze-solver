from cell import Cell
import time


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(1, self._num_cols + 1):
            cell_col = []
            self._cells.append(cell_col)
            for j in range(1, self._num_rows + 1):
                self._draw_cell(i, j)
                cell_col.append(Cell(self._win))

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        cell_x1 = self._x1 + self._cell_size_x * (i - 1)
        cell_y1 = self._y1 + self._cell_size_y * (j - 1)
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y2 = cell_y1 + self._cell_size_y

        cell = Cell(self._win)
        cell.draw(cell_x1, cell_y1, cell_x2, cell_y2)

        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)