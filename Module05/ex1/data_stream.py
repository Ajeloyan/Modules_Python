from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class StreamDataError(Exception):
    pass


class StreamExistsError(Exception):
    pass


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.type = "Generic"
        self.processed_items = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if not criteria:
            return data_batch
        return [
            item for item in data_batch
            if criteria.lower() in str(item).lower()
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "id": self.stream_id,
            "type": self.type,
            "processed": self.processed_items,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temps = []
            alerts = 0
            for item in data_batch:
                if isinstance(item, str) and "temp:" in item:
                    val = float(item.split(":")[1])
                    temps.append(val)
                    if val > 30:
                        alerts += 1

            avg_temp = sum(temps) / len(temps) if temps else 0.0
            self.processed_items += len(data_batch)
            res = (f"Sensor analysis: {len(data_batch)} "
                   f"readings processed, avg temp: {avg_temp:.1f}°C")
            if alerts > 0:
                res += f" ({alerts} extreme values!)"
            return res
        except (ValueError, IndexError):
            raise StreamDataError("Invalid sensor data format")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "critical":
            return [d for d in data_batch if isinstance(d, str)
                    and "temp:" in d and float(d.split(":")[1]) > 30]
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            net_flow = 0
            for item in data_batch:
                action, val = str(item).split(":")
                amount = int(val)
                if action == "buy":
                    net_flow += amount
                elif action == "sell":
                    net_flow -= amount

            self.processed_items += len(data_batch)
            sign = "+" if net_flow > 0 else ""
            return (
                f"Transaction analysis: {len(data_batch)} "
                f"operations, net flow: {sign}{net_flow} units"
            )
        except (ValueError, IndexError):
            raise StreamDataError("Invalid transaction data format")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "large":
            return [d for d in data_batch if isinstance(d, str)
                    and ":" in d and int(d.split(":")[1]) >= 100]
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        sing_plur = ""
        errors = len([e for e in data_batch if "error" in str(e).lower()])
        if errors > 1:
            sing_plur = "errors"
        else:
            sing_plur = "error"
        self.processed_items += len(data_batch)
        return (
            f"Event analysis: {len(data_batch)} events, "
            f"{errors} {sing_plur} detected"
        )


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        if any(s.stream_id == stream.stream_id for s in self.streams):
            raise StreamExistsError(f"Stream {stream.stream_id} "
                                    f"already exists")
        self.streams.append(stream)

    def process_all(self, data_map: Dict[str, List[Any]]) -> None:
        for stream in self.streams:
            try:
                batch = data_map.get(stream.stream_id, [])
                stream.process_batch(batch)

                prefix = stream.type.split()[0]
                unit = ('readings' if prefix == 'Sensor' else
                        'operations' if prefix == 'Financial' else 'events')
                print(f"- {prefix} data: {len(batch)} {unit} processed")
            except StreamDataError as e:
                print(f"Error: {e}")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    print("Initializing Sensor Stream...")
    s1 = SensorStream("SENSOR_001")
    print(f"Stream ID: {s1.stream_id}, Type: {s1.type}")
    s1_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: [{', '.join(s1_data)}]")
    print(s1.process_batch(s1_data))

    print("\nInitializing Transaction Stream...")
    t1 = TransactionStream("TRANS_001")
    print(f"Stream ID: {t1.stream_id}, Type: {t1.type}")
    t1_data = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: [{', '.join(t1_data)}]")
    print(t1.process_batch(t1_data))

    print("\nInitializing Event Stream...")
    e1 = EventStream("EVENT_001")
    print(f"Stream ID: {e1.stream_id}, Type: {e1.type}")
    e1_data = ["login", "error", "logout"]
    print(f"Processing event batch: [{', '.join(e1_data)}]")
    print(e1.process_batch(e1_data))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print()
    processor = StreamProcessor()
    for s in [s1, t1, e1]:
        processor.add_stream(s)

    mixed_data = {
        "SENSOR_001": ["temp:20.0", "temp:25.0"],
        "TRANS_001": ["buy:50", "buy:50", "sell:20", "buy:10"],
        "EVENT_001": ["login", "error", "logout"],
    }

    print("Batch 1 Results:")
    processor.process_all(mixed_data)

    print("\nStream filtering active: High-priority data only")
    raw_sensors = ["temp:22.5", "temp:35.0", "temp:42.1"]
    raw_transactions = ["buy:50", "sell:150", "buy:10"]

    critical_alerts = s1.filter_data(raw_sensors, criteria="critical")
    large_trans = t1.filter_data(raw_transactions, criteria="large")

    print(f"Filtered results: {len(critical_alerts)} critical sensor alerts, "
          f"{len(large_trans)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
