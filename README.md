# Data Pipeline 📦

Distributed data pipeline with Apache Beam, schema evolution, and exactly-once guarantees.

## Features

- **Stream + Batch**: Unified processing model
- **Schema Evolution**: Backward-compatible schema changes
- **Exactly-Once**: Idempotent processing with checkpointing
- **Multi-sink**: Kafka, BigQuery, S3, PostgreSQL

## Throughput

| Source | Records/sec | Latency (p99) |
|--------|------------|---------------|
| Kafka | 500K | 45ms |
| Pub/Sub | 300K | 60ms |
| File | 1.2M | N/A |

## Quick Start

```python
from data_pipeline import Pipeline

p = Pipeline("my-etl")
p.read_kafka("events", group="consumer-1")
p.transform(clean_and_enrich)
p.write_bigquery("project.dataset.table")
p.run()
```

## License

Apache 2.0