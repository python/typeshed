from _typeshed import Incomplete

NS: Incomplete

class DocumentMetadata:
    title: Incomplete
    authors: Incomplete
    description: Incomplete
    keywords: Incomplete
    generator: Incomplete
    created: Incomplete
    modified: Incomplete
    attachments: Incomplete
    lang: Incomplete
    custom: Incomplete
    xmp_metadata: Incomplete
    def __init__(
        self,
        title=None,
        authors=None,
        description=None,
        keywords=None,
        generator=None,
        created=None,
        modified=None,
        attachments=None,
        lang=None,
        custom=None,
        xmp_metadata=None,
    ) -> None: ...
    def include_in_pdf(self, pdf, variant, version, conformance, compress) -> None: ...
    def generate_rdf_metadata(self, variant, version, conformance): ...
