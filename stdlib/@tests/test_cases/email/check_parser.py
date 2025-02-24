from email.message import Message, EmailMessage
from email.parser import BytesParser, Parser
import email.policy
from typing import assert_type

p1 = Parser()
p2 = Parser(policy=email.policy.default)

assert_type(p1, Parser[Message[str, str]])
assert_type(p2, Parser[EmailMessage])

bp1 = BytesParser()
bp2 = BytesParser(policy=email.policy.default)

assert_type(bp1, BytesParser[Message[str, str]])
assert_type(bp2, BytesParser[EmailMessage])
