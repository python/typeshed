from _typeshed import Incomplete

import pyqtgraph as pg

class DataSource:
    rate: Incomplete
    period: Incomplete
    neg_period: Incomplete
    start_time: float
    sample_idx: int
    def __init__(
        self, sample_rate: float = 200.0, signal_period: float = 0.55, negative_period=None, max_length: int = 300
    ) -> None: ...
    def start(self, timestamp) -> None: ...
    def get_data(self, timestamp, max_length: int = 6000): ...

class MainWindow(pg.GraphicsLayoutWidget):
    top_plot: Incomplete
    traces: Incomplete
    timer: Incomplete
    last_update: Incomplete
    mean_dt: Incomplete
    def __init__(self) -> None: ...
    def update(self) -> None: ...

main_window: Incomplete
