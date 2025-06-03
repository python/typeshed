from collections.abc import Callable, Collection, Mapping, Sequence
from concurrent.futures.thread import ThreadPoolExecutor

from ..extractor.common import _InfoDict
from .common import FileDownloader
from .http import HttpFD

class HttpQuietDownloader(HttpFD):
    def to_screen(self, *args: object, **kargs: object) -> None: ...
    to_console_title = to_screen

class FragmentFD(FileDownloader):
    def report_retry_fragment(self, err: str, frag_index: int, count: int, retries: int) -> None: ...
    def report_skip_fragment(self, frag_index: int, err: str | None = None) -> None: ...
    def decrypter(self, info_dict: _InfoDict) -> Callable[[Mapping[str, object], bytes], bytes]: ...
    def download_and_append_fragments_multiple(self, *args: object, **kwargs: object) -> bool: ...
    def download_and_append_fragments(
        self,
        ctx: Mapping[str, object],
        fragments: Collection[Mapping[str, object]],
        info_dict: _InfoDict,
        *,
        is_fatal: Callable[[int], bool] = ...,
        pack_func: Callable[[str, int], bytes] = ...,
        finish_func: Callable[[], object] | None = None,
        tpe: ThreadPoolExecutor | None = None,
        interrupt_trigger: Sequence[bool] = (True,),
    ) -> bool: ...
