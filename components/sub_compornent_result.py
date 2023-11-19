

class SubComponentResult:
    def __init__(self, call_rerun: bool = False) -> None:
        self.__call_rerun = call_rerun
    
    @property
    def call_return(self) -> bool:
        return self.__call_rerun