from __future__ import annotations

from typing_extensions import assert_type
from xml.etree.ElementTree import Element

from markdown.inlinepatterns import DelimiterProcessor, EvaluatedText


def check_delimiter_cache(processor: DelimiterProcessor, data: str, pos: int) -> None:
    processor.build_cache(data)
    assert_type(processor.get_cached_result(), tuple[Element, int, int])
    assert_type(processor.get_cached_result(pos), tuple[Element, int, int])
    assert_type(processor.get_cached_result(None), tuple[Element, int, int])


assert_type(EvaluatedText("text"), EvaluatedText)
