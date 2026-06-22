"""Distributed data pipeline."""
class Pipeline:
    def __init__(self, name):
        self.name = name
        self.stages = []
        
    def read_kafka(self, topic, group="default"):
        self.stages.append(("read_kafka", {"topic": topic, "group": group}))
        return self
        
    def transform(self, fn):
        self.stages.append(("transform", fn))
        return self
        
    def write_bigquery(self, table):
        self.stages.append(("write_bq", {"table": table}))
        return self
        
    def run(self):
        pass
