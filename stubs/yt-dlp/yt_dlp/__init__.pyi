import optparse
from collections.abc import Callable, Collection, Iterator, Mapping
from typing import Literal, NamedTuple, Protocol, TypedDict, type_check_only
from typing_extensions import NotRequired

from .extractor import gen_extractors, list_extractors
from .networking.impersonate import ImpersonateTarget
from .YoutubeDL import YoutubeDL

__all__ = ["YoutubeDL", "gen_extractors", "list_extractors", "main", "parse_options"]

@type_check_only
class _LoggerProtocol(Protocol):  # noqa: Y046
    def __init__(self, ydl: YoutubeDL | None = None) -> None: ...
    def debug(self, message: str) -> None: ...
    def info(self, message: str) -> None: ...
    def warning(self, message: str, *, once: bool = ..., only_once: bool = ...) -> None: ...
    def error(self, message: str) -> None: ...
    def stdout(self, message: str) -> None: ...
    def stderr(self, message: str) -> None: ...

@type_check_only
class _RetrySleepFunctions(TypedDict):
    default: NotRequired[Callable[[int], int]]
    file_access: NotRequired[Callable[[int], int]]
    fragment: NotRequired[Callable[[int], int]]

@type_check_only
class _ProgressTemplateValue(TypedDict):  # noqa: Y049
    info: NotRequired[str]
    progress: NotRequired[str]

@type_check_only
class _ExternalDownloader(TypedDict):
    dash: NotRequired[str]
    default: NotRequired[str]
    ftp: NotRequired[str]
    http: NotRequired[str]
    m3u8: NotRequired[str]
    mms: NotRequired[str]
    rtmp: NotRequired[str]
    rtsp: NotRequired[str]

@type_check_only
class _DownloadRange(TypedDict):
    end_time: int
    index: NotRequired[int]
    start_time: int
    title: NotRequired[str]

@type_check_only
class _Color(TypedDict):
    stderr: NotRequired[Literal["always", "auto", "no_color", "never"]]
    stdout: NotRequired[Literal["always", "auto", "no_color", "never"]]

_ProgressTemplate = TypedDict(
    "_ProgressTemplate",
    {
        "download": _ProgressTemplateValue,
        "download-title": _ProgressTemplateValue,
        "postprocess": _ProgressTemplateValue,
        "postprocess-title": _ProgressTemplateValue,
    },
)

