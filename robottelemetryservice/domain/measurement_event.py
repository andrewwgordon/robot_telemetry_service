from typing import List
from abc import ABC

class MeasurementEvent:
    def __init__(self,
        siteName: str=None,
        dateTimeUTC: int=None,
        dataValue: float=None,
        measurementLocationId: int=None,
    ):        
        self.siteName=siteName
        self.dateTimeUTC=dateTimeUTC
        self.dataValue=dataValue
        self.measurementLocationId=measurementLocationId
    
    def __iter__(self):
        yield self.siteName
        yield self.dateTimeUTC
        yield self.dataValue
        yield self.measurementLocationId

class IMeasurementEventRepository(ABC):
    def add(self,measurements: List[MeasurementEvent]):
        pass