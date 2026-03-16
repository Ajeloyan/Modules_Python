from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        nums_len: int = len(data)
        nums_sum: int = 0
        for unit in data:
            nums_sum += unit
        nums_avg: float = nums_sum / nums_len
        return (f"Processed {nums_len} numeric values, "
                f"sum={nums_sum}, avg={nums_avg}")

    def validate(self, data: Any) -> bool:
        for unit in data:
            if unit.__class__.__name__ != "int":
                return False
        return True


class TextProcessor(DataProcessor):

    @staticmethod
    def is_word_character(c: str) -> bool:
        return ('a' <= c <= 'z' or 'A' <= c <=
                'Z' or '0' <= c <= '9' or c == '_')

    def word_count(self, str: str) -> int:
        c = 0
        for i in range(1, len(str)):
            if (not self.is_word_character(str[i]) and
                    self.is_word_character(str[i-1])):
                c += 1
        if self.is_word_character(str[-1]):
            c += 1
        return c

    def process(self, data: Any) -> str:
        text_len: int = len(data)
        nb_words: int = self.word_count(data)
        return f"Processed text: {text_len} characters, {nb_words} words"

    def validate(self, data: Any) -> bool:
        if data.__class__.__name__ == "str":
            return True
        return False


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        result: str = ""
        level: str = ""
        type_log: str = ""
        error_info: str = ""
        if "ERROR:" in data or "INFO:" in data:
            type_log, error_info = data.split(":", 1)
            if "INFO:" in data:
                level = "[INFO]"
            if "ERROR:" in data:
                level = "[ALERT]"
        result = f"{level}: {type_log} level detected:{error_info}"
        return result

    def validate(self, data: Any) -> bool:
        if data.__class__.__name__ == "str":
            if "ERROR:" in data or "INFO:" in data:
                return True
        return False


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    num_p = NumericProcessor()
    print("Initializing Numeric Processor...")
    nums: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {nums}")
    try:
        if num_p.validate(nums) is True:
            print("Validation: Numeric data verified")
            print(f"Output: {num_p.format_output(num_p.process(nums))}")
        else:
            print("Validation: Error, lits[int] excepted")
    except Exception as e:
        print(e)
    print()

    text_p = TextProcessor()
    print("Initializing Text Processor...")
    text: str = "Hello Nexus World"
    print(f"Processing data: \"{text}\"")
    try:
        if text_p.validate(text) is True:
            print("Validation: Text data verified")
            print(f"Output: {text_p.format_output(text_p.process(text))}")
        else:
            print("Validation: Error, str excepted")
    except Exception as e:
        print(e)
    print()

    log_p = LogProcessor()
    print("Initializing Log Processor...")
    log = "ERROR: Connection timeout"
    print(f"Processing data: \"{log}\"")
    try:
        if log_p.validate(log) is True:
            print("Validation: Log entry verified")
            print(f"Output: {log_p.format_output(log_p.process(log))}")
        else:
            print("Validation: Error, 'ERROR:' or 'INFO:' excepted")
    except Exception as e:
        print(e)
    print()

    print("=== Polymorphic Processing Demo ===")
    print()
    print("Processing multiple data types through same interface...")
    pro: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    tests: List[Any] = [
        [0, 2, 4],
        "Hello world!",
        "INFO: System ready"
    ]
    for index in range(len(pro)):
        if pro[index].validate(tests[index]) is True:
            print(
                f"Result {index + 1}: "
                f"{pro[index].format_output(pro[index].process(tests[index]))}"
                )


if __name__ == "__main__":
    main()
