from collections import namedtuple
from typing import Any, NamedTuple, Optional

svmem = NamedTuple(
    'svmem', [('total', int), ('available', int), ('percent', int),
              ('used', int), ('free', int), ('active', int),
              ('inactive', int), ('buffers', int), ('cached', int),
              ('shared', int), ('slab', int)])

pmem = namedtuple('pmem', ['rss', 'vms'])

def virtual_memory() -> svmem: ...

def cpu_count() -> int: ...

class Process:
    def __init__(self, pid: Optional[Any] = ...) -> None: ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __hash__(self): ...
    @property
    def pid(self): ...
    def oneshot(self) -> None: ...
    def as_dict(self, attrs: Optional[Any] = ..., ad_value: Optional[Any] = ...): ...
    def parent(self): ...
    def parents(self): ...
    def is_running(self): ...
    def ppid(self): ...
    def name(self): ...
    def exe(self): ...
    def cmdline(self): ...
    def status(self): ...
    def username(self): ...
    def create_time(self): ...
    def cwd(self): ...
    def nice(self, value: Optional[Any] = ...): ...
    def uids(self): ...
    def gids(self): ...
    def terminal(self): ...
    def num_fds(self): ...
    def io_counters(self): ...
    def ionice(self, ioclass: Optional[Any] = ..., value: Optional[Any] = ...): ...
    def rlimit(self, resource: Any, limits: Optional[Any] = ...): ...
    def cpu_affinity(self, cpus: Optional[Any] = ...): ...
    def cpu_num(self): ...
    def environ(self): ...
    def num_handles(self): ...
    def num_ctx_switches(self): ...
    def num_threads(self): ...
    def threads(self): ...
    def children(self, recursive: bool = ...): ...
    def cpu_percent(self, interval: Optional[Any] = ...): ...
    def cpu_times(self): ...
    def memory_info(self) -> pmem: ...
    def memory_info_ex(self): ...
    def memory_full_info(self): ...
    def memory_percent(self, memtype: str = ...): ...
    def memory_maps(self, grouped: bool = ...): ...
    def open_files(self): ...
    def connections(self, kind: str = ...): ...
    def send_signal(self, sig: Any) -> None: ...
    def suspend(self) -> None: ...
    def resume(self) -> None: ...
    def terminate(self) -> None: ...
    def kill(self) -> None: ...
    def wait(self, timeout: Optional[Any] = ...): ... 