@type_check_only
class _Params(TypedDict):
    usenetrc: NotRequired[bool | None]
    netrc_location: NotRequired[str | None]
    netrc_cmd: NotRequired[str | None]
    username: NotRequired[str | None]
    password: NotRequired[str | None]
    twofactor: NotRequired[str | None]
    videopassword: NotRequired[str | None]
    ap_mso: NotRequired[str | None]
    ap_username: NotRequired[str | None]
    ap_password: NotRequired[str | None]
    client_certificate: NotRequired[str | None]
    client_certificate_key: NotRequired[str | None]
    client_certificate_password: NotRequired[str | None]
    quiet: NotRequired[bool | None]
    no_warnings: NotRequired[bool | None]
    forceurl: NotRequired[bool | None]
    forcetitle: NotRequired[str | None]
    forceid: NotRequired[bool | None]
    forcethumbnail: NotRequired[bool | None]
    forcedescription: NotRequired[bool | None]
    forceduration: NotRequired[str | None]
    forcefilename: NotRequired[bool | None]
    forceprint: NotRequired[Mapping[str, Collection[str]] | Collection[str] | None]
    print_to_file: NotRequired[Mapping[str, tuple[str, str]] | None]
    forcejson: NotRequired[bool | None]
    dump_single_json: NotRequired[bool | None]
    force_write_download_archive: NotRequired[str | None]
    simulate: NotRequired[str | None]
    skip_download: NotRequired[str | None]
    format: NotRequired[str | Callable[[Mapping[str, object]], Mapping[str, object]] | None]
    allow_unplayable_formats: NotRequired[bool | None]
    ignore_no_formats_error: NotRequired[bool | None]
    format_sort: NotRequired[Collection[str] | None]
    format_sort_force: NotRequired[str | None]
    allow_multiple_video_streams: NotRequired[bool | None]
    allow_multiple_audio_streams: NotRequired[bool | None]
    check_formats: NotRequired[bool | Literal["selected"] | None]
    listformats: NotRequired[bool | None]
    outtmpl: NotRequired[str | Mapping[str, str] | None]
    outtmpl_na_placeholder: NotRequired[str | None]
    paths: NotRequired[str | None]
    restrictfilenames: NotRequired[bool | None]
    windowsfilenames: NotRequired[bool | None]
    ignoreerrors: NotRequired[bool | Literal["only_download"] | None]
    force_generic_extractor: NotRequired[bool | None]
    allowed_extractors: NotRequired[Collection[str] | None]
    ratelimit: NotRequired[int | None]
    throttledratelimit: NotRequired[int | None]
    overwrites: NotRequired[bool | None]
    retries: NotRequired[int | None]
    file_access_retries: NotRequired[int | None]
    fragment_retries: NotRequired[int | None]
    extractor_retries: NotRequired[int | None]
    retry_sleep_functions: NotRequired[_RetrySleepFunctions | None]
    skip_unavailable_fragments: NotRequired[bool | None]
    keep_fragments: NotRequired[bool | None]
    concurrent_fragment_downloads: NotRequired[int | None]
    buffersize: NotRequired[int | None]
    noresizebuffer: NotRequired[bool | None]
    http_chunk_size: NotRequired[int | None]
    continuedl: NotRequired[bool | None]
    noprogress: NotRequired[bool | None]
    progress_with_newline: NotRequired[bool | None]
    progress_template: NotRequired[_ProgressTemplate | None]
    playliststart: NotRequired[int | None]
    playlistend: NotRequired[int | None]
    playlistreverse: NotRequired[bool | None]
    playlistrandom: NotRequired[bool | None]
    lazy_playlist: NotRequired[bool | None]
    noplaylist: NotRequired[bool | None]
    logtostderr: NotRequired[bool | None]
    consoletitle: NotRequired[str | None]
    nopart: NotRequired[bool | None]
    updatetime: NotRequired[bool | None]
    writedescription: NotRequired[bool | None]
    writeannotations: NotRequired[bool | None]
    writeinfojson: NotRequired[bool | None]
    allow_playlist_files: NotRequired[bool | None]
    clean_infojson: NotRequired[bool | None]
    getcomments: NotRequired[bool | None]
    writethumbnail: NotRequired[bool | None]
    write_all_thumbnails: NotRequired[bool | None]
    writelink: NotRequired[bool | None]
    writeurllink: NotRequired[bool | None]
    writewebloclink: NotRequired[bool | None]
    writedesktoplink: NotRequired[bool | None]
    writesubtitles: NotRequired[bool | None]
    writeautomaticsub: NotRequired[bool | None]
    allsubtitles: NotRequired[bool | None]
    listsubtitles: NotRequired[bool | None]
    subtitlesformat: NotRequired[str | None]
    subtitleslangs: NotRequired[Collection[str] | None]
    matchtitle: NotRequired[bool | None]
    rejecttitle: NotRequired[bool | None]
    prefer_free_formats: NotRequired[bool | None]
    trim_file_name: NotRequired[int | None]
    verbose: NotRequired[bool | None]
    test: NotRequired[bool | None]
    keepvideo: NotRequired[str | None]
    min_filesize: NotRequired[int | None]
    max_filesize: NotRequired[int | None]
    min_views: NotRequired[str | None]
    max_views: NotRequired[str | None]
    daterange: NotRequired[str | None]
    cachedir: NotRequired[str | None]
    age_limit: NotRequired[str | None]
    download_archive: NotRequired[str | None]
    break_on_existing: NotRequired[str | None]
    break_on_reject: NotRequired[bool | None]
    break_per_url: NotRequired[bool | None]
    skip_playlist_after_errors: NotRequired[bool | None]
    cookiefile: NotRequired[str | None]
    cookiesfrombrowser: NotRequired[tuple[str, ...] | None]
    legacyserverconnect: NotRequired[bool | None]
    nocheckcertificate: NotRequired[bool | None]
    prefer_insecure: NotRequired[str | None]
    enable_file_urls: NotRequired[str | None]
    http_headers: NotRequired[Mapping[str, str] | None]
    proxy: NotRequired[str | None]
    socket_timeout: NotRequired[int | None]
    bidi_workaround: NotRequired[bool | None]
    debug_printtraffic: NotRequired[bool | None]
    prefer_ffmpeg: NotRequired[bool | None]
    include_ads: NotRequired[bool | None]
    default_search: NotRequired[str | None]
    dynamic_mpd: NotRequired[bool | None]
    extractor_args: NotRequired[Mapping[str, Mapping[str, object]] | None]
    youtube_include_dash_manifest: NotRequired[bool | None]
    youtube_include_hls_manifest: NotRequired[bool | None]
    encoding: NotRequired[str | None]
    extract_flat: NotRequired[bool | Literal["in_playlist", "discard", "discard_in_playlist"] | None]
    live_from_start: NotRequired[bool | None]
    wait_for_video: NotRequired[tuple[int, int] | None]
    mark_watched: NotRequired[bool | None]
    merge_output_format: NotRequired[str | None]
    final_ext: NotRequired[str | None]
    postprocessors: NotRequired[Collection[Mapping[str, object]]]
    fixup: NotRequired[Literal["never", "warn", "detect_or_warn"] | None]
    source_address: NotRequired[str | None]
    call_home: NotRequired[bool | None]
    sleep_interval_requests: NotRequired[int | None]
    sleep_interval: NotRequired[int | None]
    max_sleep_interval: NotRequired[int | None]
    sleep_interval_subtitles: NotRequired[int | None]
    external_downloader: NotRequired[_ExternalDownloader | None]
    download_ranges: NotRequired[Callable[[object, YoutubeDL], Iterator[_DownloadRange]] | None]
    force_keyframes_at_cuts: NotRequired[bool | None]
    list_thumbnails: NotRequired[str | None]
    playlist_items: NotRequired[Collection[int] | None]
    xattr_set_filesize: NotRequired[bool | None]
    match_filter: NotRequired[
        Callable[[Mapping[str, object], bool], str | None] | Callable[[Mapping[str, object]], str | None] | None
    ]
    color: NotRequired[_Color | None]
    ffmpeg_location: NotRequired[str | None]
    hls_prefer_native: NotRequired[bool | None]
    hls_use_mpegts: NotRequired[bool | None]
    hls_split_discontinuity: NotRequired[bool | None]
    max_downloads: NotRequired[int | None]
    dump_intermediate_pages: NotRequired[bool | None]
    listformats_table: NotRequired[bool | None]
    write_pages: NotRequired[bool | None]
    external_downloader_args: NotRequired[Literal["default"] | Mapping[str, Collection[str]] | Collection[str] | None]
    postprocessor_args: NotRequired[Mapping[str, Collection[str]] | Collection[str] | None]
    geo_verification_proxy: NotRequired[str | None]
    geo_bypass: NotRequired[bool | None]
    geo_bypass_country: NotRequired[str | None]
    geo_bypass_ip_block: NotRequired[str | None]
    compat_opts: NotRequired[dict[str, object] | None]
    # Undocumented fields below.
    _deprecation_warnings: NotRequired[Collection[str] | None]
    _warnings: NotRequired[Collection[str] | None]
    autonumber_size: NotRequired[int | None]
    autonumber_start: NotRequired[int | None]
    cn_verification_proxy: NotRequired[str | None]
    forceformat: NotRequired[object]
    load_pages: NotRequired[bool | None]
    logger: NotRequired[_LoggerProtocol]
    youtube_print_sig_code: NotRequired[bool | None]
    progress_hooks: NotRequired[list[Callable[[object], object]]]
    impersonate: NotRequired[ImpersonateTarget]

@type_check_only
class _ParsedOptions(NamedTuple):
    parser: optparse.OptionParser
    options: optparse.Values
    urls: Collection[str]
    ydl_opts: _Params

def parse_options(argv: Collection[str] | None = ...) -> _ParsedOptions: ...
def main(argv: list[str] | None = ...) -> int: ...
