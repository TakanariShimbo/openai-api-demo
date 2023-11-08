

class SubComponentResult:
    def __init__(self, go_next: bool = True, call_rerun: bool = False) -> None:
        self.__go_next = go_next
        self.__call_rerun = call_rerun

    @property
    def go_next(self) -> bool:
        return self.__go_next
    
    @property
    def call_return(self) -> bool:
        return self.__call_rerun