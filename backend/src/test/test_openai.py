import os

from dotenv import load_dotenv
from module.parser.openai import OpenAIParser

load_dotenv()


class TestOpenAIParser:
    @classmethod
    def setup_class(cls):
        api_key = os.getenv("OPENAI_API_KEY")
        cls.parser = OpenAIParser(api_key=api_key)

    def test_parse(self):
        text = "[梦蓝字幕组]New Doraemon 哆啦A梦新番[747][2023.02.25][AVC][1080P][GB_JP][MP4]"
        result = self.parser.parse(text=text)
        assert result == "XXX"
